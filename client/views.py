# myapp/views.py

from django.shortcuts import render, redirect
from pymongo import MongoClient
# from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        
        password = request.POST['password']

        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        db = client['mydatabase']  # Replace 'mydatabase' with your MongoDB database name
        collection = db['user']

        # hashed_password = make_password(password)
        user_data = {'email': email,  'password': password}
       
        
        
        if collection.find_one({'email': email}):
            if collection.find_one({'password': password}):
                collection.insert_one(user_data)
                return redirect('home')
            return render(request, 'login.html', {'error': 'incorrect password, please check'})
       
        return render(request, 'login.html', {'error': ' This email not register, please signup'})
       
       
           
 
    
    return render(request, 'login.html')
                
               
  
      
       
        
        

def home(request):
     return render(request, 'home.html')
# def signup(request):
#      return render(request, 'signup.html')

def main (request):
    return render(request, 'main.html')


def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        password = request.POST['password']
        password2 = request.POST['password2']

       
        client = MongoClient('mongodb://localhost:27017/')
        db = client['mydatabase'] 
        collection = db['user'] 
        
        if collection.find_one({'email': email}):
             
              return render(request, 'signup.html', {'error': 'email already exists'})
        if password != password2:
                return render(request, 'signup.html', {'error':"password didn't match"})
               
        user_data = {'email': email, 'name':name, 'password': password}
        collection.insert_one(user_data)
       

        return redirect('/')

         
    return render(request, 'signup.html')



def signout(request):
     logout(request)
     return redirect('login')

     
     
      