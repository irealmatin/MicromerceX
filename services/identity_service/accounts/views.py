from rest_framework_simplejwt.views import TokenObtainPairView 
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .serializers import MyTokenObtainPairSerializer , UserRegisterSerializer
from .models import User



class RegisterView(generics.CreateAPIView):
    """
    API endpoint for user registration.
    """
    queryset = get_user_model().objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    """
    API endpoint for obtaining JWT tokens with custom claims.
    """
    serializer_class = MyTokenObtainPairSerializer


class SellerAplicationView(APIView):
    """API endpoint for submitting seller applications.
    """
    permission_classes = [IsAuthenticated]

    def post(self , request , *args , **kwargs):
        """Handle seller application submission.
        
        Args:
            request: HttpRequest with user context.
            
        Returns:
            Response: Success or error message with appropriate status code."""
        
        user = request.user
        if user.role in [User.Role.SELLER, User.Role.ADMIN]:
            return Response({"message": "You are already a seller or admin."}, status=status.HTTP_400_BAD_REQUEST)

        profile = user.profile
        profile.is_seller_applicant = True
        profile.save()

        return Response({"message": "Your application to become a seller has been submitted successfully."}, status=status.HTTP_200_OK)
    

