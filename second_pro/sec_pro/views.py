from django.shortcuts import render

def index(req):
    Con ={'text': 'this is it', 'number':100}
    return render(req,'sec_pro/index.html',Con)

def other(req):
    return render(req,'sec_pro/other.html')

def relative(req):
    return render(req,'sec_pro/relative.html')

    


# Create your views here.
