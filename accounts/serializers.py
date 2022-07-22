from rest_framework import serializers
from accounts.models import CustomAccount

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = CustomAccount
        fields = [
            "first_name",
            "last_name",
            "email",
            "username",
            "phone_number",
            "date_joined",
            "address",
            "password",
            "password2",
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        try:
            user = CustomAccount(
                first_name=self.validated_data['first_name'], 
                last_name=self.validated_data['last_name'], 
                email=self.validated_data['email'],
                phone_number=self.validated_data['phone_number'],
                username=self.validated_data['username'],
                address=self.validated_data['address'],
            )
        except KeyError:
            raise serializers.ValidationError({"error": "You are missing one or more info"})
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user

# class (serializers.ModelSerializer):