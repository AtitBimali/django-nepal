from djangonepal.models import *

def data(request):
    province = Province.objects.all()
    return{
        'province':province
    }