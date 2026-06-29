import os 
import psycopg2

from dotenv  import load_dotenv 

load_dotenv()

class Conexion:
     
     @staticmethod
     def obtener_conexion():
        return psycopg2.connect(
            host=os.getenv("localhost"),
            database=os.getenv("biblioteca_3aevnd"),
            user=os.getenv("postgres"),
            password=os.getenv("chilaquiles"),
            port=os.getenv("5433")
            
        )
    