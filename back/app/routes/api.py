from flask import Blueprint
from app.Controllers.Products import ProductController

main_bp = Blueprint('main', __name__)

main_bp.add_url_rule('/products', 'get_products', ProductController.get_products, methods=['GET'])
main_bp.add_url_rule('/products', 'save_product', ProductController.save_product, methods=['POST'])
main_bp.add_url_rule('/products/<int:idToFind>', 'get_one_product', ProductController.get_one_product, methods=['GET'])
main_bp.add_url_rule('/products/<int:idToEdit>', 'edit_product', ProductController.edit_product, methods=['PATCH'])
main_bp.add_url_rule('/products/<int:idToDelete>', 'delete_product', ProductController.delete_product, methods=['DELETE'])
