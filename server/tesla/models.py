from django.db import models

class SparePart(models.Model):
    image1 = models.ImageField(upload_to='images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='images/', blank=True, null=True)
    title = models.CharField(max_length=255)
    articul = models.CharField(max_length=255, unique=True)
    model = models.CharField(max_length=255)
    marka = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    pokolenie = models.CharField(max_length=255)
    primechanie = models.TextField(blank=True, null=True)
    nomer_zapchasti = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.title} ({self.articul})"
