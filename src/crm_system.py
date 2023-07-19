```python
import src.user_interface as ui
import src.deal_flow_management as dfm
import src.investor_relations_management as irm
import src.portfolio_companies_management as pcm
import src.collaboration_tools as ct
import src.database as db

class CRMSystem:
    def __init__(self):
        self.db_connection = db.connect()
        self.current_user = None

    def login(self, username, password):
        user = db.get_user(self.db_connection, username)
        if user and user.password == password:
            self.current_user = user
            ui.display_message("login_success")
        else:
            ui.display_message("login_fail")

    def signup(self, username, password):
        if db.add_user(self.db_connection, username, password):
            ui.display_message("signup_success")
        else:
            ui.display_message("signup_fail")

    def add_deal(self, deal):
        if dfm.add_deal(self.db_connection, deal):
            ui.update_deal_list()

    def update_deal(self, deal):
        if dfm.update_deal(self.db_connection, deal):
            ui.update_deal_list()

    def delete_deal(self, deal_id):
        if dfm.delete_deal(self.db_connection, deal_id):
            ui.update_deal_list()

    def add_investor(self, investor):
        if irm.add_investor(self.db_connection, investor):
            ui.update_investor_list()

    def update_investor(self, investor):
        if irm.update_investor(self.db_connection, investor):
            ui.update_investor_list()

    def delete_investor(self, investor_id):
        if irm.delete_investor(self.db_connection, investor_id):
            ui.update_investor_list()

    def add_company(self, company):
        if pcm.add_company(self.db_connection, company):
            ui.update_company_list()

    def update_company(self, company):
        if pcm.update_company(self.db_connection, company):
            ui.update_company_list()

    def delete_company(self, company_id):
        if pcm.delete_company(self.db_connection, company_id):
            ui.update_company_list()

    def collaborate(self, message):
        ct.send_message(self.current_user, message)
```