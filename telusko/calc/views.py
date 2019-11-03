from django.shortcuts import render


# Create your views here.
def home(request):

    context = {
        'name':'Gura'
    }
    template_name = 'calc/home.html'
    return render(request,template_name,context)


def add(request):
    
    val1 = request.POST['num1']
    val2 = request.POST['num2']
    res = int(val1) + int(val2)

    context = {
        'result' : res
    }
    template_name = 'calc/result.html'
    return render(request,template_name,context)