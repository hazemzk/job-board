import django_filters
from .models import Job
class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Job
        fields = ['title', 'location', 'job_type', 'description', 'category', 'experience']
        # exclude=['published_at', 'image', 'salary', 'Vacancy', 'slug', 'owner', 'description']