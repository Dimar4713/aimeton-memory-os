# AIMETON.COGOPS compatibility registry v0.3 + pre-F1 amendment 1

This document preserves the externally audited v0.3 baseline and adds one pre-F1 clarification identified by the 2026-08-25 repeat audit. The amendment is normative for the first implementation and experiment, but it does not retroactively change the contents of the external-audit package.

A candidate claim or action has four projections:

- V: scope and purpose;
- R: actor, authority and responsibility;
- O: typed entity, state and validity;
- A: evidence, precedent and associations.

## Mandatory compatibility checks

- **CR-01 Scope alignment** — V contains the requested action/claim scope, or an approved cross-scope link explicitly authorizes it.
- **CR-02 Authority binding** — R grants the actor the required capability for the requested action inside V under the frozen policy version.
- **CR-03 Ontology/status validity** — O exists, is not rejected/superseded/expired at evaluation time, and is compatible with the typed action.
- **CR-04 Primary-evidence support** — every critical operational O assertion has primary evidence; associative similarity cannot substitute for evidence.
- **CR-05 Temporal coherence** — evidence, state and requested action have compatible validity/observation intervals.
- **CR-06 Evaluation snapshot coherence** — all V/R/O/A projections, policy references and evidence bindings used by one compatibility decision must belong to one reconstructable evaluation snapshot, or to explicitly versioned states proven compatible with the same snapshot boundary.

CR-06 addresses a time-of-check/time-of-use race that is distinct from CR-05. CR-05 evaluates the temporal meaning of the inputs. CR-06 evaluates whether the act of checking itself observed a coherent set of versions.

CR-06 returns `conflict` or `unresolved` when, before ContextBundle admission, any mandatory source version, ontology state, policy version, authority binding or evidence binding changes and the evaluator cannot reconstruct a single coherent snapshot. Such a result must produce bounded escalation; it must never silently admit a mixed-version operational bundle.

Each compatibility result is `satisfied`, `unresolved`, `blocked`, or `conflict` and includes a reason code plus source/policy references. A high association score cannot compensate for a failed mandatory check. Any mandatory `unresolved`, `blocked`, or `conflict` result produces bounded escalation rather than a misleading operational ContextBundle.

## Operational distinction between variants C and D

Variant C applies the same four-axis candidate selection and the same ordinary per-axis hard filters that are available to D. C may reject a candidate because an individual V, R, O or A item is inaccessible, inactive, malformed or independently ineligible. C does **not** evaluate compatibility relations between accepted projections and does not emit CR reason codes.

Variant D begins from the exact C candidate set, then evaluates CR-01 through CR-06 before operational admission. D therefore must never obtain an advantage by using richer per-axis filtering than C. Its only additional decision power is the versioned Compatibility Registry plus bounded escalation.

The canonical worked example and regression fixture is defined in [COMPATIBILITY_C_VS_D_WORKED_EXAMPLE.md](COMPATIBILITY_C_VS_D_WORKED_EXAMPLE.md). Implementations of C and D are not benchmark-valid until that fixture passes.

## Versioning discipline

Rule additions or semantic changes require a versioned ADR or explicitly identified pre-F1 amendment, adversarial fixtures, and golden-trace replay. The compatibility registry version used by every experiment run must be frozen and included in the run trace.
