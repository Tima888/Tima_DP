from django.db import models

class Producer(models.Model):
    name = models.CharField('Виробник', max_length=100)
    image = models.ImageField('Логотип виробника', upload_to='producers/', blank=True, null=True)

    def __str__(self):
        return self.name


class EquipmentType(models.Model):
    name = models.CharField('Тип техніки', max_length=100)
    producers = models.ManyToManyField(Producer, verbose_name='Виробники')
    image = models.ImageField('Зображення типу техніки', upload_to='equipment_types/', blank=True, null=True)

    def __str__(self):
        return self.name


class Favors(models.Model):
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE, verbose_name='Тип техніки')
    title_f = models.CharField('Назва послуги', max_length=100)
    description_f = models.CharField('Опис послуги', max_length=250)
    price = models.CharField('Ціна', max_length=100)
    duration = models.CharField('Орієнтовний час виконання', max_length=100)
    image = models.ImageField('Фото послуги', upload_to='favors/', blank=True, null=True)

    def __str__(self):
        return f"{self.title_f} для {self.equipment_type}"
