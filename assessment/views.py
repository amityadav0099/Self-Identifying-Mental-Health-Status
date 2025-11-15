from django.shortcuts import render, redirect
from .forms import AssessmentForm


def start_assessment(request):
    if request.method == 'POST':
        form = AssessmentForm(request.POST)
        if form.is_valid():
            # Get the answers from the form
            q1 = form.cleaned_data['question1']
            q2 = form.cleaned_data['question2']

            # Simple scoring logic
            score = 0

            # Question 1 scoring
            if q1 == 'never':
                score += 0
            elif q1 == 'sometimes':
                score += 1
            elif q1 == 'often':
                score += 2
            elif q1 == 'always':
                score += 3

            # Question 2 scoring
            if q2 == 'excellent':
                score += 0
            elif q2 == 'good':
                score += 1
            elif q2 == 'fair':
                score += 2
            elif q2 == 'poor':
                score += 3

            # Store result in session
            request.session['score'] = score
            return redirect('assessment:result')

    else:
        form = AssessmentForm()

    return render(request, 'assessment/quiz.html', {'form': form})


def result(request):
    # Get the score from the session
    score = request.session.get('score', 0)

    # Simple interpretation
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
