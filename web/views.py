from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import render, redirect

from web.forms import RegistrationForm, AuthForm, MoneySlotForm, MoneySlotTagForm
from web.models import MoneySlot, MoneySlotTag

User = get_user_model()


def main_view(request):
    moneyslots = MoneySlot.objects.all()
    return render(request, 'web/main.html', {
        'moneyslots': moneyslots
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
            print(form.cleaned_data)
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


def money_slot_edit_view(request, id=None):
    moneyslot = MoneySlot.objects.get(id=id) if id is not None else None
    form = MoneySlotForm(instance=moneyslot)
    if request.method == 'POST':
        form = MoneySlotForm(data=request.POST, files=request.FILES, instance=moneyslot, initial={'user': request.user})
        if form.is_valid():
            form.save()
            return redirect('main')
    return render(request, 'web/money_slot_form.html', {'form': form})


def _list_editor_view(request, model_cls, form_cls, template_name, url_name):
    items = model_cls.objects.all()
    form = form_cls
    if request.method == 'POST':
        form = form_cls(data=request.POST, initial={'user': request.user})
        if form.is_valid():
            form.save()
            return redirect(url_name)
    return render(request, f'web/{template_name}.html', {'items': items, 'form': form})


def tags_view(request):
    return _list_editor_view(request, MoneySlotTag, MoneySlotTagForm, 'tags', 'tags')


def tags_delete_view(request, id):
    tag = MoneySlotTag.objects.get(id=id)
    tag.delete()
    return redirect('tags')

