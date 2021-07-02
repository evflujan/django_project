from django.contrib import admin
from imgs.models import Img

# We want the admin UI to leave the picture and content_type alone

# Define the ImtAdmin class
class ImgAdmin(admin.ModelAdmin):
    exclude = ('picture', 'content_type')


# Register the admin class with the associated model
admin.site.register(Img, ImgAdmin)
