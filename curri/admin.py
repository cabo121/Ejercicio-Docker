from django.contrib import admin
from .models import curriculum,info

model = curriculum, info

admin.site.register(model)
