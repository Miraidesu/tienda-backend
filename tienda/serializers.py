from django.contrib.auth import authenticate
from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
	username = serializers.CharField(max_length=150)
	password = serializers.CharField(max_length=128, write_only=True)

	def validate(self, data):
		username = data.get('username')
		password = data.get('password')

		if username and password:
			user = authenticate(username=username, password=password)
			
			if not user:
				raise serializers.ValidationError("Credenciales inválidas")
			
			if not user.is_active:
				raise serializers.ValidationError("Cuenta desactivada")
			
			return user
			
		raise serializers.ValidationError("Debe incluir 'username' y 'password'")
