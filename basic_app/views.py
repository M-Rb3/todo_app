from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from basic_app.models import TODO
from django.utils import timezone
# Create your views here.
def index(request):
    todo_list = TODO.objects.order_by('-added_date')
    data_dict = {'todo_list':todo_list}
    return render(request,'basic_app/index.html',data_dict)

def add_todo(request):
    if request.method == "POST":
        content = request.POST['text']
        current_date = timezone.now()
        todo_item = TODO(text=content, added_date=current_date)
        todo_item.save()

    return HttpResponseRedirect(reverse('index'))

def delete_todo(request,todo_id):
    if request.method == 'POST':
        TODO.objects.filter(id=todo_id).delete()
    return HttpResponseRedirect(reverse('index'))
