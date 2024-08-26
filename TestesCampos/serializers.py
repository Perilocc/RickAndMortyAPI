from rest_framework import serializers
from .models import TesteCampos

class TesteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TesteCampos
        fields = "__all__"