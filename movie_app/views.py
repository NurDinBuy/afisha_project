from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from movie_app.serializers import DirectorSerializer, MovieSerializer, ReviewSerializer
from movie_app.models import Director, Movie, Review


@api_view(['GET', 'POST'])
def directors_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(data=serializer.data)
    else:
        name = request.date.get('name')
        Director.objects.create(name=name)
        return Response(data={'massage': ''})


@api_view(['GET','PUT','DELETE'])
def director_item_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'ERROR': 'Director not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer = DirectorSerializer(director)
        return Response(data=serializer.data)
    elif request.method=='DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        director.name=request.data.get('name')
        return Response(data={'massage': 'update'}, status=status.HTTP_202_ACCEPTED)


@api_view(['GET', 'POST'])
def movies_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data)
    else:
        title=request.data.get('title')
        description=request.data.get('description')
        duration=request.data.get('duration')
        category_id=request.data.get('category_id')
        Movie.objects.create(title=title,description=description,duration=duration,
                            category_id=category_id )
        return Response(data={'massage':'created'})


@api_view(['GET','PYT','DELETE'])
def movies_item_view(request, id):
    try:
        movies = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'ERROR': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MovieSerializer(movies)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        movies.title = request.data.get('title')
        movies.description = request.data.get('description')
        movies.duration = request.data.get('duration')
        movies.category_id = request.data.get('category_id')
        return Response(data={'massage': 'update'},status=status.HTTP_202_ACCEPTED)


@api_view(['GET','POST'])
def reviews_view(request):
    if request.method=='GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)
    else:
        text=request.data.get('text')
        star=request.data.get('star')
        category_id=request.data.get('category_id')
        Review.objects.create(text=text,stars=star,
                              category_id=category_id)
        return Response(data={'massage':''})


@api_view(['GET', 'PUT', 'DELETE'])
def reviews_item_view(request, id):
    try:
        movies = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'ERROR': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer = ReviewSerializer(movies)
        return Response(data=serializer.data)
    elif request.method=='DELETE':
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        movies.text = request.data.get('text')
        movies.star = request.data.get('star')
        movies.category_id = request.data.get('category_id')

        return Response(data={'massage': 'update'},status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def movie_reviews(request):
    movies_review = Movie.objects.all()
    data = MovieSerializer(movies_review, many=True).data
    return Response(data=data)