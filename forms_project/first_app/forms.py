from django import forms
from django.core import validators

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email =  forms.EmailField(label = 'Enter your mail agian:')
    text = forms.CharField(widget = forms.Textarea, validators = [validators.MinLengthValidator(5)])
    botcatcher = forms.CharField(required = False, widget = forms.HiddenInput)

    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError("There is a Bot!!!!")

    def clean(self):
        clean_all = super().clean()
        email = clean_all['email']
        vmail = clean_all['verify_email']

        if email != vmail:
            raise forms.ValidationError("Please make sure your email is matched!!")
