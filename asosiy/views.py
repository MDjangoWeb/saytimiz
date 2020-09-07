from django.shortcuts import render, redirect
from .models import Jamoa, Portfolio, YangiliklargaYozilish, Murojat
from django.core.mail import send_mail
# Create your views here.

def index(request):
    m = 32
    jamoa = Jamoa.objects.all()
    ac = 'active'
    return render(request, 'index.html', {'jamoa':jamoa, 'active_asos':ac})


def about(request):
    ac = 'active'
    jamoa = Jamoa.objects.all()
    return render(request, 'about.html', {'jamoa':jamoa, 'active_haqimizda':ac})


def blog(request):
    ac = 'active'
    return render(request, 'blog.html', {'active_blog': ac})


def contact(request):
    if request.method == 'POST':
        ism = request.POST['ism']
        email = request.POST['email']
        mavzu = request.POST['mavzu']
        matn = request.POST['matn']

        murojat = Murojat(ism=ism, email=email, mavzu = mavzu, matn=matn)
        murojat.save();

    ac = 'active'
    return render(request, 'contact.html',{'active_contact':ac})


def blog_single(request):
    return render(request, 'blog-single.html')


def portfolio(request):
    ac = "active"
    
    portfolios = Portfolio.objects.all()
    return render(request, 'portfolio.html', {'active_portfolio':ac, 'portfolios':portfolios})


def portfolio_single(request):
    return render(request, 'portfolio-single.html')


def YangiliklargaYozilishview(request):
    if request.method == "POST":
        print('yaxshi')
        e_mail = request.POST['email']
        print('juda yaxshi')
        pochta = YangiliklargaYozilish(e_pochta=e_mail)
        pochta.save()

    send_mail("Assalomu alaykum.", "Bizga qiziqish bildirganingiz uuchun rahmat. Siz yangiliklarimizdan habardor bo'lib borasiz.", "muhammadyusufbek1998@gmail.com", [e_mail], fail_silently=False)
    return redirect('index')





