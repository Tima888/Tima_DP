from django.db import models
from services.models import Service

class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'Нове'),
        ('processing', 'В обробці'),
        ('completed', 'Завершено'),
        ('rejected', 'Відхилено'),
    ]

    name = models.CharField("Ваше ім’я", max_length=100)
    email = models.CharField("Email/Телефон/Telegram", max_length=20, blank=True)
    description = models.TextField("Опис проблеми")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Сервіс")
    created_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new',
        verbose_name="Статус"
    )

    def __str__(self):
        return f"Заявка від {self.name} ({self.service.name}) — {self.get_status_display()}"
