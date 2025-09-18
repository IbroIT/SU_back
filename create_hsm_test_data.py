#!/usr/bin/env python
"""
Скрипт для создания тестовых данных для приложения HSM (Высшая школа менеджмента)
"""

import os
import sys
import django
from datetime import date, datetime, timedelta

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')
django.setup()

from hsm.models import HSMInfo, Program, Faculty, Accreditation, LearningGoal

def create_hsm_info():
    """Создать основную информацию о ВШМ"""
    print("Создание основной информации о ВШМ...")
    
    hsm_info, created = HSMInfo.objects.get_or_create(
        title="Высшая школа медицины",
        defaults={
            'title_kg': "Жогорку медицина мектеби",
            'title_en': "Graduate School of Medicine",
            'description': """Высшая школа медицины Салымбекова Университета - ведущий центр подготовки высококвалифицированных медицинских кадров в Кыргызстане. Мы готовим профессиональных врачей, способных эффективно работать в условиях современной медицины.""",
            'description_kg': """Салымбеков Университетинин Жогорку медицина мектеби - Кыргызстандагы жогорку квалификациялуу медициналык кадрларды даярдоочу алдыңкы борбор. Биз заманбап медицина шартында натыйжалуу иштей турган кесипкөй врачтарды даярдайбыз.""",
            'description_en': """The Graduate School of Management of Salymbekov University is a leading center for training highly qualified management personnel in Kyrgyzstan. We prepare professional managers capable of working effectively in the modern economy.""",
            'history': """Высшая школа менеджмента была основана в 2010 году как специализированное подразделение Салымбекова Университета. За годы работы школа выпустила более 500 специалистов в области менеджмента, многие из которых занимают руководящие позиции в крупных компаниях и государственных учреждениях.""",
            'history_kg': """Жогорку менеджмент мектеби 2010-жылы Салымбеков Университетинин атайын бөлүмү катары негизделген. Иштеген жылдары мектеп менеджмент тармагында 500дөн ашык адисти бүтүргөн, алардын көбү ири компанияларда жана мамлекеттик мекемелерде жетекчилик кызматтарды ээлешет.""",
            'history_en': """The Graduate School of Management was established in 2010 as a specialized division of Salymbekov University. Over the years, the school has graduated more than 500 specialists in management, many of whom hold leadership positions in large companies and government institutions.""",
            'main_directions': """Основные направления деятельности:
• Стратегический менеджмент
• Финансовый менеджмент  
• Маркетинг и продажи
• Управление персоналом
• Проектный менеджмент
• Цифровая трансформация бизнеса
• Предпринимательство и инновации""",
            'main_directions_kg': """Негизги иш багыттары:
• Стратегиялык менеджмент
• Каржылык менеджмент
• Маркетинг жана сатуу
• Кадрларды башкаруу
• Долбоорлук менеджмент
• Бизнести санариптик өзгөртүү
• Ишкердик жана инновациялар""",
            'main_directions_en': """Main directions of activity:
• Strategic management
• Financial management
• Marketing and sales
• Human resources management
• Project management
• Digital business transformation
• Entrepreneurship and innovation""",
        }
    )
    
    if created:
        print("✓ Основная информация о ВШМ создана")
    else:
        print("→ Основная информация о ВШМ уже существует")
    
    return hsm_info

