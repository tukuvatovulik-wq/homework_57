from django.db import migrations


def transfer_types(apps, schema_editor):
    Task = apps.get_model("webapp", "Task")
    for task in Task.objects.all():
        task.types.add(task.types_old_id)


def reverse_transfer_types(apps, schema_editor):
    Task = apps.get_model("webapp", "Task")
    for task in Task.objects.all():
        task.types_old_id = task.types.first().pk if task.types.exists() else None
        task.save(update_fields=["types_old"])


class Migration(migrations.Migration):
    dependencies = [("webapp", "0003_add_many_to_many_types")]
    operations = [
        migrations.RunPython(transfer_types, reverse_transfer_types),
    ]
