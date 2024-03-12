from .models import *
import pandas as pd 


def es_admin(user):
    return hasattr(user, 'perfil_admin')

def es_postulante(user):
    return hasattr(user, 'perfil_postulante')

# def es_admin(user: User.is_staff):
#     if user == True:
#         return True 
    

# def es_postulante(user: User.is_staff):
#     if user == False:
#         return False 
    

# def tiene_cuenta(user: User.is_authenticated):
#     if user == False:
#         return
   
    