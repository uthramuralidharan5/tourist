from rest_framework import routers, viewsets


class MyRouter(routers.DefaultRouter):
    def get_routes(self, viewset):
        routes = []
        if hasattr(viewset, 'get_extra_routes'):
            viewset_instance = viewset()
            extra_routes = viewset_instance.get_extra_routes()
            routes.extend(extra_routes)
        return super().get_routes(viewset) + routes
