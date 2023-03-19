from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from web.forms import RegistrationForm, AuthForm, MoneySlotForm, MoneySlotTagForm, MoneySlotFilterForm
from web.models import MoneySlot, MoneySlotTag

User = get_user_model()


@login_required
def main_view(request):
    moneyslots = MoneySlot.objects.filter(user=request.user)

    filter_form = MoneySlotFilterForm(request.GET)
    filter_form.is_valid()
    filters = filter_form.cleaned_data

    if filters['search']:
        moneyslots = moneyslots.filter(title__icontains=filters['search'])

    total_count = moneyslots.count()
    page_number = request.GET.get('page', 1)
    paginator = Paginator(moneyslots, per_page=2)

    return render(request, 'web/main.html', {
        'moneyslots': paginator.get_page(page_number),
        'form': MoneySlotForm(),
        'filter_form': filter_form,
        'total_count': total_count
    })


def registration_view(request):
    form = RegistrationForm()
    is_success = False
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email']
            )
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('main')
    return render(request, 'web/registration.html', {
        'form': form, 'is_success': is_success
    })


def auth_view(request):
    form = AuthForm()
    if request.method == 'POST':
        form = AuthForm(data=request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is None:
                form.add_error(None, 'Введены неверные данные! Повторите попытку')
            else:
               login(request, user)
               return redirect('main')
    return render(request, 'web/auth.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('main')


@login_required
def money_slot_edit_view(request, id=None):
    moneyslot = get_object_or_404(MoneySlot, user=request.user, id=id) if id is not None else None
    form = MoneySlotForm(instance=moneyslot)
    if request.method == 'POST':
        form = MoneySlotForm(data=request.POST, files=request.FILES, instance=moneyslot, initial={'user': request.user})
        if form.is_valid():
            form.save()
            return redirect('main')
    return render(request, 'web/money_slot_form.html', {'form': form})


@login_required
def money_slot_delete_view(request, id):
    # не факт что здесь надо user=request.user
    tag = get_object_or_404(MoneySlot, user=request.user, id=id)
    tag.delete()
    return redirect('main')


def _list_editor_view(request, model_cls, form_cls, template_name, url_name):
    items = model_cls.objects.filter(user=request.user)
    form = form_cls
    if request.method == 'POST':
        form = form_cls(data=request.POST, initial={'user': request.user})
        if form.is_valid():
            form.save()
            return redirect(url_name)
    return render(request, f'web/{template_name}.html', {'items': items, 'form': form})


@login_required
def tags_view(request):
    return _list_editor_view(request, MoneySlotTag, MoneySlotTagForm, 'tags', 'tags')


@login_required
def tags_delete_view(request, id):
    tag = get_object_or_404(MoneySlotTag, user=request.user, id=id)
    tag.delete()
    return redirect('tags')

