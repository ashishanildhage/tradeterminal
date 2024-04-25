from django.shortcuts import render

# Create your views here.
def orderdashboard(request):
  return render(request, "ordercontrol/orderdashboard.html")
