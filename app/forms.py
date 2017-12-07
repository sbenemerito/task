from django import forms

from .models import ModelA, MainModel


class MainModelForm(forms.ModelForm):
    class Meta:
        model = MainModel
        fields = ('name', 'model_c', 'model_b', 'model_a')

    def __init__(self, *args, **kwargs):
        super(MainModelForm, self).__init__(*args, **kwargs)
        
        # if updating an instance, rather than creating
        if self.instance.pk:
            # get A options from related B and C
            a_from_b = {b.related_a.pk for b in self.instance.model_b.all()}
            a_from_c = {c.related_a.pk for c in self.instance.model_c.all()}
            a_ids = a_from_b|a_from_c      

            # must select Bs and Cs, then save to show limited A options
            self.fields['model_a'].choices = ModelA.objects.filter(pk__in=a_ids
                                             ).values_list('id', 'name')  
