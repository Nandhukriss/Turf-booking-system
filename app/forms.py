# bookings/forms.py
from django import forms
from .models import Booking
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        exclude=['booked']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'user': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'phonenumber': forms.TextInput(attrs={'placeholder': 'Your Phone Number'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
        }
    
 
# Overriding  the label
    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields['date'].label = False
        self.fields['phonenumber'].label = False
        self.fields['email'].label = False
        self.fields['user'].label = False
   