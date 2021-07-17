from db_config import app
from handler.user import user
app.register_blueprint(user,url_prefix="/user")

@app.route('/')
def index():
    return 'index'

if __name__=='__main__':
    app.run(host="127.0.0.1",port='5000',debug=True)