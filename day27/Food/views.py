from django.shortcuts import render, redirect
from .models import Restaurant, Menu
from .forms import RestaurantForm, MenuShefForm
from .superClass import restjobclass
from .menuclass import MenuClass
from django.http import Http404
# Create your views here.

def index(request):
    return render(request, "Food/index.html")

def jobRestaurant(request):
    jobrestaurant = Restaurant.objects.filter(owner=request.user)
    datejob = []
    for job in jobrestaurant:
        cwi = restjobclass()
        cwi.Name_Restaurant = Restaurant.objects.filter(owner=request.user).values("restaurant").get(id=job.id)['restaurant']
        cwi.Characteristic = Restaurant.objects.filter(owner=request.user).values("characteristic").get(id=job.id)['characteristic']
        cwi.city=  Restaurant.objects.filter(owner=request.user).values("city").get(id=job.id)['city']
        cwi.image = "/media/"+job.image.path
        cwi.res_id = Restaurant.objects.filter(owner=request.user).get(id=job.id)
    
        
        if cwi.res_id.approved == 1:
            datejob.append(cwi)
                

    
        
    mapper = {"jobRestaurant": datejob}
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
    mapper = {"form": form}
    return render(request, "Food/newRestaurant.html", mapper)
         
def DelRestaurant(request,res_id):
    res = Restaurant.objects.get(id=res_id)
    res.delete()
    return render(request, "Food/DelRestaurant.html") 


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
    mapper = {"postres": post}
    return render(request,"Food/postres.html", mapper)


def getpost(request, res_id):
    res = Restaurant.objects.get(id=res_id)
    res.approved= 1
    res.save()
               
    return render(request,"Food/getdate.html")

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
        
    mapper = {"Form": form, "res":res}
    
    return render(request,'Food/update_res.html', mapper )

def menushef(request, res_id):
    jobrestaurant = Restaurant.objects.filter(id=res_id)
    menu=[]
    for res in jobrestaurant: 
        mc = MenuClass()
        mc.category = Menu.objects.filter(owner=request.user).values("categ")[0]["categ"]
        mc.dish = Menu.objects.filter(owner=request.user).values("dish")[0]["dish"]
        mc.image = "/media/"+res.image.path
        mc.price = Menu.objects.filter(owner=request.user).values("price")[0]["price"]
        
        menu.append(mc)
        
    mapper = {"menushef": menu}
    
    
    return render(request,'Food/Menu.html', mapper)

def AddMenu(request):
    
    if request.method != "POST":
        form = MenuShefForm()
    else:
        form = MenuShefForm(request.POST,  request.FILES)
        if form.is_valid:
            new_menu = form.save(commit=False)
            new_menu.owner= request.user
            new_menu.save()
            return redirect("Food:JobRestaurant")
    mapper = {"form": form}
    return render(request, "Food/newMenu.html", mapper)

