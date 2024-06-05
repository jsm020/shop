from django.db import models

class OyoqKiyimlar(models.Model):
    nomi = models.CharField(max_length=255)
    tavsif = models.TextField()
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
    olchamlari = models.CharField(max_length=50)
    zaxiradagi_soni = models.IntegerField()

    class Meta:
        verbose_name = "Ayollar oyoq kiyimlari"
        verbose_name_plural = "Ayollar oyoq kiyimlari"
    
    def __str__(self):
        return self.nomi

class OyoqKiyimRasmlari(models.Model):
    KOYLAK_RANGLARI = [
    ('qizil', 'Qizil'),
    ('ko`k', 'Ko`k'),
    ('yashil', 'Yashil'),
    ('oq', 'Oq'),
    ('qora', 'Qora'),
    ('sariq', 'Sariq'),
    ('to`q sariq', 'To`q sariq'),
    ('moviy', 'Moviy'),
    ('binafsha', 'Binafsha'),
    ('kulrang', 'Kulrang'),
    ('jigar rang', 'Jigar rang'),
    ('tilla rang', 'Tilla rang'),
    # Va hokazo...
]

    nomi = models.ForeignKey(OyoqKiyimlar, related_name="Oyoq_Kiyimlar", on_delete=models.CASCADE)
    rangi = models.CharField(
        max_length=50,
        choices=KOYLAK_RANGLARI,
        default='oq',
    )
    rasmi = models.ImageField(upload_to='oyoqkiyimlar/')

    class Meta:
        verbose_name = "Ayollar oyoq kiyimlari rasmlari"
        verbose_name_plural = "Ayollar oyoq kiyimlari rasmlari"