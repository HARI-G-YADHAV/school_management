from rest_framework import serializers
from .models import User,Subject,Mark

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'role']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name']

class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = ['id', 'student', 'subject', 'marks_obtained']

    def __init__(self, *args, **kwargs):
        super(MarkSerializer, self).__init__(*args, **kwargs)
        self.fields['student'].queryset = User.objects.filter(role='Student')
        self.fields['subject'].queryset = Subject.objects.all()