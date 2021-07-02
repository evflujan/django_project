from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.files.uploadedfile import InMemoryUploadedFile

from myarts.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

from imgs.models import Img
from imgs.forms import CreateForm


class ImgListView(OwnerListView):
    model = Img
    template_name = "imgs/list.html"


class ImgDetailView(OwnerDetailView):
    model = Img
    template_name = "imgs/detail.html"


class ImgCreateView(LoginRequiredMixin, View):
    template_name = 'imgs/form.html'
    success_url = reverse_lazy('imgs:all')

    def get(self, request, pk=None):
        form = CreateForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        form = CreateForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        # Add owner to the model before saving
        img = form.save(commit=False)
        img.owner = self.request.user
        img.save()
        return redirect(self.success_url)


class ImgUpdateView(LoginRequiredMixin, View):
    template_name = 'imgs/form.html'
    success_url = reverse_lazy('imgs:all')

    def get(self, request, pk):
        img = get_object_or_404(Img, id=pk, owner=self.request.user)
        form = CreateForm(instance=img)
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        img = get_object_or_404(Img, id=pk, owner=self.request.user)
        form = CreateForm(request.POST, request.FILES or None, instance=img)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        img = form.save(commit=False)
        img.save()

        return redirect(self.success_url)


class ImgDeleteView(OwnerDeleteView):
    model = Img
    template_name = "imgs/delete.html"


def stream_file(request, pk):
    img = get_object_or_404(Img, id=pk)
    response = HttpResponse()
    response['Content-Type'] = img.content_type
    response['Content-Length'] = len(img.picture)
    response.write(img.picture)
    return response
