from sanic import Blueprint
from sanic.response import json

bp = Blueprint("health")


@bp.get("/health")
def health_route(request):
    response = {"message": "hello there"}
    return json(response, 200)
