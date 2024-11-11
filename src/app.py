from flask import Flask
from flask_restful import Api, Resource, reqparse
import pickle
from flask_cors import CORS
 
app = Flask(__name__)
#needs to use environment variable
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
api = Api(app)
 
class ComponentData(Resource):
    def get(self, parameter):
        try:
            with open('./data/ADEL_metadata.pkl', 'rb') as dbfile,open('./data/ADEL1_metadata.pkl', 'rb') as db1file,open('./data/ADEL2_metadata.pkl', 'rb') as db2file:
                db = pickle.load(dbfile)    	   
                db1 = pickle.load(db1file)    	    
                db2 = pickle.load(db2file)
            for item in db.values():
            	if(item['valve_id']==parameter):            
                   data1=item['structured_data']
            for item in db1.values():
                if(item['component_number']==parameter):            
                   data2=item['structured_data']
            for item in db2.values():
                if(item['Item_Number']==data2['Alignment Procedure']):
                    data3=item['Notes']
    	       
            merged_data = {**data1, **data2}
            merged_data['Notes']=data3;
            return jsonify(merged_data)
        except Exception as e:
            return {'error': str(e)}, 500
	  
    # You can add other HTTP methods like POST, PUT, DELETE as needed
 
class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello, World!'}, 200
 
api.add_resource(ComponentData, '/fetchComponent/<string:parameter>')
api.add_resource(HelloWorld, '/hello')
 
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
 