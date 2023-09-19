from decimal import Decimal
from django.conf import settings
from Main.models import Camera, lens, tripods, lightings, Binoculars

class Cart:
    def __init__(self, request):
        
        self.request =  request
        
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
    
    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': int(product.price)
            }
        if override_quantity:
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]["quantity"] += quantity
        self.save()
        
    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
            
    def save(self):
        self.session.modified = True
        
    def productq(self, product_id): 
        if product_id in self.cart.keys():
            return self.cart[product_id]['quantity']
        return 0

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        
        l=[]
        for i in self.request.META['HTTP_REFERER'][22::]:
            if i == "/":
                break
            l.append(i)
        res = "".join(l)
        
        if res == "Camers":
            res = "Camera"
            
        if res == "Lens":
            res = "lens"
            
        if res == "Tripods":
            res = "tripods"
            
        if res == "Lightings":
            res = "lightings"
            
        if res == "binoculars":
            res = "Binoculars"
        
        dict = { "Camera": Camera, "lens": lens, "tripods": tripods, "lightings": lightings , "Binoculars": Binoculars } 
    
        
        
        
        
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = dict[res].objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
        
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        return sum(Decimal(item['price'])*item['quantity'] for item in self.cart.values())
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
