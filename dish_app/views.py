from rest_framework.generics import ListAPIView
from dish_app.utils import get_categories_with_published_foods
from dish_app.models import FoodListSerializer


class FoodsAPIView(ListAPIView):
    queryset = get_categories_with_published_foods()
    serializer_class = FoodListSerializer
