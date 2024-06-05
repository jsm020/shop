from django.db import models

class Sumkalar(models.Model):
    nomi = models.CharField(max_length=255)
    tavsif = models.TextField()
    narxi = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Sumkalar"
        verbose_name_plural = "Sumkalar"
    
    def __str__(self):
        return self.nomi

class Sumkalar_rasmlari(models.Model):
    nomi = models.ForeignKey(Sumkalar, related_name="Sumkalar", on_delete=models.CASCADE)
    rasmi = models.ImageField(upload_to='Sumkalar/')

    class Meta:
        verbose_name = "Sumkalar rasmlari"
        verbose_name_plural = "Sumkalar rasmlari"