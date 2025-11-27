from rest_framework import serializers
from .models import TestRun

class TestRunSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestRun
        fields = '__all__'
        read_only_fields = ('user', 'status', 'result_json', 'created_at', 'progress')
