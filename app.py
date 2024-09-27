from flask import Flask
app = Flask(__name__)

@app.route('/') 
def devops(): 
  return '<center><h1><font color=pink>Germinare Tech, EU AMO PINTO MÈDIO ROZINHA TROLHA NO ORIFICIO ANAL COMER TOdas pessasos AIAIAIAI MARCOA</center>' 
  
if __name__ == '__main__': 
  app.run(debug=True, host='0.0.0.0', port=3782) 
