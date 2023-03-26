from django.shortcuts import render
from django.http import JsonResponse
from .models import Posts
from json import loads
from datetime import date
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index (request) :
    if request.method == "GET":
        
        routes = { "routes": [
                "/","/create","/create/<id>","/all","/all/<id>", "/delete/<id>"
            ]
        }
        
        return JsonResponse(routes)
    else:
        return JsonResponse({"success": "false", "error":"Wrong method use 'GET' method for this enpoint"})
    
@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        posts = loads(request.body)
        rsp_post = []
        for instance in posts['posts']:
            post = Posts.objects.create(
                title = instance['title'],
                description = instance['description'],
                created_at = date.today(),
                last_updated = date.today(),
                username = instance.get("username",None)
            )
            data = {
                "id": post.id,
                "title": post.title,
                "status": "Post created"
            }
            rsp_post.append(data)
        return JsonResponse({"success":"true",'posts': rsp_post})
    else:
        return JsonResponse({"success":"false","error":"Wrong request method use 'POST' method for this endpoint"})

@csrf_exempt
def update_post(request, *args, **kwargs):
    if request.method == "PUT":
        id = kwargs['id']
        post = Posts.objects.get(id=id)
        data = loads(request.body)
        print(data)
        print(id)
        title = data.get("title",None)
        description = data.get("description",None)
        username = data.get("usaername",None)
        
        if title != None:
            post.title = title
        
        if description != None:
            post.description = description
        
        if username != None:
            post.username = username
        post.save()
        return JsonResponse({"success":"true","respons":"Post updated successfully"})
    else:
        return JsonResponse({"success":"false","error":"Wrong method, use 'PUT' method for this endpoint"})

def all_post(request):
    if request.method == "GET":
        posts = Posts.objects.all().order_by("last_updated")
        post_list = []
        for post in posts:
            data =  {}
            data['id'] = post.id
            data['title'] = post.title
            data['description'] = post.description   
            data['username'] = post.username
            data['created at'] = post.created_at
            data['last updated'] = post.last_updated
            post_list.append(data)
        return JsonResponse({'posts':post_list})
    else:
        return JsonResponse({"success":"true","error":"Wrong request method use 'GET' method for this endpoint"})

def sngl_post(request, *args, **kwargs):
    if request.method == "GET":
        id = kwargs['id']
        post = Posts.objects.get(id=id)
        data = {
            "id": post.id,
            "title": post.title,
            "description": post.description,
            "username": post.username,
            "created at": post.created_at,
            "last updated": post.last_updated
        }
        return JsonResponse({"post":data})
    else :
        return JsonResponse({"success":"false","error":"use GET method to request for current path"})

@csrf_exempt
def delete_post(request,*args, **kwargs):
    if request.method == "DELETE":
        id = kwargs['id']
        if id != None:
            try:
                post = Posts.objects.get(id=id)
            except :
                return JsonResponse({"success":"false","error":"Post does not exist"})
        else:
            return JsonResponse({"success":"false","error":"no id provided"})
        
        post.delete()
        return JsonResponse({"success":"true","status":"post with id " + str(id) + " successfully deleted"})
    else :
        return JsonResponse({"success":"flase","error":"Wrong request method use 'DELETE' method for this endpoint"})