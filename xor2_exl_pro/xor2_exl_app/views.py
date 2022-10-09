from django.shortcuts import render
from django.http import HttpResponse
from .resources import PersonResource
from tablib import Dataset
from .models import Person
import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.styles import Border, Side, PatternFill, Font, GradientFill, Alignment
from openpyxl.styles import colors
from openpyxl.cell import Cell
from termcolor import colored, cprint
from openpyxl.styles import numbers


def export(request):
    person_resource = PersonResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response


def simple_upload(request):
    
    ### FIRST METHOD
    
    
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        # print(imported_data)
        for data in imported_data:
            print(data[1])
            value = Person(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5]
            )
            value.save()

            result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
           person_resource.import_data(dataset, dry_run=False)  # Actually import now
        
        
        
        
       ###SECOND METHOD
    
#     import pandas as pd
#     from sqlalchemy import create_engine
    
#     engin = create_engine('mysql://root:1234@localhost/ravi')
#     if request.method == 'POST':
#         loc = request.FILES['myfile']
     
#         df = pd.read_excel(str(loc))
#         df.to_sql('people12',con=engin,if_exists='append')

    return render(request, 'input.html')
