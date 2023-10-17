from asyncio.log import logger
import aiohttp_jinja2
from aiohttp import web
import logging
import xml.etree.ElementTree as ET
from aiohttp.web_request import FileField, MultipartReader

from datetime import date
import re

from db.functions import (
    update_article,
    create_article,
    find_by_categories,
    find_by_authors,
    save_xml_file,
    find_by_id,
    find_by_date,
    get_all_categories,
    get_all_authors,
    delte_article_by_id
)

class Main(web.View):

    @aiohttp_jinja2.template('index.html')
    async def get(self):
        if "search" in self.request.rel_url.query and "parameter" in self.request.rel_url.query:
            search = self.request.rel_url.query['search']
            parameter = self.request.rel_url.query['parameter']
            articles = []
            if parameter == '1':
                articles = await find_by_categories(self.request.app['db_engine'], re.split(r"\s*\,\s*", search))
            elif parameter == '2':
                articles = await find_by_authors(self.request.app['db_engine'], re.split(r"\s*\,\s*", search))
            elif parameter == '3':
                articles = await find_by_date(self.request.app['db_engine'], date(*map(int, search.split("-")[::-1])))
                #articles = await find_by_date(self.request.app['db_engine'], "-".join(search.split("-")[::-1]))
            else:
                pass

            return { 'search': True, 'amount': len(articles), 'articles': articles}
        
        else:
            return { 'search': False}

class Article(web.View):

    async def get(self):
        opt = self.request.match_info['option']
        if opt in ("show", "edit"):
            id = self.request.rel_url.query['id']

            # get article data from db

            if opt == "show":
                article = await find_by_id(self.request.app['db_engine'], int(id))
                return aiohttp_jinja2.render_template("show.html", self.request, context={'article': article})
            if opt == "edit":

                article = await find_by_id(self.request.app['db_engine'], int(id))
                allAuthors = await get_all_authors(self.request.app['db_engine'])
                allCategories = await get_all_categories(self.request.app['db_engine'])
                return aiohttp_jinja2.render_template("edit.html", self.request,
                                                        context={
                                                            'article': article,
                                                            'allAuthors': allAuthors,
                                                            'allCategories': allCategories
                                                    })
        elif opt == "create":
            allAuthors = await get_all_authors(self.request.app['db_engine'])
            allCategories = await get_all_categories(self.request.app['db_engine'])
            return aiohttp_jinja2.render_template("create.html", self.request, 
                                        context={
                                            'allAuthors': allAuthors,
                                            'allCategories': allCategories,
                                        })
        elif opt == "remove":
            id = self.request.rel_url.query['id']
            await delte_article_by_id(self.request.app['db_engine'], int(id))
            raise web.HTTPFound("/")
        else:
            logging.debug(self.request.match_info['option'])
            raise web.HTTPFound('/')

    @aiohttp_jinja2.template('article.html')
    async def post(self):
        logging.debug("post")
        opt = self.request.match_info['option']
        if opt == "edit":
            id = self.request.rel_url.query['id']
            article = dict(await self.request.post())
            article['id'] = int(id)

            # костыль 
            article['categories'] = [article['categories']]
            article['authors'] = [article['authors']]
            article['date'] = date(*map(int, article["date"].split("-")))
            logging.debug("---------- %s ----------------" % article)
            await update_article(self.request.app['db_engine'], article)

            return web.HTTPFound(f"/article/show?id={int(id)}")

        elif opt == "create":
            data = await self.request.post()
            if isinstance(data["xmlfile"], FileField):
                file = data["xmlfile"].file
                logging.debug(file)
                #logging.debug(file.read().decode('utf-8'))
                tree = ET.ElementTree(ET.fromstring(file.read().decode('utf-8')))
                root = tree.getroot()
                articleId = await save_xml_file(self.request.app['db_engine'], root)

            else:
                article = dict(data)
                logging.debug(article)
                article['date'] = date(*map(int, article["date"].split("-")))
                article['categories'] = article['categories'].split(",")
                article['authors'] = article['authors'].split(",")
                logging.debug(article)
                del article["xmlfile"]
                logging.debug("Method: %s data: %s" % (opt, article))
                articleId = await create_article(self.request.app['db_engine'], article)

            return web.HTTPFound(f"/article/show?id={articleId}")

        else:
            logging.debug(self.request.match_info['option'])
            raise web.HTTPNotFound()
        return {
            "context": [1,2,3]
        }

    async def edit(self):
        pass