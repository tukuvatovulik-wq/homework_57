from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "статус"
        verbose_name_plural = "статусы"

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "тип задачи"
        verbose_name_plural = "типы задач"

    def __str__(self):
        return self.name


class Task(models.Model):
    summary = models.CharField(max_length=255, verbose_name="Краткое описание")
    description = models.TextField(blank=True, verbose_name="Полное описание")
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name="tasks",
        verbose_name="Статус",
    )
    types = models.ManyToManyField(
        Type,
        blank=True,
        related_name="tasks",
        verbose_name="Типы",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время обновления")

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "задача"
        verbose_name_plural = "задачи"

    def __str__(self):
        return self.summary
