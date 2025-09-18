# API Документация - Медиа-покрытие

## Обзор

API для управления медиа-покрытием Салымбековского университета с поддержкой трех языков (русский, кыргызский, английский).

Base URL: `/api/media-coverage/`

## Эндпоинты

### Категории медиа

#### Получить список категорий
```
GET /api/media-coverage/categories/
```

**Ответ:**
```json
[
  {
    "id": 1,
    "name": "tv",
    "slug": "tv",
    "icon": "📺",
    "name_ru": "Телевидение",
    "name_kg": "Телевидение", 
    "name_en": "Television",
    "description_ru": "Телевизионные сюжеты и интервью",
    "description_kg": "Телевизиялык сюжеттер жана интервьюлар",
    "description_en": "Television stories and interviews",
    "is_active": true,
    "created_at": "2025-09-18T10:00:00Z"
  }
]
```

#### Получить категорию по slug
```
GET /api/media-coverage/categories/{slug}/
```

### Медиа-издания

#### Получить список изданий
```
GET /api/media-coverage/outlets/
```

**Параметры:**
- `search` - поиск по названию или сайту
- `default_category` - фильтр по категории

**Ответ:**
```json
[
  {
    "id": 1,
    "name": "ktrk",
    "slug": "ktrk",
    "name_ru": "КТРК",
    "name_kg": "КТРК",
    "name_en": "KTRK",
    "description_ru": "",
    "description_kg": "",
    "description_en": "",
    "website": "https://ktrk.kg",
    "email": null,
    "phone": "",
    "logo": null,
    "logo_url": null,
    "logo_url_or_default": null,
    "default_category": {
      "id": 1,
      "name_ru": "Телевидение",
      "name_kg": "Телевидение",
      "name_en": "Television",
      "slug": "tv",
      "icon": "📺"
    },
    "total_articles": 5,
    "is_active": true,
    "created_at": "2025-09-18T10:00:00Z"
  }
]
```

#### Получить издание по slug
```
GET /api/media-coverage/outlets/{slug}/
```

### Теги

#### Получить список тегов
```
GET /api/media-coverage/tags/
```

**Ответ:**
```json
[
  {
    "id": 1,
    "name_ru": "Медицина",
    "name_kg": "Медицина",
    "name_en": "Medicine",
    "slug": "medicina",
    "color": "#E53E3E",
    "usage_count": 15,
    "is_active": true,
    "created_at": "2025-09-18T10:00:00Z"
  }
]
```

### Медиа-публикации

#### Получить список публикаций
```
GET /api/media-coverage/articles/
```

**Параметры:**
- `search` - поиск по заголовку, описанию, содержанию
- `category` - фильтр по категории
- `outlet` - фильтр по изданию
- `sentiment` - фильтр по тональности (positive, neutral, negative)
- `importance_score` - фильтр по важности
- `is_featured` - только рекомендуемые
- `is_verified` - только проверенные
- `ordering` - сортировка (-publication_date, importance_score, views_count, etc.)

**Ответ:**
```json
{
  "count": 30,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "title_ru": "Студенты СУ завоевали первое место в медицинской олимпиаде",
      "title_kg": "СУ студенттери медициналык олимпиадада биринчи орунду ээледи",
      "title_en": "SU students won first place in medical olympiad",
      "slug": "media-article-1",
      "description_ru": "Краткое описание медиа-публикации 1...",
      "description_kg": "Медиа басылманын 1 кыскача баяндамасы...",
      "description_en": "Brief description of media publication 1...",
      "category": {
        "id": 1,
        "name_ru": "Телевидение",
        "name_kg": "Телевидение",
        "name_en": "Television",
        "slug": "tv",
        "icon": "📺"
      },
      "outlet": {
        "id": 1,
        "name_ru": "КТРК",
        "name_kg": "КТРК",
        "name_en": "KTRK",
        "slug": "ktrk",
        "logo_url_or_default": null
      },
      "tags": [
        {
          "id": 1,
          "name_ru": "Медицина",
          "name_kg": "Медицина",
          "name_en": "Medicine",
          "slug": "medicina",
          "color": "#E53E3E"
        }
      ],
      "image": null,
      "image_url": null,
      "image_url_or_default": null,
      "original_url": "https://ktrk.kg/news/article-1",
      "publication_date": "2025-09-13",
      "importance_score": 8,
      "sentiment": "positive",
      "views_count": 234,
      "is_published": true,
      "is_featured": true,
      "is_verified": true,
      "created_at": "2025-09-18T10:00:00Z"
    }
  ]
}
```

#### Получить публикацию по slug
```
GET /api/media-coverage/articles/{slug}/
```

Возвращает детальную информацию включая полное содержание, автора, журналиста и другие поля.

#### Создать новую публикацию
```
POST /api/media-coverage/articles/
```

