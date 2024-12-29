from django.shortcuts import get_object_or_404, render
from .models import Herb, MedicinalUse


def home(request):
    return render(request, 'home.html')

def herb_list(request):
    # Fetch all herbs, prefetch related medicinal uses, and order alphabetically by name
    herbs = Herb.objects.prefetch_related('herb_medicinal_uses__medicinal_use').order_by('name')
    return render(request, 'herbs_list.html', {'herbs': herbs})

def herb_detail(request, herb_id):
    herb = get_object_or_404(Herb, id=herb_id)
    medicinal_uses = herb.herb_medicinal_uses.select_related('medicinal_use').all()
    return render(request, 'herb_detail.html', {'herb': herb, 'medicinal_uses': medicinal_uses})

def medicinal_use_list(request):
    # Order the medicinal uses alphabetically by name
    medicinal_uses = MedicinalUse.objects.prefetch_related('medicinal_use_herbs__herb').order_by('name')
    return render(request, 'medicinal_use_list.html', {'medicinal_uses': medicinal_uses})
