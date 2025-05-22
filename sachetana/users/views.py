from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from serializers import UserSerializer

class UserRegistrationView(APIView):
    def post(self, request):
        registration_number = request.data.get('registration_number')
        password = request.data.get('password')

        if not registration_number or not password:
            return Response({'error': 'Registration number and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        UserModel = get_user_model()
        if UserModel.objects.filter(registration_number=registration_number).exists():
            return Response({'error': 'User with this registration number already exists.'}, status=status.HTTP_409_CONFLICT)

        try:
            user = UserModel.objects.create(
                registration_number=registration_number,
                password=make_password(password) # Hash the password
                # Add other fields if necessary
            )
            return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': f'Registration failed: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
