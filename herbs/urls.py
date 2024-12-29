from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('herbs/', views.herb_list, name='herb_list'),
    path('herbs/<int:herb_id>/', views.herb_detail, name='herb_detail'),
    path('medicinal-uses/', views.medicinal_use_list, name='medicinal_use_list'), 
    path('<int:medicinal_use_id>/medicinal-use/', views.medicinal_use_detail, name='medicinal_use_detail'),
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('recipes/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
]