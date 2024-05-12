from . import serializers
from main import models
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response


class IndexSerializer(APIView):
     
    def get(self, request):
        serializer = serializers.CategorySerializer(models.Category.objects.all(), many=True)
        return Response(data=serializer.data)


class CategoryBookSerializer(APIView):

    def get(self, request, code):
        try:
            category = models.Category.objects.get(code=code)
            serializer = serializers.BookSerializer(models.Book.objects.filter(category=category), many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class AuthorListSerializer(generics.ListAPIView):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer


class AuthorDetailSerializer(APIView):
        
    def get(self, request, code):
        try:
            serializer = serializers.AuthorSerializer(models.Author.objects.get(code=code))
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

class BookListSerializer(generics.ListAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer


class BookDetailSerializer(APIView):
    
    def get(self, request, code):
        try:
            serializer = serializers.BookSerializer(models.Book.objects.get(code=code))
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    


        
