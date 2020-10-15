from django import forms
from .models import *
from django.forms import formset_factory


class CustomerMessageForm(forms.ModelForm):
	class Meta:
		model = CustomerMessage
		fields = '__all__'
		widgets = {
            # Basic Information
            'full_name': forms.TextInput(attrs={
                'class': "validate"
            }),
            'contact_no': forms.TextInput(attrs={
                'class': "validate"
            }),
            'message': forms.Textarea(attrs={
                'class': "materialize-textarea",
                # 'placeholder': 'Enter your message'
            }),
            'email': forms.EmailInput(attrs={
                'class': "validate"
            }),
            'gallery': forms.Select(attrs={
            	'onchange': 'changeFunction()'
        	}),
        }


class MessageSpecificationForm(forms.Form):
	value = forms.CharField(widget=forms.TextInput(attrs={
		'class': 'validate',
		'placeholder': 'Enter Value'
		}))
	specification = forms.CharField(widget=forms.TextInput(attrs={
		'class': 'validate',
		'placeholder': 'Enter spec'
		}))

MessageSpecificationFormSet = formset_factory(
    form=MessageSpecificationForm,
    max_num=10,
    extra=1,
)