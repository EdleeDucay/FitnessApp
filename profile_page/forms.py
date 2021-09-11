from django import forms

# creating a form
class EditProfileForm(forms.Form):
    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    weight = forms.CharField(max_length = 200)
    age = forms.CharField(max_length = 200)
    height = forms.CharField(max_length = 200)