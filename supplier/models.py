from django.db import models
from django.utils import timezone

NULLABLE = {"null": True, "blank": True}


class DateModelMixin(models.Model):
    created_at = models.DateTimeField(verbose_name="Время создания", **NULLABLE)

    def save(self, *args, **kwargs) -> None:
        """
        method to fill created (if no id yet)
        """
        if not self.id:
            self.created = timezone.now()
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True


class Contacts(models.Model):
    email = models.EmailField(verbose_name="email")
    country = models.CharField(max_length=100, verbose_name="страна")
    city = models.CharField(max_length=100, verbose_name="город")
    street = models.CharField(max_length=255, verbose_name="улица")
    building_number = models.SmallIntegerField(verbose_name="номер дома")

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"


    def __str__(self):
        return f"г. {self.city}, {self.street}, {self.building_number}"

class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="название")
    model = models.CharField(max_length=255, verbose_name="модель")
    release_date = models.DateField(verbose_name="дата выхода продукта на рынок")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.title


class Supplier(DateModelMixin):
    class Status(models.IntegerChoices):
        manufacture = 0, "Завод"
        distributor = 1, "Реализатор первого уровня"
        seller = 2, "Реализатор второго уровня"

    title = models.CharField(max_length=255, **NULLABLE, verbose_name="название")
    contacts = models.ForeignKey("Contacts", verbose_name="контакты", on_delete=models.PROTECT)
    product = models.ManyToManyField("Product", verbose_name="продукт")
    supplier = models.SmallIntegerField(choices=Status.choices, default=Status.seller, verbose_name="поставщик")
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="задолженность")

    class Meta:
        verbose_name = "Участник сети"
        verbose_name_plural = "Участники сети"

    def __str__(self):
        return self.title
