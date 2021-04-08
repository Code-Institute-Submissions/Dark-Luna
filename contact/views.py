""" Contact App Views """
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.template.loader import render_to_string
# from profiles.models import UserProfile
from .forms import ContactForm


def index(request):
    """ View to render contact page with contact form """

    # if request.method == 'GET':
    #     if request.user.is_authenticated:
    #         try:
    #             profile = UserProfile.objects.get(user=request.user)
    #             contact_form = ContactForm(initial={
    #                 'name': profile.full_name,
    #                 'from_email': profile.email_address,
    #                 }
    #             )
    #         except UserProfile.DoesNotExist:
    #             contact_form = ContactForm()
    #     else:
    #         contact_form = ContactForm()
    # else:
    #     contact_form = ContactForm(request.POST)
    #     if contact_form.is_valid():
    #         name = contact_form.cleaned_data['name']
    #         from_email = contact_form.cleaned_data['from_email']
    #         subject = contact_form.cleaned_data['subject']
    #         message = contact_form.cleaned_data['message']
    #         html_msg = render_to_string(
    #             'emails/email.html', {'name': name, 'subject': subject, 'message': message})
    #         try:
    #             send_mail(subject, message, settings.EMAIL_HOST_USER, [
    #                       from_email, settings.EMAIL_HOST_USER],
    #                       html_message=html_msg, fail_silently=False)

    #         except BadHeaderError:
    #             return HttpResponse('Invalid header found.')
    #         return redirect('/contact',
    #                         messages.success(request, 'Dear '
    #                                          + name.title() + ', thanks for reaching out! \
    #                                 We will answer in lightning speed.'))

    return render(request, "contact/contact.html")
