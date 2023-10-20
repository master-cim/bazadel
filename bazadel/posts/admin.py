from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from .models import Service, Status, Order, Project, Workflow

admin.site.unregister(User)


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = UserCreationForm.Meta.model
        fields = '__all__'
        field_classes = UserCreationForm.Meta.field_classes


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups',
                       'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff',
                    'date_joined',)
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('date_joined',)
    empty_value_display = '-пусто-'
    ordering = ('email',)


class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('pk', 'title',
                    'description',)
    search_fields = ('title',)
    list_filter = ('slug',)
    empty_value_display = '-пусто-'


class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'service',
                    'text', 'phone_number', 'e_mail',
                    'pub_date',)
    search_fields = ('author', 'phone_number', 'e_mail',
                    'pub_date',)
    list_filter = ('author', 'service', 'pub_date',)
    empty_value_display = '-пусто-'


class StatusAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description',
                    'prev_status',)
    search_fields = ('prev_status',)
    list_filter = ('name', )
    empty_value_display = '-пусто-'


class MembershipInline(admin.TabularInline):
    model = Project.status.through


class WorkflowAdmin(admin.ModelAdmin):
    list_display = ('pk', 'status', 'project',
                    'start_date', 'end_date',
                    'process_mng')
    search_fields = ('prev_status',)
    list_filter = ('status',  'project',
                   'start_date', 'end_date',
                    'process_mng')
    empty_value_display = '-пусто-'


class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]
    exclude = ('status',)



admin.site.register(Service, ServiceAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Workflow, WorkflowAdmin)