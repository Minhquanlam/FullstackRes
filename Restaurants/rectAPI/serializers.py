from rest_framework import serializers
from rectAPI.models import pizza

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = pizza
        fields = "__all__"