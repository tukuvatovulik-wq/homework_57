from django.db import migrations


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
            field=__import__("django").db.models.ForeignKey(
                on_delete=__import__("django").db.models.deletion.PROTECT,
                related_name="tasks_old",
                to="webapp.type",
                verbose_name="Тип",
            ),
        ),
    ]
