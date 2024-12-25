from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)

ip="172.17.0.2" #ip of u r db container 
user="faizan"
password="redhat"
dbname="db"

app.config['MYSQL_DATABASE_USER']= user
app.config['MYSQL_DATABASE_HOST']= ip
app.config['MYSQL_DATABASE_PASSWORD']= password
app.config['MYSQL_DATABASE_DB']= dbname

mysql = MySQL()

mysql.init_app(app)

@app.route("/date")
def lwdata():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("select * from student")
    data = cursor.fetchall()
    return str(data)

app.run(host='0.0.0.0')
