from django import urls


class Route:
    def __init__(self, url_prefix='', name_prefix=''):
        self.url_prefix = url_prefix.strip('/')
        self.name_prefix = name_prefix
        self.routes = {}

    def __call__(self, path=None, name=None):
        def wrapper(f):
            urlname = self.name_prefix + (name or f.__name__)
            urlpath = path or f.__name__.replace('_', '-')
            urlpath = self.url_prefix + '/' + urlpath.lstrip('/')
            self.routes[urlname] = urlpath, f
            return f
        if callable(path):
            f = path
            path = None
            return wrapper(f)
        return wrapper

    @property
    def patterns(self):
        return [urls.path(path.lstrip('/'), handler, name=name)
                for name, (path, handler) in self.routes.items()]

    @property
    def names(self):
        return {name: '/' + path.lstrip('/')
                for name, (path, _) in self.routes.items()}
