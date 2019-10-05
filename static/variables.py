from static import methods as mth 
from static import constants as cst
from notion.client import NotionClient

# driver = mth.initFirefoxConfiguredProperly()
client = NotionClient(token_v2 = cst.notion_token)
