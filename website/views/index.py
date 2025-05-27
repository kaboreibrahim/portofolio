from django.contrib import messages
from django.core.mail import send_mail,EmailMessage
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import EmailMessage, get_connection
from django.template.loader import render_to_string
from website.forms import ContactForm
from django.templatetags.static import static
from django.utils.translation import gettext as _
#view accueil
def index(request):
    form=ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['contactName']
            email = form.cleaned_data['contactEmail']
            number = form.cleaned_data['contactNumber']
            subject = form.cleaned_data['contactSubject']
            message = form.cleaned_data['contactMessage']
            
            # Contexte commun pour les deux emails
            email_context = {
                'email': email,
                'message': message,
                'phone': number,
                'subject': subject,
                'name': name,
            }
            
            try:
                connection = get_connection()
                connection.open()
                
                # Email de notification pour l'administrateur
                admin_email_subject = _("Réception de mail d'un visiteur pour une demande de contact")
                admin_email_body_html = render_to_string('email/contact_email.html', email_context)
                
                admin_email = EmailMessage(
                    admin_email_subject,
                    admin_email_body_html,
                    settings.DEFAULT_FROM_EMAIL,  # Utilisez votre email configuré dans settings
                    ['ibrahimkabore025@gmail.com'],
                    connection=connection,
                )
                admin_email.content_subtype = 'html'
                admin_email.send(fail_silently=False)
                
                # Email de confirmation pour le visiteur
                user_email_subject = _("Confirmation de réception de votre message")
                user_email_body_html = render_to_string('email/contact_email_confirmation.html', email_context)
                
                user_email = EmailMessage(
                    user_email_subject,
                    user_email_body_html,
                    settings.DEFAULT_FROM_EMAIL,  # Utilisez votre email configuré dans settings
                    [email],  # Email du visiteur
                    connection=connection,
                )
                user_email.content_subtype = 'html'
                user_email.send(fail_silently=False)
                
                messages.success(request, _("Merci pour votre message. Nous vous contacterons bientôt."))
            except Exception as e:
                messages.error(request, _("Une erreur est survenue lors de l'envoi du message : {e}"))
            finally:
                connection.close()
                
            return redirect('accueil')

    return render(request, 'base.html', {'form': form})