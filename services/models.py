from django.db import models

class Service(models.Model):
    name = models.CharField("Назва сервісу", max_length=100)
    address = models.CharField("Адреса", max_length=250)
    work_time = models.CharField("Графік роботи", max_length=100)
    description = models.TextField("Опис", blank=True)
    contact_info = models.CharField("Контактні дані", max_length=250, blank=True)
    image = models.ImageField("Зображення", upload_to='services/', blank=True, null=True)

    def __str__(self):
        return self.name
