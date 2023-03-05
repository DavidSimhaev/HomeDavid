from django.shortcuts import render, redirect
from .models import Restaurant, Menu, Comment
from .forms import RestaurantForm, MenuShefForm
from .superClass import restjobclass
from .menuclass import MenuClass
from django.http import Http404
# Create your views here.

def index(request):
    grrr= False
    if request.user.groups.filter(id=1):
        grrr = True
    mapper = {"grrr": grrr}
    
    return render(request, "Food/index.html", mapper)
# <QuerySet [{'id': 1, 'name': 'SELLER'}]>
def jobRestaurant(request):
    grrr= False
    
    if request.user.groups.filter(id=1):
        grrr = True
    if grrr:
        jobrestaurant = Restaurant.objects.filter(owner=request.user)
        datejob = []
        for job in jobrestaurant:
            cwi = restjobclass()
            cwi.Name_Restaurant = Restaurant.objects.filter(owner=request.user).values("restaurant").get(id=job.id)['restaurant']
            cwi.Characteristic = Restaurant.objects.filter(owner=request.user).values("characteristic").get(id=job.id)['characteristic']
            cwi.city=  Restaurant.objects.filter(owner=request.user).values("city").get(id=job.id)['city']
            cwi.image = "/media/"+job.image.path
            cwi.res_id = Restaurant.objects.filter(owner=request.user).get(id=job.id)
        
            if cwi.res_id.approved == 0:
                datejob.append(cwi)
    else:
        jobclient = Restaurant.objects.all()
        datejob = []
        for client in jobclient:
            cwe = restjobclass()
            cwe.Name_Restaurant = Restaurant.objects.values("restaurant").get(id=client.id)['restaurant']
            cwe.Characteristic = Restaurant.objects.values("characteristic").get(id=client.id)['characteristic']
            cwe.city = Restaurant.objects.values("city").get(id=client.id)['city']
            cwe.image = "/media/"+client.image.path
            cwe.res_id = Restaurant.objects.get(id=client.id)
            datejob.append(cwe)
    
    
    
    
    mapper = {"jobRestaurant": datejob, "grrr":grrr}
    return render(request, "Food/jobRestaurant.html", mapper )


def AddRestaurant(request):
    if request.method != "POST":
        form = RestaurantForm()
    else:
        form = RestaurantForm(request.POST,  request.FILES)
        
        if form.is_valid:
            new_restaurant = form.save(commit=False)
            new_restaurant.owner= request.user
            
            new_restaurant.save()
            return redirect("Food:JobRestaurant")
        
    
    grrr= False
    if request.user.groups.filter(id=1):
        grrr = True
    
    mapper = {"form": form,"grrr": grrr }
    return render(request, "Food/newRestaurant.html", mapper)
         
def DelRestaurant(request,res_id):
    res = Restaurant.objects.get(id=res_id)
    res.delete()
    
    grrr= False
    if request.user.groups.filter(id=1):
        grrr = True
    mapper = {"grrr": grrr}
    return render(request, "Food/DelRestaurant.html", mapper) 


def PermissionPost(request):
    post = []
    Restarans= Restaurant.objects.filter(approved=0)
    for res in Restarans:
        cwi = restjobclass()          
        cwi.date = Restaurant.objects.all().get(id=res.id)
        if cwi.date.owner == request.user.is_staff:
            raise Http404
        cwi.image = "/media/"+res.image.path
        post.append(cwi)
    grrr= False
    if request.user.groups.filter(id=1):
        grrr = True
    
    mapper = {"postres": post, "grrr": grrr}
    return render(request,"Food/postres.html", mapper)


def getpost(request, res_id):
    res = Restaurant.objects.get(id=res_id)
    res.approved= 1
    res.save()
    grrr= False
    if request.user.groups.filter(id=1):
        grrr = True
    mapper = {"grrr": grrr}           
    return render(request,"Food/getdate.html", mapper)

def updatepost(request, res_id):
    res = Restaurant.objects.get(id=res_id)
    if res.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # Current record state
        form = RestaurantForm(instance=res)
    else:
        form = RestaurantForm(request.POST, request.FILES) # Застрял :(  
        
        if form.is_valid():
            rest= form.save(commit=False)
            rest.id = res_id
            rest.date_added = res.date_added
            rest.owner = request.user
            rest.approved = 1
            if rest.image == "":
                rest.image = res.image()
            rest.save()
            return redirect('Food:JobRestaurant')
    grrr= False
    if request.user.groups.filter(id=1):
        grrr = True
    
    mapper = {"Form": form, "res":res, "grrr": grrr}
    
    return render(request,'Food/update_res.html', mapper )

def menushef(request, res_id):
    
    
    
    menuuu = Menu.objects.filter(post=res_id)
    menushef = []
    for menu in menuuu:
        cwi = MenuClass()
        
        cwi.category = Menu.objects.values("categ").get(id=menu.id)['categ']
        cwi.dish = Menu.objects.values("dish").get(id=menu.id)['dish']
        cwi.price = Menu.objects.values("price").get(id=menu.id)['price']
        cwi.image = "/media/"+menu.image.path
        menushef.append(cwi)
    res_id = Restaurant.objects.get(id=res_id)
    menu_id = Menu.objects.get(id=res_id)
    
        
    
    grrr= False
    if request.user.groups.filter(id=1):
        grrr = True
           
    mapper = {"menushef": menushef, "res_id": res_id,"menu_id":menu_id, "grrr": grrr}
    return render(request,'Food/Menu.html', mapper)

def AddMenu(request, res_id):
    res_id = Restaurant.objects.get(id=res_id)
    
    if request.method != "POST":
        form = MenuShefForm()
    else:
        form = MenuShefForm(request.POST,  request.FILES)
        if form.is_valid:
            new_menu = form.save(commit=False)
            new_menu.owner= request.user
            new_menu.post = res_id
            new_menu.save()
            return redirect("Food:JobRestaurant")
        
    grrr= False
    if request.user.groups.filter(id=1):
        grrr = True
    
    mapper = {"form": form, "res_id": res_id, "grrr": grrr}
    return render(request, "Food/newMenu.html", mapper)

def Basket(request):
    grrr= False
    if request.user.groups.filter(id=1):
        grrr = True
    menubacket = []
    menuclient= Menu.objects.filter(approved=0)    
    for menu in menuclient:
        cwi = MenuClass()
        cwi.menu = Menu.objects.all().get(id=menu.id)
        cwi.category = Menu.objects.values("categ").get(id=menu.id)['categ']
        cwi.dish = Menu.objects.values("dish").get(id=menu.id)['dish']
        cwi.price = Menu.objects.values("price").get(id=menu.id)['price']
        cwi.image = "/media/"+menu.image.path    
        
        if cwi.menu.approved == 0:
            menubacket.append(cwi)
            
        
    mapper= {"basket": menubacket, "grrr": grrr}
    return render(request, "Food/Basket.html", mapper)
        
        

def GetProduct(request, menu_id):
    res = Menu.objects.get(id=menu_id)
    res.approved= 1
    res.save()
    grrr= False
    if request.user.groups.filter(id=1):
        grrr = True
    mapper = {"grrr": grrr}           
    return render(request,"Food/GetProduct.html", mapper)
