from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *
from thenation.models import Contacts

from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import OtherPageForm,CommonMsterForm,ImagesForm
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
import re
# Create your views here.

def index(request):
   if request.user.is_authenticated:
        
    data=Contacts.objects.all()

    return render(request,"accounts/contact.html",{"data":data})
   else:
        return render(request,"accounts/login.html",{'name':'shubham'})

def signup(request):
    if request.method=="POST":
        #user singnup
        if request.POST['pass1'] == request.POST['pass2']:
            try:
                User.objects.get(username=request.POST['username'])
                return render(request,"accounts/signup.html",{'error':'user alrady taken'})
            except Exception:
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['pass1'],first_name=request.POST['firstname'],last_name=request.POST['lastname'],email=request.POST['email'])
                #auth.login(request,user)
                user.save()
            
                return render (request,'accounts/login.html')

                
        else:
            return render(request,"accounts/signup.html",{'error':'password not match'})
    else:
        return render(request,"accounts/signup.html")






def login(request):
    if request.method=="POST":
        user=auth.authenticate(username=request.POST['username'],password=request.POST['pass'])
        if user is not None:
            auth.login(request,user)
            #return render(request,'accounts/dashboard.html')
            return redirect('/accounts/')
        else:
            return render(request,'accounts/login.html',{'error':'username and password was incorrect'})




    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
    return render(request,'accounts/login.html')




def addslide(request):
    if request.method=="POST" and request.FILES['image']:
        
        desc=request.POST.get('desc')
        image=request.FILES['image']
              
        form=SliderImage(desc=desc,images=image)
        form.save()
    return render(request,"accounts/addslide.html")
@login_required
# def articals(request):
#     form=BlogSpotsForm(request.POST or None, request.FILES or  None)
#     if form.is_valid():
#         obj=form.save(commit=False)
#         obj.save()
#         return redirect("/accounts/#dashboard")
#     return render(request,"accounts/addcmspage.html",{'form':form})

# def artical(request):
#     artical=BlogSpots.objects.filter(name=request.user)


#         # return redirect("/accounts/#dashboard")
#     return render(request,"accounts/otherpages.html",{'artical':artical})
 
 


# def edit(request,myid):
    
#     obj=BlogSpots.objects.get(id=myid)
#     form=BlogSpotsForm(request.POST or None,request.FILES or None,instance=obj)
#     if form.is_valid():
#         obj=form.save(commit=False)
#         obj.save()
#         return redirect("/accounts/#dashboard")

#     return render(request,"accounts/editpost.html",{'form':form,'obj':obj})
   
# def delete(request,myid):
#     obj=BlogSpots.objects.get(id=myid)
#     obj.delete()
#     return redirect("/accounts/#dashboard")

#     return render(request,"/accounts/#dashboard",{'obj':obj})   

# def post(request,myurl):
#     title=myurl.replace('-',' ')
#     blog=BlogSpots.objects.filter(title=title)
    

#     return render(request,"thenation/post.html",{"blogs":blog[0]})
@login_required
def otherpages(request):
    data=OtherPages.objects.all()
    

    return render(request,"accounts/otherpages.html",{"data":data})
def addotherpages(request):
    if request.method == 'POST' and request.FILES['featureimages']:
        form=OtherPageForm(request.POST or None, request.FILES or  None)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.save()
            messages.success(request, "You successfully Add Page")

        return redirect("/accounts/otherpages")
    return render(request,"accounts/addotherpages.html")


def editotherpages(request,myid=None):
    data=OtherPages.objects.filter(id=myid)
    if request.method == 'POST':
        obj=OtherPages.objects.get(id=myid)
        form=OtherPageForm(request.POST or None,request.FILES or None,instance=obj)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.save()
            messages.success(request, "You successfully Update Page")

        return redirect("/accounts/otherpages")


    return render(request,"accounts/editotherpages.html",{"data":data})


   
def deleteotherpages(request,myid):
    obj=OtherPages.objects.get(id=myid)
    obj.delete()
    messages.success(request, "Page Was Deleted")

    return redirect("/accounts/otherpages")

def images(request):
    data=Images.objects.all()
    

    return render(request,"accounts/images.html",{"data":data})
def addimages(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        imageurl=request.FILES.get('imageurl')
        form=Images(title=title,imageurl=imageurl)
        form.save()
        messages.success(request, "You successfully Add Image")
        return redirect("/accounts/images")
    return render(request,"accounts/addimages.html")

def editimages(request,myid=None):
    data=Images.objects.filter(id=myid)
    if request.method == 'POST':
        obj=Images.objects.get(id=myid)
        form=ImagesForm(request.POST or None,request.FILES or None,instance=obj)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.save()
            messages.success(request, "You successfully Update Images")

        return redirect("/accounts/images")


    return render(request,"accounts/editimages.html",{"data":data})


   
def deleteimages(request,myid):
    obj=Images.objects.get(id=myid)
    obj.delete()
    messages.success(request, "Page Was Deleted")

    return redirect("/accounts/images")
 
def videos(request):
    data=CommonMsters.objects.all()
    

    return render(request,"accounts/videos.html",{"data":data})

def contact(request):
    data=Contacts.objects.all()

    return render(request,"accounts/contact.html",{"data":data})    

def addvideos(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        imageurl=request.POST.get('imageurl')
        match = re.search(r'^(http|https)\:\/\/www\.youtube\.com\/watch\?v\=(\w*)(\&(.*))?$', imageurl)
        if match:
            embed_url = 'http://www.youtube.com/embed/%s' %(match.group(2))
            # res = "<iframe width=\"560\" height=\"315\" src=\"%s\" frameborder=\"0\" allowfullscreen></iframe>" %(embed_url)
            imageurl=embed_url
        form=CommonMsters(title=title,imageurl=imageurl)
        form.save()
        messages.success(request, "You successfully Add Video")

        return redirect("/accounts/videos")
    return render(request,"accounts/addvideos.html")

def editvideos(request,myid=None):
    data=CommonMsters.objects.filter(id=myid)
    obj= get_object_or_404(CommonMsters, id=myid)
    # return HttpResponse(obj)

    if request.method == 'POST':
        form = CommonMsterForm(request.POST or None, instance= obj)
        if form.is_valid():
                obj= form.save(commit= False)

                obj.save()
                messages.success(request, "You successfully updated the post")
        return redirect("/accounts/videos")


    return render(request,"accounts/editvideos.html",{"data":data})

def deletevideos(request,myid):
    obj=CommonMsters.objects.get(id=myid)
    obj.delete()
    messages.success(request, "You successfully Deleted Video")

    return redirect("/accounts/videos")

# def settings(request):
#     data=CommonMsters.objects.all()
#     return HttpResponse(data)
    # form=SettingsForm(request.POST or None)
    # if request.method == 'POST':
    #     obj=SettingsForm.objects.get(1)
    #     form=SettingsForm(request.POST or None,instance=obj)
    #     if form.is_valid():
    #         obj=form.save(commit=False)
    #         obj.save()
    #         messages.success(request, "You successfully Update Settings")

    #     return redirect("/accounts/")
    # return render(request,"accounts/settings.html",{'data':data,'form':form})
    

# def addsettings(request):
#     form=SettingsForm(request.POST or None)
#     if request.method == 'POST':
#         form=SettingsForm(request.POST)
#         if form.is_valid():
#             obj=form.save(commit=False)
#             obj.save()
#             messages.success(request, "You successfully Add Page")

#         return redirect("/accounts/settings")
#     return render(request,"accounts/settings.html",{'form':form})




   
   
   

       

