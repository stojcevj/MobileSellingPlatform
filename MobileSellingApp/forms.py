from django import forms
from MobileSellingApp.models import Profile, MobileListing, Order


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Profile
        exclude = ('profile_user',)


class MobileListingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MobileListingForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = MobileListing
        exclude = ('listing_profile',)


class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Order
        exclude = ('order_profile','order_listing')
