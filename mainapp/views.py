from rest_framework import generics, mixins

from . import models
from . import serializers


class ListQuestion(generics.ListCreateAPIView):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer


class DetailQuestion(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.QuestionSerializer

    def get_queryset(self):
        question_id = self.kwargs.get('pk')
        return models.Question.objects.filter(pk=question_id)


class ListAnswer(generics.ListCreateAPIView):
    queryset = models.Answer.objects.all()
    serializer_class = serializers.AnswerSerializer


class DetailAnswer(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Answer.objects.all()
    serializer_class = serializers.AnswerSerializer

    def get_queryset(self):
        answer_id = self.kwargs.get('pk')
        return models.Answer.objects.filter(pk=answer_id)

class ListQuestionAnswers(generics.ListCreateAPIView):
    serializer_class = serializers.AnswerSerializer
    #def get_serializer_class(self):
    def initial(self, request, *args, **kwargs):
        print (request.data)
        question_id = self.kwargs.get('pk')
        request.data['question_id'] = question_id
        print (request.data)
        super().initial(request, *args, **kwargs)

    #def perform_create(self, serializer):
        #pass
        #question_id = self.kwargs.get('pk')
        #serializer.save(question_id=question_id)

    def get_queryset(self):
        question_id = self.kwargs.get('pk')
        return models.Answer.objects.filter(question_id=question_id)
