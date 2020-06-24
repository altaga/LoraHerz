# LoraHerz
LoraWAN, HeartRate and Enviroment Monitor

<img src="https://i.ibb.co/Sy6K5F4/Logo.png" width="1000">

# Introduction and problem

Lora tracking:

I will create a Post-hospital monitoring system based on communication Lora, for patients who suffered Covid-19 (but can be adapted to any disease afterwards), the solution will track the patient's heart rate using an ECG sensor. It has been shown that worldwide those with pre-existing conditions such as cardiac disease are the ones with more risk.

<img src="https://i.ibb.co/d5WZpp7/image.png" width="1000">

# Table of contents
* [Introduction](#introduction)
* [Solution](#solution)
* [Materials](#materials)
* [Connection Diagram](#connection-diagram)
* [Kit Assemble](#kit-assemble)
* [Create Helium Account](#create-helium-account)
* [Kit Setup](#kit-setup)
* [Miner Creation](#miner-creation)
* [Pycom Setup](#pycom-setup)
* [Gateway Setup](#gateway-setup)
* [AWS IoT Setup](#aws-iot-setup)
* [AWS Services](#aws-services)
* [IoT Things](#iot-things)
* [Node-Red Setup](#node-red-setup)
* [Product](#product)
* [Demo](#demo)

# Solution

<img src="https://i.ibb.co/PFt6CLT/20200620-152247.jpg" width="1000">

With this solution the patient will be able to track their recovery and a web app to see their progress, the doctor could have a database of their patients which can be made public to developers and doctors around the world by generating a public API. With AWS and also in the future with a lot of data, perform an AI that is capable of determining the recovery status of a patient using that data.

<img src="https://i.ibb.co/XpnyW2y/20200623-215406.jpg" width="1000">
 
I use the Thunderboard Sense 2 to obtain all the environmental data from the multiple sensors it has and serve as a tracking of the patient's environment in their recovery, in order to rule out variables such as the weather to measure the patient's recovery

# Materials:

List the hardware and software you will use to build this.

Hardware: 
- Arduino WAN 1300.
  - https://store.arduino.cc/usa/mkr-wan-1300
- AD8232 ECG Module.
    - https://www.amazon.com/dp/B07YY742WY/ref=cm_sw_em_r_mt_dp_U_GOs8EbPHKZ37T
- RPI Zero as a Gateway.
    - https://www.amazon.com/dp/B06XFZC3BX/ref=cm_sw_em_r_mt_dp_U_QPs8EbGZSKVM0
- Thunderboard Sense 2.
    - https://www.silabs.com/products/development-tools/thunderboard/thunderboard-sense-two-kit
- Cellphone as Server.

Software: 
- TTN Console.
  - https://www.thethingsnetwork.org/
- Arduino WEB IDE.
  - https://create.arduino.cc/editor/Altaga/b5350441-dbfa-4a10-a0c1-84109949f0ef/preview
- Node-RED.
  - https://nodered.org/
- AWS. https://aws.amazon.com/
  - AWS IoT.
  - AWS Lambda.
  - AWS Dynamo.

# Connection Diagram:

 <img src="https://i.ibb.co/Sdby94j/diagram.png" width="1000">

Arduino Circuit Diagram:

 <img src="https://i.ibb.co/mJ0P2ry/Sketch-bb.png" width="1000">

# Assemble:

- Assemble the circuit elements:

<img src="https://i.ibb.co/mzWwgCH/20200620-152306.jpg" width="1000">

- Put all in a case.

<img src="https://i.ibb.co/m0Zgz05/20200620-152247.jpg" width="1000">

Correct electrodes position:

<img src="https://i.ibb.co/JtRCF0T/Diagrama1.png" width="1000">

# Arduino Create Account:

El primer paso es crear una cuenta en la Arduino Create, este proceso nos servira para poder flashear nuestro Arduino MKR 1300 con el software correcto.

https://create.arduino.cc/

# Obtain the DevEUI:

Despues de ya tener nuestra cuenta, abriremos el siguiente enlace al codigo 1 que les preporcionare, este nos permitira obtener el DevEUI de nuestra board, este numero es necesario para poder consumir los servicios de LoraWAN de The Things Network (TTN).

https://create.arduino.cc/example/library/mkrwan_1_0_12/mkrwan_1_0_12%5Cexamples%5CFirstConfiguration/FirstConfiguration/preview

Podemos ver como el codigo nos muestra el DevEUI que necesitamos:

<img src="https://i.ibb.co/m6bGKsg/image.png" width="1000">

Antes de poder empezar a mandar informacion por Lora, tenemos que crear una cuenta en la red de TTN.

# TTN:

Creamos una cuenta en TTN.

https://www.thethingsnetwork.org/

Una vez creada la cuenta entramos a la consola para crear nuestra primera aplicacion.

NOTA: las aplicaciones sirven para asociar los devices en grupos y sobre ellas implementar integraciones como lo son AWSIoT o API.

https://console.thethingsnetwork.org/

Primero le damos a crear una a App.

<img src="https://i.ibb.co/1RcQwGx/image.png" width="1000">
<img src="https://i.ibb.co/vzVbJvh/image.png" width="1000">

La configuracion variara segun la region del mundo en la que te encuentres, en este caso yo vine a Aveiro, Portugal a desarrollar mi proyecto ya que en Mexico no hay una buena infraestructura de LoraWAN.

<img src="https://i.ibb.co/5G4MttW/image.png" width="1000">

Ahora obtenemos la AppEUI, esta nos servira mas adelante.

<img src="https://i.ibb.co/ZdVPWtd/image.png" width="1000">

Registraremos un nuevo device:

<img src="https://i.ibb.co/6nbdsXR/image.png" width="1000">

Al registrar el device deberemos poner el Device EUI que obtuvimos en la consola de Arduino.

<img src="https://i.ibb.co/s34WS5z/image.png" width="1000">

EL ultimo numero que nececitamos es la AppKey que nos entregara la plataforma.

<img src="https://i.ibb.co/n04zhcX/image.png" width="1000">

Ya que tenemos esos 3 numeros, podemos pasar a configurar nuestro Arduino MKR 1300 para mandar datos a la red de TTN.

# Arduino MKR Credentials Setup:

Ya con la AppEUI y la AppKEY abriremos el siguiente codigo en Arduino Create y pegaremos nuestro nuestras credenciales.

https://create.arduino.cc/editor/Altaga/c0f3d3a8-daef-440e-8d9c-3abeb6229670/preview

Pega tus credenciales aqui.

<img src="https://i.ibb.co/mJTQ1gd/image.png" width="1000">

Haz funcionar todo el sistema y obtendras lo siguiente en la plataforma de TTN.

<img src="https://i.ibb.co/p18RSbt/image.png" width="1000">

# TTN to AWS

Ya que los valores llegan a la plataforma de TTN, deberemos enviar los datos a AWSIoT, esto se puede realizar de 2 formas, oficialmente TTN tiene una guia de como hacer este proceso, pero les mostrare una segunda forma de hacerlo.

TTN official Guide: https://www.thethingsnetwork.org/docs/applications/aws/

En nuestro caso preferimos utilizar el siguiente esquema de conexion.

<img src="https://i.ibb.co/L1QgtWr/TTN-AWS-Node-Red.png" width="1000">

# AWS setup:

AWS works through roles, these roles are credentials that we create so that the services can communicate with each other, in order to carry out all our integration we need to create a role that allows the effective transmission of all services, therefore that will be the first thing To make.

Note: always start here when doing a project with AWS.

## IAM:

- Enter the IAM console.

<img src="https://i.ibb.co/CHBndXs/image.png" width="1000">

- Enter through the role tab and click "Create role".

<img src="https://i.ibb.co/1fm8rhr/image.png" width="1000">

- Create a role focused on the IoT platform.

<img src="https://i.ibb.co/42Vv4dY/image.png" width="1000">

- Press next till review.

<img src="https://i.ibb.co/dL8mF47/image.png" width="1000">

- Now we have to add the additional permissions to the Role, in the roles tab enter the role we just created and press the Attach policies button.

<img src="https://i.ibb.co/z5kVpXR/image.png" width="1000">

- Inside policies add the following:

  - AmazonIoTFullAccess

- Once that is finished, now we can start configuring the AWS Lambda but before this we need the AWS IoT Core Endopoint.

## AWS IoT Endpoint:

- First we have to access our AWS console y look for the IoT core service:

<img src="https://i.ibb.co/KVbtQLR/image.png" width="600">

- Obtain your AWS endpoint, save it because we will use it to setup the Lambda and the Node-RED.

<img src="https://i.ibb.co/ZYwrdfR/image.png" width="600">

## Lambda:

- We configure the lambda in the following way and create it:

<img src="https://i.ibb.co/LNXXY7c/image.png" width="1000">

- Once the lambda has been created we go down to the Execution role section and press the View the YOUR_ROLE button on the IAM console to be able to send the data from AWS Gateway to AWS IoT Core:

<img src="https://i.ibb.co/xJV8jxX/image.png" width="1000">

- Once that is finished, we select the lambda in our rule to finish configuring the lambda.

<img src="https://i.ibb.co/zh8Fq0C/image.png" width="1000">

- El codigo que vamos a ejecutar esta en la carpeta de "Lambda Code" lo tenemos que pegar en la lambda y modificar los siguiente parametros.

<img src="https://i.ibb.co/F7rZt8y/image.png" width="1000">

Pega tu endpoint en el codigo y coloca el Topic que consideres conveniente para mandar la informacion al IoT Core.

## API Gateway:

Ya que tenemos nuestra lambda creada, es hora de crear nuestro endpoint de AWS Gateway para mandar la informacion desde TTN.

<img src="https://i.ibb.co/JjLGZv5/image.png" width="1000">

Dentro del servicio le presionamos el boton de crear.

<img src="https://i.ibb.co/tLz4CGR/image.png" width="1000">

- En nuestro caso usaremos una HTTP API, hay muchas formas de configurarla pero esta es la mas sencilla a nuestro punto de vista.

<img src="https://i.ibb.co/4Td0nBZ/image.png" width="1000">

La configuracion de la API Gateway sera la siguiente en mi caso la funcion Lambda es LoraHR.

<img src="https://i.ibb.co/P1MdcrW/image.png" width="1000">

La forma de llamarla sera la siguiente.

<img src="https://i.ibb.co/tstmGXK/image.png" width="1000">

Lo demas lo dejaremos con su configuracion de Default y pasaremos a la pestaña de CORS para configurar el acceso de TTN a la funcion.

<img src="https://i.ibb.co/7p1HmKP/image.png" width="1000">

Para facilidad de este tutorial configuraremos los CORS de la siguiente forma.

<img src="https://i.ibb.co/3C2TFSr/image.png" width="1000">

Una vez hecho esto vamos a la seccion de API para obtener el endpoint.

<img src="https://i.ibb.co/fFtXDvp/image.png" width="1000">

El endpoint de la API junto con la funcion sera el siguiente en mi caso.

    https://XXXXXXXXXX.execute-api.us-east-1.amazonaws.com/PostHR

Ya que tenemos este numero ahora si podemos crear la integracion en TTN.

## TTN Integration:

En nuestra aplicacion iremos a la seccion de integracion.

<img src="https://i.ibb.co/wysJMwy/image.png" width="1000">

Agregamos una nueva integracion de la siguiente forma.

<img src="https://i.ibb.co/tsd1FLS/image.png" width="1000">

Y listo si hiciste todo correctamente deberas de ver los datos llegar a AWS IoT de la siguiente forma.

<img src="https://i.ibb.co/0QtLfrV/AWS-hr.png" width="1000">

NOTA: los datos que dicen -48NaN son valores que manda la plataforma por Default, sin embargo estos seran filtrados en NodeRED, aunque si lo prefieres puedes realizar este filtrado desde la Lambda.

# IoT Things:

Since we have all our platform ready, we have to create the accesses to communicate with it. So we will have to create two Things in this case, the first is for our RaspberryPi Gateway and the other will be for the NodeRed UI.

- First we have to access our AWS console y look for the IoT core service:

<img src="https://i.ibb.co/KVbtQLR/image.png" width="600">

- Obtain your AWS endpoint, save it because we will use it to setup the RSL10 App and the webpage.

<img src="https://i.ibb.co/ZYwrdfR/image.png" width="600">

- In the lateral panel select the "Onboard" option and then "Get started".

<img src="https://i.ibb.co/gmKxc7P/image.png" width="600">

- Select "Get started".

<img src="https://i.ibb.co/XSxSxbF/image.png" width="600">

- At "Choose a platform" select "Linux/OSX", in AWS IoT DEvice SDK select "Python" and then click "Next".

<img src="https://i.ibb.co/JR69Fdd/image.png" width="600">

- At Name, write any name, remember that you will have to do this process twice, so name things ion order that you can differentiate the credentials that you will put in NodeRed. Then click on "Next step".

<img src="https://i.ibb.co/NNLqqM0/image.png" width="600">

- At "Download connection kit for" press the button "Linux/OSX" to download the credential package (which we will use later) and click on "Next Step".

<img src="https://i.ibb.co/RHVTRpg/image.png" width="600">

- Click "Done".

<img src="https://i.ibb.co/N9c8jbG/image.png" width="600">

- Click "Done".

<img src="https://i.ibb.co/DtBxq0k/image.png" width="600">

- On the lateral bar, inside the Manage/Things section we can see our thing already created. Now we have to set up the policy of that thing for it to work without restrictions in AWS.

<img src="https://i.ibb.co/dQTFLZY/image.png" width="600">

- At the lateral bar, in the Secure/Policies section we can see our thing-policy, click on it to modify it:

<img src="https://i.ibb.co/jThNgtc/image.png" width="600">

- Click on "Edit policy document".

<img src="https://i.ibb.co/gV0tMtf/image.png" width="600">

Copy-paste the following text in the document and save it.

    {
    "Version": "2012-10-17",
    "Statement": [
        {
        "Effect": "Allow",
        "Action": "iot:*",
        "Resource": "*"
        }
    ]
    }

<img src="https://i.ibb.co/ydtTqB2/image.png" width="600">

- Once this is done, we will go to our pc and to the folder with the credentials previously downloaded, extract them.

<img src="https://i.ibb.co/mFKPxcY/image.png" width="600">

- Save this files for later.

# Thunderboard Setup:

Por cuestion de software, la thunderboard ya viene con su bluetooth SDK, ademas de eso Silicon Labs ya provee una aplicacion para opder visualizar estos datos en un celular como se ve a continuacion.

Board:

<img src="https://i.ibb.co/yVMwPmq/20200624-142116.jpg" width="1000">

Platform:

<img src="https://i.ibb.co/12q7dws/image.png" width="250">

El primer plan era utilizar la aplicacion como Gateway a Cloud para mandar los datos a AWS sin embargo esa caracteristica la eliminaron recientemente.

<img src="https://i.ibb.co/N625QBh/image.png" width="1000">

El segundo plan era realizar nuestra propia aplicacion de Android para realizar el Gateway, sin embargo no esta el SDK disponible aun.

Asi que el plan final fue realizar a travez de una RaspberryPi Zero W una Gateway la cual leyera los datos por BLE y los mandara por WiFi a AWS IoT.

Diagrama:

<img src="https://i.ibb.co/84ygFvq/image.png" width="1000">

Como primera parte del proceso de obtencion de datos, conectaremos la Thunderboard Sense 2 a la pc y con un monitor serial obtendremos su Bluetooth Mac ID.

<img src="https://i.ibb.co/6mMKtgw/image.png" width="1000">

Ya con ese numero pasaremos a configurar la raspberry.

# RaspberryPi Setup:

Download the operating system of the Raspberry Pi.

- To download the operating system of the Raspberry enter the following link:
- Link: https://www.raspberrypi.org/downloads/raspbian/
- Download the lastest version.

Flash the operating system in the SD.

Software: https://www.balena.io/etcher/

- Through Etcher flash the raspberry operating system but DO NOT put it inside the raspberry yet.

Create a wpa_supplicant for the connection of the raspberry to the internet.

- Since you have flashed the operating system, copy and paste the files from the "RaspberryPiFiles" folder directly into the SD card.
- Then open the "wpa_supplicant.conf" file with a text editor
- In between the quotes in the ssid line write your wifi network and in psk the network key.

        country = us
        update_config = 1
        ctrl_interface =/var/run/wpa_supplicant

        network =
        {
        scan_ssid = 1
        ssid = "yourwifi"
        psk = "yourpassword"
        }


- We save the changes and remove the SD from the PC.

We then place the SD in the raspberry and connect it to its power source.

- The power source of a Raspberry Pi is recommended to be from 5 volts to 2.5A minimum. We recommend the official ower supply for the Raspberry pi.

Once the Raspberry has already started, we need to access it through SSH or with a keyboard and a monitor.

- If you want to access it through SSH we need your IP.
- In order to analyze your network and obtain the number we will have to use one of the following programs.
- Advanced IP Scanner (Windows) or Angry IP Scanner program (Windows, Mac and Linux).
- In the following image you can see how we got the Raspberry IP.

<img src="https://i.ibb.co/q9BM6dP/image.png"> 

Connect the raspberry with ssh.

- To connect using ssh to the raspberry we need the Putty program.
- Link: https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html
- This program will let us access the command console of the raspberry.
- In Linux, just open the terminal and put the following command.

        ssh pi@RASPBERRYIP

<img src="https://i.ibb.co/PxP86Xz/terminal.png">

- Password: “raspberry”

<img src="https://i.ibb.co/QpWj18S/image.png">

First, we will install the necessary libraries for our program to work.

- For it to work we just have to input the following command.

      sudo apt-get update
      sudo apt-get install python3-pip libglib2.0-dev libatlas-base-dev git -y
      sudo pip3 install bluepy Crypto crc16 paho-mqtt

- Copia la carpeta de "Rpi Software" en la raspberry y pega los certificados que creamos antes dentro de la subcarpeta "Certs".

NOTA: puedes renombrar los certificados como estan en la imagen si no quieres editarlos en el codigo.

<img src="https://i.ibb.co/WyvkR12/image.png">

Dentro de el archivo main.py configura tu AWS IoT Core Endpoint correctamente.

<img src="https://i.ibb.co/dfPpmb7/image.png">

Si todo el proceso anterior lo realizaste correctamente corre el siguiente codigo para empezar a mandar datos a AWS IoT.

    sudo python3 main.py YOURMAC

Los datos deberan verse de la siguiente forma.

<img src="https://i.ibb.co/0svMP3W/Capture.png" width="600">

Ya que tenemos todo el backend de hardware y cloud configurados, configuraremos el frontend en Node-RED

# Node-Red Setup:

- Node Red is a tool for NodeJS where we can integrate services easily, without code and, of course, create excellent dashboards.

- NodeJS installation guide: https://www.guru99.com/download-install-node-js.html

- NodeRED installation guide: https://nodered.org/docs/getting-started/windows

- NodeRED installation guide: https://flows.nodered.org/node/node-red-dashboard

- The file "flows.json" in the folder "Node-RED Flow", has all the information to import the flow into your NodeRED.

<img src = "https://i.ibb.co/c11ZJT8/image.png" width = "400">
<img src = "https://i.ibb.co/nBL3M23/image.png" width = "400">

- Once that is done we will edit the MQTT node to enter our credentials.

<img src = "https://i.ibb.co/G9Rby7J/image.png" width = "600">

- Set Server and Port.

<img src = "https://i.ibb.co/WHrcHCd/image.png" width = "600">

- Press in the pencil in TSL configuration to add the certificates.

- Note: RootCA certificate inside "Certs" folder.

<img src = "https://i.ibb.co/nMgtkRN/image.png" width = "600">

- Select the correct topic in each MQTT nodes.

<img src = "https://i.ibb.co/rxMNZRN/image.png" width = "600">

- In my case:
    - /Device1/EnvironmentData
    - /Device1/HR

- If everything works fine press the "Deploy" button and enter the following URL to check the Dashboard.

http://localhost:1880/ui

Desktop:

<img src = "https://i.ibb.co/sFq9rM5/image.png" width = "800">

Mobile:

<img src = "https://i.ibb.co/zxx98Kt/Screenshot-20200624-154958-Red-Mobile.jpg" width = "200">
<img src = "https://i.ibb.co/NnQmmXg/Screenshot-20200624-155001-Red-Mobile.jpg" width = "200">
<img src = "https://i.ibb.co/vkmF5wk/Screenshot-20200624-155006-Red-Mobile.jpg" width = "200">





### Explanation for nodes:

- This node receives the broker's payloads, filters according to the sensor which graph it has to go to and sends it to graph and deploy.

<img src = "https://i.ibb.co/cbbM76V/image.png" width = "800">

# Product:

<img src="https://i.ibb.co/2yfQx8K/20200623-215317.jpg" width="1000">

# Demo:

This my DEMO:

Video: Click on the image:

[![Demo](https://i.ibb.co/Sy6K5F4/Logo.png)](Pendiente)

Sorry github does not allow embed videos.

* [Table of Contents](#table-of-contents)

