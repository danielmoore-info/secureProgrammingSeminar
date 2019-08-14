from flask import Flask, request

app = Flask(__name__)

@app.route("/welcome", methods=['GET'])
def welcome_user():
    return 'Welcome ' + request.args.get('username')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)