from rest_framework import serializers
from home.models import Home, Section

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = "__all__"

class HomeSerializer(serializers.ModelSerializer):
    article = SectionSerializer(many=True, read_only=True)
    class Meta:
        model = Home
        fields = "__all__"

