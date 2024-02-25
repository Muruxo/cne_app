from .models import *
import pandas as pd 


def es_admin(user: User.is_staff):
    if user == True:
        return True 
    

def es_postulante(user: User.is_staff):
    if user == False:
        return False 
   
    