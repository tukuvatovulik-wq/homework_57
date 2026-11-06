from django.db import migrations


def transfer_types(apps, schema_editor):
    Task = apps.get_model("webapp", "Task")
    for task in Task.objects.all():
        task.types.add(task.types_old_id)


def reverse_transfer_types(apps, schema_editor):
    # The original ForeignKey remains available until the final migration.
    # No reverse copy is needed when this data migration is rolled back.


class Migration(migrations.Migration):
    dependencies = [("webapp", "0003_add_many_to_many_types")]
    operations = [
        migrations.RunPython(transfer_types, reverse_transfer_types),
    ]
