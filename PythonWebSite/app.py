from flask import Flask
from PythonWebSite.Views.index import bp as index_bp
from PythonWebSite.Views.createnote import bp as createnote_bp

app = Flask(__name__)

app.register_blueprint(index_bp)
app.register_blueprint(createnote_bp)
