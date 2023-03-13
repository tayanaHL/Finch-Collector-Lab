from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from main_app.models import Finch, FinchForm


class FinchCreateView(CreateView):
    model = Finch
    form_class = FinchForm
    template_name = 'finch_form.html'
    success_url = reverse_lazy('finch_list')
