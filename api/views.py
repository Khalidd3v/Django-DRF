from django.shortcuts import render
from . models import *
from . serializers import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import io
from rest_framework.parsers import JSONParser
from rest_framework.exceptions import ParseError
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import NotFound


def homepage(request):
    return render(request, 'app/homepage.html')

@csrf_exempt
def get_students_data(request):

    if request.method == 'GET':
        student_id = request.GET.get('id') or None
        if student_id is not None:
            try:
                student = Student.objects.get(id=student_id)
                serializer = StudentSerializers(student)
                return JsonResponse(serializer.data)
            except Student.DoesNotExist:
                error_message = {'error': 'Student not found.'}
                return JsonResponse(error_message, status=404)
        all_students = Student.objects.all()
        serializer = StudentSerializers(all_students, many=True)
        return JsonResponse(serializer.data, safe=False) 
    
    if request.method == 'POST':
        try:
            json_data = JSONParser().parse(request)
            serializer = StudentSerializers(data=json_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'success': 'Data saved successfully'}, status=201)
            return JsonResponse({'error': 'Invalid data'}, status=400)
        except ParseError as e:
            return JsonResponse({'error': str(e)}, status=400)
        
    if request.method == "PUT":
        try:
            json_data = JSONParser().parse(request)
            id = json_data.get('id')
            student = Student.objects.get(id=id)
            serializer = StudentSerializers(student, data=json_data, partial=False)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'success': 'Data updated successfully'}, status=200)
            else:
                return JsonResponse(serializer.errors, status=400)
        except ParseError as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    if request.method == "DELETE":
        try:
            json_data = JSONParser().parse(request)
            id = json_data.get('id')
            student = Student.objects.get(id=id)
            try:
                if student is not None:
                    student.delete()
                    return JsonResponse({'success': f'Student deleted successfully by this ID : {id}'}, status=200)
                else:
                    return JsonResponse({'error': f'{serializer.error}'}, status=404)
            except student.DoesNotExist:
                return JsonResponse({'error': f'Student not found by ID : {id}'}, status=404)
        except Exception as e:
            return JsonResponse({'error': f'Student not found to be delete by this ID : {id}'}, status=404)
    else:
        return JsonResponse({'error': 'Unsupported request method.'}, status=405)


def readpage(request):
    return render(request, 'app/read.html')

def deletepage(request):
    return render(request, 'app/delete.html')

def updatepage(request):
    return render(request, 'app/update.html')

def createpage(request):
    return render(request, 'app/create.html')