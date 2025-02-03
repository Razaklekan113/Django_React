from django.urls import path
from .views import CreateUserView, NoteListCreate, NoteDelete, NoteUpdate
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="get_token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh"),

    path("note_list/", NoteListCreate.as_view(), name="note-list"),
    path("note_create/", NoteListCreate.as_view(), name="note-create"),
    path("note/<int:pk>/", NoteDelete.as_view(), name="delete_note"),
    path("note/<int:pk>/update/", NoteUpdate.as_view(), name="update_note")
]