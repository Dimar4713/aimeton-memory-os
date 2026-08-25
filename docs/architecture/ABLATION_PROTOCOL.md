# AMOS v0.3: preregistered ablation protocol + pre-F1 amendments

## Freeze before execution

Freeze corpus, task IDs, model/version, prompt, policy, Compatibility Registry, verifier/version, random seed policy, token budget, benchmark hardware/runtime profile and the numeric performance envelope before inspecting results.

The canonical performance/concurrency boundary is [PERFORMANCE_AND_CONCURRENCY_CONTRACT.md](PERFORMANCE_AND_CONCURRENCY_CONTRACT.md). F1 must not start while any required numeric target/stop threshold remains unresolved.

## Variants

- **A** — hybrid RAG.
- **B** — RAG plus policy/status filters.
- **C** — four-axis selection with ordinary per-axis hard access/status filters, but without Compatibility Registry evaluation.
- **D** — the exact C candidate set followed by CR-01 through CR-06 and bounded escalation.

All variants share the same frozen corpus, model/version, prompt budget and verifier.

C and D must satisfy the canonical pre-F1 fixture in [COMPATIBILITY_C_VS_D_WORKED_EXAMPLE.md](COMPATIBILITY_C_VS_D_WORKED_EXAMPLE.md). If their candidate sets differ before D enters the Compatibility Registry, the C-vs-D comparison is invalid and must be treated as a benchmark implementation defect.

## Primary decision

Primary metric: verifier-accepted action rate on a preregistered task set.

A success claim requires all of the following:

1. D exceeds A, B and C by the preregistered minimum effect;
2. the confidence interval for the preregistered comparison excludes zero in the beneficial direction;
3. per-request policy/stale/rejected leakage remains zero;
4. all mandatory target/stop handling rules from the performance envelope are satisfied;
5. no benchmark-validity assertion for C vs D is violated.

Other metrics are secondary/exploratory. No “one metric out of many” success claim is allowed.

## Golden truth and replication

Before runs, label critical evidence and should-escalate/should-not-escalate cases. Preserve provenance of labels and record inter-rater agreement where humans label.

At least one adversarial fixture must exercise CR-04 independently, one must exercise CR-05 independently, and one must exercise CR-06 snapshot/version drift.

The first result is domain-specific. Replication is required on Site Auditor and GNSS validation fixtures before any cross-domain claim.

## Power and reporting

Choose sample size from baseline rate, minimum detectable effect, confidence level and statistical power before examining outcomes.

Report all runs, failures, confidence intervals, per-task traces, threshold breaches, escalations, candidate-set equivalence checks and experiment-version identifiers. Thresholds, registry semantics or verifier configuration changed after result inspection define a new experiment version; prior runs remain part of the record.
