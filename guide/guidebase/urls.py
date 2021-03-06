from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('index', views.IndexView.as_view(), name='index'),
    path('list', views.ListView.as_view(), name='list'),
    path('list/<int:pk>', views.DetailIView.as_view(), name='place'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('planner', views.PlannerView.as_view(), name="planner")
]