from django.shortcuts import render
from django.shortcuts import redirect
from .models import Todo,DoneTable
from .forms import TodoForm
import datetime


def index(request):
    if (request.method == 'POST'):
        msg = 'Todoを追加しました！'
        form = TodoForm()
        
        do = request.POST['do']
        todo = Todo(do=do)
        todo.save()      
        data = Todo.objects.all()
    
    else:
        msg = ''
        form = TodoForm()     
        data = Todo.objects.all()

    donedata = DoneTable.objects.all().order_by('donetime').reverse()

    params = {
            'title':'Todolist',
            'message':msg,
            'form':form,
            'data':data,
            'donedata':donedata,
            }
    return render(request, 'todo/index.html', params)


#完了リストに移動
def done(request, num):
    do = Todo.objects.get(id=num)
    if (request.method == 'POST'): 
        donetime=datetime.datetime.now()
        donetime=donetime.strftime('%Y-%m-%d %H:%M:%S')
        
        doneupd = DoneTable(done=do, donetime=donetime)
        doneupd.save()

        do.delete()
        return redirect(to='/todo')
    params = {
            'title':'Todolist',
            'id':num,
            'obj':do,
            }
    return render(request, 'todo/done.html', params)

#Todoの削除
def delete(request, num):
    todo = Todo.objects.get(id=num)
    if (request.method == 'POST'):
        todo.delete()
        return redirect(to='/todo')
    params = {
            'title':'Todolist',
            'id':num,
            'obj':todo,
            }
    return render(request, 'todo/delete.html', params)


