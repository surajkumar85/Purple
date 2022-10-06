from django.shortcuts import render
from .models import Banner,Service,ReWork,TeamMember,Pricing,Work,TransImage,UserEmail
from django.core.mail import send_mail
from decouple import config
# Create your views here.
def index(request):
    return render(request,"myapp/index.html",{
        "banners" : Banner.objects.all(),
        "services" : Service.objects.all(),
        "reworks" : ReWork.objects.all()
    })

def about(request):
    if request.method == 'POST':
        form_email = request.POST['email']
        form = UserEmail() 
        form.email = form_email
        form.save()
        return render(request,"myapp/about.html",{
            "members": TeamMember.objects.all(),
            "is_added" : True
        })
    

def pricing(request):
    return render(request,"myapp/pricing.html",{
        "pricing" : Pricing.objects.all()
    })

def contact(request):
    if request.method == "POST":
        name = request.POST['full_name']
        email = request.POST['email']
        phone = request.POST['phone']
        company = request.POST['company']
        subject = request.POST['subject']
        message = request.POST['message']

        data = {
            "name" :name,
            "email":email,
            "phone":phone,
            "company" : company,
            "subject":subject,
            "message" : message
        }
        message = f'''
        Message from: {data['name']}
        User email: {data['email']}
        User Company: {data['company']}
        
        Subject: {data['subject']}
        Message: {data['message']}
        '''
        send_mail(data['subject'],message,'',[config('EMAIL_HOST_USER')])
        return render(request,"myapp/contact.html",{"is_send":True,"name":name})
    return render(request,"myapp/contact.html")

def work(request):
    return render(request,"myapp/work.html",{
        "works" : Work.objects.all(),
        "ftrans": TransImage.objects.filter(name="first"),
        "strans": TransImage.objects.filter(name="second")
    })
