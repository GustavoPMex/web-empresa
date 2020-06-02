from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.

def contact_view(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            name = request.POST.get('name',)
            email = request.POST.get('email',)
            coments = request.POST.get('coments',)

            email = EmailMessage(
                'Inouti. Nuevo mensaje',
                'De {} <{}> \n Escribió \n {}'.format(name,email,coments),
                'django.pruebasemailpruebas@gmail.com',
                ['django.pruebasemail@gmail.com'],
                reply_to=[email]
            )

            try:
                email.send()
                return redirect(reverse('contact:index')+'?ok')

            except:
                return redirect(reverse('contact:index')+'?fail')
                
    return render(request, 'contact/contact.html', {'form':contact_form})