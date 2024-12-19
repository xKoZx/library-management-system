from flask import Flask
from routes.books import book_routes
from routes.members import member_routes
from database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Register blueprints
app.register_blueprint(book_routes, url_prefix='/books')
app.register_blueprint(member_routes, url_prefix='/members')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Initialize the SQLite database
    app.run(debug=True)