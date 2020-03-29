from django.shortcuts import render

# views.py
from rest_framework import viewsets

from .serializers import MembersSerializer,Activity_periodSerializer
from .models import Members,Activity_period




class MembersViewSet(viewsets.ModelViewSet):
    queryset = Members.objects.all().order_by('real_name')
    serializer_class = MembersSerializer

	

class Activity_periodViewSet(viewsets.ModelViewSet):
    queryset = Activity_period.objects.all().order_by('member_id')
    serializer_class = Activity_periodSerializer	