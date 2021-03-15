from django.urls import path
from django.conf.urls import url
from . import views as views

urlpatterns_exchange = ([

    path('exchange/',
         views.ExchangeView.as_view(),
         name='exchange'),
    path('createkey/', views.create_key_view,
        name='create_key'),
])