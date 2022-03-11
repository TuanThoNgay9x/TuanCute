from django.shortcuts import render
from django.contrib.auth import authenticate, login, decorators
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PortForm


class Indexclass(View):
    def get(self, request):
        return HttpResponse('hello')


class loginclass(View):
    def get(self, request):
        return render(request, 'Login/login.html')

    def post(self, request):
        Username = request.POST.get('tendangnhap')
        Pasword = request.POST.get('matkhau')
        my_user = authenticate(username=Username, password=Pasword)
        if my_user is None:
            return HttpResponse('User is not available')
        login(request, my_user)
        return render(request, 'Login/success.html')


class Viewuser(LoginRequiredMixin, View):
    login_url = '/login'

    def get(self, request):
        return HttpResponse('hello anh em')


@decorators.login_required(login_url='/login')
def viewproduct(request):
    return HttpResponse('xem sản phẩm')


class AddPost(LoginRequiredMixin, View):
    login_url = '/login'

    def get(self, request):
        f = PortForm()
        context = {'fm': f}
        return render(request, 'Login/addpost.html', context)

    def post(self, request):
        f = PortForm(request.POST)
        if not f.is_valid():
            return HttpResponse('You was input not valid type')
        if request.user.has_perm('Login.add_post'):
            f.save()
        else:
            return HttpResponse('you khong co quen ok')
        return HttpResponse('ok')

