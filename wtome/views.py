from django.shortcuts import render
from django.http import HttpResponse
import pathlib
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent


def home_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    owner = "Waseem"
    context = {
        "data": owner,
        "queryset": qs.count(),
        "page_visit_count": page_qs.count(),
    }
    path = request.path
    html_template = "base.html"

    PageVisit.objects.create(path=path)
    return render(request, html_template, context)


def contact(request):
    return render(request, "contactus.html")
