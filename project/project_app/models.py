from django.db import models
from django.utils import timezone

# Create your models here.

class Department(models.Model):
    dept_no = models.IntegerField()
    dept_name = models.CharField(max_length=50)
    dept_code = models.CharField(max_length=50)

    def __str__(self):
        return self.dept_code

class Regiest_Form(models.Model):
    std_num = models.CharField(primary_key=True, max_length=20)
    std_name = models.CharField(max_length=50)
    deptartment = models.ForeignKey(
        'Department', on_delete=models.SET_NULL, blank=True, null=True)
    year_fees = models.FloatField()
    register_fees = models.FloatField()
    std_year = models.CharField(max_length=50)
    std_sem = models.CharField(max_length=50)
    std_type_to_regiest = models.CharField(max_length=50)

    def __str__(self):
        return self.std_name


    def get_total_fees(self):
        return self.year_fees + self.register_fees



class Customer_Profile(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_password = models.CharField(max_length=50)
    customer_number = models.CharField(max_length=50)
    university_number = models.CharField(max_length=50)
    customer_blance = models.FloatField()
    university_blance = models.FloatField()

    def __str__(self):
        return self.customer_name

class Transaction(models.Model):
    customer = models.ForeignKey(
        'Customer_Profile', on_delete=models.SET_NULL, blank=True, null=True)
    transaction_date = models.DateTimeField(default=timezone.now)
    register = models.ForeignKey(
        'Regiest_Form', on_delete=models.SET_NULL, blank=True, null=True)
    sender_account_number = models.CharField(max_length=50)
    reciver_account_number = models.CharField(max_length=50)
    transaction_amount = models.FloatField()

    def __str__(self):
        return self.Customer_Profile.customer_name


    def get_total(self):
        total = 0
        transaction_amount = 0
        # total = self.Regiest_Form.register_fees + self.Regiest_Form.year_fees
        total = get_total_fees()
        transaction_amount = total
        return transaction_amount
