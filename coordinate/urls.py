from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name='coordinate'

urlpatterns =[
    path('',views.DashboardView.as_view(),name="index"),
    path('dashboard/',views.DashboardView.as_view(),name="dashboard"),
    path('closet/',views.ClosetView.as_view(),name="closet"),
    path('items/create',views.ItemCreateView.as_view(),name="item_create"),
    path('item/display/',views.ItemDisplayView.as_view(),name="item_display"),
]

# if settings.DEBUG:
    # urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
