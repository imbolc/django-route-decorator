from typing import Callable, Dict, List, Tuple, Union

from django import urls


class Route:
    def __init__(
        self,
        # a prefix for any url defined by the decorator
        url_prefix: str = "",
        # a prefix for any url-name
        name_prefix: str = "",
        # should we treat double underscores in the function name
        # as a folder if no explicit route provided
        double_underscore_to_slash: bool = True,
    ):
        self.url_prefix = url_prefix.strip("/")
        self.name_prefix = name_prefix
        self.double_underscore_to_slash = double_underscore_to_slash
        self.routes: Dict[str, Tuple[str, Callable]] = {}

    def __call__(self, path: Union[str, Callable] = None, name: str = None):
        def wrapper(f: Callable) -> Callable:
            urlname = self.name_prefix + (name or f.__name__)
            urlpath = path or f.__name__
            if self.double_underscore_to_slash:
                urlpath = urlpath.replace("__", "/")  # type: ignore
            urlpath = urlpath.replace("_", "-")  # type: ignore
            urlpath = self.url_prefix + "/" + urlpath.lstrip("/")
            self.routes[urlname] = urlpath, f
            return f

        if callable(path):
            f = path
            path = None
            return wrapper(f)
        return wrapper

    @property
    def patterns(self) -> List[urls.URLPattern]:
        return [
            urls.path(path.lstrip("/"), handler, name=name)
            for name, (path, handler) in self.routes.items()
        ]

    @property
    def names(self) -> Dict[str, str]:
        return {
            name: "/" + path.lstrip("/")
            for name, (path, _) in self.routes.items()
        }
