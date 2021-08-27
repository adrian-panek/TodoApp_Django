from django.shortcuts import reverse
from django.views import generic

from .models import Task
from .forms import TaskModelForm

class HomePageView(generic.CreateView, generic.ListView):
    template_name = "main.html"
    queryset = Task.objects.all()
    form_class = TaskModelForm
    context_object_name = "tasks"

    def get_queryset(self):
       query = self.request.GET.get('search')
       if query:
          postresult = Task.objects.filter(description__contains=query)
          result = postresult
       else:
           result = None
       result = super(HomePageView, self).get_queryset()
       return result

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

