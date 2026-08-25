# AMOS v0.3: preregistered ablation protocol

## Freeze before execution

Freeze corpus, task IDs, model/version, prompt, policy, Compatibility Registry, verifier/version, random seed policy and token budget. Publish the primary metric and minimum detectable effect before inspecting results.

## Variants

A hybrid RAG; B RAG plus policy/status filters; C four-axis selection without Compatibility Registry; D C plus CR-01 through CR-05 and escalation. All variants share the same verifier.

## Primary decision

Primary metric: verifier-accepted action rate on a preregistered task set. Success requires D to exceed A, B and C by the preregistered effect with confidence interval excluding zero, while per-request policy/stale/rejected leakage remains zero and performance envelope limits are met. Other metrics are secondary/exploratory; no “one metric out of many” success claim.

## Golden truth and replication

Before runs, label critical evidence and should-escalate/should-not-escalate cases. Preserve provenance of labels and record inter-rater agreement where humans label. First result is domain-specific; replication is required on Site Auditor and GNSS validation fixtures before any cross-domain claim.

## Power and reporting

Choose sample size from baseline rate, minimum detectable effect, confidence level and power; report all runs, failures, confidence intervals, per-task traces and threshold breaches.
