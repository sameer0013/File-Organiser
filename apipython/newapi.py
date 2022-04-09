import logging
from flask import Flask,jsonify
app = Flask(__name__)

@app.route('/')
def helloworld():
    return f'HELLOWORLD! \n for armstrong write /armstrong/<int:n> in above url'

@app.route('/armstrong/<int:n>')
def armstrong(n):
    copy_n=n
    order=len(str(n))
    digit=1
    sum=0
    while n>0:
        digit=n%10
        sum+=digit**order
        n=n//10

    if(sum==copy_n): 
        print("armstrong")
        result={
            "number":copy_n,
            "Armstrong":True,
            "pthernumbers":[1,2,3,64,57],
            "serverid":"127.0.0.1:5000"
        }
    else:
        print("not")
        result={
            "number":copy_n,
            "Armstrong":False,
            "othernumbers":[1,2,3,64,57],
            "serverid":"127.0.0.1:5000"
        }
    return jsonify(result)
        

if __name__=='__main__':
    app.run(debug=True)    