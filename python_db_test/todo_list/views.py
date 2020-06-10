from django.shortcuts import render
from .forms import TestForm
from django.shortcuts import render
from django.http import HttpResponse
from .models import User  # 追加する
def home(request):
    form = {
        'name':'Wood Village',
        'form':TestForm(),
        'insert_forms':'初期値',
        'messages': User.objects.all(),
    }
    #カッコの記述違いに注意
    if(request.method == 'POST'):
        form['insert_forms'] = '文字列:' + request.POST['text'] + '<br>整数型:' + request.POST['num']
        form['form'] = TestForm(request.POST)
    

    return render(request, 'home.html',form)
