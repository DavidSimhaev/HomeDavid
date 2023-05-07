from django import forms
PRODUCT_QUANTITY_CHOISES = [(i, str(i)) for i in range(1,21)]

class CartAddProductsForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOISES, coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget= forms.HiddenInput)
    
    def __init__(self, *args, **kwargs): # --- Не понял ----
        
        super(CartAddProductsForm,self).__init__()
        if "pquant" in kwargs:
            PRODUCT_QUANTITY_CHOISES =  [(i, str(i)) for i in range(1, int(kwargs["pquant"])) ]
            self.fields["quantity"].choices = PRODUCT_QUANTITY_CHOISES
        
        
        #else:
        #    CartAddProductsForm.PRODUCT_QUANTITY_CHOISES = [(i, str(i)) for i in range(1,21)]            
        #del kwargs["pquant"]
        #
        #CartAddProductsForm.quantity= forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
        #CartAddProductsForm.override= forms.BooleanField(required=False, initial=False, widget= forms.HiddenInput)
        #super(CartAddProductsForm,self).__init__()

            
    

