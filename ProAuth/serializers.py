from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Tests
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    # Make optional fields allow blank so create() can fill them
    first_name = serializers.CharField(allow_blank=True, required=False)
    last_name = serializers.CharField(allow_blank=True, required=False)
    level = serializers.CharField(allow_blank=True, required=False)
    faculty = serializers.CharField(allow_blank=True, required=False)
    department = serializers.CharField(allow_blank=True, required=False)
    gender = serializers.CharField(allow_blank=True, required=False)
    phone_number = serializers.CharField(allow_blank=True, required=False)

    class Meta:
        model = User
        fields = (
            'id', 'email', 'username',
            'first_name', 'last_name', 'level',
            'faculty', 'department', 'gender', 'phone_number',
            'password1', 'password2'
        )

    def validate(self, attrs):
        if attrs['password1'] != attrs["password2"]:
            raise serializers.ValidationError(
                {'password': "Bobo your password no match!"}
            )
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2', None)
        password = validated_data.pop('password1')

        # Fill missing fields with empty string
        validated_data.setdefault("first_name", "")
        validated_data.setdefault("last_name", "")
        validated_data.setdefault("level", "")
        validated_data.setdefault("faculty", "")
        validated_data.setdefault("department", "")
        validated_data.setdefault("gender", "")
        validated_data.setdefault("phone_number", "")

        user = User.objects.create_user(
            password=password,
            **validated_data
        )

        return user


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tests
        fields = ('id', 'question_pointers', 'date', 'score')


class UserSerializer(serializers.ModelSerializer):
    # test_history = TestSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', "email", 'first_name', 'last_name',
                  'level', "faculty", 'username', 'gender', 'phone_number', "department", )


class UserUpdateSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(allow_blank=True, required=False)
    last_name = serializers.CharField(allow_blank=True, required=False)
    level = serializers.CharField(allow_blank=True, required=False)
    faculty = serializers.CharField(allow_blank=True, required=False)
    department = serializers.CharField(allow_blank=True, required=False)
    gender = serializers.CharField(allow_blank=True, required=False)
    phone_number = serializers.CharField(allow_blank=True, required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'level',
                  'faculty', 'department', 'gender', 'phone_number')
