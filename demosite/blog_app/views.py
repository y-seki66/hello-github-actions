from django.views import generic
from .models import Film

class FilmList(generic.ListView):
    queryset = Film.objects.filter(status=1).order_by('created_on')
    template_name = 'index.html'

class FilmDetail(generic.DetailView):
    model = Film
    template_name = 'film_detail.html'
