from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit
from crispy_forms.bootstrap import FormActions
from django.contrib.auth import authenticate
from django import forms


class AuthenticationForm(forms.Form):
    username = forms.CharField(
            label='Email',
            max_length=64,
            required=True)
    password = forms.CharField(
            label='Password',
            max_length=20,
            strip=False,
            widget=forms.PasswordInput,
            required=True)

    error_messages = {
        'invalid_login': 'That combination of email and password is invalid.'
    }

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login')

        return self.cleaned_data


    def get_user(self):
        return self.user_cache

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'login'
        self.helper.form_method = 'post'
        # user interface improvements
        self.helper.template_pack = 'bootstrap3'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-10'

        layout = Layout(
            Div('username', 'password'),
            FormActions(
                Submit('login', 'Sign-in'),
            )
        )
        self.helper.add_layout(layout)

