from fastapi import FastAPI,status,HTTPException,Response,Query,Path
from fastapi.responses import JSONResponse
from schemas import CreateExpense,UpdateExpense,ResponeExpenseByID
from typing import Annotated
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

ExpenseID = Annotated[int,Path(description="Enter the ID of your expense. This parameter is required.",
        examples=[4010],
        )]

@app.post("/expense",status_code=status.HTTP_201_CREATED)
def create_expense(expense : CreateExpense):
    new_expense_id = max(expenses["expense_id"] for expenses in users_expences) + 1
    users_expences.append({
        "expense_id" : new_expense_id,
        "description" : expense.description,
        "amount" : expense.amount
    })
    
    return {
    "expense_id": new_expense_id,
    "description": expense.description,
    "amount": expense.amount
    }



@app.get("/expenses/{expense_id}")
def get_all_expenses():
    expences =[expence for expence in users_expences]
    return expences

@app.get("/expense/{expense_id}",response_model=ResponeExpenseByID)
def get_expense_by_id(expense_id : ExpenseID):
    for expenses in users_expences:
        if expenses["expense_id"] == expense_id:
            return {
                 "expense_id": expenses["expense_id"],
                 "description": expenses["description"],
                 "amount": expenses["amount"]
                }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="ID Not Found.")    
        

@app.put("/expense/{expense_id}")  
def update_expense_by_id(expense:UpdateExpense ,expense_id:ExpenseID):
    for expenses in users_expences:
        if expenses["expense_id"] == expense_id:  
            if expense.amount is not None:
                expenses["amount"] = expense.amount

            if expense.description is not None:
                expenses["description"] = expense.description

            return JSONResponse(content={"detail":"successfully updated"},status_code=status.HTTP_200_OK)
            
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="ID Not Found.")      
    


@app.delete("/expense/{expense_id}")
def delete_expense(expense_id : ExpenseID):
    for expenses in users_expences:
        if expenses["expense_id"] == expense_id:   
            users_expences.remove(expenses)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="ID Not Found.")         
            
