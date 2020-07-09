from django.urls import path
from . import views

urlpatterns = [
    path('', views.CategoriesList.as_view()),
    path('add/', views.AddCategories.as_view(),name='add'),
    path('save/', views.SaveCategories.as_view(),name='save'),
    path('update/<int:id>', views.UpdateCategories.as_view(),name='update'),
    path('delete/<int:id>', views.DeleteCategories.as_view(),name='delete'),

    path('<int:id>/activity', views.Lits_Activity.as_view(), name='activity'),
    path('<int:id>/add_activity', views.AddActivity.as_view(), name='add_activity'),
    path('<int:id>/save_activity', views.SaveActivity.as_view(), name='save_activity'),
    path('<int:id>/activity/<int:activity_id>/edit', views.EditActivity.as_view(), name='edit_activity'),
    path('<int:id>/activity/<int:activity_id>/delete', views.DeleteActivity.as_view(), name='delete_activity'),
]
