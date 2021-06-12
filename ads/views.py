from ads.models import Ad
from ads.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView


class AdListView(OwnerListView):
    model = Ad
    fields = ['title', 'text', 'price']
    # By convention:
    # template_name = "ads/ad_list.html"


class AdDetailView(OwnerDetailView):
    model = Ad
    template_name = 'ads/ad_detail.html'
    fields = ['title', 'text', 'price']

class AdCreateView(OwnerCreateView):
    model = Ad
    fields = ['title', 'text', 'price']


class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'text', 'price']


class AdDeleteView(OwnerDeleteView):
    model = Ad
