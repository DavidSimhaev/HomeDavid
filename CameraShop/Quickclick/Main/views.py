from mixer.backend.django import mixer
from django.contrib.auth.models import User
user = mixer.blend(User)
from .superclass import Contener
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import IMG_PROFILE_FORM
from .models import Color,Category,Camera, lens, lightings, tripods, Binoculars, IMG_FILES, IMG_FILES_LENS, IMG_FILES_TRIPODS, IMG_FILES_LIGHTS, IMG_FILES_BINOCULARS, account_data, PROFILE_IMG
from django.db import connection
from .superclass import Contener
from Cart.forms import CartAddProductsForm
from Cart.Cart import Cart
from .Contaner import Contener_SCSS_to_CSS
import os

from django.http import QueryDict
# Create your views here.
from django.contrib import messages
import pathlib
from django.contrib.auth import authenticate, login, logout
import shutil

from django.conf import settings

FORM_FLAG = False
CONTENT_FLAG = False
COUNT = 0

def authentication(request):
    
    __login = request.GET.get('login')
    __password = request.GET.get('password')
    user = authenticate(request, username=__login, password=__password)
    if user is not None:
        login(request, user)
        
        return redirect(request.META.get('HTTP_REFERER','redirect_if_referer_not_found'))
    else:
        global CONTENT_FLAG
        CONTENT_FLAG = True
        count = 0
        #http://127.0.0.1:8000/Lightings/
        l=[]
        str_class = []
        #'http://127.0.0.1:8000/Camers/'
        for x in request.META['HTTP_REFERER']:
            
            if x == "/":
                count +=1
                continue
            if count == 3:
                l.extend(x)  
            if count == 4:
                arg = x
            if count == 5:
                str_class.extend(x)
        
        str_class = "".join(str_class) 
        html_name= "".join(l)
        if count > 4:
            html_name += "_product"
        if html_name == "":
            html_name= "Main"
            
        
        try:
            # ЕСЛИ ЕСТЬ АРГУМЕНТЫ
            content = (arg,str_class)
            print(html_name)
            print(str_class)
            redirect_url = reverse(f"Main:{html_name}", args=content)
            return redirect(f'{redirect_url}')
        except:
            # НЕТ АРГУМЕНТОВ
            return redirect(f"Main:{html_name}")

def UserLoggedIn(request):
    if request.user.is_authenticated == True:
        username = request.user.username
    else:
        username = None
    return username

def logout_view(request):
    username = UserLoggedIn(request)
    if username != None:
        logout(request)
        return redirect("Main:Main")

def Main(request):
    content = {}
    global CONTENT_FLAG
    if CONTENT_FLAG == True:
        content['some_flag'] = True
        CONTENT_FLAG = False
    return render(request, "Main/URLS/Main.html", content)

