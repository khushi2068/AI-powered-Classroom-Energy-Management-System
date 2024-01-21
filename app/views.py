from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User, Room
from django.contrib.auth.models import auth
from django.core.mail import send_mail
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

import cv2
import numpy as np
import time
import os.path
import wget

import random, string


def login(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        print("here")
        email = request.POST["email"]
        password = request.POST["password"]
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            print("no")
            messages.add_message(request, messages.ERROR, "Wrong username or password!")
            return render(request, "login.html")
    else:
        return render(request, "login.html")
    # return render(request, 'login.html')


@login_required(login_url="/login")
def logout(request):
    if request.user.is_anonymous:
        return redirect("/login")
    auth.logout(request)
    return redirect("/login")


@login_required(login_url="/login")
def home(request):
    data = Room.objects.all()

    return render(request, "home2.html", {"data": data})


@login_required(login_url="/login")
def liveCam(request, event, type):
    return render(request, "app/liveCam.html", {"event": event, "type": type})


def otp(request):
    if request.method == "POST":
        email = request.POST["email"]
        user = User.objects.filter(email=email).first()
        if user is not None:
            otp = "".join(random.choice(string.digits) for _ in range(7))
            user.otp = otp
            user.save()
            sub = "OTP for Password reset"
            message = "Your OTP to reset password is " + otp
            from_email = settings.EMAIL_HOST_USER
            send_mail(sub, message, from_email, [email], fail_silently=False)
            return redirect("/reset_password")
        else:
            messages.add_message(request, messages.ERROR, "User does not exist!")
            return render(request, "otp.html")
    return render(request, "otp.html")


def reset_password(request):
    if request.method == "POST":
        otp = request.POST["otp"]
        password = request.POST["password"]
        user = User.objects.filter(otp=otp).first()
        if user is not None:
            user.set_password(password)
            user.save()
            return redirect("/login")
        else:
            messages.add_message(request, messages.ERROR, "OTP is incorrect!")
            return render(request, "reset.html")
    return render(request, "reset.html")


class check_status(APIView):
    def get(self, request):
        data = {"room": [], "status": [],"people":[],'light':[]}
        for room in Room.objects.all():
            try:
                cap = cv2.VideoCapture(room.cam_url)

                success, img = cap.read()
                cap.release()
                people = gen(img)
                lightvar = light(img)
                if (not people) and lightvar:
                    room.status = True
                else:
                    room.status = False
                room.save()
                data["room"] += [room.name]
                data["status"] += [room.status]
                data['people'] += [people]
                data['light'] += [lightvar]
            except:
                print(room, " Offline")

        print(data)
        print("here")

        return Response(data, status=status.HTTP_200_OK)


def gen(img):
    whT = 320
    confThreshold = 0.4

    modelConfiguration = r"app\YOLO\YOLO\yolo\yolov3.cfg"
    modelWeights = r"app\YOLO\YOLO\yolo\yolov3.weights"

    net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

    def findObjects(outputs, img):
        for output in outputs:
            for det in output:
                scores = det[5:]
                classId = np.argmax(scores)
                confidence = scores[classId]
                if confidence > confThreshold and classId == 0:
                    return True
        return False

    blob = cv2.dnn.blobFromImage(img, 1 / 255, (whT, whT), [0, 0, 0], 1, crop=False)
    net.setInput(blob)
    layerNames = net.getLayerNames()

    outputNames = [layerNames[i - 1] for i in net.getUnconnectedOutLayers()]
    outputs = net.forward(outputNames)

    if findObjects(outputs, img):
        return True
    else:
        return False


def light(img):
    def img_estim(img, thrshld):
        is_light = np.mean(img) > thrshld
        return True if is_light else False

    if img_estim(img, 80):
        return True
    else:
        return False
