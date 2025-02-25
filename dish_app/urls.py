from django.urls import path
from dish_app.views import FoodsAPIView

app_name = 'api_v1'

urlpatterns =[
    path('foods/', FoodsAPIView.as_view(), name='foods')
]
