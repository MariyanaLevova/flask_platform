import systeminfo
from app import app
from systeminfo import main

@app.route('/')
def get_system_info():
    return "The platform is " + main.get_info()

