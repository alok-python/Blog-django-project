from django.contrib import admin
from .models import Categories, Contact,Post

# Register your models here.


admin.site.register(Categories),
admin.site.register(Post)
admin.site.register(Contact)