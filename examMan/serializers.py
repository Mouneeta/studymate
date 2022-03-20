from rest_framework import serializers 
from examMan.models import examMan

class examManSerializer(serializers.ModelSerializer):
    class Meta:
        model = examMan
        fields = '__all__'