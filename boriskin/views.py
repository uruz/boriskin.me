import asyncio
from pyramid.response import Response
from pyramid_asyncio.view import coroutine_view_config
import aiohttp
import json

@coroutine_view_config(route_name='say_hello', renderer='hello.jinja2')
def say_hello(request):
    response = yield from aiohttp.request('GET', 'https://api.github.com/users/uruz')
    body = yield from response.read()
    response = json.loads(body.decode('utf-8'))
    return {'name': response['name'], 'location': response['location']}

@coroutine_view_config(route_name='home', renderer='home.jinja2')
def homepage(request):
    return {}
