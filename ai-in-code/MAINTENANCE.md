# Правила развития инженерного маршрута / Engineering pathway maintenance

Version 0.8 · 2026-09-28 · Scope: `ai-in-code/`, `engineers/`, their public entry links.

## RU

Поручение владельца от 28.09.2026: приглашение инженерам и путь обучения должны быть доступны на русском и английском, по отдельным ссылкам. Это правило относится к данному инженерному направлению; оно не объявляет все старые материалы репозитория переведёнными.

1. Сохранять текущие русские URL. Английская пара — файл с `.en.md`. В каждой паре есть переключатель языка и одинаковые критерии результата.
2. При изменении требований менять связанные главы, приглашение и обе карты. Не повышать требования в одном языке незаметно для другого.
3. У каждой главы: входные навыки, объяснение, первичные источники и точные разделы, практика, негативный случай, самостоятельное изменение, критерий готовности и следующий шаг.
4. Проверять действующие API/SDK по первичным источникам. Указывать дату и ограничение проверки. Не путать документацию, mock, live-интеграцию и опыт эксплуатации.
5. Сначала сохранить исходную версию/commit; работать изолированно; не перезаписывать соседние учебные маршруты без причины. При недоступном локальном каноническом Git отмечать интеграцию как PENDING.
6. Не размещать личные данные кандидатов, секреты и клиентские документы. Не выдумывать оплату, место работы, обязательства и результаты обучения.
7. Перед выпуском: проверить пары RU/EN, относительные ссылки, команды, тесты и доступность опубликованной ветки; обновить changelog, validation и указатели.
8. Улучшать по реальным затруднениям: наблюдение → причина → изменение → повторная проверка. Количество написанных страниц не является доказательством эффективности обучения.

## EN

Owner instruction, 28 September 2026: engineering invitations and the learning path must be available in Russian and English through separate links. This policy applies to this engineering track; it does not claim that all older repository content is translated.

1. Preserve existing Russian URLs. Use `.en.md` counterparts with language switches and equivalent outcome criteria.
2. Update requirements, related chapters, invitations, and both maps together. Do not silently raise requirements in one language only.
3. Each chapter needs prerequisites, an explanation, primary sources with reading guidance, practice, a negative case, an independent variation, a completion gate, and a next step.
4. Check current APIs/SDKs against primary sources and record review limits. Keep documentation, mocks, live integrations, and operational experience distinct.
5. Preserve the starting commit and work in isolation. Avoid unrelated changes to older tracks. When the canonical local Git node is unavailable, record local integration as PENDING.
6. Exclude candidate personal data, credentials, and client material. Do not invent pay, location, commitments, or learner outcomes.
7. Before release, check RU/EN pairs, relative links, commands, tests, and the published branch. Update the changelog, verification record, and navigation.
8. Improve from observed difficulty: observation → cause → change → retest. Page count does not establish educational effectiveness.

[RU](README.md) · [EN](README.en.md) · [Verification](VALIDATION.md)
