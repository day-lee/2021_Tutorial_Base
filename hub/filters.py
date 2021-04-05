import django_filters
from django_filters import DateFilter
from .models import Tutorial
from django import forms


class TutorialFilter(django_filters.FilterSet):
    DATE_CHOICES        = (
                            ('newest', 'Newest'),
                            ('oldest', 'Oldest')
    )
    date_sort           = django_filters.ChoiceFilter(
                            label     ='Sort by Date',
                            choices   =DATE_CHOICES,
                            method    ='filter_by_date',
                            # widget  =forms.Select(attrs={'size': 4})
    )

    class Meta:
        model = Tutorial
        fields = {
                            'title'     : ['icontains'],
                            'instructor': ['icontains'],
                            'language'  : ['exact'],
                            'difficulty': ['exact'],
                            'tags'      : ['exact'],
        }

    def filter_by_date(self, queryset, name, value):
        expression = 'last_updated' if value == 'oldest' else '-last_updated'
        return queryset.order_by(expression)