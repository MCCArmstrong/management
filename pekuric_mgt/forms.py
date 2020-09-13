from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from .models import caviet, CustomerPurchaseForm


class UnicornForm(forms.ModelForm):
    class Meta:
        model = caviet
        fields = ('sliders', 'description', 'preview')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Changes'))


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = CustomerPurchaseForm
        fields = ('full_name', 'email', 'phone_number', 'amount', 'address')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.add_input(Submit('submit', 'Make Payment'))


class About(forms.ModelForm):
    class Meta:
        fields = ('file', 'about', 'history')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.fields['history'].widget.attrs['rows'] = 2
        # self.fields['history'].widget.attrs['columns'] = 2
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Changes'))


class ServiceForm(forms.ModelForm):
    class Meta:
        fields = ('service_title', 'service_icon', 'service_description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Changes'))


class PortFolio(forms.ModelForm):
    class Meta:
        fields = ('portflio_file', 'product_description', 'product_price')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Changes'))
