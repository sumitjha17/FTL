from rest_framework import serializers

from .models import Activity_period
from .models import Members


class Activity_periodSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Activity_period
        fields = ('start_time','end_time')		

class MembersSerializer(serializers.HyperlinkedModelSerializer):
   
    activity=Activity_periodSerializer(many=True, read_only=True)
    class Meta:
        model = Members
        fields = ('real_name', 'address','activity')
		
		

    