from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [("webapp", "0001_initial")]
    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="type",
            new_name="types_old",
        ),
        migrations.AlterField(
            model_name="task",
            name="types_old",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="tasks_old",
                to="webapp.type",
                verbose_name="Тип",
            ),
        ),
    ]
