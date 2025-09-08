from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date, timedelta
from careers.models import CareerCategory, Department, Vacancy


class Command(BaseCommand):
    help = 'Создает тестовые данные для приложения careers'

    def handle(self, *args, **options):
        self.stdout.write('Создание тестовых данных для careers...')
        
        # Создаем категории
        categories_data = [
            {
                'name': 'academic',
                'display_name': 'Преподавательские',
                'icon': '🏫',
                'description': 'Вакансии для преподавателей и научных сотрудников',
                'order': 1
            },
            {
                'name': 'administrative', 
                'display_name': 'Административные',
                'icon': '💼',
                'description': 'Административные и управленческие позиции',
                'order': 2
            },
            {
                'name': 'technical',
                'display_name': 'Технические',
                'icon': '🖥️',
                'description': 'IT и технические специалисты',
                'order': 3
            },
            {
                'name': 'service',
                'display_name': 'Обслуживающие',
                'icon': '📚',
                'description': 'Библиотекари, лаборанты, обслуживающий персонал',
                'order': 4
            }
        ]
        
        for cat_data in categories_data:
            category, created = CareerCategory.objects.get_or_create(
                name=cat_data['name'],
                defaults=cat_data
            )
            if created:
                self.stdout.write(f'Создана категория: {category.display_name}')
        
        # Создаем подразделения
        departments_data = [
            {
                'name': 'Кафедра биологии',
                'short_name': 'Биология',
                'description': 'Кафедра биологических наук',
                'head_name': 'Профессор Иванов И.И.',
                'contact_email': 'biology@salymbekov.kg',
                'contact_phone': '+996555123456'
            },
            {
                'name': 'Отдел международных связей',
                'short_name': 'Международные связи',
                'description': 'Координация международных программ и обменов',
                'head_name': 'Директор Петров П.П.',
                'contact_email': 'international@salymbekov.kg',
                'contact_phone': '+996555123457'
            },
            {
                'name': 'IT отдел',
                'short_name': 'IT',
                'description': 'Информационные технологии и техническая поддержка',
                'head_name': 'Руководитель Сидоров С.С.',
                'contact_email': 'it@salymbekov.kg',
                'contact_phone': '+996555123458'
            },
            {
                'name': 'Библиотека',
                'short_name': 'Библиотека',
                'description': 'Университетская библиотека',
                'head_name': 'Заведующий Кузнецова А.А.',
                'contact_email': 'library@salymbekov.kg',
                'contact_phone': '+996555123459'
            },
            {
                'name': 'Отдел кадров',
                'short_name': 'HR',
                'description': 'Управление человеческими ресурсами',
                'head_name': 'Начальник Смирнова М.М.',
                'contact_email': 'hr@salymbekov.kg',
                'contact_phone': '+996555123460'
            }
        ]
        
        for dept_data in departments_data:
            department, created = Department.objects.get_or_create(
                name=dept_data['name'],
                defaults=dept_data
            )
            if created:
                self.stdout.write(f'Создано подразделение: {department.name}')
        
        # Создаем вакансии
        academic_category = CareerCategory.objects.get(name='academic')
        administrative_category = CareerCategory.objects.get(name='administrative')
        technical_category = CareerCategory.objects.get(name='technical')
        service_category = CareerCategory.objects.get(name='service')
        
        biology_dept = Department.objects.get(name='Кафедра биологии')
        international_dept = Department.objects.get(name='Отдел международных связей')
        it_dept = Department.objects.get(name='IT отдел')
        library_dept = Department.objects.get(name='Библиотека')
        hr_dept = Department.objects.get(name='Отдел кадров')
        
        vacancies_data = [
            {
                'title': 'Преподаватель биохимии',
                'slug': 'prepodavatel-biohimii',
                'category': academic_category,
                'department': biology_dept,
                'location': 'Бишкек',
                'employment_type': 'full_time',
                'salary_min': 40000,
                'salary_max': None,
                'experience_years': '3+ года',
                'education_level': 'Магистр/PhD биологии',
                'short_description': 'Ведение лекций и семинаров по биохимии, подготовка методических материалов, научно-исследовательская деятельность.',
                'description': 'Кафедра биологии приглашает на работу преподавателя биохимии для ведения лекционных и практических занятий.',
                'responsibilities': '''Ведение лекций и семинаров по биохимии для студентов различных курсов
Проведение лабораторных работ и практических занятий
Разработка учебных материалов и методических пособий
Участие в научно-исследовательской работе кафедры
Руководство курсовыми и дипломными работами студентов
Участие в работе кафедры и факультета
Повышение квалификации и участие в конференциях''',
                'requirements': '''Высшее образование по специальности "Биология", "Биохимия" или смежной области
Ученая степень кандидата или доктора наук приветствуется
Опыт преподавания в вузе не менее 3 лет
Знание английского языка на уровне Upper-Intermediate
Навыки работы с современным лабораторным оборудованием
Опыт публикации научных статей в рецензируемых журналах
Коммуникабельность и умение работать в команде''',
                'conditions': '''Конкурентная заработная плата от 40,000 сом
Полный социальный пакет и медицинское страхование
Возможности профессионального развития и обучения
Доступ к современному лабораторному оборудованию
Участие в международных конференциях за счет университета
График работы: 5/2, полный рабочий день
Ежегодный оплачиваемый отпуск 42 дня''',
                'tags': 'Преподавание, Наука, Биология, Биохимия',
                'status': 'published',
                'is_featured': True,
                'deadline': date.today() + timedelta(days=30),
                'contact_person': 'Профессор Иванов И.И.',
                'contact_email': 'biology@salymbekov.kg',
                'contact_phone': '+996555123456'
            },
            {
                'title': 'Менеджер по международным связям',
                'slug': 'menedzher-mezhdunarodnyh-svyazei',
                'category': administrative_category,
                'department': international_dept,
                'location': 'Бишкек',
                'employment_type': 'full_time',
                'salary_min': 35000,
                'salary_max': 50000,
                'experience_years': '2+ года',
                'education_level': 'Высшее образование',
                'short_description': 'Развитие международных связей университета, организация программ обмена, работа с зарубежными партнерами.',
                'description': 'Отдел международных связей ищет активного менеджера для развития партнерских отношений с зарубежными университетами.',
                'responsibilities': '''Развитие и поддержание международных партнерских отношений
Организация и координация программ академической мобильности
Подготовка документации для международных проектов
Сопровождение иностранных студентов и преподавателей
Организация международных конференций и мероприятий
Ведение переговоров с зарубежными партнерами
Подготовка отчетности по международной деятельности''',
                'requirements': '''Высшее образование (предпочтительно международные отношения, лингвистика)
Опыт работы в сфере международного сотрудничества от 2 лет
Отличное знание английского языка (свободное владение)
Знание дополнительных языков приветствуется
Опыт работы с грантовыми проектами
Навыки межкультурной коммуникации
Умение работать с документооборотом
Организационные способности''',
                'conditions': '''Заработная плата 35,000 - 50,000 сом
Социальный пакет и медицинская страховка
Возможности международных командировок
Обучение и повышение квалификации
Работа в международной среде
Гибкий график работы
30 дней оплачиваемого отпуска''',
                'tags': 'Международные связи, Администрация, Образование',
                'status': 'published',
                'is_featured': False,
                'deadline': date.today() + timedelta(days=25),
                'contact_person': 'Директор Петров П.П.',
                'contact_email': 'international@salymbekov.kg',
                'contact_phone': '+996555123457'
            },
            {
                'title': 'Системный администратор',
                'slug': 'sistemnyj-administrator',
                'category': technical_category,
                'department': it_dept,
                'location': 'Бишкек',
                'employment_type': 'full_time',
                'salary_min': 45000,
                'salary_max': 65000,
                'experience_years': '3+ года',
                'education_level': 'Техническое образование',
                'short_description': 'Администрирование серверов и сетевой инфраструктуры, техническая поддержка пользователей, обеспечение информационной безопасности.',
                'description': 'IT отдел университета приглашает опытного системного администратора для поддержки IT-инфраструктуры.',
                'responsibilities': '''Администрирование серверов Windows/Linux
Поддержка и развитие сетевой инфраструктуры
Техническая поддержка сотрудников и студентов
Обеспечение информационной безопасности
Резервное копирование и восстановление данных
Мониторинг работы IT-систем
Установка и настройка программного обеспечения
Ведение технической документации''',
                'requirements': '''Высшее техническое образование
Опыт работы системным администратором от 3 лет
Знание ОС Windows Server, Linux
Опыт работы с сетевым оборудованием
Знание основ информационной безопасности
Навыки работы с базами данных
Английский язык на уровне чтения технической документации
Готовность к обучению новым технологиям''',
                'conditions': '''Заработная плата 45,000 - 65,000 сом
Полный социальный пакет
Обучение новым технологиям за счет компании
Современное оборудование для работы
Возможности профессионального роста
График работы 5/2
Дополнительные выплаты за переработки''',
                'tags': 'IT, Администрирование, Техподдержка',
                'status': 'published',
                'is_featured': True,
                'deadline': date.today() + timedelta(days=20),
                'contact_person': 'Руководитель Сидоров С.С.',
                'contact_email': 'it@salymbekov.kg',
                'contact_phone': '+996555123458'
            },
            {
                'title': 'Библиотекарь-каталогизатор',
                'slug': 'bibliotekar-katalogizator',
                'category': service_category,
                'department': library_dept,
                'location': 'Бишкек',
                'employment_type': 'full_time',
                'salary_min': 25000,
                'salary_max': 35000,
                'experience_years': '1+ год',
                'education_level': 'Библиотечное образование',
                'short_description': 'Каталогизация библиотечного фонда, работа с электронными каталогами, помощь читателям в поиске литературы.',
                'description': 'Университетская библиотека приглашает библиотекаря для работы с каталогизацией и обслуживанием читателей.',
                'responsibilities': '''Каталогизация новых поступлений
Ведение электронного каталога
Помощь студентам и преподавателям в поиске литературы
Выдача и прием книг
Проведение библиографических консультаций
Участие в мероприятиях библиотеки
Работа с периодическими изданиями''',
                'requirements': '''Высшее библиотечное образование
Опыт работы в библиотеке от 1 года
Знание библиотечно-информационных систем
Навыки работы с компьютером
Внимательность и аккуратность
Коммуникабельность
Знание английского языка приветствуется''',
                'conditions': '''Заработная плата 25,000 - 35,000 сом
Социальный пакет
Спокойная рабочая обстановка
График работы 5/2
Доступ к библиотечному фонду
Возможность повышения квалификации''',
                'tags': 'Библиотека, Каталогизация, Обслуживание',
                'status': 'published',
                'is_featured': False,
                'deadline': date.today() + timedelta(days=35),
                'contact_person': 'Заведующий Кузнецова А.А.',
                'contact_email': 'library@salymbekov.kg',
                'contact_phone': '+996555123459'
            }
        ]
        
        for vacancy_data in vacancies_data:
            vacancy, created = Vacancy.objects.get_or_create(
                slug=vacancy_data['slug'],
                defaults=vacancy_data
            )
            if created:
                self.stdout.write(f'Создана вакансия: {vacancy.title}')
        
        self.stdout.write(
            self.style.SUCCESS('Тестовые данные успешно созданы!')
        )
