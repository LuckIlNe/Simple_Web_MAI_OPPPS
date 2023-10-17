from .models import (
    Articles
)
from sqlalchemy.sql import select
from sqlalchemy.dialects.postgresql import (
    array
)

from .modules import (
    saveXMLArticle
)

import logging

async def create_article(engine, article_dict):

    logging.debug(article_dict['authors'])
    article_dict['authors'] = array(article_dict['authors'])
    logging.debug(article_dict['authors'])
    article_dict['categories'] = array(article_dict['categories'])

    newArticleId = None
    async with engine.connect() as conn:
        stmt = Articles.__table__.insert().values(article_dict).returning(Articles.__table__.c.id)
        result = await conn.execute(stmt)
        for row in result:
            newArticleId = row['id']
    return newArticleId

async def update_article(engine, article_dict):

    article_dict['authors'] = array(article_dict['authors'])
    article_dict['categories'] = array(article_dict['categories'])
    async with engine.connect() as conn:
        stmt = Articles.__table__.update().where(
            Articles.__table__.c.id == article_dict['id']).values(article_dict)
        result = await conn.execute(stmt)
    return result

async def delte_article_by_id(engine, id):

    async with engine.connect() as conn:
        stmt = Articles.__table__.delete().where(
            Articles.__table__.c.id == id)
        result = await conn.execute(stmt)
    return result

async def find_by_categories(engine, categories):

    articlesByCategories = []
    async with engine.connect() as conn:
        stmt = Articles.__table__.select().where(
            Articles.__table__.c.categories.contains(categories))
        result = await conn.execute(stmt)
        for row in result:
            articlesByCategories.append(row)

    return articlesByCategories

async def find_by_authors(engine, authors):

    articlesByAuthors = []
    async with engine.connect() as conn:
        stmt = Articles.__table__.select().where(
            Articles.__table__.c.authors.contains(authors))
        result = await conn.execute(stmt)
        for row in result:
            articlesByAuthors.append(row)
    return articlesByAuthors

async def find_by_date(engine, date):

    articlesByDate = []
    async with engine.connect() as conn:
        stmt = Articles.__table__.select().where(
            Articles.__table__.c.date == date)
        result = await conn.execute(stmt)
        for row in result:
            articlesByDate.append(row)
    return articlesByDate

async def find_by_id(engine, id):

    async with engine.connect() as conn:
        stmt = Articles.__table__.select().where(
            Articles.__table__.c.id == id)
        result = await conn.execute(stmt)
        for row in result:
            article = row
    return article

async def save_xml_file(engine, XML):
    artDict = saveXMLArticle(XML)
    logging.debug(artDict)
    return await create_article(engine, artDict)


async def get_all_authors(engine):

    authors = set()
    async with engine.connect() as conn:
        stmt = Articles.__table__.select()
        result = await conn.execute(stmt)
        for row in result:
            authors.update(row['authors'])
    return list(filter(lambda x: x is not None and len(x.split(" ")) == 2,list(authors)))

async def get_all_categories(engine):

    categories = set()
    async with engine.connect() as conn:
        stmt = Articles.__table__.select()
        result = await conn.execute(stmt)
        for row in result:
            categories.update(row['categories'])
    return list(categories)







# async def find_by_categories1(session, categories):

#     articlesByCategories = session.run_sync(session.query(Articles).filter(Articles.categories.any(categories)).all())
#     print(articlesByCategories)

#     return articlesByCategories
