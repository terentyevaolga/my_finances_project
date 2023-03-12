from django.urls import path

from web.views import main_view, registration_view, auth_view, logout_view, money_slot_edit_view

urlpatterns = [
    path('', main_view, name='main'),
    path('registration/', registration_view, name='registration'),
    path('auth/', auth_view, name='auth'),
    path('logout/', logout_view, name='logout'),
    path('money_slots/add/', money_slot_edit_view, name='money_slots_add'),
    path('money_slots/<int:id>/', money_slot_edit_view, name='money_slots_edit'),
]


