from pydantic import BaseModel,Field,field_validator,field_serializer
from typing import Annotated

class BaseExpense(BaseModel):
    description : Annotated[str,Field(max_length=32,default=None,pattern=r"^[A-Za-z0-9 ]+$")]
    amount : float = Field(gt=5)
    
    

class ResponeExpenseByID(BaseExpense):
    
    expense_id : int
    @field_serializer("amount")
    def amount_serialization(self,amount):
        
        return f"{amount*1000:,.0f} toman"
    
    



class CreateExpense(BaseExpense):
    pass


class UpdateExpense(BaseExpense):
    pass



         