from django.shortcuts import render
import requests

def main_page(request):
	return render(request, "main.html")