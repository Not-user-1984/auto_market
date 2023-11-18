from bs4 import BeautifulSoup

from autoru_service.models import Mark, Model


def parse_xml_file(file_path=None):
    if file_path is None:
        file_path = 'fixture/cars.xml'

    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'xml')

        for mark_tag in soup.find_all('mark'):
            mark_name = mark_tag.get('name')
            mark_code = mark_tag.find('code').text

            # Создаем или получаем объект Mark
            mark, created = Mark.objects.get_or_create(name=mark_name, defaults={'code': mark_code})

            for folder_tag in mark_tag.find_all('folder'):
                model_name = folder_tag.find('model').text
                generation_id = folder_tag.find('generation').get('id')

                for modification_tag in folder_tag.find_all('modification'):
                    modification_name = modification_tag.get('name')
                    modification_id = modification_tag.get('id')
                    configuration_id = modification_tag.find('configuration_id').text
                    tech_param_id = modification_tag.find('tech_param_id').text
                    body_type = modification_tag.find('body_type').text
                    years = modification_tag.find('years').text
                    complectations = modification_tag.find('complectations').text
                    Model.objects.create(
                        mark=mark,
                        name=model_name,
                        generation=generation_id,
                        modification_name=modification_name,
                        modification_id=modification_id,
                        configuration_id=configuration_id,
                        tech_param_id=tech_param_id,
                        body_type=body_type,
                        years=years,
                        complectations=complectations
                    )
