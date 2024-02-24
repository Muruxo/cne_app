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
    
    