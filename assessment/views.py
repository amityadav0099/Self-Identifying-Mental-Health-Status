from django.shortcuts import render, redirect
from .forms import AssessmentForm

def start_assessment(request):
    if request.method == 'POST':
        form = AssessmentForm(request.POST)
        if form.is_valid():

            q1 = form.cleaned_data['question1']
            q2 = form.cleaned_data['question2']

            score = 0

            score_map_q1 = {
                'never': 0,
                'sometimes': 1,
                'often': 2,
                'always': 3,
            }
            score += score_map_q1[q1]

            score_map_q2 = {
                'excellent': 0,
                'good': 1,
                'fair': 2,
                'poor': 3,
            }
            score += score_map_q2[q2]

            request.session['score'] = score
            return redirect('assessment:result')

    else:
        form = AssessmentForm()

    return render(request, 'assessment/quiz.html', {'form': form})


def result(request):
    score = request.session.get('score', 0)

    if score <= 2:
        message = "You seem to be doing well! Keep it up! 😃"
    elif score <= 4:
        message = "You have mild stress. Try relaxation or meditation. 🙂"
    elif score <= 6:
        message = "You may be feeling moderately stressed. Take breaks and talk to someone. 😐"
    else:
        message = "You seem highly stressed. Please seek help or talk to a professional. 😟"

    return render(request, 'assessment/result.html', {
        'score': score,
        'message': message
    })
