from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
#    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatRoomConsumer),
     re_path(r'ws/chat/a1/', consumers.ChatRoomConsumer),
]
