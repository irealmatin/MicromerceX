from django.urls import path
from .views import MyTokenObtainPairView , RegisterView , SellerAplicationView , test_view
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView 



urlpatterns = [
        path('register/' , RegisterView.as_view() , name= 'register'),
        path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('login/refresh/', TokenRefreshView.as_view() , name= 'token-refresh'),
        path('apply-seller/', SellerAplicationView.as_view(), name='apply-seller'),
        path('', test_view),


]
