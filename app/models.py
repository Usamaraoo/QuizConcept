from django.db import models
from django.contrib.auth.models import User


class Point(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.PositiveIntegerField(default=0)
    attempt = models.PositiveIntegerField(default=0)
    passed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.points)

    # check the point to asign user according to attemps
    def points_to_give(self):
        if self.attempt is 0:
            return 100
        elif self.attempt <= 1:
            return 50
        else:
            return 25


class Question(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()


class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    @property
    def show_answer(self):
        return f"question: {self.question.text}, answer: {self.text}"


# return the list of true false
def check_fun(ans_id_li):
    correct_ans = []
    for pk in ans_id_li:
        answer = Answer.objects.get(id=pk)
        if answer.correct is False:
            correct_ans.append(False)
    return correct_ans
