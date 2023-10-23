from django.contrib import admin

from .models import Domain, Language, Paper, Review, User

admin.site.register(Domain)
admin.site.register(Language)
admin.site.register(Paper)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewer', 'paper', 'date_requested', 'status', 'date_completed', 'result')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'id', 'last_name', 'first_name', 'email')
