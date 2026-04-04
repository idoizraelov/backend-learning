# FastAPI Basics & CRUD

This is a small project to learn how a backend server works and how it talks to a frontend client.

## What I Learned Here:
* **CRUD:** How to Create (POST), Read (GET), Update (PUT), and Delete (DELETE) data.
* **API Docs:** I used the `/docs` page (Swagger UI) as a fake frontend. It helped me understand how a client sends data (JSON) and how the server checks it.
* **Pydantic:** A tool to check that the data from the user is correct (Data Validation).
* **In-Memory Database:** Using a simple Python Dictionary to save data while learning, before using a real database.

## The Routes I Built:
* `GET /` - Returns a welcome message and a tip to visit the `/docs` page.
* `POST /shoes/` - Adds a new shoe to the system.
* `GET /shoes/{shoe_id}` - Gets the details of a specific shoe.
* `PUT /shoes/{shoe_id}` - Updates the details of an existing shoe.
* `DELETE /shoes/{shoe_id}` - Deletes a shoe from the system.

## How to Run the Server:
Open the terminal and run this command:
```bash
uvicorn learning_fastapi:app --reload