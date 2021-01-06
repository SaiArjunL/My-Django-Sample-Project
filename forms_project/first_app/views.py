from django.shortcuts import render
from . import forms
# Create your views here.

def index(req):
    return render(req, 'first_app/index.html')

def form_view(req):
    form = forms.FormName()
    if req.method == 'POST':
        form = forms.FormName(req.POST)

        if form.is_valid():
            print("Validation Successful!!!!")
            print("Name: " + form.cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print("Text: " + form.cleaned_data['text'])

    return render(req, 'first_app/form_page.html', {'form': form})
