from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

#Load .env file
load_dotenv()

def buat_koneksi():
    """Membuat koneksi ke database MySQL menggunakan SQLAlchemy"""
    try:
        user = os.getenv('DB_USER')
        password = os.getenv('DB_PASSWORD')
        host = 'localhost'
        db_name = 'capsclaklinik'

        # Format connection string: mysql+driver://username:password@host/database
        engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{db_name}')
        print("Koneksi ke database berhasil")
        return engine
    except Exception as e:
        print(f"Terjadi error: '{e}'")
        return None
    