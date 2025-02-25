# API: Получение категорий с опубликованными блюдами

## Описание

В данном репозитории реализован класс представления, который для данного API `127.0.0.1/api/v1/foods/` возвращает
выборку в которую попадают только блюда у которых `is_publish=True`
Например, если в базе данных имеются следующие данные:

- **Напитки**:
  - Чай (`is_publish=True`)
  - Кола (`is_publish=True`)
  - Спрайт (`is_publish=False`)

- **Выпечка**:
  - Булочка (`is_publish=False`)
  - Пирожок (`is_publish=False`)

- **Мясо**:
  - Отбивная (`is_publish=True`)

То возвращаемый JSON-ответ будет:
```json
[
    {
        "id": 1,
        "name_ru": "Напитки",
        "name_en": null,
        "name_ch": null,
        "order_id": 10,
        "foods": [
            {
                "internal_code": null,
                "code": 123,
                "name_ru": "Чай",
                "description_ru": null,
                "description_en": null,
                "description_ch": null,
                "is_vegan": false,
                "is_special": false,
                "cost": "123.00",
                "additional": []
            },
            {
                "internal_code": null,
                "code": 12,
                "name_ru": "Кола",
                "description_ru": null,
                "description_en": null,
                "description_ch": null,
                "is_vegan": false,
                "is_special": false,
                "cost": "12.00",
                "additional": []
            }
        ]
    },
    {
        "id": 3,
        "name_ru": "Мясо",
        "name_en": null,
        "name_ch": null,
        "order_id": 10,
        "foods": [
            {
                "internal_code": null,
                "code": 1,
                "name_ru": "Отбивная",
                "description_ru": null,
                "description_en": null,
                "description_ch": null,
                "is_vegan": false,
                "is_special": false,
                "cost": "123.00",
                "additional": []
            }
        ]
    }
]
