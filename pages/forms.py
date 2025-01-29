# pages/forms.py
from django import forms
from django.core.validators import RegexValidator
from captcha.fields import ReCaptchaField


class ContactForm(forms.Form):
    """Form used for the public contact view at /contact/success"""
    first_name = forms.CharField(
        required=True,
        label="First Name",
        max_length=50,
        widget=forms.TextInput(attrs={
            "class": "first-name-input",
        })
    )

    last_name = forms.CharField(
        required=True,
        label="Last Name",
        max_length=50,
        widget=forms.TextInput(attrs={
            "class": "last-name-input",
        })
    )

    company = forms.CharField(
        label="Company",
        max_length=65,
        required=False,
        widget=forms.TextInput(attrs={
            "class": "company-input",
        })
    )

    phone_number = forms.CharField(
        label="Phone Number",
        max_length=12,
        required=False,
        help_text="Please use the xxx-xxx-xxxx format.",
        validators=[
             RegexValidator(r'\d{3}-\d{3}-\d{4}', "Please use xxx-xxx-xxxx format."),
        ],
        widget=forms.TextInput(attrs={
            "class": "phone-number-input",
        })
    )

    contact_email = forms.EmailField(
        label="Email Address",
        help_text="Please enter the email you would like me to reply to.",
        widget=forms.EmailInput(attrs={
            "class": "custom-input",
        })
    )

    subject = forms.CharField(
        required=True,
        max_length=75,
        widget=forms.TextInput(attrs={
            "class": "subject-input",
        })
    )

    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            "class": "textarea-input",
            "placeholder": "Write me here!",
            "rows": 5
        })
    )

    captcha = ReCaptchaField(label="Are you a robot?")
