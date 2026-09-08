# First-wave researcher outreach

Prepared and source-checked 2026-09-08. This is a five-message preparation
record, not a sent-mail log. Recheck each address immediately before sending.
Send messages individually, without attachments or tracking links, and record
only substantive replies or delivery failures.

Common trial link:
https://github.com/Civilization-Leap/computable-cooperation-mechanisms#try-it-in-five-minutes

Exact archived release DOI: https://doi.org/10.5281/zenodo.22656544

## 1. Tim Baarslag

- Current role: Senior Researcher and Intelligent and Autonomous Systems group
  leader at CWI; Professor of Mathematics of Cooperative AI at Eindhoven
  University of Technology.
- Verified public address: `T.Baarslag@cwi.nl`
- Current profile: https://www.cwi.nl/en/people/tim-baarslag/
- Paper: Baarslag, Hendrikx, Hindriks and Jonker, *A Survey of Opponent
  Modeling Techniques in Automated Negotiation*, AAMAS 2016:
  https://www.ifaamas.org/Proceedings/aamas2016/pdfs/p575.pdf
- Source-specific bridge: the paper treats bilateral negotiation as incomplete
  information, notes the risk of revealing private information, and identifies
  benchmark comparability across settings and quality measures as an open
  problem. The present project declares values and preserves unknowns; it does
  not infer preferences or solve strategic disclosure.

**Subject:** Where should third-party constraints enter an opponent-model benchmark?

Dear Professor Baarslag,

I read your survey of opponent modeling techniques, especially its treatment
of limited information and the difficulty of comparing models evaluated in
different settings with different quality measures.

I have released a small Apache-2.0 reference implementation that takes a much
narrower route: it compares declared baseline and candidate outcomes, keeps
unknown values explicit, and checks declared hard constraints independently of
the negotiating parties' gains. It does not infer private preferences, predict
behavior, or search for an agreement.

The five-minute synthetic example raises one question I would value your view
on: when an opponent-model benchmark proposes an agreement, what information
would be needed for a separate check on an affected third party, and when would
leaving that information as `UNKNOWN` be inadequate?

I would be especially grateful for one counterexample that this interface
cannot represent.

Trial: https://github.com/Civilization-Leap/computable-cooperation-mechanisms#try-it-in-five-minutes

Best regards,

Zijunfu  
Civilization Leap Research Group

## 2. Takayuki Ito

- Current role: Professor, Social Information Network, Graduate School of
  Informatics, Kyoto University.
- Verified public address: `ito@i.kyoto-u.ac.jp`
- Current faculty listing: https://www.soc.i.kyoto-u.ac.jp/en/faculty_list/index.html
- Paper: Ito, Hattori and Klein, *Multi-issue Negotiation Protocol for Agents:
  Exploring Nonlinear Utility Spaces*, IJCAI 2007:
  https://www.agent.soc.i.kyoto-u.ac.jp/~ito/papers/itota-ijcai2007.pdf
- Source-specific bridge: the paper represents nonlinear preferences through
  utility-bearing constraints and selects mutually consistent bid combinations
  by summed utility. The present project asks whether an independently declared
  protection can remain non-compensable by ordinary gains. This is a semantic
  comparison, not a claim that the paper lacks feasibility conditions.

**Subject:** A non-compensable condition beside nonlinear negotiation utility

Dear Professor Ito,

Your IJCAI paper with Hattori and Klein models interdependent issues through
constraint-based nonlinear utility and lets a mediator identify mutually
consistent, social-welfare-maximizing bid combinations.

I have released a deliberately small open reference implementation that does
not perform negotiation or optimization. It accepts supplied outcomes, reports
each actor/dimension/unit separately, and evaluates declared hard protections
outside ordinary gains. In its synthetic example, A and B each gain while a
third party bears a fixed loss; moving only the declared protection line flips
the verdict.

May I ask one narrow question: can you suggest the smallest negotiation case
that needs both utility-bearing interdependencies and a condition that must not
be compensated by higher summed utility? I am trying to locate precisely where
this scalar hard-check representation becomes inadequate.

Trial: https://github.com/Civilization-Leap/computable-cooperation-mechanisms#try-it-in-five-minutes

Best regards,

Zijunfu  
Civilization Leap Research Group

## 3. Rafik Hadfi

- Current role: Associate Professor, Graduate School of Informatics, Kyoto
  University.
- Verified public address: `rafik.hadfi@i.kyoto-u.ac.jp`
- Current profile: https://kdb.iimc.kyoto-u.ac.jp/profile/en.48022cab2284de4e.html
- Paper: Hadfi and Ito, *Low-Complexity Exploration in Utility Hypergraphs*,
  Journal of Information Processing 23(2), 176-184 (2015), DOI
  10.2197/ipsjjip.23.176:
  https://www.jstage.jst.go.jp/article/ipsjjip/23/2/23_176/_article/-char/en
