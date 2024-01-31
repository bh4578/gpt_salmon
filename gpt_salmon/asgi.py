"""
ASGI config for gpt_salmon project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

# asgi.py

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from gpt_salmon import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gpt_salmon.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    # 使用 AuthMiddlewareStack 将 WebSocket 连接添加到连接范围
    'websocket': AuthMiddlewareStack(
        URLRouter(
            # 在这里添加你的 WebSocket 路由
            routing.websocket_urlpatterns
        )
    ),
})

