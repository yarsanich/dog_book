from app import app
from config import UPLOAD_FOLDER

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.run(debug = True)
