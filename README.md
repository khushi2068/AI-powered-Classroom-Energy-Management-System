# AI-powered Classroom Energy Management System: CNN-based-human-detection-to-save-electricity
The goal of this project is to design a software intending to conserve electricity based on human detection. This system will use a simple CCTV camera to detect human presence and light presence in classrooms. In case the classroom is detected empty and the lights are on, the system will notify the administrator regarding the same via a live notification Furthermore this system will allow the administrator to have access to the real time status of all classrooms in the campus through a website. This system will make administration easier and prevent unnecessary electricity wastage.

## Project Images
![alt text](https://github.com/Samarjeet09/wattsaver/blob/main/Images/img1.png)
![alt text](https://github.com/Samarjeet09/wattsaver/blob/main/Images/img2.png)
![alt text](https://github.com/Samarjeet09/wattsaver/blob/main/Images/img4.png)
![alt text](https://github.com/Samarjeet09/wattsaver/blob/main/Images/img3.png)


## Pre-Requisites:
1) A working CCTV camera. If a cctv camera is unavailable, apps like [Droid Cam](https://play.google.com/store/apps/details?id=com.dev47apps.droidcam&hl=en_IN&gl=US&pli=1) can be used to make the phone work as a cctv camera. The phone or the CCTV camera and the server should be connected to the same Local Network.
2) The host server or computer should meet the requirements of YOLOv3.


## Tech Stack

**Client:** HTML, CSS, JavaScript

**Server:** Python, Django

**Database:** SQLite

## Run Locally

1) Clone the project

```bash
git clone https://github.com/Chandravo/CNN-based-human-detection-to-save-electricity
```

2) Download YOLOv3 config and weights folder from [here](https://moderncomputervision.s3.eu-west-2.amazonaws.com/YOLO.zip).
Unzip the file.
Copy the YOLO folder and paste it inside the app folder of the cloned project.

<img src="https://res.cloudinary.com/dgbobpgf4/image/upload/v1669118757/screenshots/image_2022-11-22_173551253_qrpegw.png">

3) Navigate to yolo folder inside the YOLO folder. Inside the folder there are 3 files : coco.names, yolov3.cfg, yolov3.weights. Copy the path of each one of them and replace their path inside "gen" function inside views.py inside the app folder.  

<img src="https://res.cloudinary.com/dgbobpgf4/image/upload/v1669119283/screenshots/copypath.png">

<img src="https://res.cloudinary.com/dgbobpgf4/image/upload/v1669119415/screenshots/pastepath.png">

4) Navigate to project directory in terminal

```bash
cd config
```

5) We recommend you to use virtual environment

```bash
  python -m venv env
```

Activate virtual environment   
   
&emsp;&emsp;For Windows PowerShell
```bash
    env/Scripts/activate.ps1
```
&emsp;&emsp;For Linux and MacOS
```bash
    source env/bin/activate
```

6) Install dependencies

```bash
  pip install -r requirements.txt
```

7) Add *Secret Key* : Go to project's *settings.py* file and change the value of *SECRET_KEY* variable to desired secret key.
You can generate a new secret key [here](https://djecrety.ir)

8) Run Migrations

```bash
 python manage.py makemigrations
```

```bash
 python manage.py migrate
```

9) Create new superuser

```bash
python manage.py createsuperuser
```

10) Start the server

```bash
  python manage.py runserver
```

11) Go to ```localhost:8000/admin``` and login with the details of the superuser. Click on room option under app category.

<img src="https://res.cloudinary.com/dgbobpgf4/image/upload/v1669120294/screenshots/approom.png">

Click on "ADD ROOM +"

<img src="https://res.cloudinary.com/dgbobpgf4/image/upload/v1669120359/screenshots/addroom.png">

Enter the room name and the video endpoint of the CCTV camera

<img src="https://res.cloudinary.com/dgbobpgf4/image/upload/v1669120651/screenshots/addedroom.png">

12) The site is ready now. Go to ```localhost:8000``` to start. 
