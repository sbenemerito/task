from django.contrib import admin

from .forms import MainModelForm
from .models import (
    ModelA,
    ModelB,
    ModelC,
    MainModel
    )


class MainModelAdmin(admin.ModelAdmin):
    fields = ('name', 'model_c', 'model_b', 'model_a')
    form = MainModelForm


admin.site.register(ModelA)
admin.site.register(ModelB)
admin.site.register(ModelC)
admin.site.register(MainModel, MainModelAdmin)
