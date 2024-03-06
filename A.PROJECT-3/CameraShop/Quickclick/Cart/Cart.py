from decimal import Decimal
from django.conf import settings
from Main.models import Camera, lens, tripods, lightings, Binoculars

class Cart:
    def __init__(self, request):
        
        self.request =  request
        
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {'Camera': {}, 'lens': {} , 'tripods': {} ,'lightings': {} ,'Binoculars': {}}
            
        self.cart = cart
    
    
    def check_request(self):
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
        return res
    
    def add(self, product, quantity=1, override_quantity=False):
        print(self.cart)
        
        key = product.klass()
        
        product_id = str(product.id)
        print(key)

        if product_id not in self.cart[key]:
            

            
            self.cart[key][product_id] = {
                'quantity': 0,
                'price': int(product.price)
            }
        if override_quantity:
            self.cart[key][product_id]["quantity"] = quantity
        else:
            self.cart[key][product_id]["quantity"] += quantity
        self.save()
        
    def remove(self, product, key):
        product_id = str(product.id)
        
        
        if product_id in self.cart[key]:
            del self.cart[key][product_id]
            self.save()
            
    def save(self):
        self.session.modified = True
        
    def productq(self, product_id, obj_product): 
        
        res = self.check_request()
        
        if product_id in self.cart[obj_product].keys():
            return self.cart[obj_product][product_id]['quantity']
        
        return 0

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        res = self.check_request()
        dict = { "Camera": Camera, "lens": lens, "tripods": tripods, "lightings": lightings , "Binoculars": Binoculars } 
        # get the product objects and add them to the cart
        result = {}
        
        for key in dict:
            product_ids = self.cart[key].keys()
            
            result[key] = dict[key].objects.filter(id__in=product_ids )
            
        
        cart = self.cart.copy()
        for key in result:
            
            for id in cart[key]:
            
                cart[key][id]['product'] = result[key].get(id=id)
                
        
        for key in cart:
            for id in cart[key]:
            
                cart[key][id]['price'] = Decimal(cart[key][id]['price'])
                cart[key][id]['total_price'] = cart[key][id]['price'] * cart[key][id]['quantity']
                
                yield cart[key][id]
                
    def __len__(self):
        sum_obj = []
        for key in self.cart:
            for id in self.cart[key]:
                try:
                    sum_obj.append(self.cart[key][id]['quantity'])
                except:
                    pass
        
        
        
        return sum(sum_obj)
    
    def get_total_price(self):
        
        all_sum_obj = []
        for key in self.cart:
            for id in self.cart[key]:
                try:
                    all_sum_obj.append(self.cart[key][id]['price']*self.cart[key][id]['quantity'] )
                except:
                    pass
        return sum(all_sum_obj)
        return sum(Decimal(item['price'])*item['quantity'] for item in self.cart[res].values())
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
