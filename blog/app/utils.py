from .models import *
import pandas as pd 


def es_admin(user): 
    if hasattr(user, 'perfil_admin'):
        return True 
    else: 
        return False
    
def es_postulante(user): 
    if hasattr(user, 'perfil_postulante'):
        return True 
    else: 
        return False


# def es_admin(user: User.is_staff):
#     if user == True:
#         return True 
    

# def es_postulante(user: User.is_staff):
#     if user == False:
#         return False 
    

# def tiene_cuenta(user: User.is_authenticated):
#     if user == False:
#         return
   
    