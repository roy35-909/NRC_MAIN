from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name="Showing Homepage"),
    path('about',views.about,name="About page"),
    path('guest',views.guest,name="Guest page"),
    path('news',views.news,name="news_page"),
    path('catagory',views.program,name="Catagory_page"),
    path('projects',views.projects,name="Projects_page"),
    path('login',views.login,name="Login_page"),
    path('register',views.register,name="Register_page"),
    path('logout',views.logout,name="logout"),
    path('fpass',views.fpass,name="forgot password"),
    path('reset',views.reset,name="Reset password"),
    path('show_team_info/<str:division>',views.team_info,name="Team Info"),
    path('profile',views.profile,name="profile"),
    path('cprofile',views.complete_profile,name="c_profile"),
    path('payment',views.payment,name="payment"),
    path('transcript',views.a_payment,name="Apcepted payment"),
    path('transcript/<str:email>',views.a_payment_done,name="Apcepted payment"),
    path('delete/<str:email>',views.delete,name="Apcepted payment"),
    

    
]