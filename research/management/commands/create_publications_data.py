from django.core.management.base import BaseCommand
from research.models import Publication, ResearchCenter, ResearchArea
from datetime import date, datetime
import random


class Command(BaseCommand):
    help = 'Создать тестовые данные для публикаций'

    def handle(self, *args, **options):
        # Очистка существующих данных
        Publication.objects.all().delete()
        
        # Создание исследовательских центров если их нет
        centers_data = [
            {
                'name_ru': 'Центр молекулярной биологии',
                'name_en': 'Center for Molecular Biology',
                'name_kg': 'Молекулярдык биология борбору',
                'description_ru': 'Исследования в области молекулярной биологии и генетики',
                'description_en': 'Research in molecular biology and genetics',
                'description_kg': 'Молекулярдык биология жана генетика тармагындагы изилдөөлөр',
                'director': 'Проф. Алиев А.К.',
                'staff_count': 15,
                'established_year': 2010,
            },
            {
                'name_ru': 'Центр клинических исследований',
                'name_en': 'Clinical Research Center',
                'name_kg': 'Клиникалык изилдөөлөр борбору',
                'description_ru': 'Клинические испытания и исследования',
                'description_en': 'Clinical trials and research',
                'description_kg': 'Клиникалык сыноолор жана изилдөөлөр',
                'director': 'Проф. Кадырова М.С.',
                'staff_count': 20,
                'established_year': 2012,
            },
            {
                'name_ru': 'Центр биомедицинских технологий',
                'name_en': 'Biomedical Technologies Center',
                'name_kg': 'Биомедициналык технологиялар борбору',
                'description_ru': 'Разработка биомедицинских технологий',
                'description_en': 'Development of biomedical technologies',
                'description_kg': 'Биомедициналык технологияларды иштеп чыгуу',
                'director': 'Проф. Токтосунов Б.А.',
                'staff_count': 12,
                'established_year': 2015,
            }
        ]
        
        for center_data in centers_data:
            ResearchCenter.objects.get_or_create(**center_data)
        
        # Создание областей исследований если их нет
        areas_data = [
            {
                'title_ru': 'Молекулярная биология',
                'title_en': 'Molecular Biology',
                'title_kg': 'Молекулярдык биология',
                'description_ru': 'Исследование молекулярных основ жизни',
                'description_en': 'Study of molecular basis of life',
                'description_kg': 'Жашоонун молекулярдык негиздерин изилдөө',
                'icon': '🧬',
                'color': 'blue',
            },
            {
                'title_ru': 'Клиническая медицина',
                'title_en': 'Clinical Medicine',
                'title_kg': 'Клиникалык медицина',
                'description_ru': 'Клинические исследования и практика',
                'description_en': 'Clinical research and practice',
                'description_kg': 'Клиникалык изилдөөлөр жана практика',
                'icon': '🏥',
                'color': 'green',
            },
            {
                'title_ru': 'Биотехнологии',
                'title_en': 'Biotechnology',
                'title_kg': 'Биотехнологиялар',
                'description_ru': 'Биотехнологические разработки',
                'description_en': 'Biotechnological developments',
                'description_kg': 'Биотехнологиялык иштеп чыгуулар',
                'icon': '🔬',
                'color': 'purple',
            }
        ]
        
        for area_data in areas_data:
            ResearchArea.objects.get_or_create(**area_data)
        
        centers = list(ResearchCenter.objects.all())
        areas = list(ResearchArea.objects.all())
        
        # Данные публикаций
        publications_data = [
            {
                'title_ru': 'Молекулярные механизмы патогенеза сердечно-сосудистых заболеваний',
                'title_en': 'Molecular mechanisms of cardiovascular disease pathogenesis',
                'title_kg': 'Жүрөк-кан тамыр оорууларынын патогенезинин молекулярдык механизмдери',
                'authors': 'Алиев А.К., Кадырова М.С., Смирнов И.В., Жолдошбеков А.А.',
                'journal': 'Journal of Cardiovascular Research',
                'publication_date': date(2024, 3, 15),
                'publication_type': 'article',
                'impact_factor': 4.25,
                'citations_count': 23,
                'doi': '10.1001/jcr.2024.001',
                'abstract_ru': 'В данном исследовании изучены молекулярные механизмы развития сердечно-сосудистых заболеваний. Проанализированы генетические факторы и биохимические маркеры.',
                'abstract_en': 'This study investigated the molecular mechanisms of cardiovascular disease development. Genetic factors and biochemical markers were analyzed.',
                'abstract_kg': 'Бул изилдөөдө жүрөк-кан тамыр оорууларынын өнүгүүсүнүн молекулярдык механизмдери изилденген. Генетикалык факторлор жана биохимиялык белгилер талданган.',
                'keywords_ru': ['молекулярная биология', 'кардиология', 'патогенез'],
                'keywords_en': ['molecular biology', 'cardiology', 'pathogenesis'],
                'keywords_kg': ['молекулярдык биология', 'кардиология', 'патогенез'],
            },
            {
                'title_ru': 'Новые подходы к диагностике онкологических заболеваний',
                'title_en': 'Novel approaches to cancer diagnosis',
                'title_kg': 'Рак оорууларын диагностикалоонун жаңы ыкмалары',
                'authors': 'Токтосунов Б.А., Нурматова А.Б., Петров С.Д.',
                'journal': 'Cancer Diagnostics International',
                'publication_date': date(2024, 1, 20),
                'publication_type': 'article',
                'impact_factor': 5.12,
                'citations_count': 34,
                'doi': '10.1002/cdi.2024.005',
                'abstract_ru': 'Представлены инновационные методы ранней диагностики онкологических заболеваний с использованием биомаркеров.',
                'abstract_en': 'Innovative methods for early cancer diagnosis using biomarkers are presented.',
                'abstract_kg': 'Биобелгилерди колдонуу менен рак оорууларын эрте диагностикалоонун инновациялык ыкмалары көрсөтүлгөн.',
                'keywords_ru': ['онкология', 'диагностика', 'биомаркеры'],
                'keywords_en': ['oncology', 'diagnostics', 'biomarkers'],
                'keywords_kg': ['онкология', 'диагностика', 'биобелгилер'],
            },
            {
                'title_ru': 'Эффективность телемедицины в условиях пандемии COVID-19',
                'title_en': 'Effectiveness of telemedicine during COVID-19 pandemic',
                'title_kg': 'COVID-19 пандемиясы учурундагы телемедицинанын эффективдүүлүгү',
                'authors': 'Жолдошбеков А.А., Исаева Н.К., Браун М.',
                'journal': 'Telemedicine and e-Health',
                'publication_date': date(2023, 11, 10),
                'publication_type': 'article',
                'impact_factor': 3.87,
                'citations_count': 45,
                'doi': '10.1089/tmj.2023.0234',
                'abstract_ru': 'Анализ эффективности применения телемедицинских технологий в период пандемии COVID-19.',
                'abstract_en': 'Analysis of the effectiveness of telemedicine technologies during the COVID-19 pandemic.',
                'abstract_kg': 'COVID-19 пандемиясы учурунда телемедициналык технологияларды колдонуунун натыйжалуулугун талдоо.',
                'keywords_ru': ['телемедицина', 'COVID-19', 'цифровое здоровье'],
                'keywords_en': ['telemedicine', 'COVID-19', 'digital health'],
                'keywords_kg': ['телемедицина', 'COVID-19', 'санариптик ден соолук'],
            },
            {
                'title_ru': 'Генетические аспекты резистентности к антибиотикам',
                'title_en': 'Genetic aspects of antibiotic resistance',
                'title_kg': 'Антибиотиктерге каршылыктын генетикалык аспектилери',
                'authors': 'Нурматова А.Б., Алиев А.К., Джонсон Р.',
                'journal': 'Nature Microbiology',
                'publication_date': date(2023, 8, 5),
                'publication_type': 'article',
                'impact_factor': 15.54,
                'citations_count': 67,
                'doi': '10.1038/nmicrobiol.2023.156',
                'abstract_ru': 'Исследование генетических механизмов формирования резистентности бактерий к антибиотикам.',
                'abstract_en': 'Study of genetic mechanisms of bacterial antibiotic resistance formation.',
                'abstract_kg': 'Бактериялардын антибиотиктерге каршылыгынын калыптанышынын генетикалык механизмдерин изилдөө.',
                'keywords_ru': ['генетика', 'антибиотики', 'резистентность'],
                'keywords_en': ['genetics', 'antibiotics', 'resistance'],
                'keywords_kg': ['генетика', 'антибиотиктер', 'каршылык'],
            },
            {
                'title_ru': 'Применение искусственного интеллекта в медицинской диагностике',
                'title_en': 'Application of artificial intelligence in medical diagnostics',
                'title_kg': 'Медициналык диагностикада жасалма интеллектти колдонуу',
                'authors': 'Петров С.Д., Кадырова М.С., Ли Ч.',
                'journal': 'AI in Medicine',
                'publication_date': date(2023, 6, 12),
                'publication_type': 'article',
                'impact_factor': 7.21,
                'citations_count': 89,
                'doi': '10.1016/j.aiimed.2023.102156',
                'abstract_ru': 'Обзор современных методов применения ИИ в медицинской диагностике и их эффективность.',
                'abstract_en': 'Review of modern AI methods in medical diagnostics and their effectiveness.',
                'abstract_kg': 'Медициналык диагностикада ИИнин заманбап ыкмаларын жана алардын натыйжалуулугун карап чыгуу.',
                'keywords_ru': ['искусственный интеллект', 'диагностика', 'машинное обучение'],
                'keywords_en': ['artificial intelligence', 'diagnostics', 'machine learning'],
                'keywords_kg': ['жасалма интеллект', 'диагностика', 'машиналык үйрөнүү'],
            },
            {
                'title_ru': 'Биомеханика движения человека: новые подходы к реабилитации',
                'title_en': 'Human movement biomechanics: new approaches to rehabilitation',
                'title_kg': 'Адамдын кыймылынын биомеханикасы: реабилитациянын жаңы ыкмалары',
                'authors': 'Смирнов И.В., Токтосунов Б.А., Андерсон К.',
                'journal': 'Journal of Biomechanics',
                'publication_date': date(2023, 4, 18),
                'publication_type': 'article',
                'impact_factor': 2.89,
                'citations_count': 28,
                'doi': '10.1016/j.jbiomech.2023.111625',
                'abstract_ru': 'Исследование биомеханических аспектов движения и разработка новых методов реабилитации.',
                'abstract_en': 'Study of biomechanical aspects of movement and development of new rehabilitation methods.',
                'abstract_kg': 'Кыймылдын биомеханикалык аспектилерин изилдөө жана реабилитациянын жаңы ыкмаларын иштеп чыгуу.',
                'keywords_ru': ['биомеханика', 'реабилитация', 'движение'],
                'keywords_en': ['biomechanics', 'rehabilitation', 'movement'],
                'keywords_kg': ['биомеханика', 'реабилитация', 'кыймыл'],
            },
            {
                'title_ru': 'Наномедицина: перспективы и вызовы',
                'title_en': 'Nanomedicine: prospects and challenges',
                'title_kg': 'Наномедицина: перспективалар жана чакырыктар',
                'authors': 'Исаева Н.К., Жолдошбеков А.А., Ямамото Т.',
                'journal': 'Nature Nanotechnology',
                'publication_date': date(2024, 2, 28),
                'publication_type': 'article',
                'impact_factor': 35.47,
                'citations_count': 156,
                'doi': '10.1038/nnano.2024.045',
                'abstract_ru': 'Анализ текущего состояния и будущих перспектив развития наномедицины.',
                'abstract_en': 'Analysis of current state and future prospects of nanomedicine development.',
                'abstract_kg': 'Наномедицинанын учурдагы абалын жана келечектеги өнүгүү перспективаларын талдоо.',
                'keywords_ru': ['наномедицина', 'нанотехнологии', 'лекарственные препараты'],
                'keywords_en': ['nanomedicine', 'nanotechnology', 'drug delivery'],
                'keywords_kg': ['наномедицина', 'нанотехнологиялар', 'дары каражаттары'],
            },
            {
                'title_ru': 'Персонализированная медицина на основе геномного анализа',
                'title_en': 'Personalized medicine based on genomic analysis',
                'title_kg': 'Геномдук талдоого негизделген жекелештирилген медицина',
                'authors': 'Браун М., Нурматова А.Б., Гарсия М.',
                'journal': 'Genome Medicine',
                'publication_date': date(2024, 5, 3),
                'publication_type': 'article',
                'impact_factor': 12.3,
                'citations_count': 78,
                'doi': '10.1186/s13073-024-01248-x',
                'abstract_ru': 'Разработка персонализированных подходов к лечению на основе геномного профилирования пациентов.',
                'abstract_en': 'Development of personalized treatment approaches based on patient genomic profiling.',
                'abstract_kg': 'Бейтаптардын геномдук профилдөөсүнө негизделген жекелештирилген дарылоо ыкмаларын иштеп чыгуу.',
                'keywords_ru': ['персонализированная медицина', 'геномика', 'биоинформатика'],
                'keywords_en': ['personalized medicine', 'genomics', 'bioinformatics'],
                'keywords_kg': ['жекелештирилген медицина', 'геномика', 'биоинформатика'],
            },
            {
                'title_ru': 'Влияние экологических факторов на здоровье населения',
                'title_en': 'Impact of environmental factors on population health',
                'title_kg': 'Экологиялык факторлордун калктын ден соолугуна тийгизген таасири',
                'authors': 'Джонсон Р., Алиев А.К., Мюллер Х.',
                'journal': 'Environmental Health Perspectives',
                'publication_date': date(2023, 12, 15),
                'publication_type': 'article',
                'impact_factor': 9.18,
                'citations_count': 92,
                'doi': '10.1289/EHP11234',
                'abstract_ru': 'Комплексное исследование влияния загрязнения окружающей среды на здоровье населения.',
                'abstract_en': 'Comprehensive study of environmental pollution impact on population health.',
                'abstract_kg': 'Айлана-чөйрөнүн булганышынын калктын ден соолугуна тийгизген таасирин комплекстүү изилдөө.',
                'keywords_ru': ['экология', 'общественное здоровье', 'загрязнение'],
                'keywords_en': ['ecology', 'public health', 'pollution'],
                'keywords_kg': ['экология', 'коомдук ден соолук', 'булгануу'],
            },
            {
                'title_ru': 'Стволовые клетки в регенеративной медицине',
                'title_en': 'Stem cells in regenerative medicine',
                'title_kg': 'Регенеративдик медицинадагы стволовые клеткалар',
                'authors': 'Ли Ч., Петров С.Д., Кумар А.',
                'journal': 'Cell Stem Cell',
                'publication_date': date(2024, 4, 8),
                'publication_type': 'article',
                'impact_factor': 23.68,
                'citations_count': 134,
                'doi': '10.1016/j.stem.2024.03.012',
                'abstract_ru': 'Современные достижения в области применения стволовых клеток для регенеративной медицины.',
                'abstract_en': 'Recent advances in stem cell applications for regenerative medicine.',
                'abstract_kg': 'Регенеративдик медицина үчүн стволовые клеткаларды колдонуу тармагындагы заманбап жетишкендиктер.',
                'keywords_ru': ['стволовые клетки', 'регенерация', 'клеточная терапия'],
                'keywords_en': ['stem cells', 'regeneration', 'cell therapy'],
                'keywords_kg': ['стволовые клеткалар', 'регенерация', 'клеткалык терапия'],
            }
        ]
        
        # Создание публикаций
        publications_created = 0
        for pub_data in publications_data:
            # Случайное назначение центра и области исследований
            pub_data['research_center'] = random.choice(centers) if centers else None
            pub_data['research_area'] = random.choice(areas) if areas else None
            
            publication = Publication.objects.create(**pub_data)
            publications_created += 1
            
        self.stdout.write(
            self.style.SUCCESS(f'Успешно создано {publications_created} публикаций')
        )
