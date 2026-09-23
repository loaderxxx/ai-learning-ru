# Источники маршрута разработчика

Проверены 23 сентября 2026. Здесь официальные описания школ, документация авторов технологий и первичные исследования. Описания школ — их собственные заявления, а не независимая оценка качества. Мы не переносим полные курсы и не подтверждаем их прохождение.

## Школы и образовательные подходы

| ID | Источник | Что помогает проверить |
|---|---|---|
| S01 | [Школа 21: главная](https://21-school.ru/) | Бесплатная школа от Сбера, peer learning; в каталоге есть ИИ-инженер. |
| S02 | [Школа 21: программа и платформа](https://21-school.ru/training-and-platform) | Проекты, взаимная проверка, автоматическая проверка кода; открытая страница не раскрывает все задания. |
| S03 | [Школа 21: модуль ИИ-агентов, 17.12.2025](https://21-school.ru/news/skola-cifrovyx-texnologii-skola-21-otkrylas-v-permi-ucastniki-smogut-besplatno-osvoit-vostrebovannye-it-navyki-i-novyi-modul-po-sozdaniiu-ii-agentov) | Объявлен модуль создания агентов на ГигаЧат для всех кампусов; фактическое прохождение конкретной волной не проверено. |
| S04 | [42: концепция](https://42.fr/en/what-is-42/42-program-explained/) | Бесплатная проектная подготовка; французский аналог, который описал пользователь. |
| S05 | [42: программа](https://42.fr/en/the-program/software-engineer-degree/) | Общее ядро и специализации, включая ИИ; в перечне есть CI и тестирование. |
| S06 | [42: методика](https://42.fr/en/the-program/innovative-learning/) | Обучение и оценивание через проекты и взаимодействие учащихся. |
| S07 | [Codam FAQ](https://www.codam.nl/en/faq/) | После основ заявлены AI/ML и приложения/агенты на основе LLM. |
| S08 | [Hive: программа](https://www.hive.fi/studies/curriculum/) | Три модуля: основы на Go, full stack, углубление; это актуальная страница, не старый пересказ программы на C. |
| S09 | [Hive: модель обучения](https://www.hive.fi/) | Бесплатная очная проектная программа с взаимной проверкой; ИИ входит в описание подхода. |
| S10 | [01Edu: AI-native curriculum](https://01edu.ai/solutions/ai-native-curriculum/) | Peer-to-peer и проектная программа с ИИ; не доказательство одинакового состава и стоимости во всех кампусах. |
| S11 | [Holberton: каталог](https://hbtn.dev/programs) | В каталоге есть AI for Developers, ML/AI, backend и другие направления; детали кампусов различаются. |
| S12 | [Recurse Center](https://www.recurse.com/about) | Бесплатный самостоятельный retreat для уже умеющих программировать, без единой учебной программы. |
| S13 | [The Odin Project: маршруты](https://www.theodinproject.com/paths) | Foundations, Full Stack JavaScript и Ruby on Rails; самостоятельный веб-маршрут, не кампусная школа P2P. |
| S14 | [Full Stack Open](https://fullstackopen.com/en/) | Открытый курс современной веб-разработки; полезен как справочный маршрут по веб-основам. |
| S15 | [Хекслет: каталог](https://ru.hexlet.io/courses) | Заявлены ИИ для разработчиков и LLM-разработчик; следовательно, сама AI-тема не уникальна. |
| S16 | [Яндекс Практикум: каталог](https://practicum.yandex.ru/) | Контрольная группа профессиональных онлайн-программ; полный платный учебный план не изучен. |

## Технологии и инженерные исследования

| ID | Источник | Для какого вопроса |
|---|---|---|
| T01 | [Cursor: Rules](https://cursor.com/docs/rules) | Правила проекта и AGENTS.md задают контекст агенту; не являются механизмом изоляции. |
| T02 | [OpenAI: structured outputs](https://developers.openai.com/api/docs/guides/structured-outputs) | Структурный ответ ограничивает формат; смысловые ошибки остаются возможными. |
| T03 | [OpenAI: function calling](https://developers.openai.com/api/docs/guides/function-calling) | Модель предлагает вызов функции; приложение обрабатывает аргументы и результат. |
| T04 | [Claude: tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) | Описание инструментов и обмен результатами вызовов; формат конкретного провайдера. |
| T05 | [Gemini: function calling](https://ai.google.dev/gemini-api/docs/function-calling) | Функции и схемы в Gemini API; не взаимозаменяемость SDK с другими провайдерами. |
| T06 | [GigaChat API](https://developers.sber.ru/docs/ru/gigachat/guides/main) | Официальная точка входа в интеграцию ГигаЧат; доступ и тариф участник проверяет самостоятельно. |
| T07 | [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) | Предсказуемые workflows и более динамические agents решают разные задачи. |
| T08 | [OpenAI: evals](https://developers.openai.com/api/docs/guides/evals) | Критерии и набор примеров для оценки; это не готовая метрика качества нашего продукта. |
| T09 | [Claude: develop tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests) | Сначала определить успех и способы его измерения. |
| T10 | [Sentence Transformers: retrieve and rerank](https://sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html) | Поиск кандидатов и повторное ранжирование — разные стадии. |
| T11 | [MCP specification](https://modelcontextprotocol.io/specification/2026-07-28) | Прочитанная редакция использует JSON-RPC, инструменты и контекст; per-request metadata отличается от старых редакций. |
| T12 | [MCP transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports) | stdio и Streamable HTTP; старые handshake-сценарии требуют проверки совместимости. |
| T13 | [MCP authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) | HTTP authorization, целевая аудитория токена и права; stdio имеет другой контекст доступа. |
| T14 | [MCP security practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices) | Границы доверия и безопасность интеграций. |
| T15 | [A2A specification](https://a2a-protocol.org/latest/specification/) | Agent Card, задача, сообщения и результат работы внешнего агента; latest — изменяемая ссылка. |
| T16 | [OpenAPI specification](https://spec.openapis.org/oas/latest.html) | Описание HTTP API; просмотренная latest показывает 3.2.1, учебный контракт может использовать явно выбранную 3.1.0. |
| T17 | [JSON Schema objects](https://json-schema.org/understanding-json-schema/reference/object) | Поля, обязательность и дополнительные свойства; схема не доказывает истинность значений. |
| T18 | [OWASP LLM01 prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) | Инструкции могут попадать через пользовательский ввод или внешние документы, в том числе RAG. |
| T19 | [GitHub: Python CI](https://docs.github.com/en/actions/tutorials/build-and-test-code/python) | Автоматический запуск Python-проверок в workflow; права и версии требуют отдельной настройки. |
| T20 | [OpenTelemetry observability primer](https://opentelemetry.io/docs/concepts/observability-primer/) | Логи, метрики и трассировки помогают разбирать поведение системы. |
| R01 | [METR: early-2025 developer RCT](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) | В конкретном эксперименте 16 разработчиков и 246 задач использование тогдашних ИИ-инструментов увеличило время на 19%; не универсальный эффект. |
| R02 | [METR: update 24.02.2026](https://metr.org/blog/2026-02-24-uplift-update/) | Авторы считают последующую оценку слабой из-за отбора участников/задач и измерения времени; не переносить результат 2025 на все инструменты 2026. |

## Как читать ссылки

`latest` может измениться. Для своей реализации запишите фактическую редакцию протокола, SDK, модель и дату проверки. Разница между прочитанной документацией и возможностями выбранного клиента — предмет проверки совместимости. Наличие страницы не подтверждает доступность сервиса в вашей стране или аккаунте.

В учебном коде нет внешних API-вызовов. Примеры интеграции с моделью и протоколами, которые вы выполните сами, требуют отдельной проверки. Набор школ — сравнительный срез 11 школ, сетей и учебных инициатив, а не перепись всех школ мира.

[Маршрут разработчика](README.md) · [На главную](../README.md)
