from django.db import models

class Herb(models.Model):
    name = models.CharField(max_length=255, unique=True)
    scientific_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class HerbCategory(models.Model):
    herb = models.ForeignKey(Herb, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('herb', 'category')


class MedicinalUse(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class HerbMedicinalUse(models.Model):
    herb = models.ForeignKey(
        Herb,
        on_delete=models.CASCADE,
        related_name='herb_medicinal_uses'  # Unique related_name for Herb
    )
    medicinal_use = models.ForeignKey(
        MedicinalUse,
        on_delete=models.CASCADE,
        related_name='medicinal_use_herbs'  # Unique related_name for MedicinalUse
    )

    class Meta:
        unique_together = ('herb', 'medicinal_use')


class GrowingCondition(models.Model):
    herb = models.ForeignKey(Herb, on_delete=models.CASCADE)
    light_requirements = models.CharField(max_length=255, blank=True, null=True)
    soil_type = models.CharField(max_length=255, blank=True, null=True)
    watering_needs = models.CharField(max_length=255, blank=True, null=True)
    temperature = models.CharField(max_length=255, blank=True, null=True)


class Region(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class HerbRegion(models.Model):
    herb = models.ForeignKey(Herb, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('herb', 'region')


class CulinaryUse(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class HerbCulinaryUse(models.Model):
    herb = models.ForeignKey(Herb, on_delete=models.CASCADE)
    culinary_use = models.ForeignKey(CulinaryUse, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('herb', 'culinary_use')

class Recipe(models.Model):
    title = models.CharField(max_length=255, unique=True)
    text = models.TextField()  # Recipe description or instructions
    herbs = models.ManyToManyField(Herb, related_name='recipes')  # Many-to-many with herbs

    def __str__(self):
        return self.title