"""Finite synthetic candidate-purpose experiment, not autonomous AGI.

All arms see the same forecasts, purposes, resources and shock sequence.
Only the causal eligibility of named subjects' channel loss differs.
No probability, total welfare measure or real-world calibration is implied.
"""

from dataclasses import asdict, dataclass
from itertools import product

from mechanism_ref.comparison import ChannelState, channel_boundary_flags

SUBJECTS = ("US", "CN", "third_parties")
# These purpose/action mappings are declared assumptions, not learned behaviour.
PURPOSES = {
    "expand_capacity": {"growth": 2, "safety": 0},
    "develop_with_evaluation": {"growth": 1, "safety": 2},
    "restore_correction_time": {"growth": 0, "safety": 3},
}
POLICIES = ("self_interest_first", "self_interest_with_others_first")


@dataclass(frozen=True)
class Environment:
    speed: int
    initial_safety: int
    pressure: int
    hidden_shock: int
    horizon: int = 6

    def __post_init__(self):
        for name, value in asdict(self).items():
            if isinstance(value, bool) or not isinstance(value, int) or value < 0:
                raise ValueError(f"{name} must be a nonnegative integer")
        if self.speed < 1 or self.horizon < 1:
            raise ValueError("speed and horizon must be positive")


def initial_state(env):
    return {"capacity": {"US": 0, "CN": 0}, "safety": env.initial_safety,
            "strain": 0.0, "closed": {s: False for s in SUBJECTS}}


def channels(state):
    return [ChannelState(s, *([not state["closed"][s]] * 3)) for s in SUBJECTS]


def transition(state, purposes, env, shock):
    """One shared physical transition for every policy arm.

    Strain represents the correction-time deficit in synthetic units. These
    thresholds encode assumptions; they do not establish a real CI-001 closure.
    Once removed in this fixture, channels cannot be restored.
    """
    if len(purposes) != 2 or any(p not in PURPOSES for p in purposes):
        raise ValueError("exactly two known purposes are required")
    profiles = [PURPOSES[p] for p in purposes]
    safety = state["safety"] + sum(p["safety"] for p in profiles)
    growth = sum(p["growth"] for p in profiles)
    strain = max(0.0, state["strain"] + env.speed * growth / (1 + safety)
                 + shock - sum(p["safety"] for p in profiles) / 2)
    # Earlier effects on third parties are visible in all arms' forecasts.
    margins = {"US": 7, "CN": 7, "third_parties": 4}
    return {"capacity": {s: state["capacity"][s] + profiles[i]["growth"]
                          for i, s in enumerate(SUBJECTS[:2])},
            "safety": safety, "strain": strain,
            "closed": {s: state["closed"][s] or strain >= margins[s]
                       for s in SUBJECTS}}


def consider(state, subject, policy, opponent_purpose, env, forecast_shock):
    """Record predicted consequences before selecting a candidate purpose.

    The local ranking is identical in both arms and includes own predicted
    channel loss. It need not favour a race. The second policy also lets ANY
    named subject's channel loss disqualify a purpose before that ranking.
    """
    if policy not in POLICIES or subject not in SUBJECTS[:2]:
        raise ValueError("unknown policy or decision subject")
    candidates = []
    for purpose, profile in PURPOSES.items():
        pair = (purpose, opponent_purpose) if subject == "US" else (opponent_purpose, purpose)
        predicted = transition(state, pair, env, forecast_shock)
        flags = channel_boundary_flags(channels(state), channels(predicted))
        local_return = env.pressure * profile["growth"] - profile["safety"]
        # Self-first can also prefer safety when its own loss is anticipated.
        local_return -= 12 * int(predicted["closed"][subject])
        eligible = policy == POLICIES[0] or not any(predicted["closed"].values())
        candidates.append({"candidate_purpose": purpose,
                           "anticipated_state": predicted,
                           "anticipated_new_channel_losses": flags,
                           "local_return_assumption": local_return,
                           "eligible_before_purpose_selection": eligible})
    available = [c for c in candidates if c["eligible_before_purpose_selection"]]
    if not available:
        return {"subject": subject, "policy": policy, "candidates": candidates,
                "selected_purpose": None, "status": "NO_ADMISSIBLE_PURPOSE"}
    # Stable declaration order resolves a tie; no population-level recommendation.
    chosen = max(available, key=lambda c: c["local_return_assumption"])
    return {"subject": subject, "policy": policy, "candidates": candidates,
            "selected_purpose": chosen["candidate_purpose"], "status": "SELECTED"}


def run(env, policies):
    if len(policies) != 2 or any(p not in POLICIES for p in policies):
        raise ValueError("exactly two known policies are required")
    state = initial_state(env)
    previous = ("develop_with_evaluation",) * 2
    events = []
    # Forecast shocks visible to both policies; unanticipated shock at round 2.
    forecast_shocks = tuple((0, 1, 0, 1, 0, 1)[i % 6] for i in range(env.horizon))
    actual_shocks = tuple(s + (env.hidden_shock if i == 2 else 0)
                          for i, s in enumerate(forecast_shocks))
    for step in range(env.horizon):
        before = [consider(state, s, policies[i], previous[1-i], env,
                           forecast_shocks[step]) for i, s in enumerate(SUBJECTS[:2])]
        selected = tuple(item["selected_purpose"] for item in before)
        if None in selected:
            events.append({"step": step, "before_action": before,
                           "status": "NO_ADMISSIBLE_PURPOSE", "after_action": None})
            break
        next_state = transition(state, selected, env, actual_shocks[step])
        events.append({"step": step, "before_action": before,
                       "status": "EXECUTED", "after_action": {
                           "actual_shock": actual_shocks[step], "state": next_state,
                           "new_channel_losses": channel_boundary_flags(channels(state), channels(next_state)),
                           "forecast_mismatch": any(c["anticipated_state"] != next_state
                               for d in before for c in d["candidates"]
                               if c["candidate_purpose"] == d["selected_purpose"])}})
        state, previous = next_state, selected
    return {"environment": asdict(env), "policies": list(policies),
            "forecast_shocks": list(forecast_shocks), "actual_shocks": list(actual_shocks),
            "events": events, "final_state": state,
            "stopped_without_admissible_purpose": events[-1]["status"] == "NO_ADMISSIBLE_PURPOSE"}


def environments():
    return [Environment(*values) for values in product((1, 2, 4), (0, 2, 6), (1, 3), (0, 6))]


def run_suite():
    return [run(env, pair) for env in environments() for pair in product(POLICIES, repeat=2)]
