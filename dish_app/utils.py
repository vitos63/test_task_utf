from django.db.models import Prefetch, QuerySet
from dish_app.models import Food, FoodCategory


def get_categories_with_published_foods() -> QuerySet[FoodCategory]:
    published_foods = Food.objects.filter(is_publish=True)
    return (FoodCategory.objects.filter(food__is_publish=True).distinct()
        .prefetch_related(Prefetch('food', queryset=published_foods))
        .order_by('id'))
