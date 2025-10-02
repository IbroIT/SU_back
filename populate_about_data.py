#!/usr/bin/env python3
"""
Скрипт для заполнения базы данных данными для компонентов Status и Advices
с поддержкой трех языков: русский, английский, кыргызский
"""

import os
import sys
import django
from datetime import datetime, date

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')
django.setup()

from about_section.models import Accreditation, CouncilType, CouncilMember, CouncilDocument


def create_accreditations():
    """Создать данные аккредитаций на основе фронтенда"""
    print("Создание данных аккредитаций...")
    
    accreditations_data = [
        {
            'title': 'Министерство образования и науки Кыргызской Республики',
            'title_en': 'Ministry of Education and Science of the Kyrgyz Republic',
            'title_ky': 'Кыргыз Республикасынын билим берүү жана илим министрлиги',
            'description': 'Государственная аккредитация всех образовательных программ университета',
            'description_en': 'State accreditation of all university educational programs',
            'description_ky': 'Университеттин бардык билим берүү программаларынын мамлекеттик аккредитациясы',
            'full_description': 'Салымбеков университет успешно прошел государственную аккредитацию, подтвердив соответствие высшим стандартам качества образования в Кыргызстане.',
            'full_description_en': 'Salymbekov University has successfully passed state accreditation, confirming compliance with the highest standards of educational quality in Kyrgyzstan.',
            'full_description_ky': 'Салымбеков университети мамлекеттик аккредитацияны ийгиликтүү өткөрүп, Кыргызстандагы билим берүүнүн жогорку сапат стандарттарына дал келүүсүн тастыктады.',
            'logo': '🏛️',
            'year': '1998',
            'status': 'Активный',
            'status_en': 'Active',
            'status_ky': 'Активдүү',
            'validity': 'Бессрочно',
            'validity_en': 'Indefinitely',
            'validity_ky': 'Мөөнөтсүз',
            'level': 'Государственный',
            'level_en': 'Government',
            'level_ky': 'Мамлекеттик',
            'accreditation_type': 'government',
            'benefits': ['Государственное признание', 'Финансирование', 'Участие в госпрограммах'],
            'benefits_en': ['Government recognition', 'Financing', 'Participation in state programs'],
            'benefits_ky': ['Мамлекеттик таануу', 'Каржылоо', 'Мамлекеттик программаларга катышуу'],
            'color': 'from-blue-500 to-blue-600',
            'icon_color': 'text-blue-100',
            'badge_color': 'bg-blue-500',
            'order': 1
        },
        {
            'title': 'Всемирная федерация медицинского образования',
            'title_en': 'World Federation for Medical Education',
            'title_ky': 'Медициналык билим берүүнүн дүйнөлүк федерациясы',
            'description': 'Международное признание медицинских программ университета',
            'description_en': 'International recognition of university medical programs',
            'description_ky': 'Университеттин медициналык программаларынын эл аралык таанылышы',
            'full_description': 'Медицинские программы университета соответствуют международным стандартам WFME, что обеспечивает признание дипломов за рубежом.',
            'full_description_en': 'The university\'s medical programs meet international WFME standards, ensuring recognition of diplomas abroad.',
            'full_description_ky': 'Университеттин медициналык программалары WFME эл аралык стандарттарына дал келет, бул чет өлкөдө дипломдордун таанылышын камсыз кылат.',
            'logo': '🌍',
            'year': '2005',
            'status': 'Активный',
            'status_en': 'Active',
            'status_ky': 'Активдүү',
            'validity': 'До 2028 года',
            'validity_en': 'Until 2028',
            'validity_ky': '2028-жылга чейин',
            'level': 'Международный',
            'level_en': 'International',
            'level_ky': 'Эл аралык',
            'accreditation_type': 'international',
            'benefits': ['Международное признание', 'Возможность стажировок', 'Трудоустройство за рубежом'],
            'benefits_en': ['International recognition', 'Internship opportunities', 'Employment abroad'],
            'benefits_ky': ['Эл аралык таануу', 'Стажировка мүмкүнчүлүктөрү', 'Чет өлкөдө жумуш табуу'],
            'color': 'from-green-500 to-green-600',
            'icon_color': 'text-green-100',
            'badge_color': 'bg-green-500',
            'order': 2
        },
        {
            'title': 'Ассоциация медицинских вузов Центральной Азии',
            'title_en': 'Association of Medical Universities of Central Asia',
            'title_ky': 'Борбордук Азиянын медициналык жогорку окуу жайлардын ассоциациясы',
            'description': 'Членство в ведущей региональной ассоциации медицинских учебных заведений',
            'description_en': 'Membership in the leading regional association of medical educational institutions',
            'description_ky': 'Медициналык билим берүү мекемелеринин алдыңкы аймактык ассоциациясынын мүчөлүгү',
            'full_description': 'Университет активно участвует в разработке образовательных стандартов для медицинских вузов Центральной Азии.',
            'full_description_en': 'The university actively participates in the development of educational standards for medical universities in Central Asia.',
            'full_description_ky': 'Университет Борбордук Азиядагы медициналык жогорку окуу жайлар үчүн билим берүү стандарттарын иштеп чыгууга активдүү катышат.',
            'logo': '⚕️',
            'year': '2010',
            'status': 'Активный',
            'status_en': 'Active',
            'status_ky': 'Активдүү',
            'validity': 'Бессрочно',
            'validity_en': 'Indefinitely',
            'validity_ky': 'Мөөнөтсүз',
            'level': 'Региональный',
            'level_en': 'Regional',
            'level_ky': 'Аймактык',
            'accreditation_type': 'regional',
            'benefits': ['Обмен опытом', 'Совместные исследования', 'Академическая мобильность'],
            'benefits_en': ['Experience exchange', 'Joint research', 'Academic mobility'],
            'benefits_ky': ['Тажрыйба алмашуу', 'Биргелешкен изилдөө', 'Академиялык мобилдүүлүк'],
            'color': 'from-purple-500 to-purple-600',
            'icon_color': 'text-purple-100',
            'badge_color': 'bg-purple-500',
            'order': 3
        },
        {
            'title': 'Фонд развития медицинского образования',
            'title_en': 'Medical Education Development Fund',
            'title_ky': 'Медициналык билим берүүнү өнүктүрүү фонду',
            'description': 'Аккредитация программ последипломного медицинского образования',
            'description_en': 'Accreditation of postgraduate medical education programs',
            'description_ky': 'Дипломдон кийинки медициналык билим берүү программаларынын аккредитациясы',
            'full_description': 'Программы ординатуры и повышения квалификации аккредитованы по международным стандартам.',
            'full_description_en': 'Residency and professional development programs are accredited according to international standards.',
            'full_description_ky': 'Ординатура жана квалификацияны жогорулатуу программалары эл аралык стандарттар боюнча аккредитациядан өткөн.',
            'logo': '📚',
            'year': '2015',
            'status': 'Активный',
            'status_en': 'Active',
            'status_ky': 'Активдүү',
            'validity': 'До 2026 года',
            'validity_en': 'Until 2026',
            'validity_ky': '2026-жылга чейин',
            'level': 'Профессиональный',
            'level_en': 'Professional',
            'level_ky': 'Кесиптик',
            'accreditation_type': 'professional',
            'benefits': ['Повышение квалификации', 'Профессиональный рост', 'Сертификация'],
            'benefits_en': ['Professional development', 'Career growth', 'Certification'],
            'benefits_ky': ['Квалификацияны жогорулатуу', 'Кесиптик өсүү', 'Сертификация'],
            'color': 'from-orange-500 to-orange-600',
            'icon_color': 'text-orange-100',
            'badge_color': 'bg-orange-500',
            'order': 4
        },
        {
            'title': 'Европейская ассоциация университетов',
            'title_en': 'European University Association',
            'title_ky': 'Европалык университеттердин ассоциациясы',
            'description': 'Ассоциированное членство в престижной европейской организации',
            'description_en': 'Associate membership in a prestigious European organization',
            'description_ky': 'Престиждүү европалык уюмдун ассоциативдүү мүчөлүгү',
            'full_description': 'Сотрудничество с ведущими медицинскими университетами Европы по программам обмена и совместным исследованиям.',
            'full_description_en': 'Cooperation with leading European medical universities on exchange programs and joint research.',
            'full_description_ky': 'Европанын алдыңкы медициналык университеттери менен алмашуу программалары жана биргелешкен изилдөөлөр боюнча кызматташуу.',
            'logo': '🇪🇺',
            'year': '2018',
            'status': 'Активный',
            'status_en': 'Active',
            'status_ky': 'Активдүү',
            'validity': 'До 2025 года',
            'validity_en': 'Until 2025',
            'validity_ky': '2025-жылга чейин',
            'level': 'Международный',
            'level_en': 'International',
            'level_ky': 'Эл аралык',
            'accreditation_type': 'international',
            'benefits': ['Европейские стандарты', 'Студенческие обмены', 'Совместные проекты'],
            'benefits_en': ['European standards', 'Student exchanges', 'Joint projects'],
            'benefits_ky': ['Европалык стандарттар', 'Студенттик алмашуулар', 'Биргелешкен долбоорлор'],
            'color': 'from-teal-500 to-teal-600',
            'icon_color': 'text-teal-100',
            'badge_color': 'bg-teal-500',
            'order': 5
        },
        {
            'title': 'Ассоциация стоматологического образования',
            'title_en': 'Association for Dental Education',
            'title_ky': 'Стоматологиялык билим берүүнүн ассоциациясы',
            'description': 'Аккредитация стоматологических программ по международным стандартам',
            'description_en': 'Accreditation of dental programs according to international standards',
            'description_ky': 'Эл аралык стандарттар боюнча стоматологиялык программалардын аккредитациясы',
            'full_description': 'Стоматологическая программа университета соответствует требованиям ADEE и готовит специалистов мирового уровня.',
            'full_description_en': 'The university\'s dental program meets ADEE requirements and trains world-class specialists.',
            'full_description_ky': 'Университеттин стоматологиялык программасы ADEE талаптарына дал келет жана дүйнөлүк деңгээлдеги адистерди даярдайт.',
            'logo': '🦷',
            'year': '2020',
            'status': 'Активный',
            'status_en': 'Active',
            'status_ky': 'Активдүү',
            'validity': 'До 2027 года',
            'validity_en': 'Until 2027',
            'validity_ky': '2027-жылга чейин',
            'level': 'Профессиональный',
            'level_en': 'Professional',
            'level_ky': 'Кесиптик',
            'accreditation_type': 'professional',
            'benefits': ['Международные стандарты', 'Современное оборудование', 'Практическая подготовка'],
            'benefits_en': ['International standards', 'Modern equipment', 'Practical training'],
            'benefits_ky': ['Эл аралык стандарттар', 'Заманбап жабдуулар', 'Практикалык даярдык'],
            'color': 'from-indigo-500 to-indigo-600',
            'icon_color': 'text-indigo-100',
            'badge_color': 'bg-indigo-500',
            'order': 6
        }
    ]
    
    created_count = 0
    for data in accreditations_data:
        accreditation, created = Accreditation.objects.get_or_create(
            title=data['title'],
            defaults=data
        )
        if created:
            created_count += 1
            print(f"Создана аккредитация: {accreditation.title}")
        else:
            print(f"Аккредитация уже существует: {accreditation.title}")
    
    print(f"Создано {created_count} новых аккредитаций")


