from .models import File
from .tasks import file_processing
from .serializers import FileSerializer
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response


# Create your views here.


class FileUploadAPIView(APIView):
    """
    Класс обрабатывает POST-запрос для загрузки файла и при успешном сохранении
    асинхронно запускается задача по обработки файла с использованием Celery.
    """

    def post(self, request):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            file = serializer.save()
            file_processing.delay(file.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileListAPIView(generics.ListAPIView):
    """
    Класс возвращает список всех загруженных файлов с их данными, включая статус обработки.
    """
    serializer_class = FileSerializer
    queryset = File.objects.all()
