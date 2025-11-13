# API Endpoints Documentation

## 1. Цифры на главной странице и about HSM
**GET** `api/home/numbers/`

**Пример ответа:**
```json
[
  {
    "id": 1,
    "icon": "http://localhost:8000/media/numbers/icons/icon1.png",
    "number": "500+",
    "description_ru": "Студентов",
    "description_kg": "Студенттер",
    "description_en": "Students"
  },
  {
    "id": 2,
    "icon": "http://localhost:8000/media/numbers/icons/icon2.png",
    "number": "50+",
    "description_ru": "Преподавателей",
    "description_kg": "Окутуучулар",
    "description_en": "Teachers"
  }
]
```

---

## 2. Отзывы студентов на главной странице
**GET** `api/home/testimonials/`

**Пример ответа:**
```json
[
  {
    "id": 1,
    "photo": "http://localhost:8000/media/testimonials/photos/student1.jpg",
    "year": "3 курс",
    "name_ru": "Айдана Токтогулова",
    "name_kg": "Айдана Токтогулова",
    "name_en": "Aidana Toktogulova",
    "testimonial_ru": "Отличный университет с высоким уровнем образования...",
    "testimonial_kg": "Мыкты университет...",
    "testimonial_en": "Excellent university with high-quality education...",
    "faculty_ru": "Высшая школа медицины",
    "faculty_kg": "Медицинанын жогорку мектеби",
    "faculty_en": "Higher School of Medicine"
  }
]
```

---

## 3. Программы в HSM
**GET** `api/hsm/programs/`

**Пример ответа:**
```json
[
  {
    "id": 1,
    "name_ru": "Общая медицина",
    "name_kg": "Жалпы медицина",
    "name_en": "General Medicine",
    "description_ru": "Программа подготовки врачей общей практики...",
    "description_kg": "Жалпы практика врачтарын даярдоо программасы...",
    "description_en": "General practice physician training program...",
    "profession_ru": "Врач",
    "profession_kg": "Дарыгер",
    "profession_en": "Doctor",
    "duration_ru": "6 лет",
    "duration_kg": "6 жыл",
    "duration_en": "6 years",
    "review_ru": "Детальный обзор программы...",
    "review_kg": "Программанын деталдуу обзору...",
    "review_en": "Detailed program overview...",
    "is_active": true
  }
]
```

**GET** `api/hsm/programs/<int:pk>/`

**Пример ответа:**
```json
{
  "id": 1,
  "name_ru": "Общая медицина",
  "name_kg": "Жалпы медицина",
  "name_en": "General Medicine",
  "description_ru": "Программа подготовки врачей общей практики...",
  "description_kg": "Жалпы практика врачтарын даярдоо программасы...",
  "description_en": "General practice physician training program...",
  "profession_ru": "Врач",
  "profession_kg": "Дарыгер",
  "profession_en": "Doctor",
  "duration_ru": "6 лет",
  "duration_kg": "6 жыл",
  "duration_en": "6 years",
  "review_ru": "Детальный обзор программы...",
  "review_kg": "Программанын деталдуу обзору...",
  "review_en": "Detailed program overview...",
  "is_active": true
}
```

---

## 4. Статистика HSM (Академический состав)
**GET** `api/hsm/detail-statistics/`

**Пример ответа:**
```json
[
  {
    "id": 1,
    "intTitle": "85%",
    "description_ru": "Преподавателей с учеными степенями",
    "description_kg": "Окумуштуулук даражасы бар окутуучулар",
    "description_en": "Teachers with academic degrees"
  },
  {
    "id": 2,
    "intTitle": "15",
    "description_ru": "Докторов наук",
    "description_kg": "Илимдер доктору",
    "description_en": "Doctors of Science"
  }
]
```

**GET** `api/hsm/as-numbers/`

**Пример ответа:**
```json
[
  {
    "id": 1,
    "intTitle": "50+",
    "title_ru": "Преподавателей",
    "title_kg": "Окутуучулар",
    "title_en": "Teachers",
    "description_ru": "Высококвалифицированных преподавателей",
    "description_kg": "Жогорку квалификациялуу окутуучулар",
    "description_en": "Highly qualified teachers"
  }
]
```

---

## 5. Ссылки в навбаре (Расписание, Академический календарь и т.д.)
**GET** `api/home/navbar-links/`

**Пример ответа:**
```json
[
  {
    "id": 1,
    "name_ru": "Расписание",
    "name_kg": "Расписание",
    "name_en": "Schedule",
    "url": "https://schedule.sulaimanunijournal.kg"
  },
  {
    "id": 2,
    "name_ru": "Академический календарь",
    "name_kg": "Академиялык календарь",
    "name_en": "Academic Calendar",
    "url": "https://calendar.sulaimanunijournal.kg"
  }
]
```

---

## 6. Фотографии для студенческих клубов
**GET** `api/student-life/api/photos/`

**Параметры запроса (опционально):**
- `lang` - язык (ru, kg, en). По умолчанию: ru

