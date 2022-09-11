from django.shortcuts import render


def handler404(request, exception):
    """ Error Handler 404 - Page not Found """
    return render(request, "errors/404.html")
