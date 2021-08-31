from django.shortcuts import reverse
from django.views import generic

from .models import Task
from .forms import TaskModelForm

class HomePageView(generic.CreateView, generic.ListView):
    template_name = "main.html"
    queryset = Task.objects.all()
    form_class = TaskModelForm
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(description__contains=search_input)
        return context

    def get_success_url(self):
        return reverse("main_todo:homepage")

class AddTaskView(generic.CreateView):
    template_name = "task_add.html"
    queryset = Task.objects.all()
    form_class = TaskModelForm

    def get_success_url(self):
        return reverse("main_todo:homepage")

class UpdateTaskView(generic.UpdateView):
    template_name = "task_update.html"
    queryset = Task.objects.all()
    form_class = TaskModelForm

    def get_success_url(self):
        return reverse("main_todo:homepage")

class DeleteTaskView(generic.DeleteView):
    template_name = "task_delete.html"
    queryset = Task.objects.all()

    def get_success_url(self):
        return reverse("main_todo:homepage")

