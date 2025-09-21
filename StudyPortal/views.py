from django.shortcuts import render
def feature1_page(request):
    return render(request, 'StudyPortal/feature.html')