def create_council_types_and_members():
    """Создать данные советов и комиссий на основе фронтенда"""
    print("Создание данных советов и комиссий...")
    
    councils_data = [
        {
            'name': 'Ученый совет',
            'name_en': 'Academic Council',
            'name_ky': 'Илимий кеңеш',
            'slug': 'ученый-совет',
            'description': 'Высший коллегиальный орган управления университетом, осуществляющий общее руководство образовательной, научной и воспитательной деятельностью.',
            'description_en': 'The highest collegial governing body of the university, exercising general management of educational, scientific and educational activities.',
            'description_ky': 'Университеттин эң жогорку коллегиялык башкаруу органы, билим берүү, илимий жана тарбиялык ишмердүүлүктү жалпы башкарат.',
            'order': 1,
            'members': [
                {
                    'name': 'Иванов Иван Иванович',
                    'position': 'Ректор университета',
                    'position_en': 'University Rector',
                    'position_ky': 'Университет ректору',
                    'department': 'Администрация',
                    'department_en': 'Administration',
                    'department_ky': 'Администрация',
                    'bio': 'Доктор технических наук, профессор. Автор более 100 научных работ.',
                    'bio_en': 'Doctor of Technical Sciences, Professor. Author of more than 100 scientific works.',
                    'bio_ky': 'Техникалык илимдердин доктору, профессор. 100дөн ашык илимий эмгектин автору.',
                    'order': 1
                },
                {
                    'name': 'Петрова Анна Сергеевна',
                    'position': 'Проректор по учебной работе',
                    'position_en': 'Vice-Rector for Academic Affairs',
                    'position_ky': 'Окуу иштери боюнча проректор',
                    'department': 'Учебный отдел',
                    'department_en': 'Academic Department',
                    'department_ky': 'Окуу бөлүмү',
                    'bio': 'Кандидат педагогических наук, доцент. Стаж работы - 15 лет.',
                    'bio_en': 'Candidate of Pedagogical Sciences, Associate Professor. Work experience - 15 years.',
                    'bio_ky': 'Педагогикалык илимдердин кандидаты, доцент. Жумуш тажрыйбасы - 15 жыл.',
                    'order': 2
                },
                {
                    'name': 'Сидоров Алексей Владимирович',
                    'position': 'Декан факультета информационных технологий',
                    'position_en': 'Dean of the Faculty of Information Technology',
                    'position_ky': 'Маалыматтык технологиялар факультетинин деканы',
                    'department': 'Факультет ИТ',
                    'department_en': 'IT Faculty',
                    'department_ky': 'ИТ факультети',
                    'bio': 'Доктор технических наук, профессор. Член-корреспондент Академии наук.',
                    'bio_en': 'Doctor of Technical Sciences, Professor. Corresponding Member of the Academy of Sciences.',
                    'bio_ky': 'Техникалык илимдердин доктору, профессор. Илимдер академиясынын корреспондент-мүчөсү.',
                    'order': 3
                },
                {
                    'name': 'Кузнецова Елена Михайловна',
                    'position': 'Заведующая кафедрой экономики',
                    'position_en': 'Head of the Department of Economics',
                    'position_ky': 'Экономика кафедрасынын башчысы',
                    'department': 'Экономический факультет',
                    'department_en': 'Faculty of Economics',
                    'department_ky': 'Экономикалык факультет',
                    'bio': 'Кандидат экономических наук, доцент. Автор учебников по экономике.',
                    'bio_en': 'Candidate of Economic Sciences, Associate Professor. Author of economics textbooks.',
                    'bio_ky': 'Экономикалык илимдердин кандидаты, доцент. Экономика боюнча окуу китептердин автору.',
                    'order': 4
                }
            ]
        },
        {
            'name': 'Ректорский совет',
            'name_en': 'Rector\'s Council',
            'name_ky': 'Ректордук кеңеш',
            'slug': 'ректорский-совет',
            'description': 'Совещательный орган при ректоре университета, координирующий текущую деятельность и оперативное управление.',
            'description_en': 'An advisory body under the university rector, coordinating current activities and operational management.',
            'description_ky': 'Университет ректорунун жанындагы кеңешчи орган, учурдагы ишмердүүлүктү жана оперативдүү башкарууну координациялайт.',
            'order': 2,
            'members': [
                {
                    'name': 'Иванов Иван Иванович',
                    'position': 'Ректор университета',
                    'position_en': 'University Rector',
                    'position_ky': 'Университет ректору',
                    'department': 'Администрация',
                    'department_en': 'Administration',
                    'department_ky': 'Администрация',
                    'bio': 'Доктор технических наук, профессор. Автор более 100 научных работ.',
                    'bio_en': 'Doctor of Technical Sciences, Professor. Author of more than 100 scientific works.',
                    'bio_ky': 'Техникалык илимдердин доктору, профессор. 100дөн ашык илимий эмгектин автору.',
                    'order': 1
                },
                {
                    'name': 'Смирнов Петр Васильевич',
                    'position': 'Первый проректор',
                    'position_en': 'First Vice-Rector',
                    'position_ky': 'Биринчи проректор',
                    'department': 'Администрация',
                    'department_en': 'Administration',
                    'department_ky': 'Администрация',
                    'bio': 'Кандидат экономических наук, доцент. Стаж работы - 20 лет.',
                    'bio_en': 'Candidate of Economic Sciences, Associate Professor. Work experience - 20 years.',
                    'bio_ky': 'Экономикалык илимдердин кандидаты, доцент. Жумуш тажрыйбасы - 20 жыл.',
                    'order': 2
                },
                {
                    'name': 'Федорова Мария Петровна',
                    'position': 'Проректор по научной работе',
                    'position_en': 'Vice-Rector for Research',
                    'position_ky': 'Илимий иш боюнча проректор',
                    'department': 'Научный отдел',
                    'department_en': 'Research Department',
                    'department_ky': 'Илимий бөлүм',
                    'bio': 'Доктор физико-математических наук, профессор.',
                    'bio_en': 'Doctor of Physical and Mathematical Sciences, Professor.',
                    'bio_ky': 'Физика-математика илимдеринин доктору, профессор.',
                    'order': 3
                }
            ]
        },
        {
            'name': 'Попечительский совет',
            'name_en': 'Board of Trustees',
            'name_ky': 'Попечителдик кеңеш',
            'slug': 'попечительский-совет',
            'description': 'Орган, осуществляющий надзор за деятельностью университета, содействующий его развитию и привлечению внебюджетных средств.',
            'description_en': 'A body that supervises the activities of the university, promotes its development and attracts extra-budgetary funds.',
            'description_ky': 'Университеттин ишмердүүлүгүнө көзөмөл жүргүзүүчү, анын өнүгүшүнө жардам берүүчү жана бюджеттен тышкаркы каражаттарды тартуучу орган.',
            'order': 3,
            'members': [
                {
                    'name': 'Ковалев Андрей Николаевич',
                    'position': 'Председатель попечительского совета',
                    'position_en': 'Chairman of the Board of Trustees',
                    'position_ky': 'Попечителдик кеңештин төрагасы',
                    'department': 'Внешние организации',
                    'department_en': 'External Organizations',
                    'department_ky': 'Тышкы уюмдар',
                    'bio': 'Генеральный директор промышленного холдинга. Выпускник университета 1995 года.',
                    'bio_en': 'General Director of an industrial holding. University graduate of 1995.',
                    'bio_ky': 'Өнөр жай холдингинин башкы директору. Университеттин 1995-жылкы бүтүрүүчүсү.',
                    'order': 1
                },
                {
                    'name': 'Семенова Ольга Викторовна',
                    'position': 'Заместитель председателя',
                    'position_en': 'Vice-Chairman',
                    'position_ky': 'Төрагынын орун басары',
                    'department': 'Бизнес-сообщество',
                    'department_en': 'Business Community',
                    'department_ky': 'Бизнес коомчулугу',
                    'bio': 'Президент региональной торгово-промышленной палаты.',
                    'bio_en': 'President of the Regional Chamber of Commerce and Industry.',
                    'bio_ky': 'Аймактык соода-өнөр жай палатасынын президенти.',
                    'order': 2
                }
            ]
        },
        {
            'name': 'Профсоюзный комитет',
            'name_en': 'Trade Union Committee',
            'name_ky': 'Кесиптик бирикме комитети',
            'slug': 'профсоюзный-комитет',
            'description': 'Орган, представляющий интересы сотрудников университета, защищающий их трудовые права и социальные гарантии.',
            'description_en': 'A body representing the interests of university employees, protecting their labor rights and social guarantees.',
            'description_ky': 'Университет кызматкерлеринин кызыкчылыктарын көрсөтүүчү, алардын эмгек укуктарын жана социалдык кепилдиктерин коргоочу орган.',
            'order': 4,
            'members': [
                {
                    'name': 'Николаева Светлана Ивановна',
                    'position': 'Председатель профкома',
                    'position_en': 'Chairman of the Trade Union Committee',
                    'position_ky': 'Профкомдун төрагасы',
                    'department': 'Профсоюзная организация',
                    'department_en': 'Trade Union Organization',
                    'department_ky': 'Кесиптик бирикме уюму',
                    'bio': 'Работает в университете с 2001 года. Активный защитник прав сотрудников.',
                    'bio_en': 'Has been working at the university since 2001. Active advocate for employee rights.',
                    'bio_ky': '2001-жылдан бери университетте иштейт. Кызматкерлердин укуктарынын активдүү коргоочусу.',
                    'order': 1
                },
                {
                    'name': 'Волков Алексей Сергеевич',
                    'position': 'Заместитель председателя',
                    'position_en': 'Vice-Chairman',
                    'position_ky': 'Төрагынын орун басары',
                    'department': 'Профсоюзная организация',
                    'department_en': 'Trade Union Organization',
                    'department_ky': 'Кесиптик бирикме уюму',
                    'bio': 'Кандидат юридических наук. Специалист по трудовому праву.',
                    'bio_en': 'Candidate of Legal Sciences. Labor law specialist.',
                    'bio_ky': 'Юридикалык илимдердин кандидаты. Эмгек укугу боюнча адис.',
                    'order': 2
                }
            ]
        },
        {
            'name': 'Учебно-методический совет',
            'name_en': 'Educational and Methodological Council',
            'name_ky': 'Окуу-методикалык кеңеш',
            'slug': 'учебно-методический-совет',
            'description': 'Координационный орган, обеспечивающий качество образовательного процесса и методическое сопровождение учебных программ.',
            'description_en': 'A coordination body that ensures the quality of the educational process and methodological support of educational programs.',
            'description_ky': 'Билим берүү процессинин сапатын камсыз кылуучу жана окуу программаларын методикалык колдоочу координациялык орган.',
            'order': 5,
            'members': [
                {
                    'name': 'Федорова Мария Петровна',
                    'position': 'Председатель УМС',
                    'position_en': 'Chairman of the Educational and Methodological Council',
                    'position_ky': 'ОМК төрагасы',
                    'department': 'Учебно-методическое управление',
                    'department_en': 'Educational and Methodological Department',
                    'department_ky': 'Окуу-методикалык башкармалык',
                    'bio': 'Доктор педагогических наук, профессор. Автор методических пособий.',
                    'bio_en': 'Doctor of Pedagogical Sciences, Professor. Author of methodological manuals.',
                    'bio_ky': 'Педагогикалык илимдердин доктору, профессор. Методикалык куралдардын автору.',
                    'order': 1
                },
                {
                    'name': 'Громова Ирина Владимировна',
                    'position': 'Заместитель председателя',
                    'position_en': 'Vice-Chairman',
                    'position_ky': 'Төрагынын орун басары',
                    'department': 'Учебный отдел',
                    'department_en': 'Academic Department',
                    'department_ky': 'Окуу бөлүмү',
                    'bio': 'Кандидат педагогических наук, доцент.',
                    'bio_en': 'Candidate of Pedagogical Sciences, Associate Professor.',
                    'bio_ky': 'Педагогикалык илимдердин кандидаты, доцент.',
                    'order': 2
                }
            ]
        },
        {
            'name': 'Наградная комиссия',
            'name_en': 'Awards Commission',
            'name_ky': 'Сыйлык комиссиясы',
            'slug': 'наградная-комиссия',
            'description': 'Орган, рассматривающий вопросы поощрения сотрудников и студентов за достижения в научной, учебной и общественной деятельности.',
            'description_en': 'A body that considers issues of encouraging employees and students for achievements in scientific, educational and public activities.',
            'description_ky': 'Кызматкерлерди жана студенттерди илимий, билим берүү жана коомдук ишмердүүлүктөгү жетишкендиктери үчүн сыйлоо маселелерин карап чыгуучу орган.',
            'order': 6,
            'members': [
                {
                    'name': 'Григорьева Ольга Викторовна',
                    'position': 'Председатель наградной комиссии',
                    'position_en': 'Chairman of the Awards Commission',
                    'position_ky': 'Сыйлык комиссиясынын төрагасы',
                    'department': 'Отдел кадров',
                    'department_en': 'HR Department',
                    'department_ky': 'Кадрлар бөлүмү',
                    'bio': 'Кандидат исторических наук. Работает в университете более 25 лет.',
                    'bio_en': 'Candidate of Historical Sciences. Has been working at the university for more than 25 years.',
                    'bio_ky': 'Тарыхый илимдердин кандидаты. Университетте 25 жылдан ашык иштейт.',
                    'order': 1
                }
            ]
        },
        {
            'name': 'Комиссия по этике',
            'name_en': 'Ethics Commission',
            'name_ky': 'Этика комиссиясы',
            'slug': 'комиссия-по-этике',
            'description': 'Орган, обеспечивающий соблюдение этических норм и правил поведения в университетском сообществе.',
            'description_en': 'A body that ensures compliance with ethical norms and rules of conduct in the university community.',
            'description_ky': 'Университеттик коомчулукта этикалык нормаларды жана жүрүм-турум эрежелерин сактоону камсыз кылуучу орган.',
            'order': 7,
            'members': [
                {
                    'name': 'Дмитриев Сергей Алексеевич',
                    'position': 'Председатель комиссии по этике',
                    'position_en': 'Chairman of the Ethics Commission',
                    'position_ky': 'Этика комиссиясынын төрагасы',
                    'department': 'Юридический отдел',
                    'department_en': 'Legal Department',
                    'department_ky': 'Укуктук бөлүм',
                    'bio': 'Доктор юридических наук, профессор. Специалист по корпоративной этике.',
                    'bio_en': 'Doctor of Legal Sciences, Professor. Corporate ethics specialist.',
                    'bio_ky': 'Юридикалык илимдердин доктору, профессор. Корпоративдик этика боюнча адис.',
                    'order': 1
                }
            ]
        },
        {
            'name': 'Комиссия по льготам',
            'name_en': 'Benefits Commission',
            'name_ky': 'Жеңилдиктер комиссиясы',
            'slug': 'комиссия-по-льготам',
            'description': 'Орган, рассматривающий вопросы предоставления льгот и социальной поддержки сотрудникам и студентам университета.',
            'description_en': 'A body that considers issues of providing benefits and social support to university employees and students.',
            'description_ky': 'Университет кызматкерлерине жана студенттерине жеңилдиктерди жана социалдык колдоону берүү маселелерин карап чыгуучу орган.',
            'order': 8,
            'members': [
                {
                    'name': 'Тихонова Елена Васильевна',
                    'position': 'Председатель комиссии по льготам',
                    'position_en': 'Chairman of the Benefits Commission',
                    'position_ky': 'Жеңилдиктер комиссиясынын төрагасы',
                    'department': 'Социальный отдел',
                    'department_en': 'Social Department',
                    'department_ky': 'Социалдык бөлүм',
                    'bio': 'Кандидат социологических наук. Работает в социальной сфере 15 лет.',
                    'bio_en': 'Candidate of Sociological Sciences. Has been working in the social sphere for 15 years.',
                    'bio_ky': 'Социологиялык илимдердин кандидаты. Социалдык тармакта 15 жыл иштейт.',
                    'order': 1
                }
            ]
        },
        {
            'name': 'Финансовый комитет',
            'name_en': 'Finance Committee',
            'name_ky': 'Финансы комитети',
            'slug': 'финансовый-комитет',
            'description': 'Орган, осуществляющий контроль за финансово-хозяйственной деятельностью университета и распределением бюджетных средств.',
            'description_en': 'A body that controls the financial and economic activities of the university and the distribution of budget funds.',
            'description_ky': 'Университеттин финансы-чарба ишмердүүлүгүнө көзөмөл жүргүзүүчү жана бюджеттик каражаттарды бөлүштүрүүчү орган.',
            'order': 9,
            'members': [
                {
                    'name': 'Козлов Алексей Дмитриевич',
                    'position': 'Председатель финансового комитета',
                    'position_en': 'Chairman of the Finance Committee',
                    'position_ky': 'Финансы комитетинин төрагасы',
                    'department': 'Финансово-экономическое управление',
                    'department_en': 'Financial and Economic Department',
                    'department_ky': 'Финансы-экономикалык башкармалык',
                    'bio': 'Кандидат экономических наук. Финансовый директор университета.',
                    'bio_en': 'Candidate of Economic Sciences. Financial Director of the University.',
                    'bio_ky': 'Экономикалык илимдердин кандидаты. Университеттин финансы директору.',
                    'order': 1
                }
            ]
        },
        {
            'name': 'Антикоррупционная комиссия',
            'name_en': 'Anti-Corruption Commission',
            'name_ky': 'Коррупцияга каршы комиссия',
            'slug': 'антикоррупционная-комиссия',
            'description': 'Орган, осуществляющий профилактику коррупционных правонарушений и контроль за соблюдением антикоррупционного законодательства.',
            'description_en': 'A body that carries out the prevention of corruption offenses and monitors compliance with anti-corruption legislation.',
            'description_ky': 'Коррупциялык укук бузуулардын алдын алууну жүргүзүүчү жана коррупцияга каршы мыйзамдарды сактоого көзөмөл жүргүзүүчү орган.',
            'order': 10,
            'members': [
                {
                    'name': 'Орлов Владимир Сергеевич',
                    'position': 'Председатель антикоррупционной комиссии',
                    'position_en': 'Chairman of the Anti-Corruption Commission',
                    'position_ky': 'Коррупцияга каршы комиссиянын төрагасы',
                    'department': 'Юридический отдел',
                    'department_en': 'Legal Department',
                    'department_ky': 'Укуктук бөлүм',
                    'bio': 'Доктор юридических наук. Специалист по антикоррупционному праву.',
                    'bio_en': 'Doctor of Legal Sciences. Anti-corruption law specialist.',
                    'bio_ky': 'Юридикалык илимдердин доктору. Коррупцияга каршы укук боюнча адис.',
                    'order': 1
                }
            ]
        },
        {
            'name': 'Документы на конкурсные выборы',
            'name_en': 'Documents for Competitive Elections',
            'name_ky': 'Атаандаштык шайлоо документтери',
            'slug': 'документы-на-конкурсные-выборы',
            'description': 'Нормативные документы и материалы, регламентирующие проведение конкурсных выборов на замещение должностей в университете.',
            'description_en': 'Regulatory documents and materials governing the conduct of competitive elections for positions at the university.',
            'description_ky': 'Университетте кызматтарды толтуруу үчүн атаандаштык шайлоолорду өткөрүүнү жөнгө салуучу ченемдик документтер жана материалдар.',
            'order': 11,
            'documents': [
                {
                    'title': 'Положение о конкурсных выборах',
                    'title_en': 'Regulation on Competitive Elections',
                    'title_ky': 'Атаандаштык шайлоолор жөнүндө эреже',
                    'date': date(2023, 4, 5),
                    'size': '2.5 МБ',
                    'description': 'Основной нормативный документ, регламентирующий процедуру проведения конкурсных выборов',
                    'description_en': 'The main regulatory document governing the procedure for conducting competitive elections',
                    'description_ky': 'Атаандаштык шайлоолорду өткөрүү процедурасын жөнгө салуучу негизги ченемдик документ'
                },
                {
                    'title': 'Требования к кандидатам',
                    'title_en': 'Requirements for Candidates',
                    'title_ky': 'Талапкерлерге талаптар',
                    'date': date(2023, 4, 10),
                    'size': '1.2 МБ',
                    'description': 'Квалификационные требования и критерии отбора кандидатов',
                    'description_en': 'Qualification requirements and candidate selection criteria',
                    'description_ky': 'Квалификациялык талаптар жана талапкерлерди тандоо критерийлери'
                },
                {
                    'title': 'График проведения выборов',
                    'title_en': 'Election Schedule',
                    'title_ky': 'Шайлоо графиги',
                    'date': date(2023, 4, 15),
                    'size': '0.8 МБ',
                    'description': 'Временной график этапов проведения конкурсных выборов',
                    'description_en': 'Timeline for the stages of competitive elections',
                    'description_ky': 'Атаандаштык шайлоолордун этаптарынын убакыт графиги'
                },
                {
                    'title': 'Формы заявлений',
                    'title_en': 'Application Forms',
                    'title_ky': 'Арыз формалары',
                    'date': date(2023, 4, 20),
                    'size': '1.1 МБ',
                    'description': 'Образцы документов для подачи заявлений на участие в выборах',
                    'description_en': 'Sample documents for submitting applications for participation in elections',
                    'description_ky': 'Шайлоого катышуу үчүн арыз берүүдөгү документтердин үлгүлөрү'
                }
            ]
        }
    ]
    
    created_councils = 0
    created_members = 0
    created_documents = 0
    
    for council_data in councils_data:
        # Extract members and documents data
        members_data = council_data.pop('members', [])
        documents_data = council_data.pop('documents', [])
        
        # Create or get council type
        council_type, created = CouncilType.objects.get_or_create(
            slug=council_data['slug'],
            defaults=council_data
        )
        
        if created:
            created_councils += 1
            print(f"Создан тип совета: {council_type.name}")
        else:
            print(f"Тип совета уже существует: {council_type.name}")
        
        # Create members
        for member_data in members_data:
            member_data['council_type'] = council_type
            member, created = CouncilMember.objects.get_or_create(
                council_type=council_type,
                name=member_data['name'],
                defaults=member_data
            )
            if created:
                created_members += 1
                print(f"  Создан член совета: {member.name}")
        
        # Create documents
        for doc_data in documents_data:
            doc_data['council_type'] = council_type
            # Create a fake file path for demonstration
            doc_data['file'] = f'council_documents/{council_type.slug}/{doc_data["title"].lower().replace(" ", "_")}.pdf'
            document, created = CouncilDocument.objects.get_or_create(
                council_type=council_type,
                title=doc_data['title'],
                defaults=doc_data
            )
            if created:
                created_documents += 1
                print(f"  Создан документ: {document.title}")
    
    print(f"\nИтого создано:")
    print(f"- Типов советов: {created_councils}")
    print(f"- Членов советов: {created_members}")
    print(f"- Документов: {created_documents}")


def main():
    """Основная функция запуска скрипта"""
    print("=" * 80)
    print("Заполнение базы данных для компонентов Status и Advices")
    print("=" * 80)
    
    try:
        # Создать аккредитации
        create_accreditations()
        print()
        
        # Создать советы и их членов
        create_council_types_and_members()
        print()
        
        print("=" * 80)
        print("✅ Скрипт успешно завершен!")
        print("=" * 80)
        
    except Exception as e:
        print(f"❌ Ошибка при выполнении скрипта: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()
