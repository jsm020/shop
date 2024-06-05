from django.db import models

class AyollarKoylagi(models.Model):
    nomi = models.CharField(max_length=255)
    tavsif = models.TextField()
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
    olchamlari = models.CharField(max_length=50)
    zaxiradagi_soni = models.IntegerField()


    class Meta:
        verbose_name = "Ayollar ko'ylagi"
        verbose_name_plural = "Ayollar ko'ylagi"
    
    def __str__(self):
        return self.nomi

class AyollarKoylagiRasmlari(models.Model):
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

    nomi = models.ForeignKey(AyollarKoylagi, related_name="Ayollar_koylagi", on_delete=models.CASCADE)
    rangi = models.CharField(
        max_length=50,
        choices=KOYLAK_RANGLARI,
        default='oq',
    )
    rasmi = models.ImageField(upload_to='koylaklar/')


    class Meta:
        verbose_name = "Ayollar ko'ylagi rasmlari"
        verbose_name_plural = "Ayollar ko'ylagi rasmlari"
    