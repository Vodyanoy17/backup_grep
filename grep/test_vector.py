import pymongo
import requests
from termcolor import colored


hf_token = "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"
embedding_url = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"

def generate_embedding(text: str) -> list[float]:
   response = requests.post(
		embedding_url,
		headers={"Authorization": f"Bearer {hf_token}"},
		json={"inputs": text})
   
   if response.status_code != 200:
      raise ValueError(f"Request failed with status code {response.status_code}: {response.text}")
   return response.json()


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def enbeding_data(generate_embedding):
   uri = "mongodb+srv://scott:tiger@cluster0.v9uas.mongodb.net/?retryWrites=true&w=majority"
   # Create a new client and connect to the server
   client = MongoClient(uri, server_api=ServerApi('1'))

   #client = pymongo.MongoClient("<Your MongoDB URI>")
   # Connect to your 'sample_airbnb' database
   db = client.sample_airbnb
   # Get the 'listingsAndReviews' collection
   collection = db.listingsAndReviews

   # db = client['sample_airbnb']
   # collection = db['listingsAndReviews']

   # Fetch all documents from the collection
   #documents = collection.find()

   # Print all documents
   #  for document in documents:
   #      print(document)

   for doc in collection.find({'summary':{"$exists": True}}).limit(100):
       doc['summary_embedding_hf'] = generate_embedding(doc['summary'])
       collection.replace_one({'_id': doc['_id']}, doc)
   print("DONE")

def NY_query(generate_embedding):
   uri = "mongodb+srv://scott:tiger@cluster0.v9uas.mongodb.net/?retryWrites=true&w=majority"
   # Create a new client and connect to the server
   client = MongoClient(uri, server_api=ServerApi('1'))
   query = "NYC"

   db = client.sample_airbnb
   # Get the 'listingsAndReviews' collection
   collection = db.listingsAndReviews

   results = collection.aggregate([
   {"$vectorSearch": {
      "queryVector": generate_embedding(query),
      "path": "summary_embedding_hf",
      "numCandidates": 100,
      "limit": 2,
      "index": "vector_index_cos",
         }}
   ]);

   for document in results:
      print()
      print(colored('listing_url:', 'black'),colored(f'{document["listing_url"]}','green'))
      print(colored('name:', 'black'),colored(f'{document["name"]}','green'))
      print(colored('summary:', 'black'),colored(f'{document["summary"]}','green'))

def main():
    #print(generate_embedding("MongoDB is awesome"))
   # enbeding_data(generate_embedding)
   NY_query(generate_embedding)

if __name__ == "__main__":
    main()
