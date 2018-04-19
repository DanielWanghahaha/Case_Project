
from django.shortcuts import render
from django.shortcuts import render_to_response
from django import forms
from django.http import HttpResponse
from app.models import User

# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField()
    filename = forms.FileField()

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            # 获取表单数据
            username = form.cleaned_data['username']
            filename = form.cleaned_data['filename']
            # 获取数据库数据
            user = User()
            user.username = username
            user.filename = filename
            user.save()
            return HttpResponse('file upload ok !')
    else:
        form = UserForm()
    return render_to_response('register.html', {'form': form})