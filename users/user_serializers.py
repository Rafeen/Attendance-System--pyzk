from rest_framework import serializers
from users.models import User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('full_name','department', 'employee_id','app_user_id', 'role', 'is_admin',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.full_name = profile_data.get('full_name', profile.full_name)
        profile.department = profile_data.get('department', profile.department)
        profile.app_password = profile_data.get('app_password', profile.app_password)
        profile.employee_id = profile_data.get('employee_id', profile.employee_id)
        profile.role = profile_data.get('role', profile.role)
        profile.is_admin = profile_data.get('is_admin', profile.is_admin)
        profile.save()

        return instance

