from django.shortcuts import render


def show_url(request):
    return render(request, "hello")

