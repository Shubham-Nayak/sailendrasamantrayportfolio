from django import forms
from .models import OtherPages,CommonMsters,Images,Blog



class OtherPageForm(forms.ModelForm):
    class Meta:
        model=OtherPages
        fields=[
            
            'title',
            'featureimages',
            'description',
         

           
        ]
        widgets={
                  
                   "title":forms.TextInput(attrs={'placeholder':'Title','name':'title','id':'inputname','class':'form-control','type':'text'}),
                   "description":forms.Textarea(attrs={'placeholder':'description','name':'description','id':'exampleFormControlTextarea1','class':'description form-control','type':'text'}),
                   "featureimages":forms.ClearableFileInput(attrs={'name':'featureimages','id':'inputname','class':'form-control','type':'file'}),
                   
                   
                } 


class CommonMsterForm(forms.ModelForm):
    class Meta:
        model=CommonMsters
        fields=[
            
            'title',
            'imageurl',
         

           
        ]
        widgets={
                  
                   "title":forms.TextInput(attrs={'placeholder':'Title','name':'title','id':'inputname','class':'form-control','type':'text'}),
                   "imageurl":forms.TextInput(attrs={'placeholder':'Add Url','name':'imageurl','id':'inputname','class':'form-control','type':'text'}),
                   
                   
                }

class ImagesForm(forms.ModelForm):
    class Meta:
        model=Images
        fields=[
            
            'title',
            'imageurl',
         

           
        ]
        widgets={
                  
                   "title":forms.TextInput(attrs={'placeholder':'Title','name':'title','id':'inputname','class':'form-control','type':'text'}),
                   "imageurl":forms.TextInput(attrs={'placeholder':'Add image','name':'imageurl','id':'inputname','class':'form-control','type':'file'}),
                   
                   
                }


class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=[
            
            'title',
            'description',
            'createdon'
         

           
        ]
        widgets={
                  
                   "title":forms.TextInput(attrs={'placeholder':'Title','name':'title','id':'inputname','class':'form-control','type':'text'}),
                   "description":forms.TextInput(attrs={'placeholder':'Add Description','name':'description','id':'inputname','class':'form-control','type':'text'}),
                   "createdon":forms.TextInput(attrs={'placeholder':'Date','name':'createdon','id':'inputname','class':'form-control','type':'text'}),

                   
                   
                }