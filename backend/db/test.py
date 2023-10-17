from sqlalchemy.ext.asyncio import  create_async_engine, AsyncSession
from functions import (
    create_article, 
    update_article,
    find_by_categories,
    save_xml_file,
    get_all_categories,
    get_all_authors
)
from datetime import date
from os import listdir
from os.path import isfile, join
import xml.etree.ElementTree as ET

import asyncio
import os

if __name__ == "__main__":
    DSN = "postgresql+asyncpg://postgres:root@127.0.0.1:5432/Articles"
    engine = create_async_engine(DSN, echo=True, isolation_level="AUTOCOMMIT")
    session = AsyncSession(engine)

    # Create

    # article = {
    #     'title': 'test3',
    #     'source': 'test://n1.ru/test3',
    #     'text': 'test test test2',
    #     'date': date.today(),
    #     'capasity': '1.1',
    #     'authors': ['test2', 'test3'],
    #     'categories': ['War']
    # }
    # r = asyncio.run(create_article(engine, article))
    # print(type(r))

    # Update
    # article = {
    #     'title': 'test3',
    #     'source': 'test://n1.ru/test3',
    #     'text': 'test test test2',
    #     'date': date.today(),
    #     'capasity': '1.2',
    #     'authors': ['test1', 'test1'],
    #     'categories': ['Weapon']
    # }
    # article["id"] = 18
    # asyncio.run(update_article(engine, article))

    # categories = ["War", "Peace"]
    # asyncio.run(find_by_categories(engine, categories))
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(find_by_categories(session, categories))


    # articles = []
    # mypath = r"C:\Users\Crumpet\Desktop\PVK\parser\articles"
    # for filename in listdir(mypath):
    #     if isfile(join(mypath, filename)):
    #         with open(join(mypath, filename), "r", encoding="utf-8") as f:
    #             tree = ET.ElementTree(ET.fromstring(f.read()))
    #             articles.append(tree.getroot())
    # async def arts(articles):
    #     for art in articles:
    #         await save_xml_file(engine, art)
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(arts(articles))


    authors = asyncio.run(get_all_authors(engine))
    print(authors)

    #authors = asyncio.run(get_all_categories(engine))
    #print(authors)