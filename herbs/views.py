from django.shortcuts import get_object_or_404, render
from .models import Herb, MedicinalUse, HerbMedicinalUse, Recipe


def home(request):
    return render(request, 'home.html')

def herb_list(request):
    # Fetch all herbs with related medicinal uses, alphabetically sorted by name
    herbs = Herb.objects.prefetch_related('herb_medicinal_uses__medicinal_use').order_by('name')
    return render(request, 'herbs_list.html', {'herbs': herbs})

def herb_detail(request, herb_id):
    herb = get_object_or_404(Herb, id=herb_id)
    # Ensure the relationship is being fetched correctly
    medicinal_uses = herb.herb_medicinal_uses.select_related('medicinal_use').all()
    return render(request, 'herb_detail.html', {'herb': herb, 'medicinal_uses': medicinal_uses})

def medicinal_use_list(request):
    # Order the medicinal uses alphabetically by name
    medicinal_uses = MedicinalUse.objects.prefetch_related('medicinal_use_herbs__herb').order_by('name')
    return render(request, 'medicinal_use_list.html', {'medicinal_uses': medicinal_uses})

def medicinal_use_detail(request, medicinal_use_id):
    medicinal_use = get_object_or_404(MedicinalUse, id=medicinal_use_id)
    related_herbs = HerbMedicinalUse.objects.filter(medicinal_use=medicinal_use).select_related('herb')
    return render(request, 'medicinal_use_detail.html', {
        'medicinal_use': medicinal_use,
        'related_herbs': related_herbs,
    })

def recipe_list(request):
    recipes = Recipe.objects.order_by('title')  # Alphabetically sort recipes by title
    return render(request, 'recipe_list.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})