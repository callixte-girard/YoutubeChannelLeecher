from static import constants as cst
from static import variables as var
from notion_so import collection as coll
from uuid import uuid1
from random import choice


def addNewValueToCollectionMultiSelect(cv_url, prop, value, color=None):
    """`prop` is the name of the multi select property."""
    if color is None:
        color = choice(cst.notion_colors)
    
    collection = coll.getCollectionFromViewUrl(cv_url)    
    collection_schema = collection.get("schema")
    # print(collection_schema, end=cst.line)    

    prop_schema = next(
        (v for k, v in collection_schema.items() if v["name"] == prop), None
    )
    # print(prop_schema, end=cst.line)

    # test = collection.get_schema_property(prop)
    # print(test, end=cst.line)

    if not prop_schema:
        raise ValueError(
            f'"{prop}" property does not exist on the collection!'
        )
    if prop_schema["type"] != "multi_select" and prop_schema["type"] != "select":
        raise ValueError(f'"{prop}" is neither a single nor a multi select property!')

    if "options" not in prop_schema: prop_schema["options"] = []

    dupe = next(
        (o for o in prop_schema["options"] if o["value"] == value), None
    )

    if dupe:
        raise ValueError(f'"{value}" already exists in the schema!')
    else:
        prop_schema["options"].append(
            {"id": str(uuid1()), "value": value, "color": color}
        )
        collection.set("schema", collection_schema)
