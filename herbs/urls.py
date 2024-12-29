from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('herbs/', views.herb_list, name='herb_list'),
    path('herbs/<int:herb_id>/', views.herb_detail, name='herb_detail'),
    path('medicinal-uses/', views.medicinal_use_list, name='medicinal_use_list'), 
]