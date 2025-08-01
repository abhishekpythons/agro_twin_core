from django.shortcuts import render

def analysis_view(request):
    return render(request, 'analysis.html')
