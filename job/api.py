from .models import*
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics



@api_view(['GET'])
def job_list(request):
    all_job = Job.objects.all()
    data= JobSerializer(all_job, many =True).data
    return Response({'data':data})


@api_view(['GET'])
def job_ditail_api(request, slug):
    job_ditail = Job.objects.get(slug=slug)
    data= JobSerializer(job_ditail).data
    return Response({'data':data})


class JobListApi(generics.ListAPIView):

    queryset = Job .objects.all()
    serializer_class = JobSerializer
    
class JobDitail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class =JobSerializer
    queryset = Job .objects.all()
    lookup_field = 'slug'
