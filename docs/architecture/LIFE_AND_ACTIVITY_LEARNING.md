# Life-and-Activity Learning

Status: canonical AIMETON/AMOS architectural principle.

## Definition

**Life-and-Activity Learning** is the method by which AIMETON improves its governed memory and future behavior from the evidence produced during its own real work, rather than learning only from a separately prepared training corpus.

The operational loop is:

```text
Experience
→ Evidence
→ Observation
→ Interpretation
→ Decision
→ Action
→ Outcome
→ Verification
→ Governed memory update
→ changed future context/behavior
```

The phrase "learning" does not imply unrestricted online model-weight mutation. In AMOS MVP it primarily means evidence-governed accumulation, versioned interpretation, decision lineage, fixture creation, rule refinement, replay and measured adaptation.

## Why AIMETON development is the first living environment

The active development of AIMETON and its pilot applications naturally produces a heterogeneous stream of:

- conversations and operator instructions;
- GitHub issues, pull requests, commits and reviews;
- CI runs, logs and runtime receipts;
- architecture documents, ADRs and audits;
- files, schemas, manifests and experimental artifacts;
- infrastructure state transitions;
- hypotheses, decisions, reversals and superseding decisions;
- failures, recovery actions and verified outcomes;
- external research observations and prior-art evidence.

This stream exists independently of AMOS and therefore provides a realistic, continuously changing environment in which memory coherence can be tested from the first MVP vertical slice.

## AMOS Living Development Corpus (LDC)

The governed projection of that activity is called the **AMOS Living Development Corpus (LDC)**.

The LDC is not a bag of embeddings and not a claim that all captured material is true. It preserves provenance and separates at least these semantic levels:

- **E0 Raw Evidence** — immutable primary artifacts and source receipts;
- **E1 Observations** — normalized source-grounded statements about what was observed;
- **E2 Claims** — interpretations or propositions that may later be confirmed, contradicted or superseded;
- **E3 Decisions** — explicit choices, constraints and commitments with authority and effective interval;
- **E4 Derived Knowledge** — conclusions supported by lineage to evidence, observations and decisions.

Derived layers never replace or rewrite E0 evidence.

## Decision lineage

AMOS must preserve not only the current decision but its lineage:

```text
Decision D2
  because of Evidence E7, E9
  constrained by Policy P3
  supersedes Decision D1
  validated by Run R14
  effective from T2
```

A future ContextBundle should therefore be able to answer both:

1. what is currently authoritative; and
2. why it became authoritative and what it superseded.

## Incident-to-immunity loop

A real failure in AIMETON operation should become reusable system knowledge rather than a one-off correction:

```text
incident
→ evidence capture
→ root-cause analysis
→ missing/stale/conflicting context relation identified
→ adversarial or regression fixture
→ rule/retrieval/verifier change where justified
→ golden replay
→ future detection/prevention
```

Examples include using stale infrastructure state, confusing a green CI check with end-to-end proof, repeating already completed work, losing an architectural invariant, or accepting a secondary claim that conflicts with primary evidence.

No incident may automatically modify a mandatory compatibility rule. Rule changes remain governed by versioning, evidence and replay requirements.

## Deployment progression

Life-and-Activity Learning is introduced through bounded authority stages:

1. **Shadow** — ingest and build memory/projections without changing operational decisions.
2. **Advisor** — surface conflicts, stale evidence and alternative ContextBundles to the operator.
3. **Context Provider** — provide governed ContextBundles to the working agent/operator while actions remain externally controlled.
4. **Governed Memory** — become the normal AIMETON memory substrate under compatibility and replay guarantees.
5. **Governed adaptation/action** — post-MVP; requires separate safety, authority and verification contracts.

AMOS MVP begins in Shadow mode.

## Living-stream evaluation

The living stream is useful for development but cannot by itself prove AMOS effectiveness because using the same incidents to improve and evaluate the system creates circular validation.

Therefore the evaluation topology is:

```text
Living Development Stream
    → development / fixture generation

Frozen AIMETON holdout
    → internal unseen validation

Independent pilot domains
    → replication and boundary testing
```

The preregistered external-domain replication currently includes Site Auditor and GNSS validation fixtures. No cross-domain success claim may be based only on the development stream.

## Compatibility with the C-vs-D ablation

Living-stream material may be converted into benchmark tasks only through a versioned freeze process. Once a task enters an F1 or later frozen benchmark, its expected outcome, source corpus and relevant versions are immutable for that experiment version.

For C-vs-D comparisons:

- C and D receive the same frozen task and candidate set;
- development incidents may inspire fixtures, but a fixture used to tune D must not silently remain in the unseen holdout;
- post-hoc success claims from selectively favorable living-stream cases are prohibited.

## MVP vertical slice

The first Life-and-Activity Learning slice should ingest a small real AIMETON stream and prove:

```text
source event
→ immutable evidence envelope
→ provenance
→ V/R/O/A projections
→ CR-01…CR-06 evaluation
→ shadow ContextBundle or bounded escalation
→ trace
→ later replay against changed state
```

GitHub engineering activity is the preferred first source because it already provides stable identifiers, timestamps, commits, reviews, CI receipts and explicit state transitions. Documents and conversations follow after the event/evidence contract is stable.

## Non-goals for MVP

Life-and-Activity Learning does not authorize:

- autonomous rewriting of architecture or policy;
- silent deletion or rewriting of contradictory history;
- uncontrolled model fine-tuning from live conversations;
- treating frequency or similarity as truth;
- using the living corpus as the only benchmark;
- granting AMOS mutation authority merely because it detected a pattern.

The core invariant is:

> experience may propose change; evidence, compatibility, verification and governance determine whether change becomes authoritative.
