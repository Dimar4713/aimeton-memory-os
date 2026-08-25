# AMOS: контракт расширяемости sovereign security v0.1

## Решение

MVP не реализует секретный/ГОСТ-контур. Однако все authoritative интерфейсы AMOS обязаны быть совместимы с его последующим подключением без миграции raw evidence, Ledger, Descriptor Fabric, Context Compiler или OpenRAG-adapter.

## Неподвижные стыки

Каждый `Artifact`, `Infoblock`, `DerivedArtifact`, `ExperienceSnapshot` и элемент `ContextBundle` имеет версионируемый `SecurityLabel`:

`classification`, `compartment`, `tenant/scope`, `handling_profile`, `retention`, `export_rule`, `processing_zone`, `policy_version`.

Policy decision всегда принимает вход `subject + requested action + resource/version/span + runtime zone + purpose + policy version` и возвращает `allow | deny | redact | escrow | escalate` с audit trace.

Производный артефакт наследует наиболее строгие ограничения всех источников; ослабление метки требует отдельного human-approved policy event. Индексы, кэши, embeddings, summaries и traces не являются обходом policy.

`ContentAccess` отделён от `DescriptorAccess`: metadata может быть видима по отдельной политике, байты и смысловые spans — только после разрешения на content access. Context Compiler получает лишь разрешённые либо редактированные projections.

## Профили, а не fork архитектуры

`security_profile=baseline` — текущий MVP.

`security_profile=sovereign_gost` — будущий адаптер: isolated processing zone, certified crypto/KMS/HSM adapters, key references, controlled export and mandatory audit. AMOS хранит ссылки на key/policy receipts, но не ключи и не криптографическую реализацию.

Переход профиля возможен только для новых или переупакованных объектов через versioned migration; история и provenance сохраняются.

## Запрещено уже сейчас

- зашивать ACL только в OpenRAG, vector DB или UI;
- включать содержимое закрытого объекта в общий embedding/cache/log;
- давать LLM право менять label, policy, key reference или export rule;
- считать алгоритм ГОСТ заменой сертифицированного защищённого контура.

## P0 acceptance fixtures

1. Denied atom не появляется в bundle, cache, trace или retrieval ranking.
2. Restrictive raw source делает restrictive каждый derived artifact.
3. Redacted projection доступна без расшифрования исходника.
4. Тот же ledger replay при другой policy version даёт воспроизводимо иной allow/deny trace.
5. `sovereign_gost` profile подключается через adapter contract, без изменения доменных schemas.
