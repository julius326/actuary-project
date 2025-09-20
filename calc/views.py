from django.shortcuts import render
from .utils import arithmetic_mean_freq, geometric_mean_freq, harmonic_mean_freq
from .forms import FrequencyForm
def index(request):
    return render(request, 'index.html')

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
    return render(request, "index.html")

def averages(request):
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
        "averages.html",
        {"am": am, "gm": gm, "hm": hm, "x_values": x_values, "f_values": f_values},
    )
def hom(request):
    return render(request, "home.html")


