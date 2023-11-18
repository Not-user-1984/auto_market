from datetime import datetime, timedelta

from django.shortcuts import redirect, render

from autoru_service.models import Mark, Model
from autoru_service.perser_avto_to_db import parse_xml_file


def update_autoru_catalog(request):
    last_update = Model.objects.order_by('-id').first()
    if not last_update:
        Mark.objects.all().delete()
        Model.objects.all().delete()
        parse_xml_file()
        return redirect('home')
    else:
        Mark.objects.all().delete()
        Model.objects.all().delete()
        parse_xml_file()
        return redirect('home')

def home(request):
    all_marks = Mark.objects.all()
    if request.method == 'GET' and not all_marks:
        return render(request, 'home.html', {'no_data': True})
    elif request.method == 'POST':
        selected_mark = request.POST.get('selected_mark')
        models_of_selected_mark = Model.objects.filter(mark__name=selected_mark)
        return render(request, 'home.html', {'marks': all_marks, 'models': models_of_selected_mark})
    return render(request, 'home.html', {'marks': all_marks})
