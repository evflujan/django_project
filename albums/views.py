from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import UploadImageForm

@login_required
def upload_image_view(request):
    user = request.user
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message = 'Image uploaded succesfully!'
    else:
        form = UploadImageForm()

    template_name = 'albums/upload.html'
    return render(request, template_name, locals())


def home_view(request):
    user = request.user
    return render(request, 'albums_base.html', locals())
