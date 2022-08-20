from rest_framework import serializers
from cars.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        # fields = "__all__"
        fields = ("title", "is_completed")