from rest_framework import status


from rest_framework_simplejwt import views as jwt_views
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


from .models import Task
from .serializers import TaskSerializador

# Create your views here.
class Tasks(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        snippets = Task.objects.all()
        serializer = TaskSerializador(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializador(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# @api_view(['GET', 'POST'])
# def tareas(request):
#     print(request)
#     if request.method == 'GET':
#         snippets = Task.objects.all()
#         serializer = TaskSerializador(snippets, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         print(request.data)
#         serializer = TaskSerializador(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT'])
# def completar_tarea(request):
#     print(request.data)
#     if request.method == 'PUT':
#         task = Task.objects.get(pk=request.data['id'])
#         if not task == None:
#             task.completar()
#             serializer = TaskSerializador(task)
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#     return Response(None, status=status.HTTP_400_BAD_REQUEST)