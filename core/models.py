from django.db import models
import uuid
# Create your models here.
def profile_image_upload(instance, filename, imagetype):
    extention = filename.split(".")[-1]
    return "images/profile/%s/%s.%s" % (instance.staff_id, uuid.uuid4(), extention)

def idcard_image_upload(instance, filename, imagetype):
    extention = filename.split(".")[-1]
    return "images/idcard/%s/%s.%s" % (instance.staff_id, uuid.uuid4(), extention)
    
class Staff (models.Model):
    MALE = 'M'
    FEMALE = "F"
    EXCELLENT = 5
    GOOD = 4
    AVERAGE = 3
    UNDER = 2
    BAD = 1

    EMPLOYEE_GENDER_CHOICE = [
        (MALE, 'Male'),
        (FEMALE, 'Female')
    ]

    EMPLOYEE_SKILL_RATING = [
        (EXCELLENT , 'Excellent'),
        (GOOD , 'Good'),
        (AVERAGE , 'Average'),
        (UNDER , 'Under'),
        (BAD , 'Bad')
    ]
    
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length= 100)
    employee_code = models.CharField( max_length=10, primary_key=True, blank=True)
    phone_number = models.CharField(max_length=10, unique=True);
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=250)
    gender = models.CharField(max_length=1, choices=EMPLOYEE_GENDER_CHOICE)
    current_address = models.TextField()
    permanent_address = models.TextField()
    height = models.IntegerField()
    idcard_number = models.CharField(max_length=15)
    license_date = models.DateField()
    license_place = models.CharField(max_length=250)
    bank = models.CharField(max_length=20,blank=True)
    account_name = models.CharField(max_length=20, blank=True)
    account_number = models.CharField(max_length=20, blank=True)
    english_skill = models.IntegerField(choices=EMPLOYEE_SKILL_RATING)
    sp_experiance = models.JSONField()
    priority_area = models.CharField(max_length=100, null= False, blank=True)
    


class Store(models.Model):

class Store_Employee_Detail(models.Model):

class Province(models.Model):

class District(models.Model):

class Ward(models.Model):

class Employee_Review(models.Model):

class Employee_Training(models.Model):

