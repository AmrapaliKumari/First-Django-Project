from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Link
from django.http import HttpResponseRedirect

# Create your views here.
def scrape(request):
    if request.method=="POST": # fetching data from form n searching in the backened.
        site=request.POST.get('site','') #site is formbox name field used to fetch

        page=requests.get(site) # Requests and BeautifulSoup are Python libraries.
        soup=BeautifulSoup(page.text,'html.parser')    #Library Packages.
        link_address=[]

        for link in soup.find_all('a'):
            link_address=link.get('href')
            link_text=link.string
            Link.objects.create(address=link_address,name=link_text)
        return HttpResponseRedirect('/')
    else:
        data=Link.objects.all()    


    return render(request,'myapp/result.html',{'data':data}) 


def clear(request):
    Link.objects.all().delete()
    return render(request,'myapp/result.html')      