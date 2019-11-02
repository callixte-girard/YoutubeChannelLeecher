from static import methods as mth 
from static import constants as cst
from notion.client import NotionClient

### quick setup settings
import locale
locale.setlocale(locale.LC_TIME, "fr_FR")

### init important variables for the prog
driver = mth.initChromiumConfiguredProperly()
client = NotionClient(token_v2 = cst.notion_token)