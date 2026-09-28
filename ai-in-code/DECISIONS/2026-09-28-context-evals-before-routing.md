# Context engineering + early evals before routing / Контекст и ранние evals до роутинга

Date: 2026-09-28 · Version: 0.8.1 · Scope: AI engineering curriculum, RU/EN.

## RU — решение и причина

Обратная связь по программе: добавить context engineering и познакомить с evals хотя бы частично до routing, чтобы выбор модели объяснялся качеством, а не только ценой. Автор стороннего отзыва не установлен; личные данные и предположения об авторстве не публикуются.

В версии 0.8 критерии качества и baseline уже упоминались, но отдельный развёрнутый eval-блок стоял на этапе 09, после routing на этапе 04. Для ученика зависимость «сначала измерение — затем выбор» была недостаточно явно выражена.

Принято: сохранить 16 основных этапов и существующие URL; встроить обязательный практикум 03A внутрь этапа 03. Новый порядок: API → контекст → небольшие evals → матрица возможностей по типам задач → routing. Этап 09 остаётся углублением: системные регрессии, tools/retrieval и свежие held-out данные. Не переносим всю сложную оценку в самое начало и не дублируем старые курсы.

Правило учебного router: допустимость данных/возможностей и обязательные требования → достаточное качество на нужном классе → обоснованный компромисс стоимости/задержки/дополнительного качества. Нет подходящего варианта — уточнение, остановка или человек. Fallback не может молча снижать обязательный уровень качества или обходить права.

Альтернативы: оставить только предупреждение в 04 (мало практики); перенести весь 09 вперёд (часть заданий зависит от ещё не построенных tools/RAG); разделить раннюю и системную оценку (выбрано).

Методика: понятия сверены с первичными источниками, перечисленными в 03A. Конкретные упражнения, размеры набора и правила допуска — учебный дизайн. Реального сравнения моделей и проверки эффекта обучения этим изменением не выполнено.

Проверка следующего цикла: ученик должен объяснить выбор маршрута своей матрицей качества и показать, что дешёвая непригодная или дорогая запрещённая модель не выбирается. Пользу изменения проверять по прохождению, а не по объёму текста.

## EN — decision and rationale

Curriculum feedback requested explicit context engineering and introductory evals before routing so that model choice is justified by quality as well as price. No external feedback author has been identified or attributed.

Version 0.8 mentioned criteria and baselines but placed its detailed evaluation chapter at stage 09, after stage-04 routing. The prerequisite relationship was not explicit enough for learners.

Keep the 16 core stages and existing URLs. Add required companion 03A within stage 03: API → context → small evals → task-category capability matrix → routing. Keep stage 09 for system regressions, tools/retrieval, and fresh held-out data. This avoids moving advanced dependent work too early or duplicating older courses.

Router policy: data/capability eligibility and mandatory constraints → sufficient task-specific quality → justified cost/latency/additional-quality trade-off. If no candidate qualifies, clarify, stop, or involve a person. Fallback cannot silently lower mandatory quality or bypass permissions.

Alternatives: a warning in 04 alone (insufficient practice); move all of 09 earlier (depends on later integrations); split introductory and system-level evaluation (selected).

Concepts were checked against the primary references in 03A. Exercises, dataset sizes, and admission policies are course design, not observed model comparisons. No live-model or learner-outcome validation is claimed.

Next check: a learner can justify routing from measured quality and demonstrate rejection of a cheap inadequate or a capable prohibited model. Evaluate the change through actual learning evidence, not page count.

## Change boundary / Граница изменения

Starting public work-branch commit: `5b67e81c9e70464934a064f0c136ee677b56d127`.
Backup: `backup/chatgpt/20260928-before-context-evals`.
Target: `work/chatgpt/20260928-ai-in-code`; local canonical integration remains PENDING.
Only curriculum/navigation/recruitment documentation is changed. No runtime implementation, permission, learner identity, or private letter is modified. Existing v0.8 lab results remain historical, not a new test run. Full checkout could not be fetched in this environment (DNS resolution failure); no full-tree automated link check is claimed.

[RU pathway](../README.md) · [EN pathway](../README.en.md)
