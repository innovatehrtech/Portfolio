
from django.shortcuts import render
from .models import ServiceCategory


def home(request):

    categories = ServiceCategory.objects.prefetch_related('roles').filter(is_active=True)

    context = {
        'categories': categories
    }

    return render(request, 'recruitment/recruitment_home.html', context)

