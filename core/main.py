from fastapi import FastAPI,status,HTTPException,Response
from fastapi.responses import JSONResponse

app = FastAPI()

users_expences = [
    {
        "expense_id":4011 ,
        "description":"for buying groceries.",
        "amount" : 40
    },
    {
        "expense_id":4012 ,
        "description":"electricity charges",
        "amount" : 790
    },
    {
        "expense_id":4013 ,
        "description":"food",
        "amount" : 190.5
    },
    {
        "expense_id":4014 ,
        "description":"buying charger for my phone",
        "amount" : 1000
    }

]

@app.post("/expense",status_code=status.HTTP_201_CREATED)
def create_expense(amount: float , description : str ):
    new_expense_id = max(expense["expense_id"] for expense in users_expences) + 1
    users_expences.append({
        "expense_id" : new_expense_id,
        "description" : description,
        "amount" : amount
    })
    
    return {
    "expense_id": new_expense_id,
    "description": description,
    "amount": amount
    }



@app.get("/")
def get_all_expenses():
    expences =[expence for expence in users_expences]
    return expences

@app.get("/expense/{expense_id}")
def get_expense_by_id(expense_id : int ):
    for expense in users_expences:
        if expense["expense_id"] == expense_id:
            return{"expense id":expense["expense_id"] , "expense description ":expense["description"] , "amount ":expense["amount"]}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="ID Not Found.")    
        

@app.put("/expense/{expense_id}")  
def update_expense_by_id(expense_id : int , amount : float | None = None , description : str |None = None ):
    for expense in users_expences:
        if expense["expense_id"] == expense_id:  
            if amount is not None:
                expense["amount"] = amount

            if description is not None:
                expense["description"] = description

            return JSONResponse(content={"detail":"successfully updated"},status_code=status.HTTP_200_OK)
            
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="ID Not Found.")      
    


@app.delete("/expense/{expense_id}")
def delete_expense(expense_id : int):
    for expense in users_expences:
        if expense["expense_id"] == expense_id:   
            users_expences.remove(expense)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="ID Not Found.")         
            
