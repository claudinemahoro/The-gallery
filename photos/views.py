from django.shortcuts import render

# Create your views here.
def location (request,id):
    location=Image.filter_by_location(id=id)
    print(location)
    locate=Location.objects.all()
    return render(request,'location.html',{"location":location,'locate':locate})
