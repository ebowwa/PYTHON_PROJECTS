from tt.database import SQLiteKeyValueStore
from tt.models.user import User
from tt.terminate import terminate_thots
from tt.authentication import request_access

db = SQLiteKeyValueStore()

def handle_event(user_id: str, message: str):
    """
    Now here write the code to:
    - get the user object from the users table in sqlite. create a new user object if it doesn't exist
    - 
    """
    if db.exists("users", user_id):
        user = db.query("users", user_id)
    else:
        user = User(id=user_id, conversation=[{"role": "user", "content": message}], real_users=[])
        db.insert("users", user.model_dump())
        
    if user.user_access:
        return terminate_thots(user_id)
    else:
        return request_access(user_id)
