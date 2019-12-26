from django.contrib import admin
from .models import Regiest_Form ,Department ,Customer_Profile ,Transaction
# Register your models here.

admin.site.site_header = 'University of Science and Technology'

admin.site.register(Regiest_Form)
admin.site.register(Department)
admin.site.register(Customer_Profile)
admin.site.register(Transaction)
