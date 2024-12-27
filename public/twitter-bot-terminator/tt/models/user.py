from pydantic import BaseModel
from typing import List, Dict

class User(BaseModel):
    id: str
    conversation: List[Dict[str, str]] # Add every message in here like {"role": "user", "content": "Hello"}   or role being bot for our messages
    real_users: List[str] # Save user_ids we confirm in here
    user_access: bool = False # If we have authentication to control the users account
    
    # add stuff for user credentials here