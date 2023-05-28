from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import SearchForm
import requests
import os
from dotenv import load_dotenv

load_dotenv()


# Create your views here.

def get_api_data(keyword):
    
    #pixabay apiからjsonデータを取得してくる関数

    URL="https://pixabay.com/api/?key={0}&q={1}".format(os.getenv("API_KEY"),keyword)

    # print(URL)
    api=requests.get(URL)
    result=api.json()
    return result["hits"]

class IndexView(View):
    def get(self,request,*args,**kwargs):
        form = SearchForm(request.POST or None)

        fetch_data=get_api_data("")

        return render(request,"app/index.html",{
            "form":form,
            "fetch_data":fetch_data,
        })
    
    def post(self,request,*args,**kwargs):

        form=SearchForm(request.POST or None)

        if form.is_valid():
            
            keyword=form.cleaned_data["title"]
            print(keyword)
            fetch_data=get_api_data(keyword)

        return render(request,"app/index.html",{
            "form":form,
            "fetch_data":fetch_data,
            "keyword":keyword
        })