from Abstractions.Products import Products
from Models.ProductModel import ProductModel
from Models.VendorSessionModel import VendorSessionModel


class ProductsImplementation(Products):
    def __init__(self, username):
        self.product_model = ProductModel()
        self.vendor_session = VendorSessionModel()
        self._username = username

    def add_product(self, product_name, product_type, available_quantity, unit_price):
        if self.vendor_session.check_login:
            self.product_model.add_product (product_name,
                                            product_type,
                                            available_quantity,
                                            unit_price)
            return True
        else:
            return False
        # check if the vendor is logged in, then add the product and return True else Return False
            
    def search_product_by_name(self, product_name):
        if self.vendor_session.check_login:
            if product_name in self.product_model.product_db:
                return product_name
        else:
            return False
        # Search if the product is available in the dictionary if the vendor is authorized to access else return False
        # If product is available then return product

    def get_all_products(self):
        # Check if the vendor can retrieve all the product if not return False
        # otherwise return all the products
        if self.vendor_session.check_login:
            if self.product_model.product_db:
                return self.product_model.product_db
        else:
            return False

