from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from autoru_service.models import Mark, Model
from autoru_service.perser_avto_to_db import parse_xml_file


def update_autoru_catalog(request):
    Mark.objects.all().delete()
    Model.objects.all().delete()
    parse_xml_file()
    return redirect('home')


def delete_autoru_catalog(request):
    Mark.objects.all().delete()
    Model.objects.all().delete()
    return redirect('home')


def paginate_models(request, models):
    paginator = Paginator(models, 10)
    page_number = request.GET.get('page')
    try:
        paginated_models = paginator.page(page_number)
    except PageNotAnInteger:
        paginated_models = paginator.page(1)
    except EmptyPage:
        paginated_models = paginator.page(paginator.num_pages)
    return paginated_models



def home(request):
    all_marks = Mark.objects.all()
    selected_mark = request.GET.get('selected_mark')

    if not all_marks:
        return render(request, 'home.html', {'no_data': True})

    if request.method == 'POST':
        selected_mark = request.POST.get('selected_mark')
        return HttpResponseRedirect(f"{reverse('home')}?selected_mark={selected_mark}")

    if request.GET.get('selected_mark'):
        models_of_selected_mark = Model.objects.filter(mark__name=selected_mark)
        paginated_models = paginate_models(request, models_of_selected_mark)
        return render(request, 'home.html',
                      {'marks': all_marks, 'models': paginated_models, 'selected_mark': selected_mark})

    return render(request, 'home.html', {'marks': all_marks})
