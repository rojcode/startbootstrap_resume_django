from django.shortcuts import render

# Create your views here.
from profile_cv.models import Profile_cv


def home_page(request):
    user = Profile_cv.objects.get(first_name="Roj")
    return render(request,"profile/home.html",{"profile": user})