def create_programs():
    """Создать образовательные программы"""
    print("Создание образовательных программ...")
    
    programs_data = [
        # Бакалавриат
        {
            'name': 'Менеджмент',
            'name_kg': 'Менеджмент',
            'name_en': 'Management',
            'program_type': 'bachelor',
            'study_form': 'full_time',
            'duration_years': 4,
            'duration_semesters': 8,
            'description': 'Программа подготовки специалистов в области общего менеджмента с глубоким изучением теории и практики управления.',
            'competencies': 'Выпускники получают компетенции в области стратегического планирования, управления персоналом, финансового менеджмента, маркетинга.',
            'career_prospects': 'Менеджер среднего звена, руководитель отдела, консультант по управлению, предприниматель.',
            'order': 1
        },
        {
            'name': 'Экономика и управление',
            'name_kg': 'Экономика жана башкаруу',
            'name_en': 'Economics and Management',
            'program_type': 'bachelor',
            'study_form': 'full_time',
            'duration_years': 4,
            'duration_semesters': 8,
            'description': 'Комплексная программа, сочетающая экономическую теорию с практическими навыками управления.',
            'competencies': 'Экономический анализ, бюджетирование, управление проектами, стратегическое планирование.',
            'career_prospects': 'Экономист, аналитик, финансовый менеджер, консультант.',
            'order': 2
        },
        # Магистратура
        {
            'name': 'MBA - Мастер делового администрирования',
            'name_kg': 'MBA - Ишкердик администрациялоонун устасы',
            'name_en': 'MBA - Master of Business Administration',
            'program_type': 'master',
            'study_form': 'part_time',
            'duration_years': 2,
            'duration_semesters': 4,
            'description': 'Престижная программа МБА для руководителей высшего звена и опытных менеджеров.',
            'competencies': 'Стратегическое лидерство, инновационный менеджмент, глобальное мышление, цифровая трансформация.',
            'career_prospects': 'Топ-менеджер, генеральный директор, консультант высшего уровня, предприниматель.',
            'order': 1
        },
        {
            'name': 'Стратегический менеджмент',
            'name_kg': 'Стратегиялык менеджмент',
            'name_en': 'Strategic Management',
            'program_type': 'master',
            'study_form': 'full_time',
            'duration_years': 2,
            'duration_semesters': 4,
            'description': 'Специализированная программа для подготовки стратегических менеджеров.',
            'competencies': 'Стратегическое планирование, управление изменениями, корпоративное развитие.',
            'career_prospects': 'Стратегический менеджер, директор по развитию, консультант по стратегии.',
            'order': 2
        }
    ]
    
    created_count = 0
    for program_data in programs_data:
        program, created = Program.objects.get_or_create(
            name=program_data['name'],
            program_type=program_data['program_type'],
            defaults=program_data
        )
        if created:
            created_count += 1
    
    print(f"✓ Создано {created_count} новых программ")
    return Program.objects.all()

def create_faculty():
    """Создать профессорско-преподавательский состав"""
    print("Создание ППС...")
    
    faculty_data = [
        {
            'first_name': 'Азамат',
            'last_name': 'Салымбеков',
            'middle_name': 'Рустамович',
            'first_name_en': 'Azamat',
            'last_name_en': 'Salymbekov',
            'position': 'dean',
            'academic_degree': 'doctor',
            'academic_title': 'Профессор',
            'email': 'a.salymbekov@salymbekov.edu.kg',
            'phone': '+996 312 123456',
            'office': 'Корпус А, 301',
            'bio': 'Доктор экономических наук, профессор. Основатель и ректор Салымбекова Университета.',
            'specialization': 'Стратегический менеджмент, предпринимательство',
            'order': 1
        },
        {
            'first_name': 'Гульнара',
            'last_name': 'Иманова',
            'middle_name': 'Асановна',
            'first_name_en': 'Gulnara',
            'last_name_en': 'Imanova',
            'position': 'professor',
            'academic_degree': 'doctor',
            'academic_title': 'Профессор',
            'email': 'g.imanova@salymbekov.edu.kg',
            'phone': '+996 312 123457',
            'office': 'Корпус А, 302',
            'bio': 'Доктор экономических наук, эксперт в области финансового менеджмента.',
            'specialization': 'Финансовый менеджмент, корпоративные финансы',
            'order': 2
        },
        {
            'first_name': 'Бакыт',
            'last_name': 'Жумабеков',
            'middle_name': 'Эркинович',
            'first_name_en': 'Bakyt',
            'last_name_en': 'Zhumabekov',
            'position': 'associate_professor',
            'academic_degree': 'candidate',
            'academic_title': 'Доцент',
            'email': 'b.zhumabekov@salymbekov.edu.kg',
            'phone': '+996 312 123458',
            'office': 'Корпус А, 303',
            'bio': 'Кандидат экономических наук, специалист по маркетингу и управлению персоналом.',
            'specialization': 'Маркетинг, управление персоналом',
            'order': 3
        },
        {
            'first_name': 'Айжан',
            'last_name': 'Токтогулова',
            'middle_name': 'Мирлановна',
            'first_name_en': 'Aizhan',
            'last_name_en': 'Toktogulova',
            'position': 'senior_lecturer',
            'academic_degree': 'master',
            'email': 'a.toktogulova@salymbekov.edu.kg',
            'phone': '+996 312 123459',
            'office': 'Корпус А, 304',
            'bio': 'Магистр делового администрирования, практикующий консультант.',
            'specialization': 'Проектный менеджмент, бизнес-консалтинг',
            'order': 4
        }
    ]
    
    created_count = 0
    for faculty_member_data in faculty_data:
        faculty_member, created = Faculty.objects.get_or_create(
            first_name=faculty_member_data['first_name'],
            last_name=faculty_member_data['last_name'],
            middle_name=faculty_member_data['middle_name'],
            defaults=faculty_member_data
        )
        if created:
            created_count += 1
    
    print(f"✓ Создано {created_count} новых преподавателей")
    return Faculty.objects.all()

