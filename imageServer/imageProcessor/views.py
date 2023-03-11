from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os
from .videoModels.Gestures import main as VideoProcessor
import json
import datetime
# Create your views here.
@csrf_exempt
def index (request):
    return HttpResponse("hello")

@csrf_exempt
def processData(request):
    datetime_object = datetime.datetime.now()
    video_byte_stream = request.FILES['videoFile'].read()
    userID = request.FILES['id'].read().decode()
    sessionID = request.FILES['session_id'].read().decode()
    userFolderPath="./VideoProcessingResults/"+userID
    sessionFolderPath=userFolderPath+'/'+sessionID

    print("userID is " ,userID)
    print("SesssionID is " ,sessionID)
    if not os.path.isdir('VideoProcessingResults'):
        os.mkdir('VideoProcessingResults')
    if not os.path.isdir(userFolderPath):
        os.mkdir(userFolderPath)
    if not os.path.isdir(sessionFolderPath):
        os.mkdir(sessionFolderPath)
    userSessionPath=sessionFolderPath+'/'
    FILE_OUTPUT = 'video.mp4'
    if os.path.isfile(FILE_OUTPUT):
        os.remove(FILE_OUTPUT)
    out_file = open(userSessionPath+FILE_OUTPUT, "wb")
    out_file.write(video_byte_stream)
    out_file.close()
    handsResult,emotionResults,headDirections =VideoProcessor.startProcessing(userSessionPath+FILE_OUTPUT,userSessionPath)

    results={
        'hands':handsResult,
        'emotion':emotionResults,
        'head':headDirections

    }
    open(userSessionPath+'results.json', 'w').write(json.dumps(results))
    datetime_object2 = datetime.datetime.now()
    print(datetime_object2 - datetime_object)
    return HttpResponse("Results are saved in "+userSessionPath)