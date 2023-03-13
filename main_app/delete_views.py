from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from main_app.models import Finch

class FinchDeleteView(DeleteView):
    model = Finch
    template_name = 'finch_confirm_delete.html'
    success_url = reverse_lazy('finch_list')