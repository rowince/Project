from pyexpat import model
from attr import fields
from rest_framework import serializers
from crud.models import Student


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'city', 'roll']
