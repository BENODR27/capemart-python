from django.http import JsonResponse
from django.shortcuts import render
from requests import Response
from django.views.decorators.csrf import csrf_exempt
import json
import numpy
import os
import matplotlib.pyplot as plt
import io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from django.http import HttpResponse

def generate_plot():
    # x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
    # y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

    # plt.scatter(x, y)
    x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
    y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

    mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

    myline = numpy.linspace(1, 22, 100)

    plt.scatter(x, y)
    plt.plot(myline, mymodel(myline))
    # x = numpy.random.normal(5.0, 1.0, 100000)
    # plt.hist(x, 100)

    # Save the plot to BytesIO buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    
    plt.close()  # Close the plot to free up resources
    return buffer

@csrf_exempt
def home(request):
    
    buffer = generate_plot()
    # Return the plot image as an HttpResponse
    return HttpResponse(buffer.getvalue(), content_type='image/png')



def home2(request):
    # Construct the response JSON
    json_data = json.loads(request.body)

    # Access the 'speed' parameter from the JSON data
    speed = json_data.get('speed', [])
    mean = numpy.mean(speed)
    percentile = numpy.percentile(speed, 75)

    f = open("public/trainedDatas.csv", "a")

    f.write("jbvh")
    f.close()
    
    training_dataset = [
        {'input': 'input_data_1', 'output': 'output_data_1'},
        {'input': 'input_data_2', 'output': 'output_data_2'},
        # Add more training data as needed
    ]
    response = {
        'status': 200,
        'message': 'success',
        'result': {
            "mean":mean,
            "percentile":percentile
        }
    }


    return  JsonResponse(response)