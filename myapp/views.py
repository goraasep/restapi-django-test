from functools import partial
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from myapp.models import AppContent
from myapp.serializers import AppContentSerializer

# Create your views here.

@csrf_exempt
def contentApi(request,id=0):
    if request.method=='GET':
        if id==0:
            appcontent = AppContent.objects.all()
            appcontent_serializer=AppContentSerializer(appcontent,many=True)
        else:
            appcontent = AppContent.objects.get(pk=id)
            appcontent_serializer=AppContentSerializer(appcontent)
        return JsonResponse(appcontent_serializer.data,safe=False)
    elif request.method=='POST':
        appcontent_data=JSONParser().parse(request)
        appcontents_serializer=AppContentSerializer(data=appcontent_data)
        if appcontents_serializer.is_valid():
            appcontents_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        appcontent_data=JSONParser().parse(request)
        appcontent=AppContent.objects.get(id=id)
        appcontent_serializer=AppContentSerializer(appcontent,data=appcontent_data,partial=True)
        if appcontent_serializer.is_valid():
            appcontent_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        appcontent_data=JSONParser().parse(request)
        appcontent=AppContent.objects.get(id=id)
        appcontent_serializer=AppContentSerializer(appcontent,data=appcontent_data)
        if appcontent_serializer.is_valid():
            if appcontent_data['title']==appcontent_serializer.data['title'] and appcontent_data['content']==appcontent_serializer.data['content']:
                appcontent.delete()
                return JsonResponse("Deleted Successfully",safe=False)
        return JsonResponse("Failed to Delete",safe=False)