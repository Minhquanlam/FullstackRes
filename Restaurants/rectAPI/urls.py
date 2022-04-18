from django.conf.urls import url
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from rectAPI import views

urlpatterns = [
    path('',views.index),
    path('payment/', views.payment),
    #path('',views.payment),
    path('payment',views.order),
    path('pizza/', views.pizzas, name ="pizza"),
    path('drink/', views.drinks, name ="drink"),
    path('hamburger/', views.hamburgers, name ="hamburger"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)