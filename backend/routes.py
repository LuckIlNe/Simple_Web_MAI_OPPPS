from views import Main, Article

def setup_routes(app):
    app.router.add_route('GET', '/', Main)
    app.router.add_route('*', '/article/{option}', Article)
    app.router.add_route('GET', '/articles', Main)