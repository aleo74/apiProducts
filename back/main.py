from dotenv import load_dotenv
import os
from app.app import create_app, prepare_db

load_dotenv()

if __name__ == '__main__':
    print(os.getenv('FLASK_ENV'))
    app = create_app(config_name=os.getenv('FLASK_ENV'))
    port = os.getenv("FLASK_PORT", 5000)
    ip = os.getenv("FLASK_IP", '127.0.0.1')
    prepare_db(app)
    app.run(host=ip, port=port, debug=True)
