from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Status",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, unique=True)),
            ],
            options={
                "ordering": ["name"],
                "verbose_name": "статус",
                "verbose_name_plural": "статусы",
            },
        ),
        migrations.CreateModel(
            name="Type",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, unique=True)),
            ],
            options={
                "ordering": ["name"],
                "verbose_name": "тип задачи",
                "verbose_name_plural": "типы задач",
            },
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("summary", models.CharField(max_length=255, verbose_name="Краткое описание")),
                ("description", models.TextField(blank=True, verbose_name="Полное описание")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Время создания")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Время обновления")),
                ("status", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="tasks", to="webapp.status", verbose_name="Статус")),
                ("type", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="tasks", to="webapp.type", verbose_name="Тип")),
            ],
            options={
                "ordering": ["-created_at"],
                "verbose_name": "задача",
                "verbose_name_plural": "задачи",
            },
        ),
    ]
