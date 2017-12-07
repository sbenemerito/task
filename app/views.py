from django.http import JsonResponse

from .models import ModelB, ModelC


def RetrieveOptions(request):
    b_ids = request.GET.getlist('b[]')
    b_objects = ModelB.objects.filter(pk__in=b_ids)
    a_from_b = {(b.related_a.pk, b.related_a.name) for b in b_objects}
    
    c_ids = request.GET.getlist('c[]')
    c_objects = ModelC.objects.filter(pk__in=c_ids)
    a_from_c = {(c.related_a.pk, c.related_a.name) for c in c_objects}

    # join sets, then sort
    a_options = sorted(a_from_b|a_from_c)     

    data = {
        'a_options': a_options
    }
    return JsonResponse(data)
    