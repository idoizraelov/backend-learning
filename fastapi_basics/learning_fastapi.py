from fastapi import FastAPI
from pydantic import BaseModel


app= FastAPI()
#our database
shoes_db={}

#our data template for Pydantic model
class Shoe(BaseModel):
    id: int
    name: str
    size: int
    color: str

# Handle GET requests to the main URL
@app.get("/")
def read_root():
    #return JSON dictionary to the user
    return {
        "message": "Hello from my new server!",
        "tip": "To test the API and add shoes, go to: http://127.0.0.1:8000/docs"
    }


@app.post("/shoes/")
def add_shoe(new_shoe: Shoe):
    #save it in the dictionary
    shoes_db[new_shoe.id] = new_shoe

    #return a success message
    return {"message": "Shoe added successfully!", "shoe": new_shoe}


@app.get('/shoes/{shoe_id}')
def read_item(shoe_id: int):
    #cheack if the shoe exists in our dictionary
    if shoe_id in shoes_db:
        return shoes_db[shoe_id]

    return {"error": "Shoe not found in the factory"}


@app.delete("/shoes/{shoe_id}")
def delete_shoe(shoe_id: int):
    #check if the shoe exists
    if shoe_id in shoes_db:
        # Delete it from the dictionary
        del shoes_db[shoe_id]
        return {"message": f"Shoe {shoe_id} has been deleted."}

    # If not found, return an error
    return {"error": "Cannot delete: Shoe not found."}

@app.put("/shoes/{shoe_id}")
def update_item(shoe_id: int, update_shoe: Shoe):
    if shoe_id in shoes_db:
        # replace the old shoe with the new one
        shoes_db[shoe_id] = update_shoe
        return {"message": f"Shoe {shoe_id} has been updated."}

    return {"error": "Cannot update: Shoe not found."}
