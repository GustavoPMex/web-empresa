from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Nombre completo'}
    ), min_length=3, max_length=100)
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Email válido'}
    ))
    coments = forms.CharField(label='Dudas o comentarios', required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'row':10}
    ), min_length=10)
