from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord,User
from . import forms
from first_app.forms import NewUserForm,UserProfileInfoForm,UserForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')

    print(webpages_list)

    date_dict  = {'access_records':webpages_list}

    print(webpages_list)

    return render(request,'first_app/index.html',context=date_dict)
# Create your views here.
def welcome(request):
    return render(request,'first_app/welcome.html')

def users(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FORM INVALID")

    return render(request,"first_app/form_page.html",{"form":form})

def form_name_view(request):
    form = forms.FormName()

    print(request.method)

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("validation success")
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("Text: "+form.cleaned_data['text'])


    return render(request,'first_app/form_page.html',{'form':form})

def other(request):

    context_dict ={'text':'Manoj Pravin','age':26 }
    return render(request,'first_app/other.html',context_dict)

def relative(request):
    return render(request,'first_app/relative_url_template.html')

def register(request):

    registered = False

    if request.method == 'POST':
        user_form  = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)


        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile =  profile_form.save(commit=False)
            profile.user = user


            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()


            registered = True
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'first_app/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

@login_required
def special(request):
    return HttpResponseRedirect("Your are logged in, Nice")

@login_required
def user_logout(request):

    logout(request)
    return render(request,'first_app/index.html')

def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username)
        print(password)

        user = authenticate(username=username,password=password)
        print(user)
        
        if user:
            if user.is_active:
                login(request,user)
                return render(request,'first_app/index.html')

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print("Someone tried to login and failed")
            print("Username: {} and password ()".format(username,password))
            return HttpResponse("invalid login details supplied")

    else:
        return render(request,'first_app/login.html')

