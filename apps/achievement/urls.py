from django.urls import path
from apps.achievement import views
urlpatterns = [
    path('<int:id>', views.ListAchievement.as_view())
]