**Пример ответа:**
```json
[
  {
    "id": 1,
    "category_ru": "Студенческие клубы",
    "category_kg": "Студенттик клубдар",
    "category_en": "Student Clubs",
    "category": "Студенческие клубы",
    "description_ru": "Встреча клуба дебатов",
    "description_kg": "Дебат клубунун жолугушуусу",
    "description_en": "Debate club meeting",
    "description": "Встреча клуба дебатов",
    "photo": "http://localhost:8000/media/student_life/photos/club1.jpg"
  },
  {
    "id": 2,
    "category_ru": "Спортивные мероприятия",
    "category_kg": "Спорттук иш-чаралар",
    "category_en": "Sports Events",
    "category": "Спортивные мероприятия",
    "description_ru": "Футбольный турнир",
    "description_kg": "Футбол турнири",
    "description_en": "Football tournament",
    "description": "Футбольный турнир",
    "photo": "http://localhost:8000/media/student_life/photos/sport1.jpg"
  }
]
```

---

## 7. Электронные ресурсы для HSM
**GET** `api/hsm/e-resources/`

**Пример ответа:**
```json
[
  {
    "id": 1,
    "name_ru": "Электронная библиотека",
    "name_kg": "Электрондук китепкана",
    "name_en": "Electronic Library",
    "description_ru": "Доступ к медицинским журналам и книгам",
    "description_kg": "Медициналык журналдарга жана китептерге жеткиликтүүлүк",
    "description_en": "Access to medical journals and books",
    "features_ru": ["Более 10,000 книг", "Международные журналы", "24/7 доступ"],
    "features_kg": ["10,000ден ашык китептер", "Эл аралык журналдар", "24/7 жеткиликтүүлүк"],
    "features_en": ["Over 10,000 books", "International journals", "24/7 access"],
    "links": {
      "main": "https://library.sulaimanunijournal.kg",
      "login": "https://library.sulaimanunijournal.kg/login"
    }
  }
]
```

---

## 8. Требования приемной комиссии
**GET** `api/admissions/requirements/`

**Пример ответа:**
```json
[
  {
    "id": 1,
    "title_ru": "Документы для поступления",
    "title_kg": "Кабыл алуу үчүн документтер",
    "title_en": "Documents for Admission",
    "description_ru": "Список необходимых документов: аттестат, паспорт, фотографии...",
    "description_kg": "Керектүү документтердин тизмеси...",
    "description_en": "List of required documents: certificate, passport, photos..."
  }
]
```

---

## 9. Оплата для граждан КР
**GET** `api/admissions/bank-requisites-kg/`

**Пример ответа:**
```json
[
  {
    "id": 1,
    "bank_name_ru": "ОАО «Банк Азии»",
    "bank_name_kg": "ААК «Азия Банк»",
    "bank_name_en": "JSC Bank Asia",
    "account_number": "1234567890123456",
    "bik": "123456",
    "inn": "00123456789012",
    "recipient_ru": "Сулайман-Тоо Университет",
    "recipient_kg": "Сулайман-Тоо Университети",
    "recipient_en": "Sulaiman-Too University",
    "payment_purpose_ru": "Оплата за обучение",
    "payment_purpose_kg": "Окуу үчүн төлөм",
    "payment_purpose_en": "Tuition payment"
  }
]
```

**GET** `api/admissions/fees/`

**Пример ответа:**
```json
[
  {
    "id": 1,
    "title_ru": "Контракт (1 год)",
    "title_kg": "Контракт (1 жыл)",
    "title_en": "Contract (1 year)",
    "amount": "250000.00",
    "faculty_ru": "Высшая школа медицины",
    "faculty_kg": "Медицинанын жогорку мектеби",
    "faculty_en": "Higher School of Medicine",
    "warnings_ru": ["Оплата до 1 сентября", "Возможна рассрочка"],
    "warnings_kg": ["1-сентябрга чейин төлөө", "Бөлүп төлөө мүмкүн"],
    "warnings_en": ["Payment before September 1", "Installment available"]
  }
]
```

**GET** `api/admissions/contacts/`

**Пример ответа:**
```json
[
  {
    "id": 1,
    "phone_number": "+996 312 12 34 56",
    "email": "admissions@sulaimanunijournal.kg",
    "working_hours": "Пн-Пт: 9:00-18:00"
  }
]
```

---

## 10. Оплата для иностранных граждан
**GET** `api/admissions/requisities-foreign/`

**Пример ответа:**
```json
[
  {
    "id": 1,
    "bank_name_ru": "ОАО «Банк Азии»",
    "bank_name_kg": "ААК «Азия Банк»",
    "bank_name_en": "JSC Bank Asia",
    "account_number": "USD1234567890123456",
    "swift_code": "ASIAKG22",
    "recipient_ru": "Сулайман-Тоо Университет",
    "recipient_kg": "Сулайман-Тоо Университети",
    "recipient_en": "Sulaiman-Too University",
    "correspondent_bank": "Citibank N.A., New York, USA",
    "warnings_ru": ["Все платежи в долларах США", "Комиссия банка оплачивается отправителем"],
    "warnings_kg": ["Бардык төлөмдөр АКШ долларында", "Банк комиссиясын жиберүүчү төлөйт"],
    "warnings_en": ["All payments in USD", "Bank commission paid by sender"]
  }
]
```

