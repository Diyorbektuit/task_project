from django import forms
from .models import Client, Product, SalesManager, ServiceDepartment, Driver, InstallationTeam, Order, OrderItem

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control form-control-lg'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control form-control-lg'

class SalesManagerForm(forms.ModelForm):
    class Meta:
        model = SalesManager
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SalesManagerForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control form-control-lg'


class ServiceDepartmentForm(forms.ModelForm):
    class Meta:
        model = ServiceDepartment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ServiceDepartmentForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control form-control-lg'


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DriverForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control form-control-lg'

class InstallationTeamForm(forms.ModelForm):
    class Meta:
        model = InstallationTeam
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(InstallationTeamForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control form-control-lg'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control form-control-lg'


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(OrderItemForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control form-control-lg'
