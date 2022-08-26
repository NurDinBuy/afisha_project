from rest_framework import serializers


from movie_app.models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'
