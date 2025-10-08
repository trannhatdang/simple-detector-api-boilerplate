from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import BasicText
from .serializer import BasicTextSerializer
from . import run_model

#Stores the different "views" of the api. Love Faust
class ListAnalyzeTextView(ListCreateAPIView):
    model = BasicText
    serializer_class = BasicTextSerializer

    def get_queryset(self, request, *args, **kwargs):
        score = run_model.analyzeText(request.data['text'])
        serializer = BasicTextSerializer(data={'text': request.data['text'], 'score': score})

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'successful',
                'result' : str(score)
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Unsuccessful in analyzing analyzeText'
        }, status=status.HTTP_400_BAD_REQUEST)

class UpdateBasicTextView(RetrieveUpdateDestroyAPIView):
    model = BasicText
    serializer_class = BasicTextSerializer

    def put(self, request, *args, **kwargs):
        greenwashText = get_object_or_404(BasicText, id=kwargs.get('pk'))
        serializer = BasicTextSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update Text successful'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Text unsuccessful'
        }, status=status.HTTP_400_BAD_REQUEST)
