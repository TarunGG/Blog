from django.shortcuts import render
from django.http import JsonResponse
from .models import Posts

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
