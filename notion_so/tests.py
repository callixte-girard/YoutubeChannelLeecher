from notion.client import NotionClient

client = NotionClient(token_v2 = "aecb30784b091b5754d38501093f8230d4dbf60db6d7a727852a931fda4fc596c80126ece221c4b4f3910268a63425eeaf9b62c9b606d7437141d88b85d0e0a039061cdfb4d8ae172e7fef8dff75")

page = client.get_block("https://www.notion.so/Vid-os-sauvegarder-8fe8f4780c394a01851c631ee19e346d")
print("der page title ist:", page.title)

page.title = "Instructive YouTube Channels"
print("der page title ist:", page.title)