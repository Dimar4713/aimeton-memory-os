# Architecture baseline

The public system name is AIMETON Cognitive Operations Complex (AIMETON.COGOPS).

## Canonical starting documents

- [Four-axis coordination model](FOUR_AXIS_COORDINATION_MODEL.md)
- [Life-and-Activity Learning](LIFE_AND_ACTIVITY_LEARNING.md)
- [Compatibility Registry v0.3 + pre-F1 amendment](AIMETON_COGOPS_COMPATIBILITY.md)
- [Canonical C vs D worked example](COMPATIBILITY_C_VS_D_WORKED_EXAMPLE.md)
- [Performance and concurrency contract](PERFORMANCE_AND_CONCURRENCY_CONTRACT.md)
- [Preregistered ablation protocol](ABLATION_PROTOCOL.md)
- [Sovereign security extensibility](SOVEREIGN_SECURITY_EXTENSIBILITY.md)
- [External audit brief](EXTERNAL_AUDIT_BRIEF.md)

## Audit disposition — 2026-08-25

The v0.3 external audit is accepted as the architecture pre-MVP review. No fourth full document-only audit is required before implementation.

The externally audited v0.3 package remains historical evidence. Repository pre-F1 amendments close the remaining implementation ambiguities without rewriting that package:

1. C and D must share the same pre-registry candidate set; the worked example is normative.
2. Performance/concurrency criteria are restored as an explicit contract and must be numerically frozen before F1.
3. CR-06 adds evaluation snapshot coherence so mixed-version V/R/O/A/policy/evidence state cannot silently become an operational ContextBundle.

The next meaningful external audit should review implementation and F1 evidence: freeze commit, benchmark corpus manifest, golden fixtures, raw runs/failures, traces, confidence intervals, performance results and reproduction instructions.

## Learning method

AMOS uses **Life-and-Activity Learning**: real AIMETON work generates a governed Living Development Corpus from which evidence, observations, claims, decisions, outcomes and regression fixtures are derived. MVP starts in Shadow mode; the living stream is a development environment, not sufficient proof of effectiveness by itself. Frozen holdout and independent domain replication remain mandatory for claims.

## Engineering boundary

The initial implementation is contract-first. It proves one bounded vertical slice, not full fractality, multi-writer runtime, GraphDB, Kafka, OpenFGA, or a certified protected-data environment.

The public claim remains conditional: the deterministic compatibility registry must demonstrate measured utility improvement over defined baselines with no safety or performance regression.

## F1 entry gate

F1 is blocked until:

- every `REQUIRED_BEFORE_F1` performance target/stop value is replaced by a committed numeric value;
- the C-vs-D canonical fixture passes;
- CR-06 has an executable adversarial fixture and trace field coverage;
- corpus/model/prompt/policy/verifier/registry versions and power assumptions are frozen.

New decisions require an issue or ADR with evidence, compatibility impact, fixtures, and replay criteria.
