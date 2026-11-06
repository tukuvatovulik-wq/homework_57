from django import forms

from .models import Status, Task, Type


class TaskForm(forms.ModelForm):
    types = forms.ModelMultipleChoiceField(
        queryset=Type.objects.all(),
        required=False,
        label="Типы задачи",
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = ("summary", "description", "status", "types")
        widgets = {
            "description": forms.Textarea(attrs={"rows": 5}),
        }
        labels = {
            "summary": "Краткое описание",
            "description": "Полное описание",
            "status": "Статус",
        }

    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        label="Статус",
    )
