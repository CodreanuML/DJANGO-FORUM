from django.contrib import admin

# Register your models here.
from .models import Board,Topics,Posts
# Register your models here.
admin.site.register(Board)
admin.site.register(Topics)
admin.site.register(Posts)
