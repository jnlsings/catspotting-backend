# # https: // medium.com/@dakota.lillie/django-react-jwt-authentication-5015ee00ef9a

# from rest_framework import serializers
# # from rest_framework_simplejwt.settings import api_settings
# from django.contrib.auth.models import User

# # Serializers will serialize/unserialize User model in and out of various formats, primarily JSON


# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = ('username',)


# class UserSerializerWithToken(serializers.ModelSerializer):

#     token = serializers.SerializerMethodField()
#     password = serializers.CharField(write_only=True)

#     def get_token(self, obj):
#         jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
