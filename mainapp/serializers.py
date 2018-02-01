from rest_framework import serializers
from . import models

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = (
            'id',
            'title',
            'body',
            'creation_date',
            'votes',
        )


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Answer
        fields = (
            'id',
            'question_id',
            'body',
            'creation_date',
            'votes',
        )
