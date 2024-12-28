from django.contrib import admin
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
)

# Inline Admins
class HerbCategoryInline(admin.TabularInline):
    model = HerbCategory
    extra = 1  # Number of empty slots for new entries


class HerbMedicinalUseInline(admin.TabularInline):
    model = HerbMedicinalUse
    extra = 1
    verbose_name = "Related Herb"
    verbose_name_plural = "Related Herbs"


class HerbRegionInline(admin.TabularInline):
    model = HerbRegion
    extra = 1


class HerbCulinaryUseInline(admin.TabularInline):
    model = HerbCulinaryUse
    extra = 1


# Admin Configurations
@admin.register(Herb)
class HerbAdmin(admin.ModelAdmin):
    list_display = ('name', 'scientific_name', 'created_at', 'updated_at')
    search_fields = ('name', 'scientific_name')
    inlines = [HerbCategoryInline, HerbMedicinalUseInline, HerbRegionInline, HerbCulinaryUseInline]


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
        Display herbs related to this medicinal use in a comma-separated list.
        """
        related_herbs = Herb.objects.filter(herbmedicinaluse__medicinal_use=obj)
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