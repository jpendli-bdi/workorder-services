import pickle
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/fetchComponent/<parameter>')
def loadData(parameter):
    # for reading also binary mode is important
    dbfile = open('C:/Users/jpendli/Downloads/ADEL1_metadata.pkl', 'rb')    
    db = pickle.load(dbfile)
    #for keys in db:
       # print(keys, '=>', db[keys])
    for item in db.values():
        #print('The data is : ', item['component_number'])
        if(item['component_number']==parameter):
            return jsonify(item['structured_data'])
   # print("Values:", list(db.values()))
    dbfile.close()
   


@app.route('/hello')
def hello_world():
    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    app.run(debug=False)