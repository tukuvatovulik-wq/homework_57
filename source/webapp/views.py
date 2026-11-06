from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from .forms import TaskForm
from .models import Task


class TaskListView(TemplateView):
    template_name = "webapp/task_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Task.objects.select_related("status").prefetch_related("types")
        return context


class TaskDetailView(TemplateView):
    template_name = "webapp/task_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = get_object_or_404(
            Task.objects.select_related("status").prefetch_related("types"),
            pk=kwargs["pk"],
        )
        return context


class TaskCreateView(TemplateView):
    template_name = "webapp/task_form.html"

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data(form=TaskForm()))

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            messages.success(request, "Задача успешно добавлена.")
            return redirect("task_detail", pk=task.pk)
        return self.render_to_response(self.get_context_data(form=form))


class TaskUpdateView(TemplateView):
    template_name = "webapp/task_form.html"

    def get_task(self):
        return get_object_or_404(Task, pk=self.kwargs["pk"])

    def get(self, request, *args, **kwargs):
        form = TaskForm(instance=self.get_task())
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST, instance=self.get_task())
        if form.is_valid():
            task = form.save()
            messages.success(request, "Изменения сохранены.")
            return redirect("task_detail", pk=task.pk)
        return self.render_to_response(self.get_context_data(form=form))


class TaskDeleteView(View):
    template_name = "webapp/task_confirm_delete.html"

    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs["pk"])
        return TemplateView.as_view(template_name=self.template_name)(
            request, task=task
        )

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs["pk"])
        task.delete()
        messages.success(request, "Задача удалена.")
        return redirect("task_list")
