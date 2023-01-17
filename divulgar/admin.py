from django.contrib import admin
from .models import Raca
from .models import Tag,Pet

admin.site.register(Raca)
admin.site.register(Tag)
admin.site.register(Pet)

# Register your models here.
