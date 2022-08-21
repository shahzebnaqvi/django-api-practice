from rest_framework import serializers
from cars.models import Todo,UploadImageTest

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        # fields = "__all__"
        fields = ("title", "is_completed")
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadImageTest
        fields = ('name', 'image')