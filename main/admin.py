from django.contrib import admin
from main.models import *
from account.models import *
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Recomment)
#admin.site.register(Image)