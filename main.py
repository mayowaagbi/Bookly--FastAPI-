from fastapi import FastAPI,Header
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
async def read_root():
    return {"message":"HelloWorld"}

@app.get("/greet")
async def greet_name(name:str = "user",age:Optional[int]=0)->dict:
     return{"message" :f"Hello {name}" , "age":age} 

class BookCreateModel(BaseModel):
     title : str
     author:str

@app.post("/create_book")
async def create_book(Book_data:BookCreateModel): 
     return{
          "title":Book_data.title,
            "author":Book_data.author
            }

@app.get("/get_Header" , status_code=201)
async def get_Headers(
     accept:str = Header(None),
     content_type:str = Header(None),
     user_agent:str = Header(None),
     host:str = Header(None)
):
     request_Headers = {}
     request_Headers["Accept"] = accept
     request_Headers["Content-Type"] = content_type
     request_Headers["User-Agent"] = user_agent
     request_Headers["Host"] = host
     return request_Headers
     