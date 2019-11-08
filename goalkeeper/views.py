from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import GoalForm, HistoryForm
from .models import User, Goal, History


# Create your views here.
@login_required
def index(request):
  return render(request, 'goalkeeper/dashboard.html')

@login_required
def create_goal(request):
  if request.method == "POST":
    form = GoalForm(request.POST)
    if form.is_valid():
      goal = form.save(commit=False)
      goal.user = request.user
      goal.save()
      return redirect('dashboard')
  else:
    form = GoalForm()
  return render(request, 'goalkeeper/create_goal.html', { "form": form })

@login_required
def display_goal(request, pk):
  my_goal = get_object_or_404(Goal, pk=pk)
  if request.method == "POST":
    form = HistoryForm(request.POST)
    if form.is_valid():
      history = form.save(commit=False)
      history.user = request.user
      history.save()
      return redirect('display-goal')
  else:
    form = HistoryForm()
  return render(request, 'goalkeeper/display_goal.html', { "form": form, "goal": my_goal })

@login_required
def edit_goal(request, pk):
  OG_goal = get_object_or_404(Goal, pk=pk)
  if request.method == "POST":
    form = GoalForm(request.POST)
    if form.is_valid():
      goal = form.save(commit=False, instance=goal)
      goal.user = request.user
      goal.save()
      OG_goal.delete()
      return redirect('display-goal')
  else:
    form = GoalForm()
    form.fields['name'].initial=OG_goal.name
    form.fields['operator'].initial=OG_goal.operator
    form.fields['numeric_goal'].initial=OG_goal.numeric_goal
    form.fields['units'].initial=OG_goal.units
  return render(request, 'goalkeeper/edit_goal.html', { "form": form, "goal": OG_goal })

