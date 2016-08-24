"""Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Library_management.views import login,doLogin,user,find,book,dofind,lend,mybook,yuyue,loginadmin,dologinadmin,adminview,huanshu,shuji,leibie,yonghu,dohuanshu,heimingdan,doshuji,doleibie,doheimingdan

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login', login),
    url(r'^dologin', doLogin),
    url(r'^user', user),
    url(r'^find', find),
    url(r'^book', book),
    url(r'^dofind', dofind),
    url(r'^jieshu', lend),
    url(r'^mybook', mybook),
    url(r'^yuyue', yuyue),
    url(r'^guanli', loginadmin),
    url(r'^doguanli', dologinadmin),
    url(r'^view', adminview),
    url(r'^huanshu', huanshu),
    url(r'^shuji', shuji),
    url(r'^leibie', leibie),
    url(r'^yonghu', yonghu),
    url(r'^dohuanshu', dohuanshu),
    url(r'^heimingdan', heimingdan),
    url(r'^doshuji', doshuji),
    url(r'^doleibie', doleibie),
]
