```python
import src.database as db

class CollaborationTools:
    def __init__(self):
        self.db_connection = db.db_connection

    def share_deal(self, deal_id, user_id):
        deal = self.db_connection.get("DealSchema", deal_id)
        user = self.db_connection.get("UserSchema", user_id)
        if deal and user:
            user.shared_deals.append(deal)
            self.db_connection.update("UserSchema", user_id, user)
            return True
        return False

    def share_company(self, company_id, user_id):
        company = self.db_connection.get("CompanySchema", company_id)
        user = self.db_connection.get("UserSchema", user_id)
        if company and user:
            user.shared_companies.append(company)
            self.db_connection.update("UserSchema", user_id, user)
            return True
        return False

    def share_investor(self, investor_id, user_id):
        investor = self.db_connection.get("InvestorSchema", investor_id)
        user = self.db_connection.get("UserSchema", user_id)
        if investor and user:
            user.shared_investors.append(investor)
            self.db_connection.update("UserSchema", user_id, user)
            return True
        return False
```