from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from blogs.serializer import RegisterSerializer, BlogSerializer
from blogs.models import BlogModel
from django.db.models import Q

# Create your views here.
@csrf_exempt
def userRegister(request):
    if request.method == "POST":
        recieved_data = json.loads(request.body)
        print(recieved_data)
        serialized_data = RegisterSerializer(data =recieved_data)
        if serialized_data.is_valid():
            serialized_data.save()
            return HttpResponse(json.dumps({"status":"success"}))
        else:
            return HttpResponse(json.dumps({"status":"failed"}))
        
@csrf_exempt
def userBlog(request):
    if request.method == "POST":
        recieved_data = json.loads(request.body)
        print(recieved_data)
        serializer_check = BlogSerializer(data = recieved_data)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse(json.dumps({"status":"success"}))
        else:
            return HttpResponse(json.dumps({"status":"failed"}))
        

@csrf_exempt
def viewBlog(request):
    if request.method == "POST":
        blog_list = BlogModel.objects.all()
        serialized_data = BlogSerializer(blog_list, many = True)
        return HttpResponse(json.dumps(serialized_data.data))
    
@csrf_exempt
def viewMyBlog(request):
    if request.method == "POST":
        recieved_data = json.loads(request.body)
        print(recieved_data)
        getUser = recieved_data["userId"]
        data = list(BlogModel.objects.filter(Q(userId__icontains = getUser)).values())
        return HttpResponse(json.dumps(data))
