```python
# src/config.py

# Database configuration
DATABASE_CONFIG = {
    'host': 'localhost',
    'database': 'vc_crm',
    'user': 'root',
    'password': 'password'
}

# User session configuration
SESSION_CONFIG = {
    'session_type': 'filesystem',
    'session_cookie_secure': True
}

# Message configuration
MESSAGE_CONFIG = {
    'login_success': 'Login successful.',
    'login_fail': 'Login failed. Please check your username and password.',
    'signup_success': 'Signup successful. You can now login.',
    'signup_fail': 'Signup failed. Please check your details.'
}

# DOM elements ID configuration
DOM_ELEMENTS_ID_CONFIG = {
    'login_button': 'loginBtn',
    'signup_button': 'signupBtn',
    'deal_list': 'dealList',
    'investor_list': 'investorList',
    'company_list': 'companyList'
}
```