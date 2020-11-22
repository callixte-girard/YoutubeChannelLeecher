from static import constants as cst
from static import methods as mth
from notion.client import NotionClient


### init important variables for the prog
driver = mth.initChromiumConfiguredProperly()
client = NotionClient(token_v2=cst.notion_token)