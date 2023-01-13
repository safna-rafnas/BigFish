from django.contrib import admin

# Register your models here.
from .models import admins_db,products_db,recipie_db,category_db
admin.site.register(admins_db)
admin.site.register(products_db)
admin.site.register(recipie_db)
admin.site.register(category_db)
