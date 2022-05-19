from flask import Flask, jsonify
import config
app = Flask(__name__)


@app.route('/')
def root():
       out = {
          "hello": "world",
          "built_at": 1627037312,
          "deployed_at": 1627037348
         }
       return jsonify(out)


if __name__ == '__main__':
   app.run(host=config.CONFIG.get('host'), port=config.CONFIG.get('port'))