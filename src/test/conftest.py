import pytest
from autoru_service.models import Mark, Model

@pytest.fixture(scope='function')
def reset_db():
    Mark.objects.all().delete()
    Model.objects.all().delete()

@pytest.fixture(scope='function')
def xml_data(tmp_path):
    xml_content = """
    <cars>
        <mark name="Brand1">
            <code>123</code>
            <folder>
                <model>Model1</model>
                <generation id="1">
                    <modification name="Mod1" id="1">
                        <configuration_id>1</configuration_id>
                        <tech_param_id>2</tech_param_id>
                        <body_type>Sedan</body_type>
                        <years>2020</years>
                        <complectations>Basic</complectations>
                    </modification>
                </generation>
            </folder>
        </mark>
    </cars>
    """
    xml_file_path = tmp_path / "test_cars.xml"
    with open(xml_file_path, 'w', encoding='utf-8') as file:
        file.write(xml_content)
    return xml_file_path
