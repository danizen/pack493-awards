from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit
from crispy_forms.bootstrap import FormActions
from django import forms


class AuthenticationForm(forms.Form):
    username = forms.CharField(label='Email', max_length=64, required=True)
    password = forms.CharField(label='Password', max_length=20, widget=forms.PasswordInput, required=True)

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