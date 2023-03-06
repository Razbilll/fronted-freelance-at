from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()

@dataclass
class Authorization:
    """Датакласс с данными для авторизации."""

    global_admin: str = "global_admin"
    credentials = {
        "global_admin": {
            "login": os.getenv("GLOBAL_ADMIN_LOGIN"),
            "password": os.getenv("GLOBAL_ADMIN_PASSWORD")
        }
    }

    @staticmethod
    def get_user(user) -> Authorization:
        return Authorization.credentials.get(user)
