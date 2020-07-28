from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,response
from django.conf import settings
from .models import Contacts
from accounts.models import *
from django.core.files.storage import FileSystemStorage #new
from math import ceil
from django.utils import timezone 
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
import datetime
import re
import json

# Create your views here.

def index(request):
    name_list=OtherPages.objects.all()
    # return HttpResponse(name_list)

    video=CommonMsters.objects.all()
    data=CommonMsters.objects.all()
    currenttime = datetime.datetime.now().strftime('%H:%M:%S')

    #pagination
    paginator=Paginator(name_list,8)
    page = request.GET.get('page')
    try:
        name = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        name = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        name= paginator.page(paginator.num_pages)

    
    # for i in video:
    #     match = re.search(r'^(http|https)\:\/\/www\.youtube\.com\/watch\?v\=(\w*)(\&(.*))?$', i.imageurl)
    #     if match:
    #         embed_url = 'http://www.youtube.com/embed/%s' %(match.group(2))
    #         res = "<iframe width=\"560\" height=\"315\" src=\"%s\" frameborder=\"0\" allowfullscreen></iframe>" %(embed_url)
    #         {'video'}

    allprod={'data':name,'video':video}
    return render(request,"thenation/index.html",allprod)


def about(request):
    return render(request,"thenation/about.html")
def profile(request):
    return render(request,"thenation/profile.html")

def videos(request):
    video=CommonMsters.objects.all().order_by('id').reverse()
    return render(request,"thenation/videos.html",{'video':video})



def saveform(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        query=request.POST.get('message')
        
        contact=Contacts(name=name,email=email,subject=subject,query=query)
        contact.save()
        response_data = {}
        response_data['result'] = 'Form post successful!'
        response_data['status'] = True
        response_data['message'] = '<div class="resultdiv alert alert-success">Saved successfully</div> '

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        ) 
        # return render(request,"thenation/inddex.html",{'error':'Thanks For Contacting..'})
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
    


def admin(request):
    return render(request,"thenation/dashbord.html")



'''def addslide(request):
    if request.method=="POST" and request.FILES['image']:
        desc=request.POST.get('desc')
        image=request.FILES['image']
              
        form=SliderImage(desc=desc,images=image)
        form.save()
    return render(request,"thenation/addslide.html")'''

'''def articals(request):
    if request.method == "POST" and request.FILES['image']:
        name=request.POST.get('name')
        title=request.POST.get('title')
        heading1=request.POST.get('heading1')
        content1=request.POST.get('content1')
        heading2=request.POST.get('heading2')
        content2=request.POST.get('content2')
        link=request.POST.get('links')
        time=time=timezone.datetime.now()
        images=request.FILES['image']
        thumbnil=request.FILES['thumbnils']
        form=BlogSpot(name=name,title=title,heading1=heading1,heading2=heading2,
        content1=content1,content2=content2,links=link,time=time,images=images,thumbnils=thumbnil)
        form.save()
    return render(request,"thenation/articals.html")

       

    return render(request,"thenation/articals.html")'''