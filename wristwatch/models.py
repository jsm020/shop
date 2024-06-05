from django.db import models

class Soatlar(models.Model):
    nomi = models.CharField(max_length=255)
    tavsif = models.TextField()
    narxi = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Soatlar"
        verbose_name_plural = "Soatlar"
    
    def __str__(self):
        return self.nomi

class Soatlar_rasmlari(models.Model):
    nomi = models.ForeignKey(Soatlar, related_name="Soatlar", on_delete=models.CASCADE)
    rasmi = models.ImageField(upload_to='Soatlar/')

    class Meta:
        verbose_name = "Soatlar rasmlari"
        verbose_name_plural = "Soatlar rasmlari"