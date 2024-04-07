from django import forms
from books.models import book

# class bookForm(forms.Form):
#     title = forms.CharField(max_length=100, label='Book Title', required=True)
#     no_pages = forms.IntegerField(label='no_pages', required=True)
#     author = forms.CharField(max_length=100, label='Author', required=True)
#     price = forms.IntegerField(label='Price', required=True)
#     image = forms.ImageField(required=False, label='Image')

class BookModelForm(forms.ModelForm):
    class Meta:
        model = book
        fields = '__all__'

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title)<2:
            raise forms.ValidationError('title length must be greater than 2 chars')
        return title
    
    def clean_author(self):
        author = self.cleaned_data['author']
        if len(author)<2:
            raise forms.ValidationError('author length must be greater than 2 chars')
        return author
    
    def clean_no_pages(self):
        no_pages = self.cleaned_data['no_pages']
        if not isinstance(no_pages, int):
            raise forms.ValidationError('Number of pages must be an integer')
        return no_pages
    
    def clean_price(self):
        price = self.cleaned_data['price']
        if not isinstance(price, (int, float)):
            raise forms.ValidationError('Price must be a number')
        return price
    