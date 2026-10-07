from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include("apps.bookmodule.urls")),  # تأكدي من وجود كلمة include والنقطة بين apps و bookmodule
    path('users/', include("apps.usermodule.urls")),
]