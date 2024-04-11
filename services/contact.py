from flask import Blueprint, request, jsonify
from model.contact import Contact

#Creación de una instancia Blueprint, para cuando exista
#más de una carpeta models?
contacts = Blueprint('contacts', __name__)

@contacts.route('/contactos/v1', methods = ['GET'])
def getMensaje():
    result = {}
    result["data"] = 'flask-crud-backend'
    return jsonify(result)

@contacts.route('/contactos/v1/listar', methods = ['GET'])
def getContactos():
    result = {}
    contactos = Contact.query.all() #"Select from Contact"
    result["data"] = contactos
    result["status_cod"] = 200 #Status_code se envia como resultado del query para FrontEnd
    result["status_msg"] = "Contacts were recovery succesfully..."
    return jsonify(result), 200

@contacts.route('/contactos/<int:id>', methods = ['GET'])
def getContacto(id):
    result = {}
    contactos = Contact.query.get(id) #"Select from Contact"
    result["data"] = contactos
    result["status_cod"] = 200 #Status_code se envia como resultado del query para FrontEnd
    result["status_msg"] = "Contacts were recovery succesfully..."
    return jsonify(result), 200
