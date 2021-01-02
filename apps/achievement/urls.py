from django.urls import path
from apps.achievement import views
urlpatterns = [
    path('list', views.ListAchievement.as_view()),
    path('list/<int:id>/edit', views.EditReport.as_view(),name = 'list_edit'),
    path('list/<int:id>/update', views.Update_Achievement.as_view(),name = 'list_update'),
    path('list/<int:id>/delete', views.Delete_Achievement.as_view(),name = 'delete'),
    # path('achievement_api', views.achievementapi.as_view()), #api
    # path('target_api', views.targetapi.as_view()), #api
]
