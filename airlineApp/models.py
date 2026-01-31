from django.db import models

# Create your models here.



class UserLogin(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    utype = models.CharField(max_length=50)


class employee_details(models.Model):
    employee_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    aadhar_no = models.CharField(max_length=200)
    email_id = models.CharField(max_length=200)
    date_join = models.CharField(max_length=200)
    work_type = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=200)


class shop_details(models.Model):
    shop_id = models.CharField(max_length=200)
    shop_type = models.CharField(max_length=200)
    owner_name = models.CharField(max_length=200)
    details = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=200)


class complaints(models.Model):
    complant_id = models.CharField(max_length=200)
    give_by = models.CharField(max_length=200)
    details = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    status = models.CharField(max_length=200)


class servicedetails(models.Model):
    service_id = models.CharField(max_length=200)
    service_type = models.CharField(max_length=200)
    details = models.CharField(max_length=200)
    cost = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=200)


class incharge_details(models.Model):
    work_type = models.CharField(max_length=200)
    incharge_name = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=200)
    form_date = models.CharField(max_length=200)
    till_date = models.CharField(max_length=200)
    timing = models.CharField(max_length=200)


class Food_store(models.Model):
    store_name = models.CharField(max_length=200)
    food_type = models.CharField(max_length=200)
    timing = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=200)
    rating = models.CharField(max_length=200)


class Register(models.Model):
    username = models.CharField(max_length=200)
    email_id = models.CharField(max_length=200)
    city_type = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    moblie_no = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
