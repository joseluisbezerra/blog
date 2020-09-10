from django.shortcuts import render
from django.core.mail import send_mail

from .forms import ContactForm

def contact(request):
    send = False
    form = ContactForm(request.POST or None)
    
    if form.is_valid():
        # Enviar email
        nome = request.POST.get('nome', '')
        from_email = request.POST.get('from_email', '')
        mensagem = request.POST.get('mensagem', '')

        

        try:
            send_mail(
                f'{nome} - Mensagem do blog',
                'De {} <{}>\nEscreveu:\n{}'.format(nome, from_email, mensagem),
                from_email,
                ['luisbezerra.work@gmail.com'],
            )
            send = True
        except:
            send = False

    
    context = {
        'form': form,
        'success': send,
    }

    return render(request, 'contact/contact.html', context)