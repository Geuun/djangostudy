from django.shortcuts import redirect, render

from shortener.models import Users

# Create your views here.
def index(request):
    user = Users.objects.filter(username='admin').first()
    # user = User.object.get(username='admin')
    email = user.email if user else 'Anomymous User!'
    return render(request, 'base.html', {'welcome_msg': f'Hello {email}'})

@csrf_exempt
def get_user(request, user_id):
    print(user_id)
    if request.method == 'GET':
        abc = request.GET.get('abc')
        xyz = request.GET.get('xyz')
        user = Users.objects.filter(pk=user_id).first()
        return render(request, 'base.html', {'user': user, 'params': [abc, xyz]})

# def redirect_test(request):
#     print('Go Redirect')
#     return redirect('home')