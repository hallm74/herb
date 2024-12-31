from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (
    home,
    herb_list,
    herb_detail,
    medicinal_use_list,
    medicinal_use_detail,
    recipe_list,
    recipe_detail,
    search_view,
    unsplash_search_view  # Ensure this is included
)

urlpatterns = [
    path('', home, name='home'),
    path('herbs/', herb_list, name='herb_list'),
    path('herbs/<int:herb_id>/', herb_detail, name='herb_detail'),
    path('medicinal-uses/', medicinal_use_list, name='medicinal_use_list'),
    path('<int:medicinal_use_id>/medicinal-use/', medicinal_use_detail, name='medicinal_use_detail'),
    path('recipes/', recipe_list, name='recipe_list'),
    path('recipes/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    path('search/', search_view, name='search'),
    path('unsplash-search/', unsplash_search_view, name='unsplash_search'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)