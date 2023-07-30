from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.renderers import JSONRenderer

from django.http import JsonResponse

from . import serializers
from . import models

# Create your views here.


class ContentListAPIView(generics.ListAPIView):
    queryset = models.Content.objects.all()
    serializer_class = serializers.ContentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['need_why', 'location']


class ContentDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Content.objects.all()
    serializer_class = serializers.ContentSerializer


class ContentStatisticAPIView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        context = {
            'need_job_count': models.Content.objects.filter(need_why='xodim').count(),
            'need_employee_count': models.Content.objects.filter(need_why='ishJoyi').count(),
            'need_partner_count': models.Content.objects.filter(need_why='sherik').count(),
            'need_study_center_count': models.Content.objects.filter(need_why='oquvKursi').count()
        }

        return Response(context)
