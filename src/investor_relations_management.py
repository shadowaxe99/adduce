```python
from src.database import db_connection
from src.config import InvestorSchema

def add_investor(investor_data):
    try:
        new_investor = InvestorSchema(**investor_data)
        db_connection.session.add(new_investor)
        db_connection.session.commit()
        return {"message": "Investor added successfully."}, 201
    except Exception as e:
        return {"message": str(e)}, 400

def update_investor(investor_id, investor_data):
    try:
        investor = db_connection.session.query(InvestorSchema).filter(InvestorSchema.id == investor_id).first()
        for key, value in investor_data.items():
            setattr(investor, key, value)
        db_connection.session.commit()
        return {"message": "Investor updated successfully."}, 200
    except Exception as e:
        return {"message": str(e)}, 400

def delete_investor(investor_id):
    try:
        investor = db_connection.session.query(InvestorSchema).filter(InvestorSchema.id == investor_id).first()
        db_connection.session.delete(investor)
        db_connection.session.commit()
        return {"message": "Investor deleted successfully."}, 200
    except Exception as e:
        return {"message": str(e)}, 400
```