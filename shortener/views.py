from django.shortcuts import redirect, render

from shortener.models import Users

# Create your views here.
def index(request):
    # user = Users.objects.filter(username='admin').first()
    user = User.object.get(username='admin')
    email = user.email if user else 'Anomymous User!'
    print(email)
    print(request.user.is_authenticated)
    if request.user.is_authenticated is False:
        email = 'Anomymous User!'
    print(email)
    return render(request, 'base.html', {'welcome_msg': f'Hello {email}'})

def redirect_test(request):
    print('Go Redirect')
    return redirect('home')