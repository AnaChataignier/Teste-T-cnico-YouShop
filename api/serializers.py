from rest_framework import serializers
from main.models import PlantedTree


class PlantedTreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantedTree
        fields = ["id", "age", "planted_at", "tree", "account", "location"]
