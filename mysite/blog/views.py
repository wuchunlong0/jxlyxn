from django.shortcuts import render
from django.contrib.auth import login as auth_login #当函数名是login，必须用auth_login
from django.contrib.auth import authenticate #django验证登录
from django.http.response import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Contacts
from myAPI.pageAPI import djangoPage


PAGE_NUM = 25

# AdminLTE-2.4.5 模板
def index0(request):
    return  render(request, 'blog/index0.html', context=locals())

def index(request):
    return  render(request, 'blog/index.html', context=locals())

def login(request):
    if request.method != 'POST':
        return  render(request, 'blog/login.html', context=locals()) 
    username = request.POST['username']
    password = request.POST['password']
    href = request.POST['href']
    if href == '':  href = '/' #href空，转index
    user = authenticate(username=username, password=password) #django验证登录
    if user: 
        auth_login(request, user)
        return  HttpResponseRedirect(href)
    messages.info(request, u'登录失败！请输入一个正确的 用户名 和密码. 注意他们都是区分大小写的！')
    return  render(request, 'blog/login.html', context=locals())

def register(request):
    if request.method != 'POST':
        return  render(request, 'blog/register.html', context=locals())      
    name = request.POST['username']
    isname = User.objects.filter(username = name)
    if isname:  #判断name是否有相同的记录
        messages.info(request, name + '用户已经注册！')
        return HttpResponseRedirect('#')   
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(name, email, password) #用户,不能从Django自带登录界面，登录
    user.is_staff = False #非职员 默认False
    user.is_superuser = False #非超级用户 默认False
    user.save()
    auth_login(request, user)
    return  HttpResponseRedirect('/')  

def company(request):
    return  render(request, 'blog/company.html', context=locals())  

def device(request):
    return  render(request, 'blog/device.html', context=locals())  

def testing(request):
    return  render(request, 'blog/testing.html', context=locals())  

def contactus(request):
    if request.method != 'POST':
        return  render(request, 'blog/contactus.html', context=locals())  
    
    meg = '提交成功，我们将在24小时内联系您 ^o^'
    cleanData = request.POST.dict() 
    del cleanData['csrfmiddlewaretoken']       
    iscontact = Contacts.objects.filter(content = cleanData.get('content',''))
    if iscontact:
        meg = '已经提交过了，不要重复提交！我们将在24小时内联系您 ^o^'
    else:            
        c = Contacts(**cleanData)
        c.save()            
    return  render(request, 'blog/contactus.html', context=locals())  
    return HttpResponseRedirect('/')  

def contact_list(request, page):
    contacts = Contacts.objects.all()
    contacts_list, pageList, num_pages, page = djangoPage(contacts,page,PAGE_NUM)  #调用分页函数
    offset = PAGE_NUM * (page - 1) 
    return render(request, 'blog/contact_list.html', context=locals())

def contact_edit(request):
    id = int(request.GET.get('id','0'))
    obj = Contacts.objects.filter(id=id)
    if not obj:
        return HttpResponse('用户不存在')
    Contacts.objects.filter(id=id).update(status='1')  
    return HttpResponseRedirect('/blog/contact/list/1')  
    
def customer(request):
    return render(request, 'blog/customer.html', context=locals())

def product_profile(request):
    return render(request, 'blog/product_profile.html', context=locals()) 

def product(request):
    return render(request, 'blog/product.html', context=locals()) 

def Journalism(request):
    return render(request, 'blog/Journalism.html', context=locals())    