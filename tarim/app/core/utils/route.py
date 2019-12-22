from flask import request

def in_route(routes):
    if routes is None:
        return False
    if not isinstance(routes, list):
        routes = [routes]
    for route in routes:
        if route is None:
            continue
        if '/' in route:
            if route in request.url:
                return True
        route = route.replace('.*', '')
        if route in request.endpoint:
            return True
    return False
