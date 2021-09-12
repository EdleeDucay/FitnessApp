from django import forms

class EditProfileForm(forms.Form):
    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    weight = forms.IntegerField(help_text = "lbs", min_value = 0)
    age = forms.IntegerField(min_value = 0)
    height = forms.IntegerField(help_text = "cm", min_value = 0)