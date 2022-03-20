from rest_framework import serializers 
from studyMat.models import studyMat

class studyMatSerializer(serializers.ModelSerializer):
    class Meta:
        model = studyMat
        fields = '__all__'