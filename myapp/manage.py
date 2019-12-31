#程序入口
from app import create_app
app = create_app()
app.run(host='0.0.0.0',port=5555, debug=True)