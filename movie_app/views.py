from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from movie_app.serializers import DirectorSerializer, MovieSerializer, ReviewSerializer
from movie_app.models import Director, Movie, Review


@api_view(['GET'])
def directors_view(request):
    directors = Director.objects.all()
    serializer = DirectorSerializer(directors, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def director_item_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'ERROR': 'Director not found' }, status=status.HTTP_404_NOT_FOUND)
    serializer = DirectorSerializer(director)
    return Response(data=serializer.data)


@api_view(['GET'])
def movies_view(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def movies_item_view(request, id):
    try:
        movies = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'ERROR': 'Movie not found' }, status=status.HTTP_404_NOT_FOUND)
    serializer = MovieSerializer(movies)
    return Response(data=serializer.data)


@api_view(['GET'])
def reviews_view(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def reviews_item_view(request, id):
    try:
        movies = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'ERROR': 'Review not found' }, status=status.HTTP_404_NOT_FOUND)
    serializer = ReviewSerializer(movies)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_reviews(request):
    movies_review = Movie.objects.all()
    data = MovieSerializer(movies_review, many=True).data
    return Response(data=data)