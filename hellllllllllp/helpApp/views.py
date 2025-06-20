from django.shortcuts import render
from .serializer import StudentSerializer
from .models import StudentModel
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, APIView, permission_classes
from django.http import Http404
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions  import IsAdminUsername

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def get_students(request):
    if request.method=='GET':
        students=StudentModel.objects.all()
        serializer=StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET', 'PUT' , 'DELETE'])
def student_details(request, pk):
    try:
        student=StudentModel.objects.get(pk=pk)
    except StudentModel.DoesNotExist:
        return Response({'Error':'Student not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer=StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=='PUT':
        serializer=StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    elif request.method=='DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class GetStudents(APIView):

#     def get(self, request):
#         students=StudentModel.objects.all()
#         serializer=StudentSerializer(students, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         serilaizer=StudentSerializer(data=request.data)
#         if serilaizer.is_valid():
#             serilaizer.save()
#             return Response(serilaizer.data, status=status.HTTP_201_CREATED)
#         return Response(serilaizer.errors, status=status.HTTP_404_NOT_FOUND)
    
# class StudentDetail(APIView):

#     def get_object(self, pk):
#         try:
#             student=StudentModel.objects.get(pk=pk)
#         except StudentModel.DoesNotExist:
#             return Http404
        
#     def get(self,pk,request):
#         student=self.get_object(pk)
#         serializer=StudentSerializer(student)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self,pk, request):
#         student=self.get_object(pk)
#         serializer=StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
#     def delete(self, pk, request):
#         student=self.get_object(pk)
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        

# class StudentsListCreate(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset=StudentModel.objects.all()
#     serializer_class=StudentSerializer

#     def get(self, request):
#         return self.list(request)
#     def post(self,request):
#         return self.create(request)
    
# class StudentRetriveUpdateDelete(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset=StudentModel.objects.all()
#     serializer_class=StudentSerializer

#     def get(self, request, pk):
#         return self.retrieve(pk=pk)
    
#     def put(self, request, pk):
#         return self.update(pk=pk)
    
#     def delete(self, request, pk):
#         return self.destroy(pk=pk)
    
# class StudentViewSet(viewsets.ModelViewSet):
#     queryset=StudentModel.objects.all()
#     serializer_class=StudentSerializer
