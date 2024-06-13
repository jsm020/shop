import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import OriginValidator
from django.core.asgi import get_asgi_application
import userlar.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Rayxonshop.settings')

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": OriginValidator(
            AuthMiddlewareStack(
                URLRouter(
                    userlar.routing.websocket_urlpatterns
                )
            ),
            ["*"]
        ),
    }
)