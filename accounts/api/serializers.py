from django.contrib.auth.models import User
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    confirm = serializers.CharField(
        style={"input_type": "password"},
        write_only=True,
    )

    class Meta:
        model = User
        fields = ["username", "email", "password", "confirm"]
        extra_kwargs = {"password": {"write_only": True}}

    def save(self):
        password = self.validated_data.get("password")
        confirm = self.validated_data.get("confirm")

        if password != confirm:
            raise serializers.ValidationError(
                detail={"error": "Your passwords must match!"}
            )

        email = self.validated_data.get("email")

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                detail={"error": "This email is already in use!"}
            )

        username = self.validated_data.get("username")
        account = User(email=email, username=username)
        account.set_password(password)
        account.save()

        return account
