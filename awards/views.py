from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404

from .forms import ScoutForm
from .models import Den, Adventure, Award, Scout


@method_decorator(login_required, name='dispatch')
class DensView(ListView):
    template_name = 'awards/dens.html'

    def get_queryset(self):
        return Den.objects.all()


@login_required
def scout_list_view(request):
	return render(request, 'awards/scouts.html')


@method_decorator(login_required, name='dispatch')
class DenScoutsView(ListView):
    template_name = 'awards/denscouts.html'

    def get_queryset(self):
        self.den = get_object_or_404(Den, pk=self.args[0])
        return Scout.objects.filter(den=self.den).order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['den'] = self.den
        return context


@method_decorator(login_required, name='dispatch')
class NewScoutView(CreateView):
    template_name = 'awards/newscout.html'
    form_class = ScoutForm
    success_url = reverse_lazy('den-list')


@method_decorator(login_required, name='dispatch')
class UpdateScoutView(CreateView):
    template_name = 'awards/ascout.html'
    form_class = ScoutForm
    success_url = reverse_lazy('den-list')


@method_decorator(login_required, name='dispatch')
class DeleteScoutView(DeleteView):
    template_name = 'awards/delscout.html'
    success_url = reverse_lazy('den-list')

