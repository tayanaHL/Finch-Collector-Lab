from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from main_app.models import Finch




# Create your views here.

# def finch_list(request):
#     finch_list = [{"species": "Geospiza fortis", "beak_depth": 8.6, "beak_width": 6.2, "island": "Daphne Major"},
#     {"species": "Geospiza magnirostris", "beak_depth": 10.4, "beak_width": 7.3, "island": "Santa Cruz"},
#     {"species": "Geospiza parvula", "beak_depth": 9.5, "beak_width": 6.5, "island": "Santa Cruz"},
#     ] 
#     data = []
#     for finch in finch_list:
#         data.append({
#             "species": finch["species"],
#             "beak_depth": finch["beak_depth"],
#             "beak_width": finch["beak_width"],
#             "island": finch["island"]
#         })
#     return render


def about(request):
    return render(request, 'about.html')

def finch_list(request):
    finches = Finch.objects.all()
    return render(request, 'finch_list.html', {'finches': finches})


def finch_detail(request, finch_id):
    finch = get_object_or_404(Finch, pk=finch_id)
    return render(request, 'finch_detail.html', {'finch': finch})
