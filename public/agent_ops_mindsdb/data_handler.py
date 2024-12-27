# data_handler.py
import pandas as pd
import numpy as np

def load_data():
    # Load Bay Area data
    bay_area_data = pd.read_csv('input/Bay_Area.csv')
    bay_area_data['Neighborhoods'] = bay_area_data['Neighborhoods'].str.split('\n')

    # Load services data
    services_data = pd.read_csv('input/gallery.csv')

    company_name = "Goldson Landscaping"
    company_services = services_data['Item'].tolist()

    output_data = {
        "company_name": company_name,
        "services": company_services,
        "service_coverage": {}
    }

    for service in company_services:
        service_coverage = {}
        for city in bay_area_data['City/Town'].unique():
            neighborhoods = bay_area_data.loc[bay_area_data['City/Town'] == city, 'Neighborhoods'].tolist()[0]
            service_coverage[city] = neighborhoods
        output_data['service_coverage'][service] = service_coverage

    return output_data