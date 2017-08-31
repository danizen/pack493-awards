from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404

from .models import Den, Adventure, Award, Scout


class DensView(ListView):
    template_name = 'awards/dens.html'

    def get_queryset(self):
        return Den.objects.all()


@login_required
def scout_list_view(request):
	return render(request, 'awards/scouts.html')


class DenScoutsView(ListView):
    template_name = 'awards/denscouts.html'

    def get_queryset(self):
        self.den = get_object_or_404(Den, pk=self.args[0])
        return Scout.objects.filter(den=self.den).order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['den'] = self.den
        return context


@login_required
def new_scout_view(request):
    return render(request, 'awards/newscout.html')


@login_required
def show_scout_view(request):
    return render(request, 'awards/ascout.html')

