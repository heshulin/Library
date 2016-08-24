from django.conf import settings
from Library_management.models import User,Book,Record,Subscribe,BookCategory,BlackList
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import response
from Library_management.controllers.login_service import login_service
from Library_management.controllers.tushu_service import tushu
from Library_management.controllers.admin_login_service import admin_login_service
from Library_management.controllers.json_tool import dict_to_json
from django.http import HttpResponse
import datetime

# Create your views here.
from django.template import Context
from django.template.loader import get_template


def login(request):
    return render_to_response('login.html')

def doLogin(request):
    array = login_service(request)
    if array['state'] == 1:
        if array['msg'] == '管理员登陆':
            return HttpResponse(dict_to_json(array))
        else:
            return HttpResponse(dict_to_json(array))
    else:
        return HttpResponse(dict_to_json(array))

def user(request):

    data = tushu()
    array = {
        'UserNumber':request.session['UserNumber'],
        'data': tushu(),
    }

    return render_to_response('index.html', array)

def find(request):
    array ={
        "UserNumber":request.session['UserNumber'],
    }
    return render_to_response('find.html',array)

def dofind(request):
    BookName = request.GET.get('BookName')

    q = Book.objects.filter(BookName=BookName)

    array = {
        "UserNumber":request.session['UserNumber'],
        'Book':q
    }
    return render_to_response('dofind.html', array)

def mybook(request):
    u = User.objects.filter(UserNumber=request.session['UserNumber']).first()
    b = Record.objects.filter(UserId=u.id).all()
    list = []
    for i in b:
        oneb = Book.objects.filter(id=i.BookId).first()
        list.append(oneb)
    array = {
        "UserNumber":request.session['UserNumber'],
        'data':list
    }
    return render_to_response('mybook.html', array)



def book(request):
    id = request.GET.get('id')
    id = int(id)
    b = Book.objects.filter(id=id)
    array = {
        'i':b[0],
    }
    return render_to_response('book.html', array)


def lend(request):
    id = request.GET.get('id')
    b = Book.objects.filter(id=id).first()

    u = User.objects.filter(UserNumber=request.session['UserNumber']).first()
    print(u.id)
    qqq= int(u.id)
    re = Record.objects.filter(UserId=qqq).all()
    if len(re) == 0:
        array = {
            "msg": "预约失败",
        }
        return render_to_response('yuyue.html', array)
    for i in re:
        if(i.BookId==qqq):
            if(i.State==0):
                array = {
                    "msg": "借书失败",
                }
                return render_to_response('jieshu.html', array)
    b.BookNum = b.BookNum - 1
    b.save()
    r = Record()
    r.UserId = u.id
    r.BookId = id
    r.State = 0
    aDay = datetime.timedelta(days=30)
    r.ReturnTime = datetime.datetime.today()+aDay
    r.save()
    array = {
        "msg":"借书成功"
    }
    return render_to_response('jieshu.html', array)



def yuyue(request):
    id = request.GET.get('id')
    b = Book.objects.filter(id=id).first()

    u = User.objects.filter(UserNumber=request.session['UserNumber']).first()
    print(u.id)
    qqq = int(u.id)
    re = Subscribe.objects.filter(UserId=qqq).all()
    for i in re:
        if (i.BookId == qqq):
            if (i.State == 0):
                array = {
                    "msg": "预约失败",
                }
                return render_to_response('yuyue.html', array)
    r = Subscribe()
    r.UserId = u.id
    r.BookId = id
    r.State = 0
    r.save()
    array = {
        "msg": "预约成功"
    }
    return render_to_response('yuyue.html', array)


def loginadmin(request):
    return render_to_response('loginadmin.html')

def dologinadmin(request):
    array = admin_login_service(request)
    if array['state'] == 1:
        if array['msg'] == '管理员登陆':
            return HttpResponse(dict_to_json(array))
    else:
        return HttpResponse(dict_to_json(array))


def adminview(request):

    data = tushu()
    array = {
        'UserNumber':request.session['UserNumber'],
        'data': tushu(),
    }

    return render_to_response('adminview.html', array)


def huanshu(request):
    array = {
        "UserNumber": request.session['UserNumber'],
    }
    return render_to_response('huanshu.html',array)

def dohuanshu(request):
    UserNumber = request.GET.get('UserNumber')
    BookName = request.GET.get('BookName')
    b = Book.objects.filter(BookName=BookName).first()
    u = User.objects.filter(UserNumber=UserNumber).first()
    r = Record.objects.filter(UserId=u.id,BookId=b.id)
    if len(r)==0:
        array = {
            'msg':"没有借过此书"
        }
    else:
        b.BookNum = b.BookNum+1
        r[0].State = 1
        if r[0].ReturnTime>datetime.datetime.today():
            array = {
                'msg': "还书过晚"
            }
        else:
            array = {
                'msg': "还书成功"
            }
    return render_to_response('yuyue.html',array)

def shuji(request):
    array = {
        "UserNumber": request.session['UserNumber'],
    }
    return render_to_response('shuji.html',array)
def leibie(request):
    array = {
        "UserNumber": request.session['UserNumber'],
    }
    return render_to_response('leibie.html',array)


def doshuji(request):
    b = Book()
    b.Author = request.GET.get('Author')
    b.BookCategorytag = request.GET.get('BookCategorytag')
    b.BookName = request.GET.get('BookName')
    b.BookNum = request.GET.get('BookNum')
    b.Press = request.GET.get('Press')
    b.publicationdate =  request.GET.get('publicationdate')
    b.ISBN = request.GET.get('ISBN')
    b.Edition = request.GET.get('Edition')
    b.Price = request.GET.get('Price')
    b.save()
    array = {
        'msg': "添加成功"
    }

    return render_to_response('yuyue.html',array)

def doleibie(request):
    c = BookCategory()
    c.Tag = request.GET.get('Tag')
    c.Category = request.GET.get('Category')
    c.save()
    array = {
        'msg': "添加成功"
    }


    return render_to_response('yuyue.html',array)

def doyonghu(request):
    u = User()
    u.UserNumber = request.GET.get('UserNumber')
    u.PassWord = request.GET.get('PassWord')
    u.TrueName =request.GET.get('TrueName')
    u.IsManager = request.GET.get('IsManager')
    u.Professional = request.GET.get('Professional')
    u.Grade = request.GET.get('Grade')
    u.MaxNum =request.GET.get('MaxNum')
    u.UserCategory = request.GET.get('UserCategory')
    u.save()
    array = {
        'msg': "添加成功"
    }


    return render_to_response('yuyue.html',array)

def yonghu(request):
    array = {
        "UserNumber": request.session['UserNumber'],
    }
    return render_to_response('yonghu.html',array)

def heimingdan(request):
    array = {
        "UserNumber": request.session['UserNumber'],
    }
    return render_to_response('heimingdan.html',array)

def doheimingdan(request):
    b = BlackList()
    UserNumber = request.GET.get('UserNumber')
    u = User.objects.filter(UserNumber=UserNumber).first()
    b.UserId = u.id
    b.BlackNum = 1
    b.save()
    array = {
        'msg': "添加成功"
    }
    return render_to_response('yuyue.html',array)
