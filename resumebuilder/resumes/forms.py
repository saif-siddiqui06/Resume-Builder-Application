from django import forms

class ResumeForm(forms.Form):
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First Name',
            'style': 'width: 100%; padding: 12px; margin-bottom: 15px; border-radius: 5px; border: 1px solid #ccc; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);'
        })
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last Name',
            'style': 'width: 100%; padding: 12px; margin-bottom: 15px; border-radius: 5px; border: 1px solid #ccc; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email Address',
            'style': 'width: 100%; padding: 12px; margin-bottom: 15px; border-radius: 5px; border: 1px solid #ccc; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);'
        })
    )
    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Phone Number',
            'style': 'width: 100%; padding: 12px; margin-bottom: 15px; border-radius: 5px; border: 1px solid #ccc; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);'
        })
    )
    linkedin = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'LinkedIn Profile',
            'style': 'width: 100%; padding: 12px; margin-bottom: 15px; border-radius: 5px; border: 1px solid #ccc; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);'
        })
    )
    objective = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Professional Summary',
            'style': 'width: 100%; padding: 12px; margin-bottom: 15px; border-radius: 5px; border: 1px solid #ccc; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); height: 120px;'
        })
    )
    skills = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Skills',
            'style': 'width: 100%; padding: 12px; margin-bottom: 15px; border-radius: 5px; border: 1px solid #ccc; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); height: 120px;'
        })
    )
    experience = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Experience',
            'style': 'width: 100%; padding: 12px; margin-bottom: 15px; border-radius: 5px; border: 1px solid #ccc; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); height: 120px;'
        })
    )
    education = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Education',
            'style': 'width: 100%; padding: 12px; margin-bottom: 15px; border-radius: 5px; border: 1px solid #ccc; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); height: 120px;'
        })
    )
