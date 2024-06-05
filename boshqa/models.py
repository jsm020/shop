from django.db import models

class boshqa_mahuslot(models.Model):
    nomi = models.CharField(max_length=255)
    tavsif = models.TextField()
    narxi = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Boshqa"
        verbose_name_plural = "Boshqa"
    
    def __str__(self):
        return self.nomi

class boshqa_mahuslot_rasmlari(models.Model):
    nomi = models.ForeignKey(boshqa_mahuslot, related_name="Boshqa", on_delete=models.CASCADE)
    rasmi = models.ImageField(upload_to='Boshqa/')

    class Meta:
        verbose_name = "Boshqa rasmlari"
        verbose_name_plural = "Boshqa rasmlari"