"""
Module: Authentication Routes
Owner: T. Malleshwari
Source: Django users/views.py
Purpose: Login and authentication endpoints
"""
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdmin
from users.models import User
from audit.models import LoginAudit

class AdminOnlyTestView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        return Response({
            "message": f"Welcome Admin {request.user.username}"
        })
    
class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        # Try authenticating user
        user = authenticate(username=username, password=password)

        # CASE 1: INVALID CREDENTIALS
        if not user:
            try:
                u = User.objects.get(username=username)

                # Increase failed attempts
                u.failed_login_attempts += 1

                # Lock account after 3 failures
                if u.failed_login_attempts >= 3:
                    u.is_locked = True

                u.save()

                # Log failed attempt
                LoginAudit.objects.create(user=u, status="FAILED")

            except User.DoesNotExist:
                # Username does not exist → no user to update
                pass

            return Response(
                {"error": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        # CASE 2: ACCOUNT LOCKED
        if user.is_locked:
            LoginAudit.objects.create(user=user, status="LOCKED")
            return Response(
                {"error": "Account is locked due to multiple failed login attempts"},
                status=status.HTTP_403_FORBIDDEN
            )

        # CASE 3: SUCCESSFUL LOGIN
        user.failed_login_attempts = 0
        user.save()

        refresh = RefreshToken.for_user(user)

        # Log success
        LoginAudit.objects.create(user=user, status="SUCCESS")

        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "role": user.role
        })
