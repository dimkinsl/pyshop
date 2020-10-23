# Задание, скорее всего, сделано не корректно.
# Но лучше попробовать и решить неправильно, чем вообще не попробовать...
# P.S. Хотя функция возвращает json и в целом работает правильно.

from django.db import models

class Category(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(u'категория', max_length=30)

class Product(models.Model):
    categories = models.ManyToManyField(Category,
                                        related_name='products',
                                        blank=True, verbose_name=u"категории")
    related_products = models.ManyToManyField('Product',
                                              blank=True,
                                              verbose_name="связанные продукты")

    sku = models.CharField(u'артикул', max_length=128, unique=True)

    price = models.DecimalField(u'цена', max_digits=12, decimal_places=4)

    slug = models.SlugField(u'slug', max_length=80, db_index=True, unique=True)

    name = models.CharField(u'название', max_length=128)
    title = models.CharField(u'заголовок страницы (<title>)', max_length=256, blank=True)
    description = models.TextField(u'описание', blank=True)

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-price']

from shop.models import Product
from django.db.models import Q
from django.http import JsonResponse

def live_search(request, template_name="shop/livesearch_results.html"):
    q = request.GET.get("q", "")
    res = []
    filter_q = Q(name__icontains=q) | Q(sku__icontains=q) | Q(description__icontains=q)
    for p in Product.objects.filter(filter_q):
        res.append([p.sku, p.name, p.description, p.price])
    return JsonResponse(res, safe=False)