from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from main_app.models import Finch, Feeding, Toy
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from main_app.forms import FinchForm, FeedingForm
from django.shortcuts import redirect
from django.views.generic import ListView



def about(request):
    return render(request, 'about.html')

def finch_list(request):
    finches = Finch.objects.all()
    return render(request, 'finch_list.html', {'finches': finches})

def finch_detail(request, finch_id):
    finch = get_object_or_404(Finch, pk=finch_id)
    feedings = finch.feedings.all().order_by('-date')
    if request.method == 'POST':
        form = FeedingForm(request.POST)
        if form.is_valid():
            feeding = form.save(commit=False)
            feeding.finch = finch
            feeding.save()
            return redirect('finch_detail', finch_id=finch.id)
    else:
        form = FeedingForm()
    return render(request, 'finch_detail.html', {'finch': finch, 'form': form, 'feedings': feedings})


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

class FeedingCreateView(CreateView):
    model = Feeding
    form_class = FeedingForm
    template_name = 'feeding_form.html'

    def form_valid(self, form):
        finch = get_object_or_404(Finch, pk=self.kwargs['pk'])
        form.instance.finch = finch
        return super().form_valid(form)

    def get_success_url(self):
        finch = self.object.finch
        return reverse_lazy('finch_detail', args=[finch.pk])

    
class ToyListView(ListView):
    model = Toy
    template_name = 'main_app/toy_list.html'


class ToyCreateView(CreateView):
    model = Toy
    template_name = 'main_app/toy_form.html'
    fields = '__all__'


class FinchDetailView(DetailView):
    model = Finch
    template_name = 'main_app/finch_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        finch = self.object
        toys = Toy.objects.all()
        available_toys = [t for t in toys if finch not in t.finches.all()]
        context['toys'] = finch.toys.all()
        context['available_toys'] = available_toys
        return context

