import os
import smtplib
import email.message as mail

from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    subject = forms.CharField(label='Assunto', max_length=120)
    message = forms.CharField(label='Mensagem', widget=forms.Textarea)

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        msg = mail.Message()
        msg['Subject'] = "Email de contato enviado do portfolio"
        msg['From'] = os.environ.get('EMAIL_USER')
        msg['To'] = os.environ.get('EMAIL_USER')
        password = os.getenv('EMAIL_PASSWORD')
        msg.add_header('Content-Type', 'text/plain')
        content = f'Nome: {name}\nE-mail: {email}\nAssunto: {subject}\nMessage: {message}'
        msg.set_payload(content)

        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login(msg['From'], str(password))
        smtp.sendmail(msg['From'], [msg['To']], msg.as_string().encode("UTF-8"))