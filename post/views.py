from django.shortcuts import render
from django.utils import HttpRequest


class Post(request):
	def data_list(self):
		return HttpRequest('All the list')