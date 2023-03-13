from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from main_app.models import Finch
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from main_app.models import Finch, FinchForm


def about(request):
    return render(request, 'about.html')

def finch_list(request):
    finches = Finch.objects.all()
    return render(request, 'finch_list.html', {'finches': finches})

def finch_detail(request, finch_id):
    finch = get_object_or_404(Finch, pk=finch_id)
    return render(request, 'finch_detail.html', {'finch': finch})


class FinchCreateView(CreateView):
    model = Finch
    form_class = FinchForm
    template_name = 'finch_form.html'
    success_url = reverse_lazy('finch_list')

class FinchUpdateView(UpdateView):
    model = Finch
    form_class = FinchForm
    template_name = 'finch_form.html'
    success_url = reverse_lazy('finch_list')

class FinchDeleteView(DeleteView):
    model = Finch
    template_name = 'finch_delete.html'
    success_url = reverse_lazy('finch_list')