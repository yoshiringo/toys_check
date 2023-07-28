from django.db import models

class Toys(models.Model):
    name = models.CharField(max_length=32, verbose_name='おもちゃ名')
    price = models.BigIntegerField(verbose_name='金額', null=True, blank=True)
    date = models.DateField(verbose_name='購入日', blank=True, null=True)
    FREQ = (
        ('ほぼ使わない', 'ほぼ使わない'),
        ('たまに', 'たまに'),
        ('いつも', 'いつも'),
    )
    freq = models.CharField(verbose_name='頻度', max_length=50, choices=FREQ, blank=True)
    image = models.ImageField(upload_to='media_local', blank=True, null=True)
    tags = models.CharField(verbose_name='頻度', blank=True, null=True)
