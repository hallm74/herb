from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import (
    Herb,
    Category,
    HerbCategory,
    MedicinalUse,
    HerbMedicinalUse,
    GrowingCondition,
    Region,
    HerbRegion,
    CulinaryUse,
    HerbCulinaryUse,
    Recipe
)
from .forms import HerbAdminForm

# Inline Admins
class HerbCategoryInline(admin.TabularInline):
    model = HerbCategory
    extra = 1


class HerbMedicinalUseInline(admin.TabularInline):
    model = HerbMedicinalUse
    extra = 1
    verbose_name = "Medicinal Use"
    verbose_name_plural = "Medicinal Uses"


class HerbRegionInline(admin.TabularInline):
    model = HerbRegion
    extra = 1


class HerbCulinaryUseInline(admin.TabularInline):
    model = HerbCulinaryUse
    extra = 1


@admin.register(Herb)
class HerbAdmin(admin.ModelAdmin):
    form = HerbAdminForm
    list_display = ('name', 'scientific_name', 'created_at', 'updated_at', 'image_display')
    search_fields = ('name', 'scientific_name')
    inlines = [HerbCategoryInline, HerbMedicinalUseInline, HerbRegionInline, HerbCulinaryUseInline]

    class Media:
        js = ('js/unsplash_search.js',)  # Include the Unsplash search JavaScript

    def image_display(self, obj):
        """
        Displays an image thumbnail in the admin interface.
        Priority: local image > Unsplash image > no image message.
        """
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" alt="{obj.name}" style="max-height: 50px;">')
        elif obj.unsplash_image_url:
            return mark_safe(f'<img src="{obj.unsplash_image_url}" alt="{obj.name}" style="max-height: 50px;">')
        return "No Image"

    image_display.short_description = "Image"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(MedicinalUse)
class MedicinalUseAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_related_herbs')
    search_fields = ('name',)
    inlines = [HerbMedicinalUseInline]

    @admin.display(description='Herbs')
    def get_related_herbs(self, obj):
        """
        Fetches related herbs for a given MedicinalUse object.
        """
        related_herbs = Herb.objects.filter(herb_medicinal_uses__medicinal_use=obj)
        return ", ".join([herb.name for herb in related_herbs])


@admin.register(GrowingCondition)
class GrowingConditionAdmin(admin.ModelAdmin):
    list_display = ('herb', 'light_requirements', 'soil_type', 'watering_needs', 'temperature')
    search_fields = ('herb__name',)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(CulinaryUse)
class CulinaryUseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'text')
    filter_horizontal = ('herbs',)