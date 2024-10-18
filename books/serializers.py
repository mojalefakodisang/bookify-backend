from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = [
            'id', 'seller', 'title', 'author', 'description',
            'price', 'condition', 'published_date', 'image',
            'is_available', 'created_at'
        ]
        read_only_fields = ['id', 'seller', 'created_at']
