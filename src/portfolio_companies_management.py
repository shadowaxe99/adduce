```python
from database import db_connection
from user_interface import current_user

class Company:
    def __init__(self, name, description, industry, stage, funding):
        self.name = name
        self.description = description
        self.industry = industry
        self.stage = stage
        self.funding = funding

def add_company(name, description, industry, stage, funding):
    new_company = Company(name, description, industry, stage, funding)
    db_connection.session.add(new_company)
    db_connection.session.commit()

def update_company(company_id, name, description, industry, stage, funding):
    company = db_connection.session.query(Company).filter_by(id=company_id).first()
    company.name = name
    company.description = description
    company.industry = industry
    company.stage = stage
    company.funding = funding
    db_connection.session.commit()

def delete_company(company_id):
    company = db_connection.session.query(Company).filter_by(id=company_id).first()
    db_connection.session.delete(company)
    db_connection.session.commit()

def get_companies():
    return db_connection.session.query(Company).all()

def get_company_by_id(company_id):
    return db_connection.session.query(Company).filter_by(id=company_id).first()
```