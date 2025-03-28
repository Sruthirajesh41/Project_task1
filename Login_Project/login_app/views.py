from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import CustomUser,Mark
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
import random
from django.contrib import messages
# from django.urls import reverse

# Create your views here.
def user_registration(request):
    if request.method=='POST':
        name=request.POST['txt_name']
        age=request.POST['txt_age']
        address=request.POST['txt_address']
        district=request.POST['sel_district']
        mobile=request.POST['txt_mobile']
        email=request.POST['txt_email']
        username=request.POST['txt_username']
        password=request.POST['txt_password']
        data=CustomUser.objects.create_user(first_name=name,age=age,address=address,district=district,mobile=mobile,email=email,username=username,password=password)
        # data.set_password(password) 
        data.save()
        # return HttpResponse("Success")
        return render(request,'registration.html',{'msg':'You are successfuiuytrdelly registered'})
    else:
        return render(request,'registration.html')
def home(request):
    return render(request,'home.html')
# def login(request):

def LoginUser(request):
    if request.method=="POST":
        uname=request.POST['txt_username']
        pswd=request.POST['txt_password'] 
        print(pswd)
        user=authenticate(username=uname,password=pswd)
        if user is not None:
            login(request,user)
            return redirect(user_home)
        else:
            return render(request,'login.html',{'err':"Invalid"})
    else:
        return render(request,'login.html')
    
def send_otp(email):
    otp = random.randint(100000,999999)
    send_mail(
        'Your OTP Code',''
        f'Your OTP code is: {otp}',
        'sruthirajesh41@gmail.com',
        [email],
        fail_silently=False,
    )
    return otp

def password_reset_request(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = CustomUser.objects.get(email=email)
            
            otp = send_otp(email)

            context = {
                        "email": email,
                        "otp": otp,
            }
            return render(request,'verify_otp.html',context)
        
        except CustomUser.DoesNotExist:
            messages.error(request,'Email address not found.')
    else:
        return render(request,'password_reset.html')
    return render(request,'password_reset.html') 

def verify_otp(request):
    if request.method == 'POST':
        email =request.POST.get('email')
        otpold = request.POST.get('otpold')
        otp = request.POST.get('otp')

        if otpold==otp :
            context = {
                'otp' : otp,
                'email': email
            }
            return render(request,'set_new_password.html',context)
        else:
            messages.error(request,"Invalid OTP")
    else:
        return render(request,'verify_otp.html') 

    return render(request,'verify_otp.html') 

def set_new_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if new_password==confirm_password:
            try:
                data = CustomUser.objects.get(email=email)
                #user=CustomUser.objects.get(id=data.user_id.id)
                data.set_password(new_password)
                data.save()
                messages.success(request,'Password has been reset successfully')
                return redirect(LoginUser)
            except CustomUser.DoesNotExist:
                messages.error(request,'Password doesnot match')
        return render(request,'set_new_password.html',{'email':email})               
    return render(request,'set_new_password.html',{'email':email})

def LogoutUser(request):
    logout(request)
    return redirect('login')
    
def user_home(request):
    return render(request,'user_home.html')
def add_mark(request):
    grade=""
    user=CustomUser.objects.get(id=request.user.id)
    # print(user)
    # print(request.POST)  # Debugging

    if request.method=="POST":
        sem_name=request.POST['txt_sem']
        exam_mark=request.POST['txt_exam_mark']
        ce=request.POST['txt_ce']
        # sem_name=request.POST.get('txt_sem','')
        # exam_mark=request.POST.get('txt_exam_mark','')
        # ce=request.POST.get('txt_ce','')
        m1=int(exam_mark)
        m2=int(ce)
        total=m1+m2
        print(total)
        # total=exam_mark+ce
        if total<=500:
            grade='A'
        elif total>=300:
            grade='B'
        elif total>=200:
            grade='C'
        elif total<200:
            grade='D'
        else:
            grade="Failed"
        obj_mark=Mark.objects.create(user_id=user,semester_name=sem_name,exam_mark=exam_mark,ce_mark=ce,total_mark=total,grade=grade)
        obj_mark.save()
        return redirect(MarkDetails)
        # reverse('mark_details', kwargs={'id': user.id})
    else:
        return render(request,'add_mark.html')
def MarkDetails(request):
    obj_id=CustomUser.objects.get(id=request.user.id)
    report=Mark.objects.filter(user_id=obj_id.id)
    return render(request,'mark_details.html',{'data':report})
def Editmark(request):
    edit_data=CustomUser.objects.get(id=request.user.id)
    edit_mark=Mark.objects.get(user_id=edit_data.id)
    if request.method=='POST':
        edit_mark.semester_name=request.POST['txt_sem']
        edit_mark.exam_mark=request.POST['txt_exam_mark']
        edit_mark.ce_mark=request.POST['txt_ce']
        m1=int(edit_mark.exam_mark)
        m2=int(edit_mark.ce_mark)
        edit_mark.total_mark=m1+m2
        # print(total)
        # total=exam_mark+ce
        if edit_mark.total_mark<=500:
            edit_mark.grade='A'
        elif edit_mark.total_mark>=300:
            edit_mark.grade='B'
        elif edit_mark.total_mark>=200:
            edit_mark.grade='C'
        elif edit_mark.total_mark<200:
            edit_mark.grade='D'
        else:
            edit_mark.grade="Failed"
        edit_mark.save()
        return redirect('mark_details')
    else:
        return render(request,'editmark.html',{'data':edit_mark})
        

    
        

        
    
    
    

