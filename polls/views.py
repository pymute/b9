from django.shortcuts import render
from django.http import JsonResponse
from .models import StudentModel
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentSerializer
class StudentALLview :
    def get(self,request,*args,**kwargs):
        all_students = StudentModel.object.all()
        serializer = StudentSerializer(all_students,many=True)
        return Response(serializer.data)
def get(request):
    if request.method =='GET':
        all_students = StudentModel.object.all()
        serializer = StudentSerializer(all_students,many=True)
        print(serializer.data)
        return Response(serializer.data)
def get_by_email(request):
    if request.method =='GET':
        try:
            data = StudentModel.object.get(id=)
        except StudentModel.DoesNotExist:
            return JsonResponse({'msg':'0'})
        return JsonResponse({'id':data.id,
                             'last_name':data.last_name,
                             'email':data.email})
