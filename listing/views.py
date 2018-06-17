from django.shortcuts import render, get_object_or_404
from .models import Listing, Vendor

def detail(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    return render(request, 'listing/detail.html', {'listing': listing})