**Тело запроса:**
```json
{
  "title_ru": "Заголовок на русском",
  "title_kg": "Заголовок на кыргызском",
  "title_en": "Title in English",
  "slug": "unique-slug",
  "description_ru": "Описание на русском",
  "description_kg": "Описание на кыргызском", 
  "description_en": "Description in English",
  "category": 1,
  "outlet": 1,
  "original_url": "https://example.com/article",
  "publication_date": "2025-09-18",
  "importance_score": 5,
  "sentiment": "positive",
  "tag_ids": [1, 2, 3]
}
```

### Специальные коллекции

#### Рекомендуемые публикации
```
GET /api/media-coverage/articles/featured/
```

#### Популярные публикации
```
GET /api/media-coverage/articles/popular/
```

#### Последние публикации
```
GET /api/media-coverage/articles/recent/
```

### Поиск

#### Расширенный поиск
```
GET /api/media-coverage/search/
POST /api/media-coverage/search/
```

**Параметры:**
- `query` - поисковый запрос
- `category` - ID категории
- `outlet` - ID издания
- `sentiment` - тональность
- `importance_score_min` - минимальная важность
- `importance_score_max` - максимальная важность
- `date_from` - дата публикации от
- `date_to` - дата публикации до
- `is_featured` - только рекомендуемые
- `is_verified` - только проверенные
- `ordering` - сортировка
- `page` - номер страницы
- `page_size` - размер страницы

### Дашборд

#### Получить статистику дашборда
```
GET /api/media-coverage/dashboard/
```

**Ответ:**
```json
{
  "total_articles": 30,
  "total_views": 5420,
  "total_outlets": 6,
  "total_categories": 5,
  "articles_by_category": {
    "Телевидение": 8,
    "Интернет": 12,
    "Газеты": 6,
    "Радио": 3,
    "Журналы": 1
  },
  "sentiment_stats": {
    "positive": 15,
    "neutral": 10,
    "negative": 5
  },
  "top_outlets": [
    {
      "name_ru": "AKIpress",
      "article_count": 8
    }
  ],
  "popular_tags": [
    {
      "name_ru": "Медицина",
      "usage_count": 15,
      "color": "#E53E3E"
    }
  ],
  "recent_articles": [...],
  "featured_articles": [...]
}
```

### Аналитика

#### Получить аналитику за период
```
GET /api/media-coverage/analytics/
```

**Параметры:**
- `period` - период (day, week, month, quarter, year)
- `start_date` - начальная дата
- `end_date` - конечная дата

**Ответ:**
```json
{
  "timeline_data": [
    {
      "date": "2025-09-18",
      "total_articles": 5,
      "total_views": 1234,
      "total_reach": 15000,
      "positive_articles": 3,
      "neutral_articles": 1,
      "negative_articles": 1
    }
  ],
  "category_distribution": {
    "Телевидение": 8,
    "Интернет": 12
  },
  "sentiment_trends": {
    "positive": 15,
    "neutral": 10,
    "negative": 5
  },
  "outlet_performance": [
    {
      "name": "AKIpress",
      "articles_count": 8,
      "avg_importance": 6.5,
      "total_views": 2340
    }
  ],
  "top_journalists": [
    {
      "journalist_name": "Айгуль Асанова",
      "articles_count": 5,
      "avg_importance": 7.2,
      "total_views": 1200
    }
  ],
  "keyword_cloud": [
    {
      "keyword": "медицина",
      "count": 25
    }
  ]
}
```

### Статистика

#### Получить историческую статистику
```
GET /api/media-coverage/statistics/
```

**Параметры:**
- `date` - фильтр по дате

## Коды ошибок

- `400` - Неверные параметры запроса
- `401` - Требуется аутентификация
- `403` - Недостаточно прав доступа
- `404` - Ресурс не найден
- `500` - Внутренняя ошибка сервера

## Аутентификация

Для создания, обновления и удаления медиа-материалов требуется аутентификация.

Публичные эндпоинты (только чтение):
- Получение списков и деталей публикаций
- Поиск и аналитика
- Дашборд и статистика

Приватные эндпоинты (требуют аутентификации):
- Создание, обновление, удаление публикаций
- Управление категориями, изданиями и тегами

## Мультиязычность

API поддерживает три языка:
- `ru` - русский (по умолчанию)
- `kg` - кыргызский  
- `en` - английский

Все текстовые поля возвращают значения для всех языков. Клиент может выбирать нужный язык на фронтенде.

## Пагинация

Списки используют стандартную пагинацию Django REST Framework:
- `page` - номер страницы (по умолчанию: 1)
- `page_size` - размер страницы (по умолчанию: 20, максимум: 100)

## Фильтрация и поиск

Поддерживается:
- Полнотекстовый поиск по всем языкам
- Фильтрация по категориям, изданиям, тегам
- Фильтрация по датам и статусам
- Сортировка по различным полям
