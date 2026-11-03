from django.shortcuts import render

# Create your views here.

def login_view(request):
    # if request.user.is_authenticated:
    #     msg = f'user is authenticated as {request.user.username}'
    # else:
    #     msg = f'user is not authenticated'
    # return render(request, 'accounts/login.html', {'msg':msg})
    return render(request, 'accounts/login.html')

# def logout_view(request):
#     return

def signup_view(request):
    return render(request, 'accounts/signup.html')