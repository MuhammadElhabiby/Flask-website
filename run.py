from app import create_app, db
from app.models import TextEntry
import os

app = create_app()

# Ensure the db directory exists
if not os.path.exists('/app/db'):
    os.makedirs('/app/db')

with app.app_context():
    db.create_all()  # Create the database tables if they don't exist

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
