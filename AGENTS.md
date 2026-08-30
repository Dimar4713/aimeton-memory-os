# AGENTS.md

## Scope

Эти правила обязательны для всего `aimeton-memory-os`. Более узкий `AGENTS.md` MAY усиливать, но не ослаблять их.

Каноническое AIMETON-wide governance-ядро: `Dimar4713/aimeton-architecture/AGENTS.md`.

## Repository mission

AMOS реализует bounded MVP evidence-governed memory core и ContextBundle compiler для AIMETON.COGOPS. Это не общий RAG framework, не автономный agent executor и не доказанный полный Memory OS до прохождения preregistered validation/ablation gates.

Локальные источники истины: `README.md`, `docs/architecture/`, `schemas/`, tests/evidence, связанные Issues/PR и текущий exact `main` SHA.

## Before work

1. Прочитать этот файл, README, применимые architecture/contracts/schemas, status/evidence и активные Issues/PR/CI.
2. При межрепозиторной работе прочитать корневые `AGENTS.md` всех затрагиваемых репозиториев до первой mutation.
3. Для runner/deployment reality читать `aimeton-infrastructure`; для normative AIMETON decisions — `aimeton-architecture`.
4. Явно различать `hypothesis != normative intent != implementation != observed runtime != validated evidence`.

## 3×3 Reality Check

Перед blocker, root-cause, strong architectural claim, compatibility decision, security/cost decision или consequential write первое объяснение считается гипотезой.

Проверить:

- architecture/lifecycle;
- alternatives/control paths;
- history/live;
- source/contract;
- runtime/live;
- independent evidence;
- falsification attempt.

Нельзя объявлять AMOS-свойство доказанным только потому, что его описывает собственный документ или тест, построенный из той же гипотезы.

## GitHub / execution fallback

До просьбы о ручном действии владельца проверить:

`GitHub connector/API → AIMETON GitHub MCP/router → REST/GraphQL/gh через trusted AIMETON server → owner`.

`private repo`, `нет доступа`, `невозможно`, `нужен пользователь` до этой проверки являются provisional claims.

Секреты и credential values не публикуются. Сначала переиспользовать существующие AIMETON auth/secret contracts.

## Continuous Mission / Motor State

```text
READ → DECIDE → ACTION → READ-BACK → EVIDENCE → NEXT SAFE ACTION
```

После каждого material action проверить фактический результат и выполнить следующий безопасный шаг при отсутствии objective authority blocker. Отсутствие нового сообщения владельца не является blocker.

Поддерживать очередь current → next → following.

Перед завершением tool-сессии обязательны MOTOR-CHECK и STOP-CHECK. GREEN CI, PR, schema validation или успешный unit test не завершают mission, если critical-path acceptance/evidence ещё отсутствует.

## Memory / evidence truth boundary

- Original evidence/provenance является сильнее производного индекса, summary или retrieval projection.
- Descriptor/projection/context bundle не становится source of truth только потому, что его создал AMOS.
- Compatibility Registry, authority/policy и evidence association должны быть детерминированно воспроизводимы.
- Cross-repo evidence/projections MUST pin canonical repository, exact source SHA, source path, immutable blob/object id и/или content digest.
- Generated projection без drift gate не считается актуальной.
- OpenRAG и иные retrieval edges не получают скрытого policy/source-of-truth authority.

## Runner / infrastructure boundary

Persistent CI и future shared-burst placement принадлежат AIMETON runner placement contract. Не создавать выделенный compute или локальный autoscaler только для удобства AMOS.

Runner lifecycle/inventory/controller authority находится в `aimeton-infrastructure`; изменения workload placement выполняются через классификацию и canonical contract, а не hardcoded runner identity.

## Security / authority

Без owner authorization запрещены новые расходы, необратимые production/provider writes, ослабление evidence/policy/security gates, изменение license/trademark boundary и публикация private/secrets material.

## Definition of Done

Применимые пункты обязательны:

- source/schema/tests synchronized;
- exact-SHA CI/read-back verified;
- docs/status/evidence updated;
- hypothesis vs validated claim marked honestly;
- cross-repo provenance/drift checked;
- next safe action выполнен либо зафиксирован exact blocker;
- strong conclusions прошли 3×3.
