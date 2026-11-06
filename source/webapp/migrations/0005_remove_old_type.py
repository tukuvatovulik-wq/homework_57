from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [("webapp", "0004_transfer_types")]
    operations = [
        migrations.RemoveField(
            model_name="task",
            name="types_old",
        ),
    ]
