# AIMETON.COGOPS compatibility registry v0.3

A candidate claim or action has four projections:

- V: scope and purpose;
- R: actor, authority and responsibility;
- O: typed entity, state and validity;
- A: evidence, precedent and associations.

The current mandatory checks are:

- CR-01 scope alignment;
- CR-02 authority binding;
- CR-03 ontology/status validity;
- CR-04 primary-evidence support;
- CR-05 temporal coherence.

Each result is satisfied, unresolved, blocked, or conflict and includes a reason code plus source/policy references. A high association score cannot compensate for a failed mandatory check. An unresolved, blocked, or conflicting result produces bounded escalation rather than a misleading operational ContextBundle.

Rule additions or semantic changes require a versioned ADR, adversarial fixtures, and golden-trace replay.
