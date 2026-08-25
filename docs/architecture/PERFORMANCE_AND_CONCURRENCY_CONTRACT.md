# AMOS performance and concurrency contract — pre-F1 baseline

Status: normative pre-F1 contract.

This document restores the performance/concurrency boundary that was present in the v0.2 audit package but was not carried into the v0.3 repository baseline. It intentionally does **not** invent replacement numbers. The exact target and stop thresholds are experimental inputs and must be frozen in-repository before the first F1 run.

## 1. Performance envelope

The following dimensions are mandatory and must have both a target threshold and a stop threshold before F1 execution:

| Metric | Unit | Target threshold | Stop threshold | Measurement scope |
|---|---:|---|---|---|
| evidence ingest throughput | requests/s | `REQUIRED_BEFORE_F1` | `REQUIRED_BEFORE_F1` | sustained benchmark window |
| operational read throughput | requests/s | `REQUIRED_BEFORE_F1` | `REQUIRED_BEFORE_F1` | sustained benchmark window |
| vault growth | GiB/month | `REQUIRED_BEFORE_F1` | `REQUIRED_BEFORE_F1` | normalized pilot workload |
| Context Compiler latency | p95 ms | `REQUIRED_BEFORE_F1` | `REQUIRED_BEFORE_F1` | end-to-end compiler call |
| descriptor/search latency | p95 ms | `REQUIRED_BEFORE_F1` | `REQUIRED_BEFORE_F1` | candidate retrieval before LLM |
| cost | currency/month and cost/accepted-action | `REQUIRED_BEFORE_F1` | `REQUIRED_BEFORE_F1` | declared hardware/provider profile |

The F1 preregistration commit must replace every `REQUIRED_BEFORE_F1` marker with a numeric value, record the benchmark hardware/runtime profile, and identify the measurement script/fixture. F1 is invalid if any marker remains unresolved.

A successful utility result for variant D is **not** an experimental success when any mandatory stop threshold is exceeded. Performance and safety/utility gates are combined with logical AND.

## 2. Capacity escalation rule

The MVP baseline remains PostgreSQL-oriented and intentionally simple. Kafka/Redpanda, a specialized vector database, a graph database, or a different durable workflow substrate must not be adopted merely because they are conventional at scale.

Escalation to a more complex substrate requires all of the following:

1. a frozen performance threshold is exceeded on the representative workload;
2. the bottleneck is measured and attributable to the current substrate rather than a defect in implementation or benchmark setup;
3. an ADR records the evidence, migration cost and rollback path;
4. the proposed replacement is benchmarked against the same workload.

## 3. Concurrent-write boundary

For the MVP and F1 experiment there is exactly **one authoritative writer per active scope**.

Writes must use transactional persistence plus idempotency/outbox semantics where applicable. A second writer attempting to mutate the same active authoritative scope must not silently overwrite the first writer.

Required outcome:

```text
concurrent authoritative mutation
→ detect ownership/version conflict
→ hold_conflict
→ no silent last-write-wins
→ preserve both attempted operations and provenance for review/replay
```

`hold_conflict` is an operational safety state, not a successful write.

Multi-writer lease/fencing protocols, CRDT semantics and active-active authoritative mutation are explicitly post-MVP research. Passing F1 cannot be used to claim production readiness for those modes.

## 4. Relation to CR-06

The single-writer rule controls **who may mutate an active scope**. CR-06 controls **whether one compatibility evaluation observed a coherent set of versions**. They are complementary and neither substitutes for the other.

Even with one authoritative writer, a read/evaluation can race with a committed state transition. Therefore ContextBundle admission still requires snapshot/version coherence.

## 5. Preregistration and change control

Before F1, the repository must contain a committed experiment envelope with:

- all numeric target and stop thresholds;
- benchmark hardware/runtime profile;
- dataset/corpus identifier;
- measurement commands or fixtures;
- policy/model/verifier/registry versions;
- change-control rule stating that thresholds cannot be relaxed after result inspection.

Any threshold change after the first result is observed creates a new experiment version and requires a fresh run set. Historical runs remain reportable and must not be discarded.
