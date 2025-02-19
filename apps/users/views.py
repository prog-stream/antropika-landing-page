from datetime import timezone
import logging
from django.shortcuts import render
from apps.users.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.exceptions import ValidationError
from django.db import IntegrityError

from antropika_landing_page.settings import env


class HomeView(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        try:
            app_url = env("APP_URL")
            context = {
                "registerUrl": f"{app_url}/onboarding",
            }
            return Response(context, template_name="index.html")
        except Exception as e:
            logging.exception(e)
            return Response(
                {"message": "Something went wrong"}, template_name="error.html"
            )


class LandingPageView(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        try:
            app_url = env("APP_URL")
            context = {
                "url": f"{app_url}/register",
            }
            return Response(context, template_name="landing_page.html")
        except Exception as e:
            logging.exception(e)
            if isinstance(e, ValidationError) and "unique" in str(e):
                return Response(
                    {"message": "User Already registered"}, template_name="error.html"
                )
            return Response(
                {"message": "Something went wrong"}, template_name="error.html"
            )


class RegisterView(APIView):
    # renderer_classes = [TemplateHTMLRenderer]

    def post(self, request):
        try:
            first_name = request.data.get("first_name")
            last_name = request.data.get("last_name")
            email = request.data.get("email")
            phone = request.data.get("phone")
            language = request.data.get("language")
            response_data = {"code": None, "data": None, "message": None}

            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                language=language,
                status=1,
            )
            user.save()
            response_data = {
                "code": 201,
                "data": None,
                "message": "Registrazione riuscita",
            }

            return Response({"success": response_data})
        except IntegrityError as e:
            logging.exception(e)
            response_data = {
                "code": 422,
                "data": None,
                "message": "Utente già registrato",
            }
            if "duplicate key value violates unique constraint" in str(e):
                return Response({"success": response_data})
        except Exception as e:
            logging.exception(e)
            response_data = {
                "code": 422,
                "data": None,
                "message": "Qualcosa è andato storto",
            }
            return Response({"error": response_data})
