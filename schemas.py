from pydantic import BaseModel
#use these when u get a lot of values

#post request- adding data to the database
#Put request- uppdateing data modifying data in a database
#delete request - delete
class Item(BaseModel):
    task:str