# Tests and fixtures

The first tests are contract-first and deterministic:

1. schema validation;
2. policy/stale/rejected leakage denial;
3. CR-01 through CR-05 compatibility outcomes;
4. escalation instead of silent fallback;
5. replay and restore-to-answer fixtures.

No external model call is a prerequisite for safety-critical acceptance.
