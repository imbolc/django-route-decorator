A flask-style `route` decorator for django views
================================================

> Simple things should be simple, complex things should be possible (c)Alan Kay

There is some contradiction between decoupling and DRY principles
in django urls. Why not use flasky `@route` decorator to fix this issue?

Simple things should be simple
------------------------------
Just decorate your views with an instance of `Route`:

    from route_decorator import Route

    route = Route()

    @route
    def foo_view(request):
        ...

    @route
    def bar_view(request):
        ...


And don't forget to add the routes into your `urls.py`:

    from . import views

    urlpatterns += views.route.patterns


Now you have your views binded to `/foo-view` and `/bar-view` respectively.

You can also get map urlname -> url with `route.names` to pass them to
frontend eg. In our case it would be:

    {
        'foo_view': '/foo-view',
        'bar_view': '/bar-view'
    }


Complex things should be possible
---------------------------------
You can pass `url_prefix` and `name_prefix` to route:

    route = Router('/api', 'api:')

And also use `path` and `name` in a decorator:

    @route('/baz', 'baz-name')
    def baz_view(request):
        ...

So it would be bind to `/api/baz` with name `api:baz-name`.
