from django.shortcuts import render, redirect
from .utils import arithmetic_mean_freq, geometric_mean_freq, harmonic_mean_freq
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usermedia
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect


def pc(request):
    return render(request, 'pc.html')

def calculate(request):
    if request.method == "POST":
        age = int(request.POST.get("age"))
        smoker = request.POST.get("smoker") == "yes"
        coverage = int(request.POST.get("coverage"))

        # Simple premium formula
        base_rate = 500
        age_factor = 1 + max(0, age - 30) * 0.02
        smoker_factor = 1.5 if smoker else 1
        premium = base_rate * age_factor * smoker_factor * (coverage / 100000)

        return render(request, "results"
                               ".html", {"premium": round(premium, 2)})
    return render(request, "pc.html")

from django.shortcuts import render

def interests(request):
    Sinterest = None

    if request.method == "POST":
        try:
            principal = float(request.POST.get("principal"))
            rate = float(request.POST.get("rate"))
            time = float(request.POST.get("time"))

            Sinterest = (principal * rate * time) / 100

        except (TypeError, ValueError):
            Sinterest = "Invalid input"

    return render(request, "interests.html", {"Sinterest": Sinterest})
def amountsi(request):
    Amount = None
    if request.method == "POST":
        try:
            principal = float(request.POST.get("principal"))
            rate = float(request.POST.get("rate"))
            time = float(request.POST.get("time"))

            Amount = principal * (1 + (rate/100)*time)
            Amount = round(Amount, 2)
        except:
            Amount = "Invalid input"

    return render(request, "amountsi.html", {"Amount": Amount})

def moct(request):
    am = gm = hm = None

    # Default 4 empty fields if GET
    x_values = [""] * 4
    f_values = [""] * 4

    if request.method == "POST":
        x_values = request.POST.getlist("x")
        f_values = request.POST.getlist("f")

        # Clean and calculate if valid
        try:
            x = [float(val) for val in x_values if val.strip()]
            f = [float(val) for val in f_values if val.strip()]

            if len(x) == len(f) and len(x) > 0:
                am = arithmetic_mean_freq(x, f)
                gm = geometric_mean_freq(x, f)
                hm = harmonic_mean_freq(x, f)
        except ValueError:
            pass  # ignore invalid input

        # Ensure lists always have 4 items (for table display)
        while len(x_values) < 4:
            x_values.append("")
        while len(f_values) < 4:
            f_values.append("")

    return render(
        request,
        "probabilityandstatistics/moct.html",
        {"am": am, "gm": gm, "hm": hm, "x_values": x_values, "f_values": f_values},
    )
def hom(request):
    return render(request, "home.html")
def SMA3101(request):
    return render(request, "SMA3101.html")
def ITAS(request):
    return render(request, "ITAS.html")
def mod(request):
    return render(request, "probabilityandstatistics/mod.html")
def probability(request):
    return render(request, "probabilityandstatistics/probability.html")

def register(request):
    if request.method == "POST":
        name = request.POST.get("username")
        email = request.POST.get("email")
        phonenumber = request.POST.get("phonenumber")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        # Validate fields
        if not all([name, email, phonenumber, password, password2]):
            messages.error(request, "All fields are required.")
            return render(request, "register.html")

        if password != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, "register.html")

        if Usermedia.objects.filter(Email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, "register.html")

        # Save the user
        user = Usermedia(
            Name=name,
            Email=email,
            Phone_number=phonenumber,
            Password=password,
        )

        user.set_password(password)
        user.save()

        messages.success(request, "Registration successful!")
        return redirect('hom')

    return render(request, "register.html")



def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')


        from django.contrib.auth.models import User
        try:
            user_obj = User.objects.get(email=email)
            username = user_obj.username
        except User.DoesNotExist:
            username = None

        if username:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')

        messages.error(request, "Invalid email or password")

    return render(request, 'login.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


def logout_view(request):
    logout(request)
    return redirect('login')




