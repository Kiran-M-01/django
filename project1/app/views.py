from django.shortcuts import render

def sample(request):
    context = {
        'name': 'tejas',
        'age': 20,
        'gender': 'male',
        'sent' : 'Victory has defeated you. Peace has cost you your strength.'
    }
    return render(request, 'sample.html', context)


def sum(request,a,b):
    context = {
        'a' : a,
        'b' : b,
        'c' : a + b
    }

    return render(request,'sum.html', context)

def isvowel(request,ch):
    context = { 'ch' : ch}
    return render(request,'isvowel.html',context)


# IF, IF - ELSE CONDITIONS

# 1. Positive Number
def positive(request,num):
    context = {
        "num": num,
        "type": "positive"
    }
    return render(request, "if-if-else.html", context)


# 2. Voting Eligibility
def vote(request,age):
    context = {
        "age": age,
        "type": "vote"
    }
    return render(request, "if-if-else.html", context)


# 3. Check Name
def name(request,name):
    context = {
        "name": name,
        "type": "name"
    }
    return render(request, "if-if-else.html", context)


# 4. Fruit List
def fruits(request,fruit_list):
    # fruit_list = ["Apple", "Banana", "Mango"]
    context = {
        "fruits": fruit_list,
        "type": "fruits"
    }
    return render(request, "if-if-else.html", context)


# 5. Login Status (if)
def login(request):
    context = {
        "logged_in": True,
        "type": "login"
    }
    return render(request, "if-if-else.html", context)


# 6. Even or Odd (if-else)
def evenodd(request,num):
    context = {
        "num": num,
        "type": "evenodd"
    }
    return render(request, "if-if-else.html", context)


# 7. Adult or Minor (if-else)
def adult(request,age):
    context = {
        "age": age,
        "type": "adult"
    }
    return render(request, "if-if-else.html", context)


# 8. Pass or Fail (if-else)
def result(request,marks):
    context = {
        "marks": marks,
        "type": "result"
    }
    return render(request, "if-if-else.html", context)


# 9. Login Status (if-else)
def userlogin(request):
    context = {
        "logged_in": False,
        "type": "userlogin"
    }
    return render(request, "if-if-else.html", context)


# 10. Stock Availability (if-else)
def stock(request,quantity):
    context = {
        "stock": quantity,
        "type": "stock"
    }
    return render(request, "if-if-else.html", context)




# ELIF CONDITION
def char_check(request,ch):
    context = {
        'ch' : ch
    }
    return render(request, "elif.html", context)



# ELIF 5 EXAMPLES
# 1. Character Check
def char_check(request, ch):
    return render(request, "elif.html", {
        "type": "char",
        "ch": ch
    })


# 2. Grade Check
def grade(request, marks):
    return render(request, "elif.html", {
        "type": "grade",
        "marks": marks
    })


# 3. Month Number
def month(request, num):
    return render(request, "elif.html", {
        "type": "month",
        "num": num
    })


# 4. Week Day
def weekday(request, day):
    return render(request, "elif.html", {
        "type": "weekday",
        "day": day
    })



# 6. Traffic Signal
def signal(request, color):
    return render(request, "elif.html", {
        "type": "signal",
        "color": color
    })


#   NESTED IF 5 EXAMPLES

def nested1(request, age):
    return render(request, "elif.html", {"type":"citizen","age":age})

def nested2(request, marks):
    return render(request, "elif.html", {"type":"result","marks":marks})

def nested3(request, salary):
    return render(request, "elif.html", {"type":"salary","salary":salary})


def nested5(request, year):
    return render(request, "elif.html", {"type":"nested5","year":year})

def nested6(request, temp):
    return render(request, "elif.html", {"type":"temperature","temp":temp})



# FOR LOOP
def char(request):
    return render(request, "for.html")


from django.conf import settings
import os

file_path = os.path.join(settings.BASE_DIR,'products.json')

file = open(file_path,'r')
json_data = file.read()
# file.read()

import json

py_data = json.loads(json_data)

products_api = py_data['products']

def products(request):
    context = {
        'products' : products_api
    }
    return render(request, 'products_list.html', context)



def products_ui(request):
    context = {
        'products' : products_api
    }
    return render(request, 'products_list.html', context)


def product_detail(request, id):
    product = products_api[id - 1]  # Assuming the ID corresponds to the index in the list

    context = {
        "product": product
    }

    return render(request, "product_detail.html", context)