from django.db import models

class Taqinchoqlar(models.Model):
    nomi = models.CharField(max_length=255)
    tavsif = models.TextField()
    narxi = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Taqinchoqlar"
        verbose_name_plural = "Taqinchoqlar"
    
    def __str__(self):
        return self.nomi

class Taqinchoqlar_rasmlari(models.Model):
    nomi = models.ForeignKey(Taqinchoqlar, related_name="Taqinchoqlar", on_delete=models.CASCADE)
    rasmi = models.ImageField(upload_to='Taqinchoqlar/')

    class Meta:
        verbose_name = "Taqinchoqlar rasmlari"
        verbose_name_plural = "Taqinchoqlar rasmlari"