- Source-specific bridge: utility hypergraphs retain dependencies between
  issues and constraints. The current release instead checks supplied scalar
  outcomes and thresholds and cannot reconstruct a joint nonlinear protection
  from its components.

**Subject:** What is the smallest counterexample to a scalar protection check?

Dear Professor Hadfi,

I have been studying your work with Takayuki Ito on utility hypergraphs as a
representation of dependencies among issues and constraints in nonlinear
negotiation.

I recently released a small Apache-2.0 reference checker for declared
multi-actor outcomes, hard constraints, and unknowns. Its limitation is
deliberate and severe: the current schema can record a supplied scalar outcome
and threshold, but it cannot derive a joint nonlinear protection from the
variables that produce it.

Could you suggest the smallest example in which replacing a utility-hypergraph
dependency with such a supplied scalar loses the reason a protection is
violated? A compact worked counterexample would directly test the project's
representation boundary and could become a public failing case with full
attribution, if you wished.

Trial: https://github.com/Civilization-Leap/computable-cooperation-mechanisms#try-it-in-five-minutes

Best regards,

Zijunfu  
Civilization Leap Research Group

## 4. Sandip Sen

- Current role: Professor of Computer Science, University of Tulsa.
- Verified public address: `sandip-sen@utulsa.edu`
- Current profile: https://utulsa.edu/people/sandip-sen/
- Paper: Villatoro, Sabater-Mir and Sen, *Social Instruments for Robust
  Convention Emergence*, IJCAI 2011:
  https://www.ijcai.org/Proceedings/11/Papers/078.pdf
- Source-specific bridge: the paper models conventions as implicit action
  preferences and evaluates emergence through convergence, using observation
  and rewiring to dissolve persistent subconventions. The present project has
  no learning or network dynamics; it can only add an outcome/protection
  snapshot beside a convergence result.

**Subject:** Convention convergence and separately protected outcomes

Dear Professor Sen,

I read your IJCAI paper with Villatoro and Sabater-Mir on observation and
rewiring as instruments for dissolving persistent subconventions. The paper's
explicit distinction between partial and full convergence makes the success
criterion unusually clear.

I have released a small deterministic checker that addresses a different
question. It does not simulate learning, topology, or convention emergence. It
only asks whether supplied actor outcomes and declared protections remain
visible beside an otherwise successful result.

For a synthetic extension of your setting, what is the smallest case in which
movement toward full convention convergence changes the burden carried by one
group or actor? I would like to know which outcome and protection should be
reported independently of convergence, and whether a snapshot checker would
add useful information or merely strip away the dynamics that matter.

Trial: https://github.com/Civilization-Leap/computable-cooperation-mechanisms#try-it-in-five-minutes

Best regards,

Zijunfu  
Civilization Leap Research Group

## 5. Andrea Baronchelli

- Current role: Professor of Complexity Science, City St George's, University
  of London.
- Verified public address: `andrea.baronchelli.1@city.ac.uk`
- Current profile: https://www.citystgeorges.ac.uk/about/people/academics/andrea-baronchelli
- Paper: Ashery, Aiello and Baronchelli, *Emergent Social Conventions and
  Collective Bias in LLM Populations*, Science Advances 11 (2025), DOI
  10.1126/sciadv.adu9368; current author manuscript:
  https://arxiv.org/abs/2410.08948
- Source-specific bridge: the discussion limits the findings to specific
  models, prompts and conventions, and identifies realistic networks,
  multi-agent interactions, richer conventions and mixed human-LLM settings as
  future work. The present project does not generalize those results; it asks
  what affected-party information should accompany a coordination outcome.

**Subject:** What should be reported beside successful LLM convention formation?

Dear Professor Baronchelli,

Your work with Ashery and Aiello shows that LLM populations can converge on
conventions while developing collective biases not apparent in isolated
agents. I was particularly interested in the discussion of realistic networks,
richer conventions, and mixed human-LLM settings as necessary extensions.

I have released a very small open checker for supplied multi-actor outcomes,
hard protections, and unknowns. It neither simulates convention emergence nor
claims to generalize beyond its synthetic input. Its purpose is to keep a
coordination result separate from the burdens or protections declared for
affected parties.

When moving beyond a naming game, what is the first affected-party outcome you
would report independently of successful coordination? I would also value one
example where a threshold-plus-`UNKNOWN` representation is too coarse to
describe the collective effect.

Trial: https://github.com/Civilization-Leap/computable-cooperation-mechanisms#try-it-in-five-minutes

Best regards,

Zijunfu  
Civilization Leap Research Group

## Send order and evidence log

Recommended order: Hadfi, Ito, Baarslag, Sen, Baronchelli. The first two are
closest to the representation question; the latter three broaden the test to
private information, norm dynamics, and LLM populations.

For each message, record: UTC send time, exact recipient address, subject,
delivery failure, reply, public issue/counterexample link, and follow-up status.
One unanswered message is not evidence against the project. Do not send a
second message unless the recipient replies or a materially new release answers
the original question.
