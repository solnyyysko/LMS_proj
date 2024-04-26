from django.db import models
from tasks.models import Project, Task

class BugReport(models.Model):
    STATUS_CHOICES = [
        ('New', 'Новая'),
        ('In_progress', 'В работе'),
        ('Completed', 'Завершена'),
    ]
    PRIORITY_CHOICES = [
        ('Highest', 'Наивысший'),
        ('High', 'Высокий'),
        ('Moderate', 'Умеренный'),
        ('Low', 'Низкий'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    project = models.ForeignKey(
        Project,
        related_name='bugs',
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        related_name='bugs',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New'
    )
    priority = models.CharField(
        max_length=50,
        choices=PRIORITY_CHOICES
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class FeatureRequest(models.Model):
    STATUS_CHOICES = [
        ('Review', 'Рассмотрение'),
        ('Accepted', 'Принято'),
        ('Rejected', 'Отклонено'),
    ]
    PRIORITY_CHOICES = [
        ('Highest', 'Наивысший'),
        ('High', 'Высокий'),
        ('Moderate', 'Умеренный'),
        ('Low', 'Низкий'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    project = models.ForeignKey(
        Project,
        related_name='features',
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        related_name='features',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='Review'
    )
    priority = models.CharField(
        max_length=50,
        choices=PRIORITY_CHOICES
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title