from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    last_name = serializers.CharField(max_length=200)
    phone = serializers.CharField()
    date_of_birth = serializers.DateField()
