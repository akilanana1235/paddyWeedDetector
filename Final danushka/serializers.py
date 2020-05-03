from rest_framework importserializers
from weedApp.models import File

class fileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"