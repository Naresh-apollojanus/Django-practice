from django import forms

from .models import FoodItem, Cook, CookInfo


class AddFoodItem(forms.Form):
    name = forms.CharField(max_length=20)
    qty = forms.IntegerField()
    price = forms.IntegerField()
    discount = forms.IntegerField()


class ModelForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = '__all__'


class CookForm(forms.ModelForm):
    phone_nos = forms.CharField(max_length=20)
    pan_nos = forms.IntegerField()

    class Meta:
        model = Cook
        exclude = ('cook_info',)

    def save(self, commit=True):
        cook = super(CookForm, self).save()
        cook.cook_info = CookInfo.objects.create(phone_no=self.cleaned_data.get('phone_nos'),
                                                 pan_no=self.cleaned_data.get('pan_nos'))
        cook.save()
        return cook


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
