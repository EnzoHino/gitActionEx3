from flask import Flask
app = Flask(__name__)

@app.route('/') 
def devops(): 
  return '<center><h1><font color=red>Germinare Tech, EU AMO PINTAOZAO GRANDAO VERMELHAO INCHADAO AIAIAIAI MARCOA</center>' 
  
if __name__ == '__main__': 
  app.run(debug=True, host='0.0.0.0', port=3782) 