def Camers(request):
    product = Camera.objects.all()
    line = (len(product.values())//4+1)
    if len(product.values()) % 4 == 0:
        line = line -1
    cart_product_form = CartAddProductsForm(pquant=1)
    category_camera = {" ": ""}
    category_camera_spec = {" ": ""}
    category_matrix_format = {" ": ""}
    category_Bayonet = {" ": ""}
    category_Color = {" ": ""}
    for i in product:
        category_camera[i.category]= ""
        category_camera_spec[i.firm] = ""
        category_matrix_format[i.Matrix_format] = ""
        category_Bayonet[i.Bayonet] = ""
        category_Color[i.color] = ""
    
    
   
    quant = []
    cart_product_form = []
    for elem in product:    
        if elem.stock < 21:
            pquant = elem.stock + 1
        
            cart_product_form.append(CartAddProductsForm(pquant=pquant))
        else:
            pquant = 21
            cart_product_form.append(CartAddProductsForm())
        
 

        quant.append(Cart(request).productq(str(elem.id), elem.klass()))
    if product == []:
            mylist = False
    else:
        mylist = zip(product, cart_product_form)
    
    content = {"Camers":mylist, 
               "line": 440* line,
               "quant": quant,
               "category_camera": category_camera.keys(),
               "category_camera_spec": category_camera_spec.keys(), 
               "category_matrix_format": category_matrix_format.keys(),
               "category_Bayonet": category_Bayonet.keys(),
               "category_Color": category_Color.keys()
               }
    global CONTENT_FLAG
    if CONTENT_FLAG == True:
        content['some_flag'] = True
        CONTENT_FLAG = False
    
        
        
    return render(request, "Main/URLS/Camers.html", content )
  
def Camers_filtred(request):
    global CONTENT_FLAG
    ID_CAMERA = request.GET.get('ID-CAMERA')
    ID_CAMERA_SPEC = request.GET.get('ID-CAMERA-SPEC')
    ID_MATRIX_FORMAT = request.GET.get("ID-MATRIX_FORMAT")
    ID_BAYONET = request.GET.get("ID-BAYONET")
    ID_COLOR = request.GET.get("ID-COLOR")
    ID_BUDJET = request.GET.get("pi_input")
    ID_LENS = request.GET.get("ID-LENS")
    ID_HAND = request.GET.get("ID-HAND")
    if ID_LENS == "false":
        ID_LENS = False
    else:
        ID_LENS = True 
    if ID_HAND == "false":
        ID_HAND = False
    else:
        ID_HAND = True
    try:
        category = Category.objects.values().filter(model= ID_CAMERA)[0]["id"]
        selected_category = True
    except:
        category = None
    try:
        color = Color.objects.values().filter(color= ID_COLOR)[0]["id"]
        selected_color= True
    except:
        color = None
            
    product_1 = Camera.objects.filter(category= category)
    product_2 = Camera.objects.filter(firm= ID_CAMERA_SPEC)
    product_3 = Camera.objects.filter(Matrix_format= ID_MATRIX_FORMAT)
    product_4 = Camera.objects.filter(Bayonet= ID_BAYONET)
    product_5 = Camera.objects.filter(color= color)
    product_6 = Camera.objects.filter(lens= ID_LENS)
    product_7 = Camera.objects.filter(hand= ID_HAND)
    list_product = [product_1,product_2,product_4,product_3,product_5, product_6, product_7]
    result = []
    len_objest = 4
    last_step = True
    first = True
    ex_list = []
    RESULT_LIST_ID = []
    for index in range(len(list_product)):
        if str(list_product[index]) == "<QuerySet []>":
            len_objest -=1
            last_step = False
        else:
            if last_step== True:
                last_step_list = list_product[index]
                ex_list.append(last_step_list)
            else:
                try:
                    for elem in last_step_list:
                        if elem in list_product[index]:
                                RESULT_LIST_ID.append(elem) # тут
                                first = False
                        last_step = True
                    if first == False:
                        res= list(set(RESULT_LIST_ID) & set(list_product[index+1]))
                        RESULT_LIST_ID.clear()
                        first = True
                except:
                    res = product_5  

    try:
        if last_step == False and len_objest == 0 and selected_category: # ПРОВЕРКА ЕСЛИ ТОЛЬКО ВЫБРАНА КАТЕГОРИЯ 

            
            for elem in product_1:
                RESULT_LIST_ID.append(elem)
    except:
        pass
    try:
        if last_step == True and len_objest == 0 and selected_color: # ПРОВЕРКА ЕСЛИ ТОЛЬКО ВЫБРАНА КАТЕГОРИЯ 

            
            for elem in product_5:
                RESULT_LIST_ID.append(elem)
    except:
        pass
    
    res_end = []
    first = True   
    try:
        if last_step == False and len_objest == 0 and selected_color: # ПРОВЕРКА ЕСЛИ ТОЛЬКО ВЫБРАН ЦВЕТ
            for elem in product_5:
                RESULT_LIST_ID.append(elem)
    except:
        pass
  
    try:
        res
    except:
        for index in range(len(ex_list)):
            try:
                if first:
                    first = False
                    res_end.extend(list(set(ex_list[index]) & set(ex_list[index+1])))
                if first == False:
                    res = list(set(res_end[::-1]) & set(ex_list[index+1]))
                    print(res)
                    first = True
                if res == []:
                    break
            except:
                pass
    c = 0
    
    
    if last_step == True and str(list_product[-2]) == "<QuerySet []>":
        while True:
            c+=1
            if str(list_product[-2-c]) != "<QuerySet []>":
                res =list(set(list_product[-2-c]) & set(RESULT_LIST_ID))
                break

    try:  
        result = []
        for elem in res:
            if int(elem.price) <= int(ID_BUDJET):
                result.append(elem)
        line = (len(result)//4+1)
        if len(result) % 4 == 0:
            line = line -1
        cart_product_form = CartAddProductsForm(pquant=1)
        category_camera = {" ": ""}
        category_camera_spec = {" ": ""}
        category_matrix_format = {" ": ""}
        category_Bayonet = {" ": ""}
        category_Color = {" ": ""}
        for i in Camera.objects.all():
            category_camera[i.category]= ""
            category_camera_spec[i.firm] = ""
            category_matrix_format[i.Matrix_format] = ""
            category_Bayonet[i.Bayonet] = ""
            category_Color[i.color] = ""
        
        if result == []:
            result = True
            
            
        quant = []
        cart_product_form = []
        for elem in result:    
            if elem.stock < 21:
                pquant = elem.stock + 1
            
                cart_product_form.append(CartAddProductsForm(pquant=pquant))
            else:
                pquant = 21
                cart_product_form.append(CartAddProductsForm())
            quant.append(Cart(request).productq(str(elem.id), elem.klass()))
        if result == []:
            mylist = False
        else:
            mylist = zip(result, cart_product_form)
            
        content = {"Camers":mylist, 
               "line": 440* line,
               "FORM_TO_BACKET":cart_product_form,
               "category_camera": category_camera.keys(),
               "category_camera_spec": category_camera_spec.keys(), 
               "category_matrix_format": category_matrix_format.keys(),
               "category_Bayonet": category_Bayonet.keys(),
               "category_Color": category_Color.keys()
               }
        if CONTENT_FLAG == True:
            content['some_flag'] = True
            CONTENT_FLAG = False
        return render(request, "Main/URLS_FILTRED/Camera_filtred.html", content )
    except:
        result = []
        for elem in RESULT_LIST_ID:
            if int(elem.price) <= int(ID_BUDJET):
                result.append(elem)
        line = (len(result)//4+1)
        if len(result) % 4 == 0:
            line = line -1
        cart_product_form = CartAddProductsForm(pquant=1)
        category_camera = {" ": ""}
        category_camera_spec = {" ": ""}
        category_matrix_format = {" ": ""}
        category_Bayonet = {" ": ""}
        category_Color = {" ": ""}
        for i in Camera.objects.all():
            category_camera[i.category]= ""
            category_camera_spec[i.firm] = ""
            category_matrix_format[i.Matrix_format] = ""
            category_Bayonet[i.Bayonet] = ""
            category_Color[i.color] = ""
            
        quant = []
        cart_product_form = []
        for elem in result:    
            if elem.stock < 21:
                pquant = elem.stock + 1
            
                cart_product_form.append(CartAddProductsForm(pquant=pquant))
            else:
                pquant = 21
                cart_product_form.append(CartAddProductsForm())
            quant.append(Cart(request).productq(str(elem.id), elem.klass()))
        if result == []:
            mylist = False
        else:
            mylist = zip(result, cart_product_form)
        
        content = {"Camers":mylist, 
               "line": 440* line,
               "FORM_TO_BACKET":cart_product_form,
               "category_camera": category_camera.keys(),
               "category_camera_spec": category_camera_spec.keys(), 
               "category_matrix_format": category_matrix_format.keys(),
               "category_Bayonet": category_Bayonet.keys(),
               "category_Color": category_Color.keys()
               }
        if CONTENT_FLAG == True:
            content['some_flag'] = True
            CONTENT_FLAG = False
        return render(request, "Main/URLS_FILTRED/Camera_filtred.html", content )
        
def Lens(request):
    product = lens.objects.all()
    line = (len(product.values())//4+1)
    if len(product.values()) % 4 == 0:
        line = line -1
    cart_product_form = CartAddProductsForm(pquant=1)
    
    
    category_obj_camera = {" ": ""}
    category_type = {" ": ""}
    category_Color = {" ": ""}
    for i in product:
        category_obj_camera[i.category]= ""
        category_type[i.type] = ""
        category_Color[i.color] = ""
    
    quant = []
    cart_product_form = []
    for elem in product:    
        if elem.stock < 21:
            pquant = elem.stock + 1
        
            cart_product_form.append(CartAddProductsForm(pquant=pquant))
        else:
            pquant = 21
            cart_product_form.append(CartAddProductsForm())
        
 

        quant.append(Cart(request).productq(str(elem.id), elem.klass()))
    mylist = zip(product, cart_product_form)
    content = {"Lens": mylist,
               "line": 440* line,
               "category_obj_camera": category_obj_camera.keys(), 
               "category_type": category_type.keys(),
               "category_Color": category_Color.keys()
               }
    
    global CONTENT_FLAG
    if CONTENT_FLAG == True:
        content['some_flag'] = True
        CONTENT_FLAG = False

    return render(request, "Main/URLS/Lens.html", content )

def Lens_filtred(request):
    
    global CONTENT_FLAG
    category_obj_camera = request.GET.get('category_obj_camera')
    category_type = request.GET.get('category_type')
    Category_Color = request.GET.get("category_Color")
    ID_BUDJET = request.GET.get("pi_input")
    ID_LENS = request.GET.get("ID-LENS")
    ID_HAND = request.GET.get("ID-HAND")
    if ID_LENS == "false":
        ID_LENS = False
    else:
        ID_LENS = True 
    if ID_HAND == "false":
        ID_HAND = False
    else:
        ID_HAND = True
    try:
        category = Category.objects.values().filter(model= category_obj_camera)[0]["id"]
        selected_category = True
    except:
        category = None
    try:
        color = Color.objects.values().filter(color= Category_Color )[0]["id"]
        selected_color= True
    except:
        color = None   
    product_1 = lens.objects.filter(category= category)
    product_2 = lens.objects.filter(type= category_type)
    product_5 = lens.objects.filter(color= color)

    product_7 = lens.objects.filter(hand= ID_HAND)
    list_product = [product_1,product_2,product_5, product_7]
    result = []
    len_objest = 2
    last_step = True
    first = True
    ex_list = []
    RESULT_LIST_ID = []
    for index in range(len(list_product)):
        
        print(list_product[index])
        
        
        if str(list_product[index]) == "<QuerySet []>":
            len_objest -=1
            last_step = False
        else:
            if last_step== True:
                last_step_list = list_product[index]
                ex_list.append(last_step_list)
            else:
                try:
                    for elem in last_step_list:
                        if elem in list_product[index]:
                                RESULT_LIST_ID.append(elem) # тут
                                first = False
                        last_step = True
                    if first == False:
                        res= list(set(RESULT_LIST_ID) & set(list_product[index+1]))
                        RESULT_LIST_ID.clear()
                        first = True
                except:
                    res = product_5  

    try:
        if last_step and len_objest == 0 and selected_category: # ПРОВЕРКА ЕСЛИ ТОЛЬКО ВЫБРАНА КАТЕГОРИЯ 

            
            for elem in product_1:
                RESULT_LIST_ID.append(elem)
    except:
        pass
    try:
        if last_step == True and len_objest == 0 and selected_color: # ПРОВЕРКА ЕСЛИ ТОЛЬКО ВЫБРАНА КАТЕГОРИЯ 

            
            for elem in product_5:
                RESULT_LIST_ID.append(elem)
    except:
        pass
    
    res_end = []
    first = True  

   
  
    try:
        res
    except:
        for index in range(len(ex_list)):
            try:
                if first:
                    first = False
                    res_end.extend(list(set(ex_list[index]) & set(ex_list[index+1])))
                if first == False:
                    res = list(set(res_end[::-1]) & set(ex_list[index+1]))
                    print(res)
                    first = True
                if res == []:
                    break
            except:
                pass
    c = 0
    
    if last_step == True and str(list_product[-2]) == "<QuerySet []>":
        while True:
            c+=1
            if str(list_product[-2-c]) != "<QuerySet []>":
                res =list(set(list_product[-2-c]) & set(RESULT_LIST_ID))
                break

    try:  
        result = []
        for elem in res:
            if int(elem.price) <= int(ID_BUDJET):
               
                result.append(elem)
        line = (len(result)//4+1)
        if len(result) % 4 == 0:
            line = line -1
        cart_product_form = CartAddProductsForm(pquant=1)
        category_camera = {" ": ""}
        category_camera_spec = {" ": ""}
        category_matrix_format = {" ": ""}
        category_Bayonet = {" ": ""}
        category_Color = {" ": ""}
        for i in lens.objects.all():
            category_camera[i.category]= ""
            category_camera_spec[i.type] = ""
            category_Color[i.color] = ""
       
        if result == []:
            result = True 
        quant = []
        cart_product_form = []
        for elem in result:    
            if elem.stock < 21:
                pquant = elem.stock + 1
            
                cart_product_form.append(CartAddProductsForm(pquant=pquant))
            else:
                pquant = 21
                cart_product_form.append(CartAddProductsForm())
        if result == []:
            mylist = False
        else:
            mylist = zip(result, cart_product_form)
        
        print(result)
        content = {"Lens":mylist, 
               "line": 440* line,
               "category_camera": category_camera.keys(),
               "category_camera_spec": category_camera_spec.keys(), 
               
               "category_Color": category_Color.keys()
               }
        if CONTENT_FLAG == True:
            content['some_flag'] = True
            CONTENT_FLAG = False
            
        return render(request, "Main/URLS_FILTRED/Lens_filtred.html", content )
    except:
        
        result = []
        for elem in RESULT_LIST_ID:
            if int(elem.price) <= int(ID_BUDJET):

                result.append(elem)
        line = (len(result)//4+1)
        if len(result) % 4 == 0:
            line = line -1
        
        category_camera = {" ": ""}
        category_camera_spec = {" ": ""}
        category_matrix_format = {" ": ""}
        category_Bayonet = {" ": ""}
        category_Color = {" ": ""}
        for i in Camera.objects.all():
            category_camera[i.category]= ""
            category_camera_spec[i.firm] = ""
            category_matrix_format[i.Matrix_format] = ""
            category_Bayonet[i.Bayonet] = ""
            category_Color[i.color] = ""
            
        quant = []
        cart_product_form = []
        for elem in result:    
            if elem.stock < 21:
                pquant = elem.stock + 1
            
                cart_product_form.append(CartAddProductsForm(pquant=pquant))
            else:
                pquant = 21
                cart_product_form.append(CartAddProductsForm())
        
        if result == []:
            mylist = False
        else:
            mylist = zip(result, cart_product_form)
        content = {"Lens":mylist, 
               "line": 440* line,
               "FORM_TO_BACKET":cart_product_form,
               "category_camera": category_camera.keys(),
               "category_camera_spec": category_camera_spec.keys(), 
               "category_matrix_format": category_matrix_format.keys(),
               "category_Bayonet": category_Bayonet.keys(),
               "category_Color": category_Color.keys()
               }
        if CONTENT_FLAG == True:
            content['some_flag'] = True
            CONTENT_FLAG = False
        return render(request, "Main/URLS_FILTRED/Lens_filtred.html", content )
  
def Lighting(request):
    
    
    product = lightings.objects.all()
    line = (len(product.values())//4+1)
    if len(product.values()) % 4 == 0:
        line = line -1
    
    cart_product_form = CartAddProductsForm(pquant=1)    
    content = {"Lightings": product, "line": 440* line, "FORM_TO_BACKET": cart_product_form}

    global CONTENT_FLAG
    if CONTENT_FLAG == True:
        content['some_flag'] = True
        CONTENT_FLAG = False
    
    return render(request, "Main/URLS/Lightings.html", content )

def Tripods(request):
    
    
    
    product = tripods.objects.all()
    line = (len(product.values())//4+1)
    if len(product.values()) % 4 == 0:
        line = line -1
    
    cart_product_form = CartAddProductsForm(pquant=1)
    
    content = {"Tripods": product, "line": 440* line, "FORM_TO_BACKET": cart_product_form}
    
    global CONTENT_FLAG
    if CONTENT_FLAG == True:
        content['some_flag'] = True
        CONTENT_FLAG = False
    
    return render(request, "Main/URLS/Tripods.html", content )

def binoculars(request):
    
    
    
    product = Binoculars.objects.all()
    line = (len(product.values())//4+1)
    if len(product.values()) % 4 == 0:
        line = line -1
        
    cart_product_form = CartAddProductsForm(pquant=1)
    
    content = {"Binoculars": product, "line": 440* line, "FORM_TO_BACKET": cart_product_form}
    
    global CONTENT_FLAG
    if CONTENT_FLAG == True:
        content['some_flag'] = True
        CONTENT_FLAG = False
    
    return render(request, "Main/URLS/binoculars.html" , content)

def update_variable(value):
    """Allows to update existing variable in template"""
    return value
def Camera_product(request, cam_id, obj_product):
    Camera_product = Camera.objects.get(id=cam_id)
    font_bool = len(Camera_product.name) + len(Camera_product.firm)
    
    
    ############ ДАННЫЕ ############################
    
    images_pr = Contener
    images_pr.cls = IMG_FILES.objects.filter(post=Camera_product)
    images_pr.quintity = []
    try:
        images_pr.common_denominator = 100//len(images_pr.cls)
        images_pr.array = []
        images_pr.len = len(images_pr.cls)+1   
        for i in range(len(images_pr.cls)):
            images_pr.array.append(i*images_pr.common_denominator)
            images_pr.quintity.append(i+1)
    except ZeroDivisionError:
        images_pr.common_denominator = 1
        images_pr.array = [1]
        images_pr.len = 1
    ############ ДАННЫЕ ############################
    path = f"{os.getcwd()}/Main/static/Main/css/style.scss".replace("\\", "/")
    result_text_css = Contener_SCSS_to_CSS(str(images_pr.len-1)+"00",images_pr.common_denominator, images_pr.len-1).write_arg()
    with open(path, "w+", encoding= "utf-8") as f:
        f.write(result_text_css)
     
    if Camera_product.stock < 21:
        pquant = Camera_product.stock + 1
    
        cart_product_form = CartAddProductsForm(pquant=pquant)
    else:
        pquant = 21
        cart_product_form = CartAddProductsForm()

    quant = Cart(request).productq(str(cam_id), obj_product)

    if pquant !=1:
        
        mapper= {"Camera": Camera_product, "font_bool": font_bool, "quant": quant ,"FORM_TO_BACKET":cart_product_form, "images_pr":images_pr }
        
        global CONTENT_FLAG
        if CONTENT_FLAG == True:
            mapper['some_flag'] = True
            CONTENT_FLAG = False
            
        
        
        return render(request, "Main/URLS_2/product_camera.html", mapper)
    else:
        
        return render(request, "Main/URLS_2/product_camera.html", mapper)
        
def Lens_product(request, lens_id, obj_product):
    Camera_product = lens.objects.get(id=lens_id)
    font_bool = len(Camera_product.name)
    
    ############ ДАННЫЕ ############################
    images_pr = Contener
    images_pr.cls = IMG_FILES_LENS.objects.filter(post=Camera_product)
    images_pr.quintity = []
    try:
        images_pr.common_denominator = 100//len(images_pr.cls)
        images_pr.array = []
        images_pr.len = len(images_pr.cls)+1   
        for i in range(len(images_pr.cls)):
            images_pr.array.append(i*images_pr.common_denominator)
            images_pr.quintity.append(i+1)
    except ZeroDivisionError:
        images_pr.common_denominator = 1
        images_pr.array = [1]
        images_pr.len = 1
    ############ ДАННЫЕ ############################
    path = f"{os.getcwd()}/Main/static/Main/css/style.scss".replace("\\", "/")
    result_text_css = Contener_SCSS_to_CSS(str(images_pr.len-1)+"00",images_pr.common_denominator, images_pr.len-1).write_arg()
    with open(path, "w+", encoding= "utf-8") as f:
        f.write(result_text_css)
     
    
    if Camera_product.stock < 21:
        pquant = Camera_product.stock + 1
        cart_product_form = CartAddProductsForm(pquant=pquant)
    else:
        pquant = 21
        cart_product_form = CartAddProductsForm()
    
    quant = Cart(request).productq(str(lens_id), obj_product)
    
    
    
    
    if pquant !=1:
        mapper= {"Lens": Camera_product, "font_bool": font_bool, "quant": quant ,"FORM_TO_BACKET":cart_product_form, "images_pr": images_pr}
        global CONTENT_FLAG
        if CONTENT_FLAG == True:
            mapper['some_flag'] = True
            CONTENT_FLAG = False
            
        return render(request, "Main/URLS_2/lens_product.html", mapper)
    
    else:    
        return render(request, "Main/URLS_2/lens_product.html", mapper)
    
def Tripods_product(request, trip_id, obj_product ):
    Camera_product = tripods.objects.get(id=trip_id)
    font_bool = len(Camera_product.name)
    ############ ДАННЫЕ ############################
    images_pr = Contener
    images_pr.cls = IMG_FILES_TRIPODS.objects.filter(post=Camera_product)
    images_pr.quintity = []
    try:
        images_pr.common_denominator = 100//len(images_pr.cls)
        images_pr.array = []
        images_pr.len = len(images_pr.cls)+1   
        for i in range(len(images_pr.cls)):
            images_pr.array.append(i*images_pr.common_denominator)
            images_pr.quintity.append(i+1)
    except ZeroDivisionError:
        images_pr.common_denominator = 1
        images_pr.array = [1]
        images_pr.len = 1
    ############ ДАННЫЕ ############################
    path = f"{os.getcwd()}/Main/static/Main/css/style.scss".replace("\\", "/")
    result_text_css = Contener_SCSS_to_CSS(str(images_pr.len-1)+"00",images_pr.common_denominator, images_pr.len-1).write_arg()
    with open(path, "w+", encoding= "utf-8") as f:
        f.write(result_text_css)
    if Camera_product.stock < 21:
        pquant = Camera_product.stock + 1
        cart_product_form = CartAddProductsForm(pquant=pquant)
    else:
        pquant = 21
        cart_product_form = CartAddProductsForm()
    
    quant = Cart(request).productq(str(trip_id), obj_product)
    if pquant !=1:
        mapper= {"Trip": Camera_product, "font_bool": font_bool, "quant": quant ,"FORM_TO_BACKET":cart_product_form, "images_pr": images_pr}
        global CONTENT_FLAG
        if CONTENT_FLAG == True:
            mapper['some_flag'] = True
            CONTENT_FLAG = False
            
        
        return render(request, "Main/URLS_2/trip_product.html", mapper)
    else:
        return render(request, "Main/URLS_2/trip_product.html", mapper)
    
def Lighting_product(request, Lighting_id, obj_product):
    Camera_product = lightings.objects.get(id=Lighting_id)
    font_bool = len(Camera_product.name)
    ############ ДАННЫЕ ############################
    images_pr = Contener
    images_pr.cls = IMG_FILES_LIGHTS.objects.filter(post=Camera_product)
    images_pr.quintity = []
    try:
        images_pr.common_denominator = 100//len(images_pr.cls)
        images_pr.array = []
        images_pr.len = len(images_pr.cls)+1   
        for i in range(len(images_pr.cls)):
            images_pr.array.append(i*images_pr.common_denominator)
            images_pr.quintity.append(i+1)
    except ZeroDivisionError:
        images_pr.common_denominator = 1
        images_pr.array = [1]
        images_pr.len = 1
    ############ ДАННЫЕ ############################
    path = f"{os.getcwd()}/Main/static/Main/css/style.scss".replace("\\", "/")
    result_text_css = Contener_SCSS_to_CSS(str(images_pr.len-1)+"00",images_pr.common_denominator, images_pr.len-1).write_arg()
    with open(path, "w+", encoding= "utf-8") as f:
        f.write(result_text_css)
    if Camera_product.stock < 21:
        pquant = Camera_product.stock + 1
        cart_product_form = CartAddProductsForm(pquant=pquant)
    else:
        pquant = 21
        cart_product_form = CartAddProductsForm()
    quant = Cart(request).productq(str(Lighting_id), obj_product)
    if pquant !=1:
        mapper= {"lightings": Camera_product, "font_bool": font_bool, "quant": quant ,"FORM_TO_BACKET":cart_product_form, "images_pr": images_pr}
        global CONTENT_FLAG
        if CONTENT_FLAG == True:
            mapper['some_flag'] = True
            CONTENT_FLAG = False
            
        
        return render(request, "Main/URLS_2/lightings_product.html", mapper)
    else:
        return render(request, "Main/URLS_2/lightings_product.html", mapper)
      
def Binoculars_product(request, Binoculars_id, obj_product):
    Camera_product = Binoculars.objects.get(id=Binoculars_id)
    font_bool = len(Camera_product.name)
    ############ ДАННЫЕ ############################
    images_pr = Contener
    images_pr.cls = IMG_FILES_BINOCULARS.objects.filter(post=Camera_product)
    images_pr.quintity = []
    try:
        images_pr.common_denominator = 100//len(images_pr.cls)
        images_pr.array = []
        images_pr.len = len(images_pr.cls)+1   
        for i in range(len(images_pr.cls)):
            images_pr.array.append(i*images_pr.common_denominator)
            images_pr.quintity.append(i+1)
    except ZeroDivisionError:
        images_pr.common_denominator = 1
        images_pr.array = [1]
        images_pr.len = 1
    ############ ДАННЫЕ ############################
    path = f"{os.getcwd()}/Main/static/Main/css/style.scss".replace("\\", "/")
    result_text_css = Contener_SCSS_to_CSS(str(images_pr.len-1)+"00",images_pr.common_denominator, images_pr.len-1).write_arg()
    with open(path, "w+", encoding= "utf-8") as f:
        f.write(result_text_css)
    if Camera_product.stock < 21:
        pquant = Camera_product.stock + 1
        cart_product_form = CartAddProductsForm(pquant=pquant)
    else:
        pquant = 21
        cart_product_form = CartAddProductsForm()
    
    quant = Cart(request).productq(str(Binoculars_id), obj_product)
    if pquant !=1:
        mapper= {"Binoculars": Camera_product, "font_bool": font_bool,  "quant": quant ,"FORM_TO_BACKET":cart_product_form, "images_pr": images_pr}
        global CONTENT_FLAG
        if CONTENT_FLAG == True:
            mapper['some_flag'] = True
            CONTENT_FLAG = False
            
        
        return render(request, "Main/URLS_2/Binoculars_product.html", mapper)
    else:
        return render(request, "Main/URLS_2/Binoculars_product.html", mapper)

def Profile_Page(request):
    global FORM_FLAG
    global CONTENT_FLAG
    global COUNT
    
    Profile_name = request.user.username
    first_name = request.user.first_name
    last_name = request.user.last_name
    email = request.user.email
    l = request.user.groups.values_list('name',flat = True) # QuerySet Object
    status = list(l)[0]
    
    user_id = User.objects.values().filter(username=Profile_name)[0]["id"]
    try:
        foto = PROFILE_IMG.objects.get(post=user_id)
    except:
        foto = False
    mapper = {"Profile_name": Profile_name,
              "first_name": first_name,
              "last_name": last_name ,
              "email": email,
              "foto": foto,
              "status": status}
    if CONTENT_FLAG == True:
            mapper['some_flag'] = True
            CONTENT_FLAG = False
                        
    return render(request, "Main/URLS/Profile.html", mapper)

def Change_Profile_Name(request):
    Name_change = request.GET.get('name-change')
    name = User.objects.get(username= request.user.username)
    name.first_name = Name_change
    name.save()
    return redirect("Main:Profile")

def Change_Profile_Last(request):
    Name_change = request.GET.get('name-change')
    name = User.objects.get(username= request.user.username)
    name.last_name = Name_change
    name.save()
    return redirect("Main:Profile")

def Change_Profile_Email(request):
    global CONTENT_FLAG
    Name_change = request.GET.get('name-change')
    if "@" not in Name_change:
        CONTENT_FLAG = True
        return redirect("Main:Profile")
    name = User.objects.get(username= request.user.username)
    name.email = Name_change
    name.save()
    return redirect("Main:Profile")

def Change_Profile_Foto(request):
    print(request.user.id)
    if request.method != "POST":
        # NO DATE IN REQUEST
        form = IMG_PROFILE_FORM()
    else:
        if str(PROFILE_IMG.objects.values().filter(post=request.user.id)) == '<QuerySet []>':
            pass
        else:
            PROFILE_IMG.objects.filter(post=str(request.user.id)).delete()
            
        data = dict(request.POST)
        new_dict = {}
        for key in data.keys():
            new_dict[key]= data[key][0]
        new_dict["post"] = str(request.user.id)
        query_dict = QueryDict('', mutable=True)
        query_dict.update(new_dict)
        form = IMG_PROFILE_FORM(query_dict, request.FILES)

        if form.is_valid():
            

            form.save()
            return redirect("Main:Profile")
    mapper = {}
    mapper["FORM_FOTO"]= form
    

    return render(request, "Main/URLS_3/Change_foto.html", mapper)

 
    
def ErrorGetData(request):
    return render(request, "Main/product/error.html")    