""" Views Workshops App """
import random
from django.db.models.aggregates import Count
from django.db.models import Q
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.db.models.functions import Lower
from .models import Category, Workshop
from .forms import CategoriesForm, WorkshopsForm


def workshops(request):
    """ A view to return lessons in selected category """

    workshops = Workshop.objects.all()
    all_workshops = Workshop.objects.all()
    categories = Category.objects.all()

    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                workshops = workshops.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            workshops = workshops.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            workshops = workshops.filter(category__name__in=categories)
            categories = Category.objects.all()

        if 'q' in request.GET:
            query = request.GET['q']
            if query != "":
                queries = Q(name__icontains=query) | Q(
                    description__icontains=query) | Q(
                    category__name__icontains=query)
                workshops = workshops.filter(queries)
            else:
                messages.error(
                    request, "Please enter a search criteria.")
                return redirect(request.path)

    current_sorting = f'{sort}_{direction}'

    # Get number of workshops in each category
    categories_list = Category.objects.annotate(Count('workshop'))

    context = {
        'workshops': workshops,
        'categories': categories,
        'categories_list': categories_list,
        'all_workshops': all_workshops,
        'current_sorting': current_sorting,
        'query_text': query,
    }

    return render(request, 'workshops/workshops.html', context)


def workshop(request, workshop_id):
    """ A view to return workshop details """

    all_workshops = list(Workshop.objects.all())
    selected_workshop = get_object_or_404(Workshop, pk=workshop_id)

    if Workshop.objects.count() < 4:
        context = {
            'workshop': selected_workshop,
            'random_workshops': Workshop.objects.count(),
        }
    else:
        random_workshops = random.sample(all_workshops, 4)
        context = {
            'workshop': selected_workshop,
            'workshops': random_workshops,
            'random_workshops': Workshop.objects.count(),
        }
    print(Workshop.objects.count())

    return render(request, 'workshops/workshop.html', context)


# Categories admin
@staff_member_required
def categories_admin(request):
    """ A view to manage workshop categories """

    categories = Category.objects.all()

    template = "workshops/admin-categories.html"
    context = {
        'categories': categories,
    }

    return render(request, template, context)


@staff_member_required
def add_categories_admin(request):
    """ Admin view to add workshop category """

    if request.method == 'POST':
        form = CategoriesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully!')
            return redirect(reverse('categories_admin'))
        else:
            messages.error(
                request, 'Adding new category failed. Please ensure the form is valid.')
    else:
        form = CategoriesForm()

    template = "./admin/admin-forms.html"
    context = {
        'form': form,
    }

    return render(request, template, context)


@staff_member_required
def edit_categories_admin(request, category_id):
    """ Admin view to edit workshop category """

    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        form = CategoriesForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Category edited successfully!')
            return redirect(reverse('categories_admin'))
        else:
            messages.error(
                request, 'Editing category failed. \
                Please ensure the form is valid.')
    else:
        form = CategoriesForm(instance=category)

    template = "./admin/admin-forms.html"
    context = {
        'form': form,
        'category': category,
    }

    return render(request, template, context)


@staff_member_required
def remove_categories_admin(request, category_id):
    """ Admin view to remove workshop category """

    category = get_object_or_404(Category, pk=category_id)
    category.delete()
    messages.success(request, 'Category removed successfully!')

    return redirect(reverse('categories_admin'))


# Workshops Admin
@staff_member_required
def workshops_admin(request):
    """ A view to manage workshops """

    all_workshops = Workshop.objects.all()

    template = "workshops/admin-workshops.html"
    context = {
        'all_workshops': all_workshops,
    }

    return render(request, template, context)


@staff_member_required
def add_workshops_admin(request):
    """ Management view to add workshops """

    if request.method == 'POST':
        form = WorkshopsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Workshop added successfully!')
            return redirect(reverse('workshops_admin'))
        else:
            messages.error(
                request, 'Adding new workshop failed. Please ensure the form is valid.')
    else:
        form = WorkshopsForm()

    template = "./admin/admin-forms.html"
    context = {
        'form': form,
    }

    return render(request, template, context)


@staff_member_required
def edit_workshops_admin(request, workshop_id):
    """ Admin view to edit workshops """

    edit_workshop = get_object_or_404(Workshop, pk=workshop_id)
    if request.method == 'POST':
        form = WorkshopsForm(request.POST, request.FILES,
                             instance=edit_workshop)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Workshop edited successfully!')
            return redirect(reverse('workshops_admin'))
        else:
            messages.error(
                request, 'Editing workshop failed. \
                Please ensure the form is valid.')
    else:
        form = WorkshopsForm(instance=edit_workshop)

    template = "./admin/admin-forms.html"
    context = {
        'form': form,
        'edit_workshop': edit_workshop,
    }

    return render(request, template, context)


@staff_member_required
def remove_workshops_admin(request, workshop_id):
    """ Admin view to remove workshops """

    removed_workshop = get_object_or_404(Workshop, pk=workshop_id)
    if removed_workshop.image:
        removed_workshop.image.delete()
        removed_workshop.delete()
    else:
        removed_workshop.delete()
    messages.success(request, 'Workshop removed successfully!')

    return redirect(reverse('workshops_admin'))
