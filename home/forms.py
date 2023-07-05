from django import forms
from .models import Membership


class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ('full_name', 'email',
                  'phone_number', 'payment_option')
