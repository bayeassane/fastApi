from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.get('/')
def index():
    return {'data': {'name': 'Asan'}}


@app.get('/items/{item_id}')
def read_item(item_id: int):
    return {'item_id': item_id}


@app.get('/blog')
def blog(limit=10, published: bool=True, sort: Optional[str]=None):
    if published:
        return {'data': f'{limit} published Blogs from the db'} 
    else:
        return {'data': f'{limit} Blogs from the db'}
    


@app.get('/blog/{id}')
def show(id):
    return {'blog_id': id}

@app.get('/blog/{id}/comments')
def comments(id):
    return {'data': {'id': id}}


@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f'Blog is created with as {request.title}'}



if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)