from app import app
from config import UPLOAD_FOLDER

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
app.run(debug = True)
