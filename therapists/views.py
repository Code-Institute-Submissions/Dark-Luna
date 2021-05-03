""" A views for Therapists App """
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from therapists.forms import TherapistForm
from .models import TherapistProfile


def index(request):
    """ A view to return team page """

    therapists = TherapistProfile.objects.all()

    context = {
        'therapists': therapists,
    }

    return render(request, 'therapists/therapists.html', context)


# Therapists Management
@staff_member_required
def therapists_admin(request):
    """ A view to manage therapists cards """

    therapists = TherapistProfile.objects.all()
    template = "therapists/admin-therapists.html"
    context = {
        'therapists': therapists,
    }

    return render(request, template, context)


@staff_member_required
def add_therapist_admin(request):
    """ Management view to add therapist card """

    if request.method == 'POST':
        form = TherapistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Therapist Profile card added successfully!')
            return redirect(reverse('therapists_admin'))
        else:
            messages.error(
                request, 'Adding new Therapist failed. \
                Please ensure the form is valid.')
    else:
        form = TherapistForm()

    template = "./admin/admin-forms.html"
    context = {
        'form': form,
    }

    return render(request, template, context)


@staff_member_required
def edit_therapist_admin(request, therapist_id):
    """ Management view to edit therapist card """

    therapist = get_object_or_404(TherapistProfile, pk=therapist_id)
    if request.method == 'POST':
        form = TherapistForm(
            request.POST, request.FILES, instance=therapist)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Therapist edited successfully!')
            return redirect(reverse('therapists_admin'))
        else:
            messages.error(
                request, 'Editing Therapist failed. \
                Please ensure the form is valid.')
    else:
        form = TherapistForm(instance=therapist)

    template = "./admin/admin-forms.html"
    context = {
        'form': form,
        'therapist': therapist,
    }

    return render(request, template, context)


@staff_member_required
def remove_therapist_admin(request, therapist_id):
    """ Management view to remove a therapist """

    therapist_profile = get_object_or_404(TherapistProfile,  pk=therapist_id)
    if therapist_profile.image:
        therapist_profile.image.delete()
        therapist_profile.delete()
    else:
        therapist_profile.delete()
    messages.success(request, 'Therapist removed successfully!')

    return redirect(reverse('therapists_admin'))
