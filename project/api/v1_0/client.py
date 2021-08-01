# -*- coding: utf-8 -*-
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.status import *
from project.apps.core.models import Client, ClientPost


class ClientViewSet(ViewSet):
    permission_classes = (AllowAny,)

    def list(self, request):
        clients = Client.objects.all()
        clients_json = []
        for client in clients:
            client_json = client.as_json()
            posts = ClientPost.objects.filter(client=client)
            client_json['posts'] = [post.as_json() for post in posts ]
            clients_json.append(client_json)
        return Response(clients_json, status=HTTP_200_OK)