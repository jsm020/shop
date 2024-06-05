from django.db import models

class Parfemeriya(models.Model):
    nomi = models.CharField(max_length=255)
    tavsif = models.TextField()
    narxi = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Parfemeriya mahsulotlari"
        verbose_name_plural = "Parfemeriya mahsulotlari"
    
    def __str__(self):
        return self.nomi

class Parfemeriya_rasmlari(models.Model):
    nomi = models.ForeignKey(Parfemeriya, related_name="Parfemeriya", on_delete=models.CASCADE)
    rasmi = models.ImageField(upload_to='parfemeriya/')

    class Meta:
        verbose_name = "Parfemeriya mahsulotlari rasmlari"
        verbose_name_plural = "Parfemeriya mahsulotlari rasmlari"