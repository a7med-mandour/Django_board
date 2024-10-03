from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login , logout ,authenticate, views 
from .forms import SignForm
from django.views.generic import UpdateView
from django.contrib.auth.models import User
# Create your views here.



def signup(request):
    # form = UserCreationForm()
    if request.method == "POST":
        form = SignForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "you are sign up ")
            return redirect('home')
    else:
        # Initialize form for GET request (or if POST fails)
        form = SignForm()
    return render(request,'signup.html',{'form':form})


def user_logout(request):
    logout(request)
    messages.success(request, "you are logged out ")
    return redirect('home')

def user_login(request):
    if request.method == "POST" :
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
        # messages.success(request, "you are not logged in ")

    return render(request, "login.html",{"form":form})



class EditAccount(UpdateView):

    model = User
    fields = ['username','first_name','last_name']
    pk_url_kwarg = 'account_id'
    template_name = 'edit_account.html'
    context_object_name ='account'

    def get_object(self):
        return self.request.user

