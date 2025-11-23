from django import forms
from .models import Notification

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['type', 'email', 'mobile', 'subject', 'body']
        widgets = {
            'type': forms.HiddenInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        mode = cleaned_data.get('type')
        email = cleaned_data.get('email')
        mobile = cleaned_data.get('mobile')

        if mode == "Email":
            if not email or not email.endswith('@gmail.com'):
                self.add_error('email', 'Email must end with @gmail.com only.')
        if mode == "SMS":
            if not mobile or len(mobile) != 10 or not mobile.isdigit():
                self.add_error('mobile', 'Mobile number must be exactly 10 digits.')
