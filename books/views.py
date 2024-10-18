from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Book
from .serializers import BookSerializer


class BookListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(seller=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class BookDetailView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def patch(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        if book.seller != request.user:
            return Response({
                'detail': 'You do not have permission to update this book'
            }, status=status.HTTP_403_FORBIDDEN)

        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def delete(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        if book.seller != request.user:
            return Response({
                'detail': 'You do not have permission to delete this book'
            }, status=status.HTTP_403_FORBIDDEN)
        book.delete()
        return Response({
            'detail': 'Book deleted successfully'
        }, status=status.HTTP_204_NO_CONTENT)
