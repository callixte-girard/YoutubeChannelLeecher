# from notion.block import VideoBlock
from static import variables as var

def insertPocketArticlesIntoTable(table_url, articles):
    # Access a database using the URL of the database page or the inline block
    art_index = 0
    cv = var.client.get_collection_view(table_url)
    for art in articles:
        art_index += 1
        row = cv.collection.add_row()
        # if art.title != art.link : ### it's better with url as title than nothing
        row.name = art.title
        row.url = art.link
        row.pocket_timestamp = art.added_on
        # row.imported_from_pocket = True
        langs = []
        for tag in art.tags:
            lang = tag.split(" ")[1]
            lang = lang.replace("-", " ")
            print("[ {} ]".format(lang))
            langs.append(lang)
        row.languages = langs
        print("{} / {} done".format(art_index, len(articles)))
        print("---------------------")
        # render = row.children.add_new(VideoBlock, width=200)
        # render.set_source_url(art.link)
