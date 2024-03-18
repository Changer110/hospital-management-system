from django.contrib import admin
from App.models.user import User

admin.site.register(User)

# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
# # from App.models import User

# class CustomUserCreationForm(UserCreationForm):
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password"])
#         if commit:
#             user.save()
#         return user

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm

# admin.site.register(User)
# admin.site.unregister(get_user_model())
# admin.site.register(get_user_model(), CustomUserAdmin)