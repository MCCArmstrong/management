from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse, request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic, View
from django.views.decorators.csrf import csrf_exempt
from users.models import User
from .forms import UnicornForm, About, PurchaseForm, ServiceForm
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib import messages
from .models import caviet, unicornabout, DailyTask, unicornService, \
    ProductPortfolio, MakeRequest, ProductReviewRating, CustomerPurchaseForm
import json
from django.views.generic.base import TemplateView
from django.views.generic import View
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from users.forms import CreateUserForm
from django.conf import settings as django_settings
import requests


class IndexView(ListView):
    template_name = 'pekuric_mgt/home.html'
    queryset = unicornService.objects.all().order_by("id")[:4]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = unicornabout.objects.all()
        context['unicornabout'] = query
        return context


class AboutView(generic.TemplateView):
    template_name = 'pekuric_mgt/about-us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductView(ListView):
    template_name = 'pekuric_mgt/product.html'
    queryset = ProductPortfolio.objects.all().order_by("-id")[:4]


class ProductDetailView(DetailView):
    model = ProductPortfolio
    template_name = 'pekuric_mgt/project-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ServiceView(ListView):
    template_name = 'pekuric_mgt/services.html'
    queryset = unicornService.objects.all().order_by("id")[:3]


class ServiceDetails(DetailView):
    model = unicornService
    template_name = 'pekuric_mgt/serviceDetails.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AjaxableResponseMixin:
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response


class PaymentForm(AjaxableResponseMixin, CreateView):
    model = CustomerPurchaseForm
    template_name = 'admin/customerInfo.html'
    form_class = PurchaseForm

    def post(self, request, *args, **kwargs):
        form = PurchaseForm(request.POST)
        if form.is_valid():
            url = 'https://api.paystack.co/transaction/initialize'
            callback_url = request.build_absolute_uri(str(reverse_lazy('pekuric_mgt:payment-info')))

            fields = {
                'email': form.cleaned_data['email'],
                'amount': int(form.cleaned_data['amount']) * 100,
                'callback_url': callback_url
            }
            header = {
                "Authorization": "Bearer %s" % django_settings.PAYSTACK_SECRET_KEY,
                'Content-Type': 'application/json',
                "Cache-Control": 'no-cache',

            }
            req = requests.post(url, json=fields, headers=header)
            # print(req.json)
            result = req.json()
            if result['status']:
                redirect_url = result['data']['authorization_url']
                return HttpResponseRedirect(redirect_url)


class MakeRequestView(AjaxableResponseMixin, CreateView):
    model = MakeRequest
    fields = ["fullname", "mobile", "businessname", "business_category"]
    template_name = 'admin/usersRequestForm.html'
    success_url = reverse_lazy("pekuric_mgt:make-request")

    def get_form(self, form_class=None):
        form = super().get_form()
        for field in form.fields:
            form.fields[field].widget.attrs.update({"class": 'form-control'})
            return form


class CreateService(AjaxableResponseMixin, CreateView):
    model = unicornService
    fields = ["service_title", "service_icon", "service_description"]
    template_name = "admin/service-create.html"
    success_url = reverse_lazy("pekuric_mgt:create-about")

    def get_form(self, form_class=None):
        form = super().get_form()
        for field in form.fields:
            form.fields[field].widget.attrs.update({"class": 'form-control'})
            return form


class UpdateService(AjaxableResponseMixin, UpdateView):
    model = unicornService
    # form_class = ServiceForm
    template_name = "admin/service-create.html"
    success_url = reverse_lazy("pekuric_mgt:create-about")

    def get_form(self, form_class=None):
        form = super().get_form()
        for field in form.fields:
            form.fields[field].widget.attrs.update({"class": 'form-control'})
            return form


class Dashboard(generic.TemplateView):
    # login_url = 'pekuric_mgt:user-signin'
    template_name = 'admin/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ProductPortfolio'] = ProductPortfolio.objects.all().order_by('-id')[:2]
        return context


class ProductRatings(generic.TemplateView):
    template_name = 'admin/productRating.html'

    @csrf_exempt
    def api_handel_rating(request):
        if request.method == 'POST':
            ProductReviewRating.objects.create(user=request.user, product_id=request.POST.get('product_id'),
                                               rating_value=request.POST.get('rating_value'),
                                               review_note=request.POST.get('review_note'))
            return HttpResponse(json.dumps({"response": "ok", "message": "Review sent"}))
        else:
            return HttpResponse({'response': 'error', 'message': 'Invalid request method'})

    def auto_login_user(request):
        if User.objects.all().exists():
            login(request, User.objects.all()[0])
        return HttpResponseRedirect(reverse_lazy('pekuric_mgt:portfolio'))


