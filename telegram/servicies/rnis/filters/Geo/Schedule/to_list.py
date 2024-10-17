from ....request import Request


def to_list(**d):
    json = Request.Body.default()            # Дефолтный JSON
    Request.Body.token(json, d.get('token')) # token
    Request.Body.filters(json, 'withRoute', d.get('route_uuid'))
    Request.Body.filters(json, 'withDate', d.get('date'))
    Request.Body.filters(json, 'withComponent', d.get('component', 'kiutr'))
    Request.Body.filters(json, 'withoutGeometry', d.get('geometry', True))
    Request.Body.column_search(json, 'schedule_status_uuid', d.get('status')) # Поиск по колонке

    # Request.Body.filters(json)               # Пустые фильтры
    # Request.Body.filters(json, 'key', d.get('key')) # Фильтры по ключу можно добавить функции 'to_str', 'to_list'
    # Request.Body.order(json)          # Дефолтная сортировка по UUID
    # Request.Body.order(json, d.get('column'), d.get('direction')) # Сортировка по заданным параметрам
    # Request.Body.pagination(json)     # Дефолтная пагинация
    # Request.Body.column_search(json, 'key', d.get('key')) # Поиск по колонке
    # Request.Body.payload(json, 'key', d.get('key')) # Добавить данные в вывод
    # Request.Body.response_data(json)  # Дефолтный вывод атрибутов в списке ["items/uuid"]

    Request.Body.pagination(json, d.get('page'), d.get('limit', 300))   # Пагинация по заданным параметрам
    Request.Body.response_data(json, d.get('response_data'))  # Вывод атрибутов в списке заданные пользователем
    # print(j.dumps(json, indent=4, ensure_ascii=False))
    return json