# Run a test server
import os
from app import app

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=os.getenv("APP_PORT"), threaded=True, debug=True)
