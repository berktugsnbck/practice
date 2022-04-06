from flask import Flask, render_template, session, redirect
import pika


app=Flask(__name__)
app.secret_key = "test"


@app.route("/")
def routeTo():
    return redirect("/producer")


@app.route("/producer")
def index():
    connection_parameters = pika.ConnectionParameters('192.168.1.100', port=5672)
    connection = pika.BlockingConnection(connection_parameters)
    channel = connection.channel()
    channel.queue_declare(queue='countbox')
    if 'produce' in session:
        session['produce'] +=1
        message=f"{session['produce']}"
        channel.basic_publish(exchange='', routing_key='countbox', body=message)
        print(f"que: {session['produce']}")
    
    else:
        session['produce'] = 0
        channel.basic_publish(exchange='', routing_key='countbox', body='restarted')
        print(f"que: {session['produce']}")

    return render_template("index.html")    
      
@app.route("/clear")
def clear():
    session.clear()
    return redirect("/producer")



if __name__ == '__main__':
	app.run( host='0.0.0.0', port=5000)                     