class Portfolio(AjaxableResponseMixin, CreateView):
    model = ProductPortfolio
    template_name = 'admin/portfolio-create.html'
    fields = ['product_name', 'portfolio_file', 'product_description', 'product_price', 'date_created']
    success_url = reverse_lazy('pekuric_mgt:portfolio')

    def get_form(self, form_class=None):
        form = super().get_form()
        for field in form.fields:
            form.fields[field].widget.attrs.update({"class": 'form-control'})
            return form


class PortfolioView(ListView):
    template_name = 'admin/portfolio.html'
    model = ProductPortfolio
    queryset = ProductPortfolio.objects.all().order_by("id")[:4]


class PortfolioDeleteView(DeleteView):
    model = ProductPortfolio
    success_url = reverse_lazy("pekuric_mgt:portfolio-slides")
    template_name = 'admin/portfolio.html'

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            return super().post(self, request, *args, **kwargs)
        return super().dispatch()


class Gallery(generic.TemplateView):
    template_name = 'admin/gala.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UnicornInsert(AjaxableResponseMixin, CreateView):
    # login_url = 'pekuric_mgt:user-signin'
    model = caviet
    fields = ['sliders', 'description', 'preview']
    template_name = 'admin/form.html'
    success_url = reverse_lazy('pekuric_mgt:preview')

    def get_form(self, form_class=None):
        form = super().get_form()
        for field in form.fields:
            form.fields[field].widget.attrs.update({"class": 'form-control'})
            return form


class unicornUpdate(AjaxableResponseMixin, UpdateView):
    model = caviet
    form_class = UnicornForm
    success_url = reverse_lazy('pekuric_mgt:edit')
    template_name = 'admin/update_form.html'


class unicornDelete(DeleteView):
    model = caviet
    success_url = reverse_lazy("pekuric_mgt:preview")
    template_name = 'admin/table_list.html'

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            return super().post(self, request, *args, **kwargs)
        return super().dispatch()


class Preview(ListView):
    model = caviet
    template_name = 'admin/table_list.html'
    queryset = caviet.objects.all().order_by("id")[:4]


class TaskManagement(LoginRequiredMixin, ListView):
    login_url = 'pekuric_mgt:user-signin'
    template_name = 'admin/task_list.html'
    queryset = DailyTask.objects.all().order_by("id")[:4]


class TaskCreate(AjaxableResponseMixin, CreateView):
    model = DailyTask
    fields = ["task_name", "task_description", "task_date", "time_assigned", "time_completed"]
    template_name = 'admin/task_list.html'
    success_url = reverse_lazy("pekuric_mgt:daily-task")

    def get_form(self, form_class=None):
        form = super().get_form()
        for field in form.fields:
            form.fields[field].widget.attrs.update({"class": 'form-control'})
            return form


class TaskUpdate(AjaxableResponseMixin, UpdateView):
    model = caviet
    form_class = UnicornForm
    success_url = reverse_lazy('pekuric_mgt:daily-task')
    template_name = 'admin/task_list.html'


class TaskDelete(LoginRequiredMixin, DeleteView):
    login_url = 'pekuric_mgt:user-signin'
    model = caviet
    success_url = reverse_lazy("pekuric_mgt:daily-task")
    template_name = 'admin/task_list.html'


class ProductDetail(DetailView):
    model = caviet
    template_name = 'admin/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Menu(AjaxableResponseMixin, CreateView):
    model = unicornabout
    fields = ["file", "about", "history"]
    template_name = "admin/about-create.html"
    success_url = reverse_lazy("pekuric_mgt:create-about")

    def get_form(self, form_class=None):
        form = super().get_form()
        for field in form.fields:
            form.fields[field].widget.attrs.update({"class": 'form-control'})
            return form


class UpdateAbout(AjaxableResponseMixin, UpdateView):
    # login_url = 'pekuric_mgt:user-signin'
    model = unicornabout
    template_name = 'admin/update-menu.html'
    form_class = About


def product_search(request):
    return render(request, 'admin/app_mainheader.html')
    search_keyword = request.GET["query"]
    search_result = caviet.objects.filter(Q(sliders__icontains=search_keyword) |
                                          Q(description__icontains=search_keyword) |
                                          Q(preview__icontains=search_keyword)).values('sliders', 'description',
                                                                                       'preview')
    search_result = list(search_result)
    return JsonResponse(search_result, safe=False)


class UserRegistration(FormView):
    form_class = CreateUserForm
    template_name = 'admin/signup.html'
    success_url = reverse_lazy("pekuric_mgt:user-signin")

    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)


class UserSignin(LoginView):
    template_name = 'admin/login.html'
    # success_url = reverse_lazy("pekuric_mgt:panel")
    redirect_field_name = reverse_lazy("pekuric_mgt:panel")

    def get_form(self, form_class=None):
        form = super().get_form()
        for field in form.fields:
            form.fields[field].widget.attrs.update({"class": "form-control", "placeholder": field.title()})
        return form


class UserLogout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse_lazy("pekuric_mgt:'user-signin"))
