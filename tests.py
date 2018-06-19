from route_decorator import Route


def test_without_prefixes():
    route = Route()

    @route
    def foo_view(request):
        pass

    @route('/bar', 'bar-name')
    def bar_view(request):
        pass

    assert len(route.names) == 2
    assert route.names['foo_view'] == '/foo-view'
    assert route.names['bar-name'] == '/bar'

    assert len(route.patterns) == 2
    assert str(route.patterns[0]) == "<URLPattern 'foo-view' [name='foo_view']>"  # noqa
    assert str(route.patterns[1]) == "<URLPattern 'bar' [name='bar-name']>"


def test_with_prefixes():
    route = Route('/api', 'api:')

    @route
    def api_foo(request):
        pass

    assert route.names['api:api_foo'] == '/api/api-foo'

    @route('/bar', 'bar-name')
    def bar_view(request):
        pass

    assert route.names['api:bar-name'] == '/api/bar'
