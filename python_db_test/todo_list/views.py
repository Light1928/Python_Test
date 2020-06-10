from django.shortcuts import render
from .forms import TestForm

def home(request):
    form = {
        'name':'Wood Village',
        'form':TestForm(),
        'insert_forms':'初期値',
    }
    #カッコの記述違いに注意
    if(request.method == 'POST'):
        form['insert_forms'] = '文字列:' + request.POST['text'] + '<br>整数型:' + request.POST['num']
        form['form'] = TestForm(request.POST)

    return render(request, 'home.html',form)
