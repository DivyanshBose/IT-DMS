from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Desktop, MultifunctionalDevice, Printer, Ups, LogoPic
from django.http import HttpRequest, JsonResponse
from django.db.models import Q


@login_required(login_url='emp_login')
def home(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    desktop_count = Desktop.objects.count()
    printer_count = Printer.objects.count()
    ups_count = Ups.objects.count()
    mfd_count = MultifunctionalDevice.objects.count()
    context = {
        'desktop_count': desktop_count,
        'printer_count': printer_count,
        'ups_count': ups_count,
        'mfd_count': mfd_count, 
    }
    return render(request, 'home.html', context)

def index(request):
    pic = LogoPic.objects.all()
    context = {"img" : pic}
    return render(request, 'index.html', {'context': context})
    # return render(request, 'index.html')

def signup(request):
    error = ""
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            return redirect('emp_login')
        except Exception:
            error = "yes"

    return render(request, 'signup.html', {'error':error})

def emp_login(request):
    if request.user.is_authenticated:
        return redirect('home')  
    error = ""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            error = "no"
        else:
            error = "yes"
            
    return render(request, 'emp_login.html', {'error':error})

def admin_login(request):  
    error = ""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            error = "no"
        else:
            error = "yes"
            
    return render(request, 'admin_login.html', {'error':error})

@login_required(login_url='admin_login')
def addDevice(request):   # sourcery skip: extract-method, last-if-guard
    if not request.user.is_authenticated:
        return redirect('admin_login')

    if request.method=="POST":
        devices = request.POST.get('devices')
        
        if devices == 'Desktop':  
            voucher_number_desktop = request.POST.get('SerialNumberD')
            monitor_brand_name = request.POST.get('MonitorBrandNameD')
            monitor_model_name = request.POST.get('MonitorModelNameD')
            cpu_brand_name = request.POST.get('CpuBrandNameD')
            cpu_model_name = request.POST.get('CpuModelNameD')
            cpu_processor = request.POST.get('CpuProcessorD')
            cpu_ram = request.POST.get('CpuRamD')
            mouse_serial_number = request.POST.get('MouseSerialNumberD')
            keyboard_serial_number = request.POST.get('KeyboardSerialNumberD')
            grant_desktop = request.POST.get('GrantD')
            yop_desktop = request.POST.get('YopD')
            gp_desktop = request.POST.get('GroupD')
            nomenclature_desktop = request.POST.get('NomenclatureD')

            

            data_desktop = Desktop(
                voucher_numberd = voucher_number_desktop,
                monitor_brand_name=monitor_brand_name,
                monitor_model_name=monitor_model_name,
                cpu_brand_name=cpu_brand_name,
                cpu_model_name=cpu_model_name,
                cpu_processor=cpu_processor,
                cpu_ram=cpu_ram,
                keyboard_serial_number=keyboard_serial_number,
                mouse_serial_number=mouse_serial_number,
                grant=grant_desktop,
                year_of_purchase=yop_desktop,
                group=gp_desktop,
                nomenclature=nomenclature_desktop
                )
            data_desktop.save()

        elif devices == 'Printer':

            # Process form data for Printer device
            voucher_number_printer = request.POST.get('SerialNumberP')
            brand_name_printer = request.POST.get('BrandNameP')
            model_name_printer = request.POST.get('ModelNameP')
            grant_printer = request.POST.get('GrantP')
            yop_printer = request.POST.get('YopP')
            printer_type = request.POST.get('TypeP')
            gp_printer = request.POST.get('GroupP')
            nomenclature_printer = request.POST.get('NomenclatureP')

            data_printer = Printer(
                voucher_numberp = voucher_number_printer,
                brand_name=brand_name_printer,
                model_name=model_name_printer,
                grant=grant_printer,
                pyop=yop_printer,
                ptype=printer_type,
                group=gp_printer,
                nomenclature=nomenclature_printer,
            )
            data_printer.save()

        elif devices == 'UPS':

            voucher_number_ups = request.POST.get('SerialNumberU')
            brand_name_ups = request.POST.get('BrandNameU')
            model_name_ups = request.POST.get('ModelNameU')
            grant_ups = request.POST.get('GrantU')
            yop_ups = request.POST.get('YopU')
            ups_power = request.POST.get('PowerU')
            ups_type = request.POST.get('TypeU')
            gp_ups = request.POST.get('GroupU')
            nomenclature_ups = request.POST.get('NomenclatureU')

            data_ups = Ups(
                voucher_numberu = voucher_number_ups,
                brand_name=brand_name_ups,
                model_name=model_name_ups,
                grant=grant_ups,
                uyop=yop_ups,
                ups_power=ups_power,
                ups_type=ups_type,
                group=gp_ups,
                nomenclature=nomenclature_ups,
            )
            data_ups.save()
        
        elif devices == 'Multi Functional Device' :

            vnumber = request.POST.get('SerialNumberM')           
            brandname = request.POST.get('BrandnameM')
            modelname = request.POST.get('ModelnameM')
            grantm = request.POST.get('GrantM')
            yopm = request.POST.get('YopM')  
            gpm = request.POST.get('GroupM')
            nomenclaturem = request.POST.get('NomenclatureM')

            dataX=MultifunctionalDevice(
                voucher_numberm = vnumber,      
                brand_name = brandname,
                model_name = modelname,
                grant = grantm,
                purchaseyear = yopm,
                group = gpm,
                nomenclature = nomenclaturem
                )
            dataX.save()
                
        return redirect('viewDevice')
        
    return render(request, 'addDevice_base.html')

@login_required(login_url='admin_login')
def admin_dashboard(request):
    users = User.objects.all()
    desktop_count = Desktop.objects.count()
    printer_count = Printer.objects.count()
    ups_count = Ups.objects.count()
    mfd_count = MultifunctionalDevice.objects.count()
    all_permissions = Permission.objects.all()

    context = {
        'desktop_count': desktop_count,
        'printer_count': printer_count,
        'ups_count': ups_count,
        'mfd_count': mfd_count, 
        'users' : users,
        'all_permissions': all_permissions,
    }

    return render(request, 'admin_dashboard.html', context)

@login_required(login_url='admin_login')
def viewDevice(request):

    desktop_data = Desktop.objects.all()
    printer_data = Printer.objects.all()
    ups_data = Ups.objects.all()
    multifunctional_data = MultifunctionalDevice.objects.all()

    return render(request, 'viewDevice.html', {
        'desktop': desktop_data,
        'printer': printer_data,
        'ups': ups_data,
        'multifunctionaldevice': multifunctional_data,
    })

@login_required(login_url='emp_login')
def viewDeviceUser(request):

    desktop_data = Desktop.objects.all()
    printer_data = Printer.objects.all()
    ups_data = Ups.objects.all()
    multifunctional_data = MultifunctionalDevice.objects.all()

    return render(request, 'viewDeviceUser.html', {
        'desktop': desktop_data,
        'printer': printer_data,
        'ups': ups_data,
        'multifunctionaldevice': multifunctional_data,
    })

@login_required(login_url='admin_login')
def viewDesktop(request):
    desktop_data = Desktop.objects.all()
    return render(request, 'viewDesktop.html', {'desktop': desktop_data})

@login_required(login_url='emp_login')
def viewDesktopUser(request):
    desktop_data = Desktop.objects.all()
    return render(request, 'viewDesktopUser.html', {'desktop': desktop_data})


@login_required(login_url='admin_login')
def viewPrinter(request):
    printer_data = Printer.objects.all()
    return render(request, 'viewPrinter.html', {'printer': printer_data})

@login_required(login_url='emp_login')
def viewPrinterUser(request):
    printer_data = Printer.objects.all()
    return render(request, 'viewPrinterUser.html', {'printer': printer_data})

@login_required(login_url='admin_login')
def viewUPS(request):
    ups_data = Ups.objects.all()
    return render(request, 'viewUPS.html', {'ups': ups_data})

@login_required(login_url='emp_login')
def viewUPSUser(request):
    ups_data = Ups.objects.all()
    return render(request, 'viewUPSUser.html', {'ups': ups_data})

@login_required(login_url='admin_login')
def viewMFD(request):
    multifunctional_data = MultifunctionalDevice.objects.all()
    return render(request, 'viewMFD.html', {'multifunctionaldevice': multifunctional_data})

@login_required(login_url='emp_login')
def viewMFDUser(request):
    multifunctional_data = MultifunctionalDevice.objects.all()
    return render(request, 'viewMFDUser.html', {'multifunctionaldevice': multifunctional_data})



@login_required(login_url='admin_login')
def editDesktop(request,pid):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    desktop_data = Desktop.objects.get(voucher_numberd = pid)
    return render(request, 'editDesktop.html', {'desktop': desktop_data})


@login_required(login_url='admin_login')
def updateDesktop(request, pid):
    voucher_number_desktop = request.POST.get('SerialNumberD')
    monitor_brand_name = request.POST.get('MonitorBrandNameD')
    monitor_model_name = request.POST.get('MonitorModelNameD')
    cpu_brand_name = request.POST.get('CpuBrandNameD')
    cpu_model_name = request.POST.get('CpuModelNameD')
    cpu_processor = request.POST.get('CpuProcessorD')
    cpu_ram = request.POST.get('CpuRamD')
    mouse_serial_number = request.POST.get('MouseSerialNumberD')
    keyboard_serial_number = request.POST.get('KeyboardSerialNumberD')
    grant_desktop = request.POST.get('GrantD')
    yop_desktop = request.POST.get('YopD')
    gp_desktop = request.POST.get('GroupD')
    nomenclature_desktop = request.POST.get('NomenclatureD')

    d = Desktop.objects.get(voucher_numberd = pid)
    d.voucher_numberd = voucher_number_desktop
    d.monitor_brand_name=monitor_brand_name
    d.monitor_model_name=monitor_model_name
    d.cpu_brand_name=cpu_brand_name
    d.cpu_model_name=cpu_model_name
    d.cpu_processor=cpu_processor
    d.cpu_ram=cpu_ram
    d.keyboard_serial_number=keyboard_serial_number
    d.mouse_serial_number=mouse_serial_number
    d.grant=grant_desktop
    d.year_of_purchase=yop_desktop
    d.group=gp_desktop
    d.nomenclature=nomenclature_desktop
    d.save()

    return redirect('viewDesktop')


@login_required(login_url='admin_login')
def editPrinter(request,pid):
    printer_data = Printer.objects.get(voucher_numberp = pid)
    return render(request, 'editPrinter.html', {'printer': printer_data})

@login_required(login_url='admin_login')
def updatePrinter(request, pid):
    voucher_number_printer = request.POST.get('SerialNumberP')
    brand_name_printer = request.POST.get('BrandNameP')
    model_name_printer = request.POST.get('ModelNameP')
    grant_printer = request.POST.get('GrantP')
    yop_printer = request.POST.get('YopP')
    printer_type = request.POST.get('TypeP')
    gp_printer = request.POST.get('GroupP')
    nomenclature_printer = request.POST.get('NomenclatureP')

    p = Printer.objects.get(voucher_numberp = pid)
    p.voucher_numberp = voucher_number_printer
    p.brand_name=brand_name_printer
    p.model_name=model_name_printer
    p.grant=grant_printer
    p.pyop=yop_printer
    p.ptype=printer_type
    p.group=gp_printer
    p.nomenclature=nomenclature_printer
    p.save()

    return redirect('viewPrinter')


@login_required(login_url='admin_login')
def editUPS(request,pid):
    ups_data = Ups.objects.get(voucher_numberu = pid) 
    return render(request, 'editUPS.html', {'ups': ups_data})

@login_required(login_url='admin_login')
def updateUPS(request, pid):
    voucher_number_ups = request.POST.get('SerialNumberU')
    brand_name_ups = request.POST.get('BrandNameU')
    model_name_ups = request.POST.get('ModelNameU')
    grant_ups = request.POST.get('GrantU')
    yop_ups = request.POST.get('YopU')
    ups_power = request.POST.get('PowerU')
    ups_type = request.POST.get('TypeU')
    gp_ups = request.POST.get('GroupU')
    nomenclature_ups = request.POST.get('NomenclatureU')

    u = Ups.objects.get(voucher_numberu = pid)
    u.voucher_numberu = voucher_number_ups
    u.brand_name=brand_name_ups
    u.model_name=model_name_ups
    u.grant=grant_ups
    u.uyop=yop_ups
    u.ups_power=ups_power
    u.ups_type=ups_type
    u.group=gp_ups
    u.nomenclature=nomenclature_ups
    u.save()

    return redirect('viewUPS')

@login_required(login_url='admin_login')
def editMFD(request,pid):
    multifunctional_data = MultifunctionalDevice.objects.get(voucher_numberm = pid) 
    return render(request, 'editMFD.html', {'multifunctionaldevice': multifunctional_data})


@login_required(login_url='admin_login')
def updateMFD(request, pid):
    vnumber = request.POST.get('SerialNumberM')           
    brandname = request.POST.get('BrandnameM')
    modelname = request.POST.get('ModelnameM')
    grantm = request.POST.get('GrantM')
    yopm = request.POST.get('YopM')  
    gpm = request.POST.get('GroupM')
    nomenclaturem = request.POST.get('NomenclatureM')

    m = MultifunctionalDevice.objects.get(voucher_numberm = pid)
    m.voucher_numberm = vnumber   
    m.brand_name = brandname
    m.model_name = modelname
    m.grant = grantm
    m.purchaseyear = yopm
    m.group = gpm
    m.nomenclature = nomenclaturem

    m.save()
    
    return redirect('viewMFD')


@login_required(login_url='admin_login')
def deleteDesktop(request,pid):
    d = Desktop.objects.get(voucher_numberd = pid)
    d.delete()
    
    return redirect('viewDesktop')

@login_required(login_url='admin_login')
def deletePrinter(request,pid):
    p = Printer.objects.get(voucher_numberp = pid)
    p.delete()
    
    return redirect('viewPrinter')

@login_required(login_url='admin_login')
def deleteUPS(request,pid):
    u = Ups.objects.get(voucher_numberu = pid)
    u.delete()
    
    return redirect('viewUPS')

@login_required(login_url='admin_login')
def deleteMFD(request,pid):
    m = MultifunctionalDevice.objects.get(voucher_numberm = pid)
    m.delete()
    
    return redirect('viewMFD')

@login_required(login_url='admin_login')
def searchDevice(request):
    if request.method == "POST":
        serial_number = request.POST.get('Srno')
        group = request.POST.get('Group')
        grant = request.POST.get('Grant')
        purchase_year = request.POST.get('purchaseyear')

        queryset = Desktop.objects.none()
        printer_queryset = Printer.objects.none()
        ups_queryset = Ups.objects.none()
        mfd_queryset = MultifunctionalDevice.objects.none()
         
        if serial_number:
            queryset |= Desktop.objects.filter(Q(voucher_numberd__icontains=serial_number))
            printer_queryset |= Printer.objects.filter(Q(voucher_numberp__icontains=serial_number))
            ups_queryset |= Ups.objects.filter(Q(voucher_numberu__icontains=serial_number))
            mfd_queryset |= MultifunctionalDevice.objects.filter(Q(voucher_numberm__icontains=serial_number))

        if group:
            queryset |= Desktop.objects.filter(Q(group__icontains=group))
            printer_queryset |= Printer.objects.filter(Q(group__icontains=group))
            ups_queryset |= Ups.objects.filter(Q(group__icontains=group))
            mfd_queryset |= MultifunctionalDevice.objects.filter(Q(group__icontains=group))

        if grant:
            queryset |= Desktop.objects.filter(Q(grant__icontains=grant))
            printer_queryset |= Printer.objects.filter(Q(grant__icontains=grant))
            ups_queryset |= Ups.objects.filter(Q(grant__icontains=grant))
            mfd_queryset |= MultifunctionalDevice.objects.filter(Q(grant__icontains=grant))

        if purchase_year:
            queryset |= Desktop.objects.filter(Q(year_of_purchase__icontains=purchase_year))
            printer_queryset |= Printer.objects.filter(Q(pyop__icontains=purchase_year))
            ups_queryset |= Ups.objects.filter(Q(uyop__icontains=purchase_year))
            mfd_queryset |= MultifunctionalDevice.objects.filter(Q(purchaseyear__icontains=purchase_year))

        if not (serial_number or group or grant or purchase_year):
            return render(request, 'deviceData.html', {})

        return render(request, 'deviceData.html', {
            "desktop": queryset,
            "printer_queryset": printer_queryset,
            "ups_queryset": ups_queryset,
            "mfd_queryset": mfd_queryset
        })

    else:
        return render(request, 'searchDevice.html')

@login_required(login_url='emp_login')
def searchDeviceUser(request):
    if request.method == "POST":
        serial_number = request.POST.get('Srno')
        group = request.POST.get('Group')
        grant = request.POST.get('Grant')
        purchase_year = request.POST.get('purchaseyear')

        queryset = Desktop.objects.none()
        printer_queryset = Printer.objects.none()
        ups_queryset = Ups.objects.none()
        mfd_queryset = MultifunctionalDevice.objects.none()
         
        if serial_number:
            queryset |= Desktop.objects.filter(Q(voucher_numberd__icontains=serial_number))
            printer_queryset |= Printer.objects.filter(Q(voucher_numberp__icontains=serial_number))
            ups_queryset |= Ups.objects.filter(Q(voucher_numberu__icontains=serial_number))
            mfd_queryset |= MultifunctionalDevice.objects.filter(Q(voucher_numberm__icontains=serial_number))

        if group:
            queryset |= Desktop.objects.filter(Q(group__icontains=group))
            printer_queryset |= Printer.objects.filter(Q(group__icontains=group))
            ups_queryset |= Ups.objects.filter(Q(group__icontains=group))
            mfd_queryset |= MultifunctionalDevice.objects.filter(Q(group__icontains=group))

        if grant:
            queryset |= Desktop.objects.filter(Q(grant__icontains=grant))
            printer_queryset |= Printer.objects.filter(Q(grant__icontains=grant))
            ups_queryset |= Ups.objects.filter(Q(grant__icontains=grant))
            mfd_queryset |= MultifunctionalDevice.objects.filter(Q(grant__icontains=grant))

        if purchase_year:
            queryset |= Desktop.objects.filter(Q(year_of_purchase__icontains=purchase_year))
            printer_queryset |= Printer.objects.filter(Q(pyop__icontains=purchase_year))
            ups_queryset |= Ups.objects.filter(Q(uyop__icontains=purchase_year))
            mfd_queryset |= MultifunctionalDevice.objects.filter(Q(purchaseyear__icontains=purchase_year))

        if not (serial_number or group or grant or purchase_year):
            return render(request, 'deviceDataUser.html', {})

        return render(request, 'deviceDataUser.html', {
            "desktop": queryset,
            "printer_queryset": printer_queryset,
            "ups_queryset": ups_queryset,
            "mfd_queryset": mfd_queryset
        })

    else:
        return render(request, 'searchDeviceUser.html')

# def uploadPic(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             pr = LogoPic.objects.all()
#             pr.delete()
#             pic = request.FILES['pic']
#             new = LogoPic(pic = pic)
#             new.save()
#             return redirect('index')
#         else:
#             return redirect('index')
#     else:
#         return redirect('index')

def Logout(request):
    logout(request)
    return redirect('index')

