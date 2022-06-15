from django.contrib import admin
from . models import InputImage,OutputImage,TestImage,TestOutput

# Register your models here.
admin.site.register(InputImage)
admin.site.register(OutputImage)
admin.site.register(TestImage)
admin.site.register(TestOutput)