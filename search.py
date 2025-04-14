from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, TEXT, KEYWORD
from whoosh.writing import AsyncWriter
import os

# Define the schema for your index
schema = Schema(
    id=KEYWORD(stored=True, unique=True),
    name=TEXT(stored=True),
    country=TEXT(stored=True),
    description=TEXT(stored=True)
)

# Create an index directory
if not os.path.exists("search_index"):
    os.mkdir("search_index")

# Create the index
index = create_in("search_index", schema)

def index_campaigns(campaigns):
    index = open_dir("search_index")
    writer = AsyncWriter(index)
    for campaign in campaigns:
        writer.update_document(
            id=str(campaign["id"]),
            name=campaign["Name"],
            country=campaign["Country"],
            description=campaign["Description"]
        )
    
    writer.commit()