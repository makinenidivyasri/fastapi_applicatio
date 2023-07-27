from fastapi import FastAPI,HTTPException,status,Response
from typing import Optional
from pydantic import BaseModel
from random import randrange
from . import schemas

app = FastAPI()

all_posts = [{"title":"trams","content":"the trams size is between bus and train","post_id": 1},
        {"title":"sunrise","content":"sunraises at 5 and sets at 9","post_id": 2}]


@app.get("/posts",status_code=status.HTTP_200_OK)
def get_posts():
    return all_posts

@app.post("/posts/createPost",status_code=status.HTTP_201_CREATED)
def create_post(newData: schemas.NewPost):
    newData1 = newData
    newData1.post_id = randrange(1,10000)
    all_posts.append(newData1)
    print(newData1)
    return all_posts

@app.delete("/posts/delete_post/{id}")
def delete_post(id : int):
    for element in all_posts:
        if element["post_id"] == id:
            print(element)
            print(f'book id: {id} deleted successfully')
            all_posts.remove(element)
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"ID : {id} does not exist to perform this operation")
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/modifyPost/",status_code=status.HTTP_200_OK)
def modify_post(newData : schemas.ModifyPost):
    for index in range(len(all_posts)):
        if all_posts[index]["post_id"] == newData.post_id:
            print(newData)
            all_posts[index] = newData
            print(all_posts)
    return all_posts

@app.get("/posts/getPostByID/{id}",response_model=schemas.PostOutput)
def getPostByID(id : int):
    for index in range(len(all_posts)):
        if all_posts[index]["post_id"] == id:
            return all_posts[index]
















