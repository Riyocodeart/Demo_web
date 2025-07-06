from django.contrib import admin
from .models import categories,product,customer,order
# Register your models here.
admin.site.register(categories)
admin.site.register(product)
admin.site.register(customer)
admin.site.register(order)