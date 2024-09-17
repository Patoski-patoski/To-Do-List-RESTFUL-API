from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Import Migrate
import yaml

app = Flask(__name__)

# Load database configuration
with open("../app_v2/config/config.yaml", "r", encoding="utf-8") as db_file:
    db_config = yaml.safe_load(db_file)

    user = db_config["mysql_user"]
    password = db_config["mysql_password"]
    host = db_config["mysql_host"]
    database = db_config["mysql_db"]
    port = db_config["mysql_port"]

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql://{user}:{password}@{host}:{port}/{database}"
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Initialize Migrate

from models.models import User  # Import models here