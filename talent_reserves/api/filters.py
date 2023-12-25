import django_filters.rest_framework as django_filters

from blog.models import Post
from coaches.models import Coach
from news.models import News


class IntegerListFilter(django_filters.BaseInFilter,
                        django_filters.NumberFilter):

    def filter(self, qs, value):
        if not value:
            return qs
        return qs.filter(**{f'{self.field_name}__in': value})


class PostFilter(django_filters.FilterSet):
    tags = IntegerListFilter(field_name='tags__name', lookup_expr='in')

    class Meta:
        model = Post
        fields = ('tags',)


class CoachFilter(django_filters.FilterSet):
    direction_ids = IntegerListFilter(field_name='directions__pk',
                                      lookup_expr='in')

    class Meta:
        model = Coach
        fields = ('direction_ids',)


class NewsFilter(django_filters.FilterSet):
    tags_ids = IntegerListFilter(field_name='tags__pk', lookup_expr='in')

    class Meta:
        model = News
        fields = ('tags_ids',)
