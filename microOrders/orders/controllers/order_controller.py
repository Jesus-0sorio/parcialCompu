from flask import Blueprint, request, jsonify, session
import requests
from orders.models.order_model import Orders
from db.db import db

order_controller = Blueprint('order_controller', __name__)

@order_controller.route('/api/orders', methods=['GET'])
def get_all_orders():
    print("listado de ordenes")
    orders = Orders.query.all()
    return jsonify([{'id': order.id, 'userName': order.userName, 'userEmail': order.userEmail, 'saleTotal': order.saleTotal} for order in orders])

# Get single order by id
@order_controller.route('/api/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    print("obteniendo ordenes")
    order = Orders.query.get_or_404(order_id)
    return jsonify({'id': order.id, 'userName': order.userName, 'userEmail': order.userEmail, 'saleTotal': order.saleTotal})

@order_controller.route('/api/orders', methods=['POST'])
def create_order():

    data = request.get_json()
    user_name = session.get('username')
    user_email = session.get('email')

    if not user_name or not user_email:
        return jsonify({'message': 'Información de usuario inválida'}), 400

    products = data.get('products')

    if not products or not isinstance(products, list):
        return jsonify({'message': 'Falta o es inválida la información de los productos'}), 400

    total_amount = 0
    inventory_updated = True

    for product in products:
        product_id = product.get('id')
        quantity = product.get('quantity')
        
        if not product_id or not quantity:
            return jsonify({'message': f'Faltan datos del producto: {product}'}), 400

        # Obtener detalles del producto desde el microservicio de productos
        product_details_url = f'http://192.168.80.3:5003/api/products/{product_id}'
        product_response = requests.get(product_details_url)

        if product_response.status_code != 200:
            return jsonify({'message': f'Error al obtener detalles del producto con ID {product_id}'}), 404

        product_details = product_response.json()

        # Verificar si hay suficiente quantity
        if product_details['quantity'] < quantity:
            return jsonify({'message': f'Stock insuficiente para el producto {product_details["name"]}'}), 400

        # Calcular el total
        total_amount += product_details['price'] * quantity

        # Actualizar el inventario llamando al endpoint de actualización de productos
        product_details['quantity'] -= quantity

        update_response = requests.put(product_details_url, json=product_details)

        if update_response.status_code != 200:
            inventory_updated = False
            break

    if not inventory_updated:
        return jsonify({'message': 'Error al actualizar el inventario'}), 500

    # Si llegamos aquí, todo está bien y podemos crear la orden
    new_order = Orders(userName=user_name, userEmail=user_email, saleTotal=total_amount)

    # Aquí agregarías la lógica para guardar la orden en la base de datos
    db.session.add(new_order)
    db.session.commit()

    return jsonify({'message': 'Orden creada exitosamente'}), 201