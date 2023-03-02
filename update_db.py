"""Script to update database. Execute python3 update_db.py JSON_OBJ_NAME"""

import json
import sys
import model
from server import app
from seed_database import seed_database 

# # Prevents error: 
# app.app_context().push() 

model.connect_to_db(app)

file_name = sys.argv[1]

seed_database(file_name)







