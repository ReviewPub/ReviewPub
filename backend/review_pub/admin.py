from django.contrib import admin

from .models import Domain, Language, Paper, Review, User

admin.site.register(Domain)
admin.site.register(Language)
admin.site.register(Paper)
admin.site.register(Review)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'id', 'last_name', 'first_name', 'email')
