from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Questions, Choice


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Questions.objects.order_by('-pub_date')[:5]

# Create your views here.
def owner(request):
    return HttpResponse("Hello, world. 71985d37 is the polls index.")

class DetailView(generic.DetailView):
    model = Questions
    template_name = 'detail.html'



class ResultsView(generic.DetailView):
    model = Questions
    template_name = 'results.html'

class ResultsView(generic.DetailView):
    model = Questions
    template_name = 'results.html'

def vote(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
