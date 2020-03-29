from rest_framework import serializers

from .models import Activity_period
from .models import Members


class Activity_periodSerializer(serializers.HyperlinkedModelSerializer):

   
	
    class Meta:
        model = Activity_period
        fields = ('start_time','end_time')		







class MembersSerializer(serializers.HyperlinkedModelSerializer):
    #activity = serializers.StringRelatedField(many=True)#, read_only=True,view_name='activity_period-detail')
    #activity = serializers.SlugRelatedField(many=True,read_only=True,slug_field='member_id#')
    activity=Activity_periodSerializer(many=True, read_only=True)
    class Meta:
        model = Members
        fields = ('real_name', 'address','activity')
		
		

    