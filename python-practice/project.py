class Product:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def create(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = price
        if isinstance(quantity, str):
            self.quantity = int(quantity) 
        else:
            self.quantity = quantity

    def getProductinfo(self):
        return (self.name, self.category, self.price, self.quantity)

    def updateProduct(self, product_attribute, value):
        try:
            if not isinstance(product_attribute, str):
                raise TypeError("the provided input is not a string")
        
            if product_attribute == "name":
                self.name = value
            elif product_attribute == "category":
                self.category = value
            elif product_attribute == "price":
                self.price = value
            elif product_attribute == "quantity":
                self.quantity = value
            else:
                print("attribute not found in the product attribute list")
                return False
        
            print("Product updated successfully")
            return True
    
        except TypeError as e:  
            print("please enter a valid attribute name as string")
            return False
        finally:
            return

    def toDictionary(self):
        return {"name": self.name, "category": self.category, "price": self.price, "quantity": self.quantity}

class inventory():
    def __init__(self):
        self.items = []
        self.is_empty = True

    def addProduct(self, Product):
        self.items.append(Product)
        self.is_empty = False 

    def updateProductByName(self, product_name, attribute, value):
        if self.is_empty:
            print("inventory is empty")
            return
    
        for product in self.items:
            if product.name == product_name:
                product.updateProduct(attribute, value)
                return
    
        print(f"Product '{product_name}' not found")


    def RemoveProduct(self, name):
        if self.is_empty:
            print("inventory is empty")
            return
        
        for product in self.items:
            products = product.toDictionary()
            
            if name in products.values():
                self.items.remove(product)
                print(f"item {name} is removed")
                
                if len(self.items) == 0:
                    self.is_empty = True
                return
        
        print(f"Product '{name}' not found")
        
    def SearchProduct(self, name):
        if self.is_empty:
            print("inventory is empty")
            return
        
        for product in self.items:
            products = product.toDictionary()
            
            if name in products.values():
                print("Found product:")
                for key, value in products.items():
                    print(f"{key}: {value}")
                return  
            
        print("couldn't find the product")
    
    def displayAllProducts(self):
        if self.is_empty:
            print("no products in inventory")
            return
        
        print(f"\n all products ({len(self.items)} items or item):")
        for product in self.items:
            print(f"{product.name} | {product.category} | {product.price}rupees | quantity: {product.quantity}")

def main():
    Inventory = inventory()
    
    menu_options = ("1. add product","2. remove product", "3. search poduct","4. dsplay all prods", " update product by naem","6. Exit")
    
    while True:
        print("\n  menu")
        for option in menu_options:
            print(option)
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            try:
                name = input("eter product name: ")
                category = input("enter category")
                price = float(input("Enter price "))
                quantity = int(input("Enter quantity: "))
                product = Product(name, category, price, quantity)
                Inventory.addProduct(product)
                print(f"Product '{name}' added successfully!")
            except ValueError:
                print("Invalid input  Please enter valid price and quantity.")
                
        elif choice == "2":
            name = input("enter product name to remove: ")
            Inventory.RemoveProduct(name)
            
        elif choice == "3":
            name = input("enter product name to search: ")
            Inventory.SearchProduct(name)
            
        elif choice == "4":
            Inventory.displayAllProducts()

        elif choice == "5":
            product_name = input("enter product name to update: ")
            attribute = input("enter product attribute to update: ")
            value = input("now enter its new value: ")
            Inventory.updateProductByName(product_name, attribute, value)
        elif choice == "6":
            print("exiting the menu")
            break
            
        else:
            print("wrong choice")

if __name__ == "__main__":
    main()
