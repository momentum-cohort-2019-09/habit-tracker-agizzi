from django import forms
from .models import User, Goal, History

class GoalForm(forms.ModelForm):
  class Meta:
    model = Goal
    fields = ['name', 'operator', 'numeric_goal', 'units']

class HistoryForm(forms.ModelForm):
  class Meta:
    model = History
    fields = ['day_of_input', 'daily_input']