from rest_framework import viewsets
from api.serializers import StudentSerializers
from crud.models import Student


class StudSerializers(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
