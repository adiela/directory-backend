from django.contrib import admin
from django.apps import apps


class CustomAdmin(admin.ModelAdmin):
    readonly_fields = ['created_by', 'updated_by']


# all models
listings_models = apps.get_app_config('listings').get_models()

for model in listings_models:
    try:
        admin.site.register(model, CustomAdmin)
    except admin.sites.AlreadyRegistered:
        pass
