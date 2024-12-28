from django.shortcuts import get_object_or_404, render
from .models import Herb


def home(request):
    return render(request, 'home.html')

def herb_list(request):
    herbs = Herb.objects.prefetch_related('herbmedicinaluse_set__medicinal_use').all()
    return render(request, 'herbs_list.html', {'herbs': herbs})

def herb_detail(request, herb_id):
    herb = get_object_or_404(Herb, id=herb_id)
    medicinal_uses = herb.herbmedicinaluse_set.select_related('medicinal_use')
    return render(request, 'herb_detail.html', {'herb': herb, 'medicinal_uses': medicinal_uses})
