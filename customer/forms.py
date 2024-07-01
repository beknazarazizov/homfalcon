from django.forms import ModelForm

from customer.models import Customer


class CustomerModelForm(ModelForm):
    class Meta:
        model = Customer
        exclude = ()
