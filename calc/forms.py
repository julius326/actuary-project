# calc/forms.py
from django import forms


class FrequencyForm(forms.Form):
    x1 = forms.FloatField(label="Value 1 (x1)")
    f1 = forms.IntegerField(label="Frequency 1 (f1)")

    x2 = forms.FloatField(label="Value 2 (x2)")
    f2 = forms.IntegerField(label="Frequency 2 (f2)")

    x3 = forms.FloatField(label="Value 3 (x3)")
    f3 = forms.IntegerField(label="Frequency 3 (f3)")

    x4 = forms.FloatField(label="Value 4 (x4)")
    f4 = forms.IntegerField(label="Frequency 4 (f4)")
