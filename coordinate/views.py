from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import resolve_url
from django.urls import reverse_lazy
from django.urls import reverse

from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView

# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from django.db.models import Prefetch
from django.db.models import OuterRef, Subquery
from django.db.models import Count
from django.db.models import Q
import random

from .models import Item
from .forms import ItemForm

# Create your views here.
class IndexView(TemplateView):
    template_name='coordinate/index.html'
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='今日のコーディネート'
        return context
        
# class DashboardView(LoginRequiredMixin,TemplateView):
class DashboardView(TemplateView):
    template_name='coordinate/dashboard.html'
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='今日のコーディネート'
        return context
        
# class ClosetView(LoginRequiredMixin,ListView):
class ClosetView(ListView):
    template_name='coordinate/closet.html'
    model=Item
    
    def get_queryset(self):
        # user=self.request.user
        # return Item.objects.filter(user=user)
        return Item.objects.all()
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='クローゼット'
        return context

# class ItemCreateView(LoginRequiredMixin,CreateView,SuccessMessageMixin):
class ItemCreateView(CreateView,SuccessMessageMixin):
    template_name='coordinate/item_create.html'
    model=Item
    form_class=ItemForm
    success_url=reverse_lazy('coordinate:item_create')
    success_message='クローゼットに服を追加しました'
    
    def form_valid(self,form):
        item=form.save(commit=False)
        # user=self.request.user
        # item.user=user
        item.save()
        messages.success(self.request,self.success_message)
        return super().form_valid(form)
        
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='服の追加'
        return context

# class ItemDisplayView(LoginRequiredMixin,TemplateView):
class ItemDisplayView(TemplateView):
    template_name='coordinate/item_display.html'
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='今日のおすすめコーデ'
        
        # user=self.request.user
        # items=Item.objects.filter(user=user)
        items=Item.objects.all()
        season=self.request.GET.get("season")
        context["season"]=season
        
        if season :
            items=items.filter(Q(season=season) | Q(season="all"))
            context["selected_season"]=season
        else:
            context["selected_season"]="すべての季節"
            
        proposed_hair=items.filter(category="hair").order_by("?").first()
        proposed_shoes=items.filter(category="shoes").order_by("?").first()

        random_number=random.random()
        if random_number>0.5:
            proposed_tops=items.filter(category="tops").order_by("?").first()
            proposed_bottoms=items.filter(category="bottoms").order_by("?").first()
            proposed_onepiece=None
            proposed_onepiece_tops=None
            context["proposed_pattern"]="separate"
        else:
            proposed_tops=None
            proposed_bottoms=None
            proposed_onepiece=items.filter(category="onepiece").order_by("?").first()
            proposed_onepiece_tops=items.filter(category="onepiece-tops").order_by("?").first()
            context["proposed_pattern"]="onepiece"

        context["proposed_hair"]=proposed_hair
        context["proposed_shoes"]=proposed_shoes
        context["proposed_tops"]=proposed_tops
        context["proposed_bottoms"]=proposed_bottoms
        context["proposed_onepiece"]=proposed_onepiece
        context["proposed_onepiece_tops"]=proposed_onepiece_tops
        return context
