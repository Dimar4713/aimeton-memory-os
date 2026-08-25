# aimeton-memory-os

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)

Evidence-governed, four-axis memory core and context compiler for the AIMETON Cognitive Operations Complex (AIMETON.COGOPS).

## Scope

This repository implements the bounded AMOS MVP core:

- immutable evidence and descriptor-first access;
- policy-aware ContextBundle compilation;
- four projections: scope/purpose (V), role/authority (R), ontology/state (O), and evidence/associations (A);
- deterministic compatibility checks before operational context admission;
- governed writes, verifiable actions, and replayable traces.

It is not a general RAG framework, a full fractal runtime, a graph database, or an autonomous agent executor.

## MVP boundary

The first vertical slice proves:

raw evidence → projections → compatibility checks → ContextBundle → permitted action → deterministic verification → trace and recovery.

OpenRAG is an optional document/retrieval edge. It is not the source of truth, policy engine, or final ContextBundle builder.

## Repository layout

- docs/architecture — contracts and architecture decisions
- schemas — machine-readable contracts
- src/aimeton_memory_os — implementation package
- tests — golden fixtures and deterministic validation
- scripts — local, dependency-controlled validation tools

## Status

Pre-code MVP foundation. Architectural claims are hypotheses to be evaluated by the preregistered ablation protocol.

## License and trademarks

Apache-2.0. See LICENSE and NOTICE. AIMETON names and marks are governed separately by TRADEMARKS.md.

SPDX-License-Identifier: Apache-2.0