**GET** `api/admissions/fees-foreign/`

**Пример ответа:**
```json
[
  {
    "id": 1,
    "title_ru": "Контракт (1 год)",
    "title_kg": "Контракт (1 жыл)",
    "title_en": "Contract (1 year)",
    "amount": "3500.00",
    "faculty_ru": "Высшая школа медицины",
    "faculty_kg": "Медицинанын жогорку мектеби",
    "faculty_en": "Higher School of Medicine",
    "warnings_ru": ["Оплата в долларах США", "Оплата до 1 сентября"],
    "warnings_kg": ["АКШ долларында төлөө", "1-сентябрга чейин төлөө"],
    "warnings_en": ["Payment in USD", "Payment before September 1"]
  }
]
```

**GET** `api/admissions/contacts-foreign/`

**Пример ответа:**
```json
[
  {
    "id": 1,
    "phone_number": "+996 312 12 34 56",
    "email": "international@sulaimanunijournal.kg",
    "whatsapp": "+996 555 12 34 56",
    "telegram": "@su_international"
  }
]
```

---

## 11. Часто задаваемые вопросы (FAQ)
**GET** `api/admissions/faqs/`

**Пример ответа:**
```json
[
  {
    "id": 1,
    "question_ru": "Какие документы нужны для поступления?",
    "question_kg": "Кабыл алуу үчүн кандай документтер керек?",
    "question_en": "What documents are required for admission?",
    "answer_ru": "Для поступления необходимы следующие документы: аттестат о среднем образовании, паспорт, 6 фотографий 3x4...",
    "answer_kg": "Кабыл алуу үчүн төмөнкү документтер керек...",
    "answer_en": "The following documents are required for admission: high school certificate, passport, 6 photos 3x4..."
  },
  {
    "id": 2,
    "question_ru": "Сколько стоит обучение?",
    "question_kg": "Окуу канча турат?",
    "question_en": "How much does education cost?",
    "answer_ru": "Стоимость обучения составляет 250,000 сомов в год для граждан КР...",
    "answer_kg": "Окуунун наркы КР жарандары үчүн жылына 250,000 сом...",
    "answer_en": "Tuition costs 250,000 soms per year for KR citizens..."
  }
]
```

---

## 12. Инструкции для студентов
**GET** `api/student-life/instruction-files/`

**Пример ответа:**
```json
[
  {
    "id": 1,
    "title_ru": "Правила пользования библиотекой",
    "title_kg": "Китепкананы пайдалануу эрежелери",
    "title_en": "Library Usage Rules",
    "file": "http://localhost:8000/media/student_life/instruction_files/library_rules.pdf"
  },
  {
    "id": 2,
    "title_ru": "Инструкция по регистрации на курсы",
    "title_kg": "Курстарга катталуу боюнча нускама",
    "title_en": "Course Registration Instructions",
    "file": "http://localhost:8000/media/student_life/instruction_files/registration.pdf"
  }
]
```




---

## ?????? ???????????? ??????????

**???? ????????? ????????:** 13 ?????? 2025

| ? | ???????? | ?????? | ???????? |
|---|----------|--------|----------|
| 1 | `api/home/numbers/` |  200 OK | ???????? |
| 2 | `api/home/testimonials/` |  200 OK | ???????? |
| 3 | `api/hsm/programs/` |  200 OK | ???????? |
| 4 | `api/hsm/detail-statistics/` |  200 OK | ???????? |
| 5 | `api/hsm/as-numbers/` |  200 OK | ???????? |
| 6 | `api/home/navbar-links/` |  200 OK | ???????? |
| 7 | `api/student-life/api/photos/` |  200 OK | ???????? |
| 8 | `api/hsm/e-resources/` |  200 OK | ???????? |
| 9 | `api/admissions/requirements/` |  200 OK | ???????? |
| 10 | `api/admissions/bank-requisites-kg/` |  200 OK | ???????? |
| 11 | `api/admissions/fees/` |  200 OK | ???????? |
| 12 | `api/admissions/contacts/` |  200 OK | ???????? |
| 13 | `api/admissions/requisities-foreign/` |  200 OK | ???????? |
| 14 | `api/admissions/fees-foreign/` |  200 OK | ???????? |
| 15 | `api/admissions/contacts-foreign/` |  200 OK | ???????? |
| 16 | `api/admissions/faqs/` |  200 OK | ???????? |
| 17 | `api/student-life/instruction-files/` |  200 OK | ???????? |

### ???????????? ????????:

1. **?????? 500 ? pi/student-life/api/photos/:**
   - ???????: ???????????? ???????????? (????????????? PhotoSerializer ?????? Photoserializer)
   - ???????: ???????? ??? ????????? ?? ?????????? ????????????

2. **?????? 500 ?? ???? ?????????? admissions:**
   - ???????: ????????????? ????? migrations ? ??????? ?? ???? ??????? ? ??
   - ???????: ??????? ????? migrations, ????????? ??????? makemigrations ? migrate

### ??? ????????? ?????????????? ? ???????? ?????????! 
