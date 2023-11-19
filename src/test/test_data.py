import pytest
from autoru_service.models import Mark, Model
from autoru_service.perser_avto_to_db import parse_xml_file
from autoru_service.views import (delete_autoru_catalog, home, paginate_models, update_autoru_catalog)
from datetime import datetime, timedelta
from django.test import RequestFactory
from django.utils import timezone

# Тест для парсера
@pytest.mark.django_db
def test_parse_xml_file(xml_data):
    parse_xml_file(xml_data)

    assert Mark.objects.count() == 1
    assert Model.objects.count() == 1

    mark = Mark.objects.get(name="Brand1")
    assert mark.code == "123"

    model = Model.objects.get(name="Model1")
    assert model.mark == mark
    assert model.generation == 1
    assert model.modification_name == "Mod1"
    assert model.modification_id == 1
    assert model.configuration_id == 1
    assert model.tech_param_id == 2
    assert model.body_type == "Sedan"
    assert model.years == "2020"
    assert model.complectations == "Basic"


# Тест для update_autoru_catalog
@pytest.mark.django_db
def test_update_autoru_catalog(reset_db):
    request = RequestFactory().get('/')
    response = update_autoru_catalog(request)
    assert response.status_code == 302
    now = timezone.now()
    updated_model = Model.objects.first()
    time_difference = now - updated_model.created_at
    assert time_difference.total_seconds() <= 60
