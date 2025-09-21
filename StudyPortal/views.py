from django.http import HttpResponse
def hello_feature1(request):
    return HttpResponse("Hello from Feature 1 branch")
