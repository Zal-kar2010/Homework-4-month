from django import forms
from users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from captcha.fields import CaptchaField

class LoginWithCaptchaForm(AuthenticationForm):
    captcha = CaptchaField()



GENDER = (
    ('М', 'М'),
    ('Ж', 'Ж')
)

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'age',
            'gender',
            'phone_number'
        )
        def save(self, commit=True):
            user = super(CustomRegisterForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            user.phone_number = self.cleaned_data['phone_number']
            if commit:
                user.save()
            return user