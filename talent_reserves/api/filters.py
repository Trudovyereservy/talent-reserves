import django_filters.rest_framework as django_filters

from blog.models import Post


class ListFilter(django_filters.Filter):
    def filter(self, qs, value):
        if not value:
            return qs
        value_list = value.split(',')
        return qs.filter(**{f'{self.field_name}__in': value_list})


class PostFilter(django_filters.FilterSet):
    tags = ListFilter(field_name='tags__name', lookup_expr='in')

    class Meta:
        model = Post
        fields = ('tags',)
