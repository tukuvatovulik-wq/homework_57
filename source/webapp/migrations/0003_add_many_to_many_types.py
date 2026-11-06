from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("webapp", "0002_rename_type_to_types_old")]
    operations = [
        migrations.AddField(
            model_name="task",
            name="types",
            field=models.ManyToManyField(
                blank=True,
                related_name="tasks",
                to="webapp.type",
                verbose_name="Типы",
            ),
        ),
    ]
