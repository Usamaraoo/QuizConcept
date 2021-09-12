from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Question, Point, check_fun
from django.contrib.auth import authenticate, login


def home(request):
    if request.user.is_authenticated:
        points = Point.objects.get(user=request.user)  # getting user points
        ques = Question.objects.all()

        if request.method == 'POST':
            ans_id_li = request.POST.getlist('answer')
            # checking  Answers
            check_li = check_fun(ans_id_li)
            # On right answer
            if False not in check_li and ques.count() == len(ans_id_li):
                points.points += points.points_to_give()
                points.passed = True
                points.save()
                messages.success(request, f'    Correct answer point "{points}"   ',
                                 extra_tags='alert alert-success')
                return redirect('home')
            # On wrong answer
            points.attempt += 1
            points.save()

            messages.error(request, 'Unfortunately, there are one or more mistakes.',
                           extra_tags='alert alert-danger')
            return redirect('home')
        context = {'questions': ques, 'points': points}
        return render(request, 'app/home.html', context)

    else:
        user = authenticate(username='Usama', password='123')
        login(request, user)
        return redirect('home')
