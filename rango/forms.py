from django import forms
from rango.models import Page, Category
class CategoryForm(forms.ModelForm):
	name=forms.CharField(max_length=128, help_text="Please enter the category name.")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	slug = forms.CharField(widget=forms.HiddenInput(), required = False)
	
	class Meta:
		model= Category
		fields = ('name',)

class PageForm(forms.ModelForm):
	title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
	url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial = 0)
	
	class Meta:
		model = Page
		exclude =('category',)
	
	def clean(self):
		cleaned_data = self.cleaned_data
		url = cleaned_data.get('url')
		title = cleaned_data.get('title')
		pages_list=Page.objects.order_by('views')
		for inserted_page in pages_list:
			if inserted_page.title==title:
				raise forms.ValidationError("Inserted title already exist")
			if inserted_page.url==url:
				raise forms.ValidationError("Inserted url already exist")
		if url and not url.startswith('http://'):
			url = 'http://' + url
			cleaned_data['url']= url
		return cleaned_data
		
	