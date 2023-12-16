from app.Models.Product import Product
from flask import jsonify, request


class ProductController:

    @classmethod
    def get_products(cls):
        products = Product.get_all()
        if products:
            return jsonify([product.to_dict() for product in products])
        else:
            return {'message': 'No products found'}, 404

    @classmethod
    def save_product(cls):
        data = request.get_json()
        if data:
            code = data.get('code')
            name = data.get('name')
            description = data.get('description')
            price = data.get('price')
            quantity = data.get('quantity')
            inventoryStatus = data.get('inventoryStatus')
            category = data.get('category')
            image = data.get('image')
            rating = data.get('rating')

            if not code or not name or not description or not price or not quantity \
                    or not inventoryStatus or not category:
                return {'message': 'Missing required fields'}, 400

            new_product = Product(
                code=code,
                name=name,
                description=description,
                price=price,
                quantity=quantity,
                inventoryStatus=inventoryStatus,
                category=category,
                image=image,
                rating=rating
            )

            try:
                new_product.save()
                return {'message': 'Product saved successfully'}, 201
            except Exception as e:
                return {'message': f'Error saving product: {str(e)}'}, 500
        else:
            return {'message': 'No data provided'}, 400

    @classmethod
    def get_one_product(cls, idToFind):
        product = Product.get_by_id(idToFind)
        if product:
            return jsonify(product.to_dict())
        return {'message': 'Product not found'}, 404

    @classmethod
    def edit_product(cls, idToEdit):
        data = request.get_json()
        if data:
            product = Product.get_by_id(idToEdit)
            if product:
                code = data.get('code', product.code)
                name = data.get('name', product.name)
                description = data.get('description', product.description)
                price = data.get('price', product.price)
                quantity = data.get('quantity', product.quantity)
                inventoryStatus = data.get('inventoryStatus', product.inventoryStatus)
                category = data.get('category', product.category)
                image = data.get('image', product.image)
                rating = data.get('rating', product.rating)

                product.code = code
                product.name = name
                product.description = description
                product.price = price
                product.quantity = quantity
                product.inventoryStatus = inventoryStatus
                product.category = category
                product.image = image
                product.rating = rating

                try:
                    product.save()
                    return {'message': 'Product updated successfully'}, 200
                except Exception as e:
                    return {'message': f'Error updating product: {str(e)}'}, 500
            else:
                return {'message': 'Product not found'}, 404
        else:
            return {'message': 'No data provided'}, 400

    @classmethod
    def delete_product(cls, idToDelete):
        product = Product.get_by_id(idToDelete)
        if product:
            try:
                product.delete()
                return {'message': 'Product deleted successfully'}, 200
            except Exception as e:
                return {'message': f'Error deleting product: {str(e)}'}, 500
        else:
            return {'message': 'Product not found'}, 404
