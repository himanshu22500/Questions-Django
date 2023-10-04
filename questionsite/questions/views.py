from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Question
from django.http import HttpResponse


def get_list_of_questions(request):
    all_questions = Question.objects.all()
    return render(request, 'get_list_of_questions.html', {'questions': all_questions})


def create_question(request):
    if request.method == "POST":
        text = request.POST['question']
        answer = request.POST['answer']
        Question.objects.create(text=text, answer=answer)
        return HttpResponse("Got it")
    return render(request, 'create_question_form.html', {})


def get_question(request, question_id):
    question_obj = get_object_or_404(Question, id=question_id)
    return render(request, 'each_question_form.html', {'question': question_obj})


def update_question(request, question_id):
    if request.method == "POST":
        text = request.POST['question']
        answer = request.POST['answer']
        question_obj = Question.objects.get(id=question_id)
        question_obj.text = text
        question_obj.answer = answer
        question_obj.save()
        return HttpResponse("Got it")

    return render(request, 'update_question_success.html', {})


def delete_question(request, question_id):
    Question.objects.filter(id=question_id).delete()
    return render(request, 'delete_question_success.html', {})
