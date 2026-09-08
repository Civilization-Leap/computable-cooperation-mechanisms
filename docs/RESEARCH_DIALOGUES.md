# Five paper-specific research conversations

Prepared 2026-09-08. These are proposed conversation targets and technical questions, not a sent-mail log. Institutional affiliations and contact details should be rechecked before sending; use a current individual profile, not a historical paper's email by default. No response or endorsement is implied.

Each entry distinguishes the source's actual scope from our proposed comparison. Constraint-based negotiation and norm research have substantial prior art. This tiny evaluator does not replace their optimization, learning, or simulation methods.

## Tim Baarslag — limited information and comparison criteria

[Current CWI profile](https://www.cwi.nl/people/tim-baarslag). Paper: Baarslag, Hendrikx, Hindriks and Jonker, [A Survey of Opponent Modeling Techniques in Automated Negotiation](https://www.ifaamas.org/Proceedings/aamas2016/pdfs/p575.pdf), AAMAS 2016, pp. 575–576.

The introduction discusses withholding private information to avoid exploitation; the conclusion identifies comparison difficulties when models use different settings and quality measures. Our narrower object uses declared values, leaves explicit unknowns visible, and reports actor/dimension/unit outcomes separately. It does not infer private preferences or solve the disclosure problem.

Conversation question: when an opponent-model benchmark proposes an agreement, what information would be needed for a separate third-party protection check, and when would preserving a value as unknown be inadequate? Ask for one counterexample to the interface, not validation of the entire framework.

## Takayuki Ito — utility-bearing constraints versus non-compensable checks

[Current Kyoto University faculty listing](https://www.soc.i.kyoto-u.ac.jp/en/faculty_list/index.html). Paper: Ito, Hattori and Klein, [Multi-issue Negotiation Protocol for Agents: Exploring Nonlinear Utility Spaces](https://www.agent.soc.i.kyoto-u.ac.jp/~ito/papers/itota-ijcai2007.pdf), IJCAI 2007, especially §2 and the proposed bidding protocol.

The model represents nonlinear utilities with constraints carrying utility values; a mediator searches combinations of bids for social welfare. The comparison to our project is a difference in task and semantics: a declared hard threshold produces an independent check result, and ordinary outcome gains do not offset it. This is not evidence that the paper lacks feasibility restrictions or that the distinction is novel.

Conversation question: can a minimal contract example require both weighted preference regions and an untradeable third-party condition, and where would our scalar threshold representation lose essential interdependence?

## Rafik Hadfi — dependencies that scalar checks cannot express

[Kyoto University research profile](https://kdb.iimc.kyoto-u.ac.jp/profile/en.48022cab2284de4e.html). Paper: Hadfi and Ito, [Low-Complexity Exploration in Utility Hypergraphs](https://www.jstage.jst.go.jp/article/ipsjjip/23/2/23_176/_pdf/-char/en), Journal of Information Processing 23(2), 176–184 (2015), DOI 10.2197/ipsjjip.23.176; §2.2–§3.

The paper maps issue/constraint dependencies into utility hypergraphs and explores utility-maximizing contracts with message passing. Our current release has only individual resource/outcome threshold checks and accepts predeclared candidate outcomes. It does not calculate a joint nonlinear protection from its constituent variables.

Conversation question: what is the smallest case where replacing a joint dependency by a supplied scalar loses the reason a protection is violated? A worked counterexample would directly serve Issue #5. This asks for a limitation of our representation, not a claim to outperform the hypergraph method.

## Sandip Sen — convergence and protected outcomes are different questions

[University of Tulsa profile](https://utulsa.edu/people/sandip-sen/). Paper: Villatoro, Sabater-Mir and Sen, [Social Instruments for Robust Convention Emergence](https://www.ijcai.org/Proceedings/11/Papers/078.pdf), IJCAI 2011, pp. 420–425, especially §2–§3.

The paper studies observation and rewiring to overcome persistent subconventions. In its model, norms are implicit in action preferences, and convention emergence is assessed through shared action choices. Our evaluator can separately record declared per-actor outcomes and thresholds, but has no learning process or network dynamics.

Conversation question: in a synthetic extension where convergence changes an affected group's burden, which outcome and protection would need to be recorded separately from convergence? A snapshot check could be investigated as a reporting layer; no such integration has been implemented or tested here.

## Andrea Baronchelli — group behavior and limits of synthetic settings

[University profile](https://www.citystgeorges.ac.uk/about/people/academics/andrea-baronchelli). Paper: Ashery, Aiello and Baronchelli, [Emergent Social Conventions and Collective Bias in LLM Populations](https://arxiv.org/html/2410.08948v2), Science Advances (2025), DOI 10.1126/sciadv.adu9368; Discussion and Materials and Methods.

The discussion explicitly limits the findings to the tested models, prompts and conventions, and identifies realistic social networks and richer interactions as future work. Our code checks supplied outcomes and thresholds; it does not simulate convention emergence, resolve those generalization limits, or establish a route to AGI alignment.

Conversation question: when moving beyond a naming game, which affected-party outcome should be reported independently of successful coordination, and where would a threshold-plus-unknown representation be too coarse? A useful first response would be one missing variable or one example that cannot be faithfully encoded.

## Common follow-through

Attach one [five-minute trial link](https://github.com/Civilization-Leap/computable-cooperation-mechanisms#try-it-in-five-minutes), then the [synthetic comparison](SHARED_EQUIPMENT_COMPARISON.md) only if it helps the particular question. Keep one paper-specific question per message. Five candidates do not imply five simultaneous sends or a measured advantage over other outreach methods. The current individualized preparation package is [RESEARCH_OUTREACH_WAVE1.md](RESEARCH_OUTREACH_WAVE1.md); neither document marks a message as sent.
