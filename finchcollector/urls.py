"""finchcollector URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from main_app import views
from main_app.views import FinchCreateView, FinchUpdateView, FinchDeleteView



urlpatterns = [
    path('finch/create/', FinchCreateView.as_view(), name='finch_create'),
    path('finch/<int:pk>/update/', FinchUpdateView.as_view(), name='finch_update'),
    path('finch/<int:pk>/delete/', FinchDeleteView.as_view(), name='finch_delete'),
    path('admin/', admin.site.urls),
    path('', views.finch_list, name='finch_list'),
    path('about/', views.about, name='about'),
    path('finches/', views.finch_list, name='finch_list'),
    path('finches/<int:finch_id>/', views.finch_detail, name='finch_detail'),
     path('toys/', views.ToyListView.as_view(), name='toy_list'),
    path('toys/add/', views.ToyCreateView.as_view(), name='toy_add'),
    path('finches/<int:pk>/', views.FinchDetailView.as_view(), name='finch_detail')
]