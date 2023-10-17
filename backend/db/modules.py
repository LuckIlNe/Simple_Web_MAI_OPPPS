import xml.etree.ElementTree as ET
import logging
from datetime import date


def saveXMLArticle(article):
    #logging.debug(XMLstring)
    #articleXML = ET.ElementTree(ET.fromstring(XMLstring))
    articleDict = dict()
    for elem in article:
        logging.debug("------------------- %s ----------" % elem.tag)
        if elem.attrib["type"] == 'list':
            articleDict[elem.tag] = [subelem.text for subelem in elem ]
        elif elem.tag == "date":
            dateList = list(map(int, elem.text.split("/")))
            articleDict[elem.tag] = date(dateList[2], dateList[1], dateList[0])
        else:
            articleDict[elem.tag] = elem.text.lstrip("<![CDATA[ ").rstrip(" ]]>")
    return articleDict

if __name__ == "__main__":

    with open("2022-05-13-moon-flowers.xml", "r", encoding="utf-8") as f:
        article = f.read()
    print(saveXMLArticle(article))
