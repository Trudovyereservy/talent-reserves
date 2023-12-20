import django_filters.rest_framework as django_filters

from blog.models import Post
from coaches.models import Coach


class IntegerListFilter(django_filters.BaseInFilter,
                        django_filters.NumberFilter):
    def filter(self, qs, value):
        if not value:
            return qs
        return qs.filter(**{f'{self.field_name}__in': value})


class PostFilter(django_filters.FilterSet):
    tags_ids = IntegerListFilter(field_name='tags__pk', lookup_expr='in')

    class Meta:
        model = Post
        fields = ('tags_ids',)


class CoachFilter(django_filters.FilterSet):
    directions = IntegerListFilter(
        field_name='directions__pk', lookup_expr='in')

    class Meta:
        model = Coach
        fields = ('directions',)
