"""Original teaching code. Structural/quotation checks are not semantic truth checks."""
from copy import deepcopy
import json
from pathlib import Path

FIXTURES = Path(__file__).resolve().parents[1] / 'fixtures'
DEMO_TEXT = (FIXTURES / 'note.txt').read_text(encoding='utf-8').strip()
DEMO_CARD = json.loads((FIXTURES / 'demo-card.json').read_text(encoding='utf-8'))
LABELS = {'meeting_time': 'Время встречи', 'meeting_date': 'Дата встречи',
          'price_rub': 'Стоимость, RUB', 'participants': 'Участники',
          'join_link': 'Ссылка', 'followup': 'Следующее действие'}
ITEM_SCHEMA = {'type': 'object', 'properties': {
    'value': {'type': ['string', 'null']}, 'quote': {'type': ['string', 'null']}},
    'required': ['value', 'quote'], 'additionalProperties': False}
SCHEMA = {'type': 'object', 'properties': {k: deepcopy(ITEM_SCHEMA) for k in LABELS},
          'required': list(LABELS), 'additionalProperties': False}


class InputError(ValueError):
    pass


class OutputError(ValueError):
    pass


def clean_text(text):
    if not isinstance(text, str) or not text.strip() or len(text) > 8000:
        raise InputError('Нужен непустой текст до 8000 символов.')
    return text.strip()


def validate_card(card, source):
    if not isinstance(card, dict) or set(card) != set(LABELS):
        raise OutputError('Ответ не содержит ровно шесть ожидаемых полей.')
    for key, item in card.items():
        if not isinstance(item, dict) or set(item) != {'value', 'quote'}:
            raise OutputError('У каждого поля должны быть value и quote.')
        value, quote = item['value'], item['quote']
        if value is None:
            if quote is not None:
                raise OutputError('У неизвестного поля value и quote должны быть null.')
            continue
        if not isinstance(value, str) or not value.strip() or len(value) > 1000:
            raise OutputError('Некорректное значение поля.')
        if not isinstance(quote, str) or not quote.strip() or len(quote) > 2000 or quote not in source:
            raise OutputError('Подтверждающая цитата не найдена в исходном тексте.')
    return deepcopy(card)


def demo_extract(text):
    source = clean_text(text)
    if source != DEMO_TEXT:
        raise InputError('Деморежим знает только учебный пример. Загрузите пример или подключите свой Ollama.')
    return validate_card(DEMO_CARD, source)
