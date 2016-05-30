from django.shortcuts import render


def disclaimer(request):
    return render(
        request,
        "disclaimer.html",
        {},
    )


def privacy(request):
    return render(
        request,
        "privacy.html",
        {},
    )


def terms(request):
    return render(
        request,
        "terms.html",
        {},
    )
