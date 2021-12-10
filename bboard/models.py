from django.db import models

# Create your models here.
class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT,verbose_name='Рубрика')

    class Meta:
        verbose_name='Обьявление'
        verbose_name_plural='Обьявления'
        ordering=['-published']

class Rubric(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')

    class Meta:
        verbose_name='Рубрика'
        verbose_name_plural='Рубрики'
        ordering=['name']
