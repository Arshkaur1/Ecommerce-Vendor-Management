from Abstractions.Vendor import Vendor
from Models.VendorModel import VendorModel
from Models.VendorSessionModel import VendorSessionModel


class VendorImplementation(Vendor):

    def __init__(self):
        self.vendor_model = VendorModel()
        self.vendor_session = VendorSessionModel()

    def login(self, username, password):
        if self.vendor_model.is_correct_vendor(username, password):
            if self.vendor_session.login(username):
                print("Vendor Data does exists!")
        else:
            print("Vendor Data does not exists!!")
        # Add you code here after verifying the vendor data exists in the dictionary 

    def logout(self):
        self.vendor_session.logout(self)
        print("User is Logged out successfully!")
        # Add your code here to log out the current vendor
