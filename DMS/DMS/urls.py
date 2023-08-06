"""
URL configuration for DMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from deviceMS.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('home/', home, name='home'),
    path('emp_login', emp_login, name='emp_login'),
    path('admin_login', admin_login, name='admin_login'),
    path('logout/', Logout, name='logout'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('addDevice/', addDevice, name='addDevice'),
    path('viewDevice/', viewDevice, name='viewDevice'),
    path('viewDeviceUser/', viewDeviceUser, name='viewDeviceUser'),
    path('viewDesktopUser/', viewDesktopUser, name='viewDesktopUser'),
    path('viewPrinterUser/', viewPrinterUser, name='viewPrinterUser'),
    path('viewUPSUser/', viewUPSUser, name='viewUPSUser'),
    path('viewMFDUser/', viewMFDUser, name='viewMFDUser'),
    path('editDesktop/<int:pid>', editDesktop, name='editDesktop'),
    path('editPrinter/<int:pid>', editPrinter, name='editPrinter'),
    path('editUPS/<int:pid>', editUPS, name='editUPS'),
    path('editMFD/<int:pid>', editMFD, name='editMFD'),
    path('updateDesktop/<int:pid>', updateDesktop, name='updateDesktop'),
    path('updatePrinter/<int:pid>', updatePrinter, name='updatePrinter'),
    path('updateUPS/<int:pid>', updateUPS, name='updateUPS'),
    path('updateMFD/<int:pid>', updateMFD, name='updateMFD'),
    path('deleteDesktop/<int:pid>', deleteDesktop, name='deleteDesktop'),
    path('deletePrinter/<int:pid>', deletePrinter, name='deletePrinter'),
    path('deleteUPS/<int:pid>', deleteUPS, name='deleteUPS'),
    path('deleteMFD/<int:pid>', deleteMFD, name='deleteMFD'),
    path('viewDesktop/', viewDesktop, name='viewDesktop'),
    path('viewPrinter/', viewPrinter, name='viewPrinter'),
    path('viewUPS/', viewUPS, name='viewUPS'),
    path('viewMFD/', viewMFD, name='viewMFD'),
    path('searchDevice/', searchDevice, name='searchDevice'),
    path('searchDeviceUser/', searchDeviceUser, name='searchDeviceUser'),

]
