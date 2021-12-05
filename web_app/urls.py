from django.contrib.auth import views
from django.urls import path

from web_app.forms import UserLoginForm
from web_app.views import EventView, NominationView, UserView

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name = 'auth.html',
                                           authentication_form=UserLoginForm),
         name='login'),
    path('events/', EventView.as_view(), name = 'events'),
    path('events/<int:pk>', NominationView.as_view(), name = 'nomination'),
    path('events/<int:pk_event>/<int:pk>', UserView.as_view(), name = 'users'),
]