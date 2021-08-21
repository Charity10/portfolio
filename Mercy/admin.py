from django.contrib import admin
from .models import Home, About, Category, Skill, Project, Profile

# Register your models here.
admin.site.register(Home)


class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [         
        ProfileInline,
    ]

class skillInline(admin.TabularInline):
    model = Skill
    extra = 2


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        skillInline,
    ]


admin.site.register(Project)
