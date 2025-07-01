from django.urls import path
from core.views_learning import LearningMaterialListView
from .views_order import CreateOrderView
from .views_ai import AskAIQuestionView
from .views_auth import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('learning/', LearningMaterialListView.as_view(), name='learning-list'),
    path('order/create/', CreateOrderView.as_view(), name='create-order'),
    path('ask/', AskAIQuestionView.as_view(), name='ask-ai'),
    path("register/", RegisterView.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
