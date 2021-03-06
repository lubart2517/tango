# -*- coding: utf-8 -*- 
from django import forms
from rango.models import Page, Category, UserProfile
from django.contrib.auth.models import User
class CategoryForm(forms.ModelForm):
	name=forms.CharField(max_length=128, help_text="Введіть ім'я нової категорії")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	slug = forms.CharField(widget=forms.HiddenInput(), required = False)
	
	class Meta:
		model= Category
		fields = ('name',)

class PageForm(forms.ModelForm):
	title = forms.CharField(max_length=128, help_text="Введіть імя сторінки.")
	url = forms.URLField(max_length=200, help_text="Введіть адресу сторінки.")
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
				self.add_error('title','Inserted title already exist')
				
			if inserted_page.url==url:
				self.add_error('url','Inserted url already exist')
		if url and not url.startswith('http://'):
			url = 'http://' + url
			cleaned_data['url']= url
		return cleaned_data

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	
	class Meta:
		model = User
		fields = ('username', 'email', 'password')
class UserProfileForm(forms.ModelForm):
	class Meta:
		model= UserProfile
		fields = ('website', 'picture')

	