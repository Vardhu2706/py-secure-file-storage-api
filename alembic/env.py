import os
from dotenv import load_dotenv
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from sqlalchemy.ext.declarative import declarative_base
from alembic import context
import sys
import os

# Import your model's MetaData object here
from app.db.base import Base  # import all models indirectly
from app.models import user_model, file_model  # Import models to ensure Alembic recognizes them

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))

# Load the .env file and get the database URL
load_dotenv()  # This loads environment variables from the .env file
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./files.db")  # Default to SQLite

# Alembic Config object, provides access to the values within the .ini file
config = context.config

# Set the SQLAlchemy URL dynamically from the environment variable
config.set_main_option('sqlalchemy.url', DATABASE_URL)

# Set up logging configuration (optional but useful)
fileConfig(config.config_file_name)

# Create a base class for our models to register them with SQLAlchemy
target_metadata = Base.metadata

def run_migrations_online():
    # Connect to the database and run migrations
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',  # Look for sqlalchemy.* keys
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        # Set up transaction for running migrations
        with connection.begin():
            context.configure(
                connection=connection,
                target_metadata=target_metadata
            )
            # Run migrations
            with context.begin_transaction():
                context.run_migrations()

def run_migrations_offline():
    # Run migrations offline (if needed, typically for generating migrations)
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, 
        target_metadata=target_metadata, 
        literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
