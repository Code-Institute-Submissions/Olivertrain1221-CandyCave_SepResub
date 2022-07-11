from django.db import models


class Category(models.Model):
    """
    To physically see the fixture types see fixtures Ollie!
    Meta class to overwrite django auto 'Categorys'
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=250)
    friendly_name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Sweet(models.Model):
    """
    Model for the Sweets on the site added with fixtures
    """
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=250, null=True, blank=True)
    name = models.CharField(max_length=250)
    detail = models.TextField()
    measurement_of_sweet = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=1, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def info(self):
        return self.detail

    def __str__(self):
        return self.name
