from django.db import models

# Create your models here.

class Question(models.Model):
    #accepted_answer_id = models.ForeignKey()
    #owner_id = models.ForeignKey()
    title = models.TextField()
    body = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(default=0)
    #answers
    #is_answered = BooleanField(default=False)

    def __str__(self):
        return self.title

class Answer(models.Model):
    #owner_id = models.ForeginKey()
    question_id = models.ForeignKey(
        'Question',
        on_delete = models.CASCADE
    )
    body = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(default=0)

    #is_accepted = BooleanField(default=False)
