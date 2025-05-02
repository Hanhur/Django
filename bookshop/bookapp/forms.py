from django import forms

class BookForm(forms.Form):
    book_name = forms.CharField(
        label = 'Název knihy',
        max_length = 90,
        required = True
    )
    book_price = forms.IntegerField(
        label = 'Cena knihy',
        min_value = 1,
        max_value = 10000,
        required = True
    )