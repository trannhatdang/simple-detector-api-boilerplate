from rest_framework import serializers

from .models import BasicText

class BasicTextSerializer(serializers.ModelSerializer):

    class Meta: 
        model = BasicText
        fields = ['text', 'score']
