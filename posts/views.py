from django.shortcuts import render
from django.http import JsonResponse
from .models import Posts
from json import loads
from datetime import date
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index (request) :
    if request.method == "GET":
        
        routes = {
            'routes':[
                {
                    'route': '/',
                    'method': 'GET',
                    'response': 'returns all available routes'
                },
                {
                    'route': '/all/',
                    'method': 'GET',
                    'response': 'returns all posts available in database'
                    
                },
                {
                    'route': '/all/id',
                    'method': 'GET',
                    'response': 'returns the post with provided id'
                    
                },
                {
                    'route': '/create/',
                    'method': 'POST',
                    'parameter': {
                        'title': 'maximum limit of 200 characters (required)',
                        'description': 'Text field (required)',
                        'created by': 'name of the user 100 characters limit (optional)'
                    },
                    'response': 'creates a post with the provided title and description'
                },
                {
                    'route': '/create/id',
                    'method': 'PATCH',
                    'usage': 'to edit the post with provided id but atleast one parameted is required',
                    'parameter': {
                        'title': 'new title with maximum limit of 200 characters (optional)',
                        'description': 'new description text field (optional)',
                        'created by': 'name of the user (optional)'
                    },
                    'response': 'edit the post accordingly to provided parameters'
                },
                {
                    'route': '/remove/id',
                    'method': 'DELETE',
                    'usage': 'to delete the post with provided id',
                    'response': 'deletes the post with provided id from database'
                },
            ]
        }
        
        return JsonResponse(routes)
    
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
                "title": post.title
            }
            
            rsp_post.append(data)
        return JsonResponse({"success":"true",'posts': rsp_post})

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
        
        return JsonResponse({"success":"true","something":"something"})

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

@csrf_exempt
def delete_post(request,*args, **kwargs):
    if request.method == "DELETE":
        id = kwargs['id']
        post = Posts.objects.get(id=id)
        post.delete()
        return JsonResponse({"success":"true"})