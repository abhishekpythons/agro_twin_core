from django.shortcuts import render

def analysis_view(request):
    return render(request, 'analysis.html')

def analyze(request, shapefile_path):
    # Calculate the output.jpg, save it at MEDIA_ROOT
    return "output.jpg"
