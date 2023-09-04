from rest_framework import serializers

from problems.models import Problem


class ProblemSerializer(serializers.ModelSerializer):
    # Сериализатор для задач
    class Meta:
        model = Problem
        fields = '__all__'
