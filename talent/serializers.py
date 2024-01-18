from rest_framework import serializers
from talent.models import Talent

class TalentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talent
        fields = ['id','username','email']
        