def create_accreditations():
    """Создать аккредитации"""
    print("Создание аккредитаций...")
    
    accreditations_data = [
        {
            'name': 'Государственная лицензия на образовательную деятельность',
            'name_en': 'State License for Educational Activities',
            'organization': 'Министерство образования и науки КР',
            'organization_en': 'Ministry of Education and Science of KR',
            'accreditation_type': 'national',
            'description': 'Лицензия на право ведения образовательной деятельности в сфере высшего образования.',
            'issue_date': date(2010, 9, 15),
            'expiry_date': date(2025, 9, 15),
            'certificate_number': 'Л-001-2010',
            'order': 1
        },
        {
            'name': 'Институциональная аккредитация',
            'name_en': 'Institutional Accreditation',
            'organization': 'Национальное агентство аккредитации и рейтинга',
            'organization_en': 'National Agency for Accreditation and Rating',
            'accreditation_type': 'institutional',
            'description': 'Подтверждение соответствия образовательной деятельности государственным стандартам.',
            'issue_date': date(2020, 6, 10),
            'expiry_date': date(2026, 6, 10),
            'certificate_number': 'ИА-002-2020',
            'order': 2
        },
        {
            'name': 'Международная аккредитация AACSB',
            'name_en': 'AACSB International Accreditation',
            'organization': 'Association to Advance Collegiate Schools of Business',
            'organization_en': 'Association to Advance Collegiate Schools of Business',
            'accreditation_type': 'international',
            'description': 'Престижная международная аккредитация бизнес-школ.',
            'issue_date': date(2022, 3, 1),
            'expiry_date': date(2027, 3, 1),
            'certificate_number': 'AACSB-2022-001',
            'order': 3
        }
    ]
    
    created_count = 0
    for accreditation_data in accreditations_data:
        accreditation, created = Accreditation.objects.get_or_create(
            name=accreditation_data['name'],
            organization=accreditation_data['organization'],
            defaults=accreditation_data
        )
        if created:
            created_count += 1
    
    print(f"✓ Создано {created_count} новых аккредитаций")
    return Accreditation.objects.all()

def create_learning_goals():
    """Создать цели и результаты обучения"""
    print("Создание целей обучения...")
    
    goals_data = [
        {
            'title': 'Лидерство и управление командой',
            'title_en': 'Leadership and Team Management',
            'description': 'Развитие навыков эффективного лидерства и управления командами.',
            'competencies': 'Способность мотивировать сотрудников, принимать решения, управлять конфликтами.',
            'career_prospects': 'Руководитель отдела, менеджер проекта, team lead.',
            'order': 1
        },
        {
            'title': 'Стратегическое мышление',
            'title_en': 'Strategic Thinking',
            'description': 'Формирование навыков стратегического планирования и анализа.',
            'competencies': 'Анализ рынка, планирование развития, оценка рисков.',
            'career_prospects': 'Стратегический менеджер, консультант, аналитик.',
            'order': 2
        },
        {
            'title': 'Финансовая грамотность',
            'title_en': 'Financial Literacy',
            'description': 'Понимание финансовых процессов и умение работать с финансовой отчетностью.',
            'competencies': 'Финансовый анализ, бюджетирование, управление денежными потоками.',
            'career_prospects': 'Финансовый менеджер, контроллер, CFO.',
            'order': 3
        }
    ]
    
    created_count = 0
    for goal_data in goals_data:
        goal, created = LearningGoal.objects.get_or_create(
            title=goal_data['title'],
            defaults=goal_data
        )
        if created:
            created_count += 1
    
    print(f"✓ Создано {created_count} новых целей обучения")
    return LearningGoal.objects.all()

def main():
    """Основная функция для создания всех тестовых данных"""
    print("Начинаем создание тестовых данных для ВШМ...")
    print("=" * 50)
    
    try:
        # Создаем основную информацию
        hsm_info = create_hsm_info()
        
        # Создаем программы
        programs = create_programs()
        
        # Создаем ППС
        faculty = create_faculty()
        
        # Создаем аккредитации
        accreditations = create_accreditations()
        
        # Создаем цели обучения
        learning_goals = create_learning_goals()
        
        print("=" * 50)
        print("✅ Все тестовые данные успешно созданы!")
        print(f"📊 Статистика:")
        print(f"   • Информация о ВШМ: {HSMInfo.objects.count()}")
        print(f"   • Программы обучения: {Program.objects.count()}")
        print(f"   • Преподаватели: {Faculty.objects.count()}")
        print(f"   • Аккредитации: {Accreditation.objects.count()}")
        print(f"   • Цели обучения: {LearningGoal.objects.count()}")
        
    except Exception as e:
        print(f"❌ Ошибка при создании данных: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
