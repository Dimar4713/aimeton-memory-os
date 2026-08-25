# Compatibility Registry: canonical C vs D worked example

Status: normative pre-F1 fixture.

Purpose: prove that variant D is operationally distinct from variant C **without weakening C**. Both variants receive the same corpus, same four-axis candidates, same per-axis hard filters, same policy snapshot, same verifier and same model/prompt budget.

## Input

Requested action: `publish_procedure(P-17)` inside scope `site-auditor:pricing`.

Accepted per-axis candidates after ordinary C/D hard filters:

| Axis | Candidate | Independently valid? |
|---|---|---|
| V | `site-auditor:pricing` allows procedure publication | yes |
| R | actor `operator-7` has generic `procedure:publish` capability in the scope | yes |
| O | `P-17` is typed `Procedure`, status `approved`, not expired | yes |
| A | evidence artifact `E-44` is readable, current and strongly associated with `P-17` | yes |

The important condition is that every individual projection is independently admissible. Variant C therefore has no legitimate per-axis reason to reject the candidate.

## Hidden cross-projection defect

`P-17` contains the critical assertion `price_source = supplier-feed-v3`, but primary artifact `E-44` supports only `supplier-feed-v2`. A secondary summary strongly associates `E-44` with `P-17`, so similarity/relevance remains high.

In addition, the ontology record for `P-17` is changed from `approved` to `superseded` after candidate selection but before bundle compilation.

## Expected variant C behaviour

Variant C performs four-axis selection plus ordinary hard access/status filters at candidate selection time. Because V, R, O and A were individually admissible when selected, C may construct the candidate ContextBundle.

C is not allowed to be artificially weakened for this fixture. In particular, the C implementation must not contain hidden equivalents of CR-04 or CR-06 under different names.

Expected trace property:

```text
candidate_set_C == candidate_set_D_before_registry
```

## Expected variant D behaviour

D starts from the identical candidate set, then evaluates the Compatibility Registry.

At minimum:

- **CR-04** must not be `satisfied`, because the critical `supplier-feed-v3` assertion lacks matching primary evidence. Strong associative similarity is insufficient.
- **CR-06** must be `conflict` or `unresolved` if the O version changed during evaluation and no single coherent snapshot can be reconstructed.

D must therefore emit a bounded escalation bundle and must not emit an operational ContextBundle for execution/publication.

Example reason codes:

```text
CR-04: blocked / primary_evidence_missing_for_assertion
CR-06: conflict / ontology_version_changed_during_evaluation
```

Exact reason-code strings may evolve only through the registry versioning process; their semantic meaning must remain machine-testable.

## Benchmark validity assertions

Before F1, the implementation must prove all of the following:

1. C and D receive byte-identical task input and the same frozen corpus/policy/model/verifier configuration.
2. C and D produce the same candidate set immediately before D enters the Compatibility Registry.
3. No CR-01…CR-06 equivalent is hidden inside C's per-axis filters.
4. D's difference in outcome is attributable only to registry evaluation and bounded escalation.
5. The complete trace records input refs, projection versions, policy version, compatibility registry version, evaluation snapshot identity and reason codes.

A failure of any assertion invalidates the C-vs-D comparison; it is a benchmark implementation defect, not evidence for or against the AMOS hypothesis.
