from django import forms
from service.models import Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ["name", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Your Name"}),
            "message": forms.Textarea(attrs={"class": "form-control", "placeholder": "Your Feedback"}),
        }
