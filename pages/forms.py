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
    )

    last_name = forms.CharField(
        required=True,
        label="Last Name",
        max_length=50,
    )

    company = forms.CharField(
        label="Company",
        max_length=65,
        required=False,
    )

    phone_number = forms.CharField(
        label="Phone Number",
        max_length=12,
        required=False,
        help_text="Please use the xxx-xxx-xxxx format.",
        validators=[
             RegexValidator(r'\d{3}-\d{3}-\d{4}', "Please enter a valid phone number in the xxx-xxx-xxxx format."),
        ],
    )

    contact_email = forms.EmailField(
        label="Email Address",
        help_text="Please enter the email you would like me to reply to.",
        validators=[
            RegexValidator(r'^(\w|\.)+@(\w+\.)?\w+\.\w{1,3}$', "Please enter a valid email address.")
        ],
    )

    subject = forms.CharField(required=True, max_length=75)

    message = forms.CharField(widget=forms.Textarea, required=True)

    captcha = ReCaptchaField(label="Are you a robot?")
