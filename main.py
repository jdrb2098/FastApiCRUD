from fastapi import FastAPI, Body, Depends
import models
import schemas
from database import Base, engine, sessionLocal
from sqlalchemy.orm import Session

#if we dont have a database yet these will creatre our database using de  engine configuration
#that we have in database.py
Base.metadata.create_all(engine)

#create a function that alow us to acces the database

def get_session():
    session = sessionLocal()
    try:
        yield session
    finally:
        session.close()    

app = FastAPI() #core configuration these is how initiate our aplication
#install uvicorn that gona be our async server (uvicorn main:app --reload)
#port8000/docs# to view thw information whit an interface like postman

fakeDatabase ={
    1:{'task': 'Clean car'},
    2:{'task': 'Write blog'},
    3:{'task': 'Start stream'},
}
@app.get("/")
def getItems(session: Session = Depends(get_session)):
    items = session.query(models.Item).all()
    return items

@app.get("/{id}")
def getItem(id:int, session: Session = Depends(get_session)):
    item = session.query(models.Item).get(id)
    return item


#option1
# @app.post("/")
# def addItem(task:str):
#     newId = len(fakeDatabase.keys()) +1
#     fakeDatabase[newId] = {"task":task}
#     return fakeDatabase

#option2
@app.post("/")
def addItem(item:schemas.Item, session: Session = Depends(get_session)):
    item = models.Item(task = item.task)
    session.add(item)
    session.commit()
    session.refresh(item)
    
    return item


#option3

# @app.post("/")
# def addItem(body = Body()):
#     newId = len(fakeDatabase.keys()) +1
#     fakeDatabase[newId] = {"task": body['task']}
#     return fakeDatabase

@app.put("/{id}")
def updateItem(id:int, item:schemas.Item, session: Session = Depends(get_session)):
    itemObject = session.query(models.Item).get(id)
    itemObject.task = item.task
    session.commit()

    return itemObject

@app.delete("/{id}")
def deleteItem(id:int, session: Session = Depends(get_session)):
    itemObject = session.query(models.Item).get(id)
    session.delete(itemObject)
    session.commit()
    session.close
    return 'item was deleted'
