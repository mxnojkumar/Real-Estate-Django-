from django import forms
from . models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = [
            "title", 
            "price", 
            "num_of_bedrooms", 
            "num_of_bathrooms", 
            "size_of_property", 
            "address",
            "image",
        ]