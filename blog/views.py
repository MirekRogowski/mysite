from django.shortcuts import render


# Create your views here.
def post_list(request):
    test = {}
    return render(request, 'blog/post_list.html', test)

