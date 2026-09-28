# Проверка выпуска / Release verification

Version 0.8 · Review date 2026-09-28.

[Русская программа](README.md) · [English pathway](README.en.md) · [Machine-readable lab record](lab/validation.json)

## RU — что подготовлено

16 учебных этапов с полными парами RU/EN: объяснения, источники, задания, негативные проверки, самостоятельные изменения и критерии. Два приглашения инженерам, две карты пути, рабочая тетрадь, словарь/помощь и общие двуязычные правила/источники. Это развёрнутый учебный путь; он не означает, что за ученика реализованы все внешние интеграции.

Сохранены старые русские маршруты developers, advanced, practical и next. Их структура и точки связи изучены; полной повторной построчной проверки и повторного запуска всех старых лабораторий в этом выпуске не проводилось. Отчёты прежних выпусков остаются историческими, а не новыми результатами.

## RU — фактически выполнено

- Новый `lab/core.py` запущен локально в среде подготовки, Python 3.13.5, стандартная библиотека, без сети и ключей.
- `python -m unittest discover -s <lab> -p 'test_*.py' -v`: **30 тестов, 30 прошли, 0 ошибок/провалов**. Исходные Git blob SHA указаны в `lab/validation.json` для проверки совпадения опубликованного кода.
- Демо: `mode=mock`, `status=answered`, запасная заглушка, три модельные попытки, результат вычисления 1000 центов. Текст финального ответа заранее записан в сценарии.
- Проверены в тестах: строгие аргументы, запрет неизвестного tool и чужой записи, передача call ID, ограничение шагов/попыток, допустимый fallback, отсутствие fallback при запрете, повтор call ID и конфликт аргументов, отсутствие вымышленного секрета в событийному журнале/ошибке.
- Первичные источники изучены в границах, указанных в [реестре источников](SOURCES.md).

## RU — что не подтверждено

Живые модели и их качество; реальные provider SDK; MCP runtime; embeddings/RAG; настоящий сетевой deadline; SQLite/idempotency после рестарта; HTTP/UI; Docker; удалённый CI; реализации TypeScript/C#/Java; прохождение учениками; найм и коммерческие условия. Это задания программы, а не функции готового стартового стенда.

Фильтрация чужой записи в mock-тесте проверяет серверное правило, не устойчивость настоящей модели ко всем prompt injection. Проверка формы финального текста не доказывает его истинность. Синхронный лимит шагов не прерывает зависший внешний вызов.

Материалы сохраняются в публичной рабочей ветке `work/chatgpt/20260928-ai-in-code`. Доступность этой ветки и интеграция в `main` — разные состояния. Локальный канонический Git-узел в этом сеансе недоступен; его интеграция остаётся PENDING.

## EN — prepared

Sixteen teaching stages with complete RU/EN counterparts: explanations, sources, exercises, negative checks, independent variations, and completion criteria. Two engineering invitations and pathway maps, paired workbooks and troubleshooting pages, and shared bilingual maintenance/source records. This is an expanded learning pathway, not a claim that every external integration has already been implemented for the learner.

Older Russian developers, advanced, practical, and next tracks are preserved. Their structure and connection points were reviewed; this release does not claim a complete line-by-line re-audit or rerun of every older lab. Earlier verification reports remain historical evidence.

## EN — executed

- The new `lab/core.py` ran locally in the preparation environment using Python 3.13.5 and only the standard library, without credentials or network calls.
- Test discovery completed **30 tests: 30 passed, no failures/errors**. Tested source Git blob hashes are recorded in `lab/validation.json` for comparison with published contents.
- The demo returned `mode=mock`, `status=answered`, the backup script, three model attempts, and a calculated total of 1000 cents. Its final sentence is predefined.
- Tests cover strict arguments, unknown tools, tenant denial, call-ID correlation, call/step limits, transient-only fallback, repeated IDs/conflicting arguments, and exclusion of fictional secrets from event/error output.
- Primary sources were reviewed within the scope described in [SOURCES](SOURCES.md).

## EN — not verified

Live models or their quality; provider SDK execution; MCP runtime; embeddings/RAG; real network deadlines; restart-safe SQLite idempotency; HTTP/UI; Docker; remote CI; TypeScript/C#/Java implementations; learner outcomes; hiring or commercial terms. These are course assignments, not implemented features of the starter lab.

A mocked cross-tenant test verifies an application boundary, not universal model prompt-injection resistance. Structurally valid final text is not necessarily factual. A synchronous step cap does not interrupt a hung external call.

The release uses the public work branch `work/chatgpt/20260928-ai-in-code`. Branch availability is distinct from integration into `main`. The canonical local Git node is unavailable in this session; local integration remains PENDING.
