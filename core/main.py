from fastapi import FastAPI

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

@app.post("/expense")
def create_expense(amount: float , description : str | None = None):
    new_expense_id = max(expense["expense_id"] for expense in users_expences) + 1
    users_expences.append({
        "expense_id" : new_expense_id,
        "description" : description,
        "amount" : amount
    })
    print(users_expences)
    return {f"{new_expense_id } , {description} , {amount}"}



@app.get("/")
def get_all_expenses():
    expences =[expence for expence in users_expences]
    return expences

@app.get("/expense/{expense_id}")
def get_expense_by_id(expense_id : int ):
    for expense in users_expences:
        if expense["expense_id"] == expense_id:
            return{"expense id":expense["expense_id"] , "expense description ":expense["description"] , "amount ":expense["amount"]}
        

@app.put("/expense/{expense_id}")  
def update_expense_by_id(expense_id : int , amount : float , description : str |None = None ):
    for expense in users_expences:
        if expense["expense_id"] == expense_id:  
            expense["description"] = description
            expense["amount"] = amount   
            return expense    
    


@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id : int):
    for expense in users_expences:
        if expense["expense_id"] == expense_id:   
            users_expences.remove(expense)
            
