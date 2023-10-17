from aiohttp import web
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from aiohttp_session import setup, session_middleware
from sqlalchemy.ext.asyncio import  create_async_engine

import jinja2
import aiohttp_jinja2
import logging
import asyncio

from routes import setup_routes
from db.init import setup_db
from settings import config

async def init_app():
    #fernet_key = fernet.Fernet.generate_key()
    #secret_key = base64.urlsafe_b64decode(fernet_key)
    app = web.Application(#loop=loop,
        middlewares=[
    #        session_middleware(EncryptedCookieStorage(secret_key)),
    ],
    handler_args={'max_field_size': 20000, 'max_line_size': 20000})
    app['config'] = config
    await setup_db(app)
    setup_routes(app)
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('./templates'))

    return app

if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s: %(message)s",
        level="DEBUG"
    )

    app = init_app()
    web.run_app(app)

"""
    loop = asyncio.run()

    try:
        app = loop.run_until_complete(init_app(loop))
        web.run_app(app, host="0.0.0.0", port=8080)
    except Exception:
        logging.warn(Exception)
        loop.stop()
    finally:
        loop.stop()
"""