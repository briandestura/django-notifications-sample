from django.shortcuts import render

from django.views.generic import ListView
from .models import Badassness


# Create your views here.
class BadassListView(ListView):
    model = Badassness
    paginate_by = 5
    context_object_name = 'badasses'
    template_name = 'foo/badass_list.html'


def test(request):
    return render(request, 'foo/test_live.html')
