# -*- coding: utf8 -*-

import asyncio
import time
import base64
import requests
from cryptography import fernet
from time import sleep
from aiohttp import web
from aiohttp_session import setup, get_session, session_middleware
from aiohttp_session.cookie_storage import EncryptedCookieStorage

async def handler(request):
    session = await get_session(request)
    key = session['key'] if 'key' in session else None 
    text = format(key)
    return web.Response(text=text)

async def posthandler(request):
    session = await get_session(request)
    session['key'] = request.text()
    return web.Response('')

async def make_app():
    app = web.Application()
    fernet_key = fernet.Fernet.generate_key()
    secret_key = base64.urlsafe_b64decode(fernet_key)
    setup(app, EncryptedCookieStorage(secret_key))
    app.add_routes([web.get('/', handler)])  
    app.add_routes([web.post('/', posthandler)])
    return app

if __name__ == '__main__':
    web.run_app(make_app())