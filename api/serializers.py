from rest_framework import serializers
from main import models


class CategorySerializer(serializers.ModelSerializer):


    class Meta:
        model = models.Category
        exclude = ['id']


class AuthorSerializer(serializers.ModelSerializer):


    class Meta:
        model = models.Author
        exclude = ['id']

    
class BookSerializer(serializers.ModelSerializer):


    class Meta:
        model = models.Book
        exclude = ['id']

    
class QuoteSerializer(serializers.ModelSerializer):


    class Meta:
        model = models.Quote
        exclude = ['id']


class ReviewSerializer(serializers.ModelSerializer):


    class Meta:
        model = models.Review
        exclude = ['id']