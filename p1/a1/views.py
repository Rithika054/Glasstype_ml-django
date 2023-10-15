from django.http import HttpResponse
from django.shortcuts import render
import joblib
from .models import *
#from django.contrib.auth import authenticate,login,logout
def home(request):
        return render(request,"home.html")

def index(request):
        return render(request,"index.html")

def result(request):
        r=joblib.load('glassmodel.sav')
        lis=[]
        lis = [float(request.GET.get(key, 0.0)) for key in ['RI', 'Na', 'Mg', 'AI', 'Si', 'K', 'Ca', 'Ba', 'Fe']]
        # lis.append(request.GET['RI'])
        # lis.append(request.GET['Na'])
        # lis.append(request.GET['Mg'])
        # lis.append(request.GET['AI'])
        # lis.append(request.GET['Si'])
        # lis.append(request.GET['K'])
        # lis.append(request.GET['Ca'])
        # lis.append(request.GET['Ba'])
        # lis.append(request.GET['Fe'])
        print(lis)
        
        ans=r.predict([lis])
        return render(request,"result.html",{'ans':ans,'lis':lis})

# #BASE_DIR / 'db.sqlite3'
# def result(request):
#     #try:
#         r = joblib.load('finalmodel.sav')  # Load the model
#         lis = [float(request.GET.get(key, 0.0)) for key in ['RI', 'Na', 'Mg', 'AI', 'Si', 'K', 'Ca', 'Ba', 'Fe']]
#         print(lis)

#         ans = r.predict([lis])
#         return render(request, "result.html", {'ans': ans, 'lis': lis})
# #     except Exception as e:
# #         # Handle exceptions here, e.g., display an error message or log the error.
# #         error_message = "An error occurred while processing your request."
# #         return render(request, "error.html", {'error_message': error_message})