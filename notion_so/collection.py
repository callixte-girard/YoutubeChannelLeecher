from static import constants as cst
from static import variables as var


def getCollectionFromViewUrl(cv_url):
    coll_view = var.client.get_collection_view(cv_url, force_refresh=True) ### very important to always force refresh
    collection = coll_view.collection
    return collection


def getCorrespondingRowFromVidUrl(collection, vid_url):
    rows = collection.get_rows()
    for row in rows:
        # print(row.url)
        if row.url == vid_url: return row
    return None