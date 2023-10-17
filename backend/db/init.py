import asyncpg
from sqlalchemy.ext.asyncio import  create_async_engine
from sqlalchemy.orm import Session


def construct_async_db_url(config):
    DSN = "postgresql+asyncpg://{user}:{password}@{host}:{port}/{database}"#?async_fallback=true"
    config_db = config
    return DSN.format(
        user=config_db['user'],
        password=config_db['password'], 
        database=config_db['database'], 
        host=config_db['host'],
        port=config_db['port']
    )

async def setup_db(app):
    print(construct_async_db_url(app['config']['postgres']))
    engine = create_async_engine(construct_async_db_url(app['config']['postgres']), echo=True, isolation_level="AUTOCOMMIT")
    app['db_engine'] = engine
    app['db_session'] = Session(engine)
    #return pool
    return 1