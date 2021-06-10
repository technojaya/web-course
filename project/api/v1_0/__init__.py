# -*- coding: utf-8 -*-
from rest_framework import routers

from project.api.v1_0.client import ClientViewSet

router = routers.SimpleRouter()

router.register(r'clients', ClientViewSet, basename='clients')