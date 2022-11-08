"""
Flask-Surfer
------------

Extension to add CSRF protection to flask applications.
"""

from flask import current_app

from .csrf import *

def get_protector() -> CSRFProtection:
    csrf = current_app.extensions.get("csrf_protection")
    if csrf is None:
        raise NotImplementedError("Missing CSRFProtection module in application")
    return csrf
