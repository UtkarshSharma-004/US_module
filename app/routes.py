from flask import Blueprint,request,jsonify
from .db import get_db
from config import setup_logging

logger=setup_logging()

main=Blueprint('main',__name__)

db=get_db()
object_collection3 = db['CARTOON']

@main.route('/add_cartoon',methods=['POST'])
def add_cartoon():
    data1= request.get_json()
    
    for i in range(len(data1)):
        cartoon = data1[i]['cartoon']
        genre = data1[i]['genre']
        creator = data1[i]['creator']

        if cartoon is None or genre is None or creator is None :
            return jsonify({'error': 'cartoon or genre or creator is missing'}), 400
        object_collection3.insert_one({'cartoon':cartoon,'genre':genre, "creator" :creator})
    return jsonify ({'message':'cartoon added successfully'})

@main.route('/get_cartoon/<cartoon>',methods=['GET'])
def get_cartoon(cartoon):
    cartoon_data = object_collection3.find_one({'cartoon': cartoon})

    if cartoon_data is None:
        return jsonify({'error': f'NO data found for cartoon: {cartoon}'}) , 404
    
    cartoon_data['_id'] = str(cartoon_data['_id'])

    return jsonify(cartoon_data)

