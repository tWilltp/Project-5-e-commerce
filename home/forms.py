from django import forms
from django.forms import ModelForm
from .models import Membership


class MembershipForm(ModelForm):
    class Meta:
        model = Membership
        fields = ['full_name', 'email',
                  'phone_number', 'subscription']

    # def init(self, *args, *kwargs):

    #     super().__init__(*args, *kwargs)
    #     placeholders = {
    #         'full_name': 'Full Name',
    #         'email': 'Email',
    #         'phone_number': 'Phone Number',
    #         'payment_option': 'subscription',
    #     }

    # self.fields['full_name'].widget.attrs['autofocus'] = True
    # for field in self.fields:
    #     if self.fields[field].required:
    #         placeholder = f'{placeholders[fields]} *'
    #     else:
    #         placeholder = placeholders[field]
    #     self.fields[field].widget.attrs['placeholder'] = placeholder
    #     self.fields[field].widget.attrs['class'] = 'stripe-style-input'
    #     self.fields[field].label = False
