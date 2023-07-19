```python
from src.database import db_connection
from src.config import DealSchema

class DealFlowManagement:
    def __init__(self):
        self.connection = db_connection
        self.deal_schema = DealSchema

    def add_deal(self, deal_data):
        try:
            new_deal = self.deal_schema(**deal_data)
            self.connection.session.add(new_deal)
            self.connection.session.commit()
            return {"message": "Deal added successfully."}, 200
        except Exception as e:
            return {"message": str(e)}, 400

    def update_deal(self, deal_id, deal_data):
        try:
            deal = self.connection.session.query(self.deal_schema).filter_by(id=deal_id).first()
            for key, value in deal_data.items():
                setattr(deal, key, value)
            self.connection.session.commit()
            return {"message": "Deal updated successfully."}, 200
        except Exception as e:
            return {"message": str(e)}, 400

    def delete_deal(self, deal_id):
        try:
            deal = self.connection.session.query(self.deal_schema).filter_by(id=deal_id).first()
            self.connection.session.delete(deal)
            self.connection.session.commit()
            return {"message": "Deal deleted successfully."}, 200
        except Exception as e:
            return {"message": str(e)}, 400
```