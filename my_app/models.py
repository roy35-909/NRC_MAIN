from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    fpass_token = models.CharField(max_length=150,null=True,blank=True)
    t_shirt_size = models.CharField(max_length=5,null=True,blank=True)
    is_selected = models.BooleanField(default=False)
    is_payment_done = models.BooleanField(default=False)
    is_payment_apcepted = models.BooleanField(default=False)
    is_team_registration_done = models.BooleanField(default=False)
    payment_id = models.CharField(max_length=200,null=True,blank=True)
    upcomming_event = models.CharField(max_length=200,null=True,blank=True)
    upcomming_event_venue = models.CharField(max_length=200,null=True,blank=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= []

class Team(models.Model):
    leader = models.ForeignKey(User,on_delete=models.CASCADE,related_name="teams")
    name = models.CharField(max_length=60)
    email = models.EmailField()
    t_shirt_size = models.CharField(max_length=5,null=True,blank=True)
    def __str__(self):
        return self.email

class Project(models.Model):
    leader = models.ForeignKey(User,on_delete=models.CASCADE, related_name="project")
    project_title = models.CharField(max_length=200)
    team_name = models.CharField(max_length=200)
    institution = models.CharField(max_length=150)
    catagory = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)
    distric = models.CharField(max_length=30)
    photo = models.ImageField(upload_to="media/projects" ,null=True,blank=True)
    def __str__(self):
        return self.team_name
class Home(models.Model):
    signature = models.CharField(default="roy77",max_length=5)
    open_payment_link = models.BooleanField(default=False)
    date = models.CharField(max_length=100)
    video_url = models.URLField()
    rodemap_banner = models.ImageField(upload_to = "media/rodemap")
    prize_logo = models.ImageField(upload_to = "media/prize_logo")
    foter_description = models.TextField(max_length=1000)
    youtube_link = models.URLField(null=True,blank=True)
    facebook_link = models.URLField(null=True,blank=True)
    linked_in_link = models.URLField(null=True,blank=True)
    contact = models.TextField(max_length=200,null=True,blank=True)
    phone1 = models.CharField(max_length=15,null=True,blank=True)
    phone2 = models.CharField(max_length=15,null=True,blank=True)
    phone3 = models.CharField(max_length=15,null=True,blank=True)
    email = models.EmailField(blank=True,null=True)
    hotline1 = models.CharField(max_length=15,null=True,blank=True)
    hotline2 = models.CharField(max_length=15,null=True,blank=True)

    def __str__(self):
        return self.signature
class Notice(models.Model):
    full_date = models.CharField(max_length=30)
    day = models.CharField(max_length=2)
    month = models.CharField(max_length=5)
    tag = models.CharField(max_length=20)
    notice = models.CharField(max_length=100)
    details = models.TextField(max_length= 500,null=True,blank=True)
    def __str__(self):
        return self.notice
class Faq(models.Model):
    q = models.CharField(max_length=200)
    a = models.CharField(max_length=200)

    def __str__(self):
        return self.q   
class Catagory(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500,null=True,blank=True)
    s_description = models.TextField(max_length=150)
    first_prize = models.CharField(max_length=100,null=True,blank=True) 
    secound_prize = models.CharField(max_length=100,null=True,blank=True) 
    third_prize = models.CharField(max_length=100,null=True,blank=True)
    photo = models.ImageField(upload_to="media/catagory",null=True,blank=True)
    def __str__(self):
        return self.title


class What_you_get(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title
class News(models.Model):
    photo = models.ImageField(upload_to = "media/news")
    title = models.CharField(max_length=300)
    s_about = models.TextField(max_length=200)
    about = models.TextField(max_length=500)
    date = models.CharField(max_length=20)
    def __str__(self):
        return self.title
class Sponsor(models.Model):
    logo = models.ImageField(upload_to = "media/sponsor")
    name = models.CharField(max_length=50)
    link = models.URLField(null=True,blank=True)
    def __str__(self):
        return self.name
class Guest(models.Model):
    inaguration_crermony_chief_guest = models.BooleanField(default=False)
    closing_crermony_chief_guest = models.BooleanField(default=False)
    honorable_judge = models.BooleanField(default=False)
    photo = models.ImageField(upload_to = "media/Guest",null=True,blank=True)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    facebook_link = models.URLField(null=True,blank=True)
    Twiter_link = models.URLField(null=True,blank=True)
    Linkedin_link = models.URLField(null=True,blank=True)
    def __str__(self):
        return self.name
