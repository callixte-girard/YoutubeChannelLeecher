from static import variables as var


### first select page to play with
# page = client.get_block("https://www.notion.so/Vid-os-sauvegarder-8fe8f4780c394a01851c631ee19e346d")
page = var.client.get_block("https://www.notion.so/376fe76b991d4c0d8026929c438ebaf0")

### obvious tests
# print("der page title ist:", page.title)

# page.title = "Instructive YouTube Channels"
# print("der page title ist:", page.title)

# print("parent of [{}] is [{}]".format(page.title, page.parent.title))
# print("children of [{}] are [{}]".format(page.title, page.children))

### get entries of a table
# Access a database using the URL of the database page or the inline block
cv = var.client.get_collection_view("https://www.notion.so/376fe76b991d4c0d8026929c438ebaf0?v=6906f6eaae864c1bb4ba9cda654cf412")

# List all the records with "Bob" in them
row = cv.collection.add_row()
row.name = "this is a test"
row.language = ["javascript"]
row.url = "www.pipou.fr"
row.imported_from_pocket = True