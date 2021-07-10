from django import forms


class ContactForm(forms.Form):
    nome = forms.CharField(label='Seu nome', widget=forms.TextInput(
        attrs={'placeholder': 'Digite o nome'}))
    from_email = forms.EmailField(label='Seu email', widget=forms.TextInput(
        attrs={'placeholder': 'Digite o email'}))
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea(
        attrs={'placeholder': 'Digite o assunto'}))
