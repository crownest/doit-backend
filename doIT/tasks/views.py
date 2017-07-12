from django.shortcuts import render
from .models import Task, Reminder
from django.utils import timezone
from django.shortcuts import render, get_object_or_404



# def task_list(request):
#     title = request.GET['title']
#     tasks = Task.objects.filter(end_time__gte=timezone.localtime(
#                                 timezone.now())).order_by('date')
#     return HttpResponse("Your task : %s", % title)
#     # return render(request, 'tasks_list.html', {'tasks':tasks})
#
#
# def task_detail(request, pk):
#     task = get_object_or_404(Task, pk=pk)
#     return render(request, 'task_detail.html', {'task': task})
