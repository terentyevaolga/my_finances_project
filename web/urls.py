from django.urls import path

from web.views import main_view, registration_view, auth_view, logout_view, money_slot_edit_view, tags_view, \
    tags_delete_view, money_slot_delete_view, analytics_view, import_view

urlpatterns = [
    path('', main_view, name='main'),
    path('import/', import_view, name='import'),
    path('analytics/', analytics_view, name='analytics'),
    path('registration/', registration_view, name='registration'),
    path('auth/', auth_view, name='auth'),
    path('logout/', logout_view, name='logout'),
    path('money_slots/add/', money_slot_edit_view, name='money_slots_add'),
    path('money_slots/<int:id>/', money_slot_edit_view, name='money_slots_edit'),
    path('money_slots/<int:id>/delete', money_slot_delete_view, name='money_slot_delete'),
    path('tags/', tags_view, name='tags'),
    path('tags/<int:id>/delete', tags_delete_view, name='tags_delete'),
]



