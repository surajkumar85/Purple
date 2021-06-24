from django.db import models

# Create your models here.
class Banner(models.Model):
    slide_no = models.IntegerField()
    banner_heading = models.CharField(max_length=200)
    banner_content = models.TextField()
    is_active = models.BooleanField(null=True)

    def __str__(self):
        return f"{self.slide_no}"

class Service(models.Model):
    image = models.ImageField(upload_to="img")
    btn_text = models.CharField(max_length=50)
    card_text = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.btn_text}"

class Work(models.Model):
    image = models.ImageField(upload_to="workimg")
    work_text = models.CharField(max_length=50)
    working_text = models.CharField(max_length=100,default='lorem ispsun manjo man')

    def __str__(self):
        return f"{self.work_text}"

class ReWork(models.Model):
    image = models.ImageField(upload_to="workimg")
    head_text = models.CharField(max_length=50)
    card_text = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.head_text}"

class TeamMember(models.Model):
    image = models.ImageField(upload_to="teamimg")
    memb_name = models.CharField(max_length=50)
    memb_job = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.memb_name}"

class Pricing(models.Model):
    plan = models.CharField(max_length=50)
    plan_price = models.CharField(max_length=50000)
    plan_user = models.CharField(max_length=100)
    plan_space = models.CharField(max_length=100)
    plan_source = models.CharField(max_length=100)
    plan_support = models.CharField(max_length=50)
    customization = models.CharField(max_length=50,null=True,blank=True)
    is_main = models.BooleanField(null=True)

    def __str__(self):
        return f"{self.plan}"


class TransImage(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="transwork")
    image_large = models.ImageField(upload_to="transwork")

    def __str__(self):
        return f"{self.name}"

class UserEmail(models.Model):
    email = models.EmailField()

    def __str__(self):
        return f"{self.email}"