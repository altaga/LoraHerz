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

<img src="Solucion" width="1000">

With this solution the patient will be able to track their recovery and a web app to see their progress, the doctor could have a database of their patients which can be made public to developers and doctors around the world by generating a public API. With AWS and also in the future with a lot of data, perform an AI that is capable of determining the recovery status of a patient using that data.

<img src="Solucion" width="1000">
 
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

# Kit Assemble:

- Kit Elements:

<img src="https://i.ibb.co/CVkGvtW/20200609-002859.jpg" width="1000">

- Connect the Kit.

<img src="https://i.ibb.co/W6p3ZpP/20200609-002950.jpg" width="1000">

- Put all in a case.

<img src="https://i.ibb.co/gJrrtx1/20200609-003442.jpg" width="1000">

- Pycom Gateway:

<img src="https://i.ibb.co/FgGCXsH/20200609-003404.jpg" width="1000">
<img src="https://i.ibb.co/XxL85ZT/20200609-003412.jpg" width="1000">

# Create Helium Account:

El primer paso es crear una cuenta en la console de helium, este proceso nos servira para obtener las crecenciales que pondremos en nuestro kit mas adelante.

https://console.helium.com/

Nos vamos a la pestaña de Devices para crear las credenciales de nuestro primer device.

<img src="https://i.ibb.co/wCZMnB0/image.png" width="1000">

Dentro de la plataforma crearemos un device para obtener las credenciales de conexion.

<img src="https://i.ibb.co/2v5NPtN/image.png" width="1000">

Guardamos estos valores para la configuracion de nuestro device.

# Kit Setup:

Toda la guia para programar el kit con Arduino IDE esta en la guia oficial de helium.

https://developer.helium.com/devices/arduino-quickstart/st-discovery-lrwan1

Una vez hayamos terminado exitosamente la guia de helium pasarmos a descargar y abrir el documento en la carpeta "ArduinoIDE" y abrirlo.

<img src="https://i.ibb.co/v3y8zcy/image.png" width="1000">

Añade las siguientes librerias:

<img src="https://i.ibb.co/xLtZsFh/image.png" width="400">
<img src="https://i.ibb.co/RYW8gdD/image.png" width="400">

Ahora pondremos las credenciales que obtuvimos en la Helium Console.

<img src="https://i.ibb.co/jTs5QWD/image.png" width="400">

Si todo sale bien, deberias de poder flashear el codigo en el kit.

**En el caso de que estes en una zona dentro del coverage de Helium, haz click [here](#checkpoint)**

Revisa el Coverage en tu region.
https://network.helium.com/coverage

# Miner Creation:

En este caso la creacion de un minero en AWS esta detallada perfectamente en la documentacion oficial e Helium.

https://developer.helium.com/blockchain/run-your-own-miner

Los unicos datos que necesitaremos en este caso luego de hacer funcionar el minero sera la IPv4 Public IP:

<img src="https://i.ibb.co/xL7m3Kv/image.png" width="1000">

Al minero se le genera un nombre pseudo-aleatorio en el caso de nuestro Miner obtuvimos el siguiente nombre.

<img src="https://i.ibb.co/rMqT8Dg/image.png" width="1000">

# Pycom Setup:

La configuracion del Gateway la realizamos con una Fipy de la marca Pycom.

https://pycom.io/product/fipy/

Para poder configurarla correctamente, tenemos que seguir primero la guia oficial para configurarla y activarla en su plataforma Pybytes.

https://docs.pycom.io/gettingstarted/

Recomiendo leerla a detalle ya que la board tambien tiene muchisimas aplicaciones mas.

# Gateway Setup:

Nota: en nuestro caso usamos la extension de Pymakr en Visual Studio Code.

https://docs.pycom.io/pymakr/installation/vscode/

Una vez terminada la seccion anterior deberemos descargar la carpeta llamada "Pycom Helium Gateway".

<img src="https://i.ibb.co/wW9c18s/image.png" width="1000">

Abrimos con VS code la carpeta para poder empezar a editar la configuracion de la gateway.

<img src="https://i.ibb.co/gZN7h4d/image.png" width="1000">

Tenemos que configurar los siguientes parametros dentro de nuestro archivo de config.py

<img src="https://i.ibb.co/PN1d6rS/image.png" width="1000">

Estas son las constantes que pondremos en nuestro codigo para que la conexion con el minero funcione correctamente.

    Server = IPv4 Public IP from EC2 Miner
    Port   = 1680 (Helium Miner Port) 

    NTP = "pool.ntp.org"
    NTP_PERIOD_S = 3600

    WIFI_SSID = 'YOUR_SSID'
    WIFI_PASS = 'YOURPASS'

    LORA_FREQUENCY = 904300000
    LORA_GW_DR = "SF7BW125" # DR_0
    LORA_NODE_DR = 0

Si todo funciona correctamente debera de ver los push y los pull de la gateway con el minero.

En la consola de Pycom.

<img src="https://i.ibb.co/r7fNrLg/Message.png" width="1000">

En la consola de el Kit.

<img src="https://i.ibb.co/TtHf4Qw/image.png" width="1000">

    {"UTC":[2,44,2],"Lat":19.24,"Lon":99.9,"Alt":2234.74,"Hum":37.20,"Press":777.72,"Temp":29.02,"Acc":[9,0,1026],"Gyro":[-1190,210,140],"Mag":[-111,87,-750]}

###### Checkpoint:

En la consola de Helium deberemos de ver como llegan los datos:

<img src="https://i.ibb.co/Js3KC2r/Data.png" width="1000">
<img src="https://i.ibb.co/TB3dYR9/image.png" width="1000">

Ya que los datos estan llegando a la consola de Helium, es hora de configurar que lleguen a AWS IoT core.

# AWS IoT Setup:

La configuracion de AWS IoT esta muy bien explicada en la documentacion oficial de Helium.

https://developer.helium.com/console/integrations/awsiotcore

Ya que tenemos configurado el servicio, guardaremos el topic que utilizamos para mandar los datos a AWS para poder utilizarlo despues.

<img src="https://i.ibb.co/r4zRY9p/image.png" width="1000">

Cada vez que se recibe un dato en AWS veremos lo siguiente.

<img src="https://i.ibb.co/LQgKWSj/image.png" width="1000"> Insertar imagen

# AWS Services:

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

<img src="https://i.ibb.co/f22SfJ0/image.png" width="1000">

- Now we have to add the additional permissions to the Role, in the roles tab enter the role we just created and press the Attach policies button.

<img src="https://i.ibb.co/z5kVpXR/image.png" width="1000">

- Inside policies add the following:

  - AmazonDynamoDBFullAccess

<img src="https://i.ibb.co/7r0KcNJ/image.png" width="1000">

- Once that is finished, now we can start configuring the Rule within AWS IoT Core.

## DynamoDB

Once we receive the data to our AWS IoT Core, we will configure the Rules to connect the following services.

<img src="https://i.ibb.co/zhzZXGh/Create.png" width="1000">

- Set any name for the Rule.

<img src="https://i.ibb.co/Rj05MW5/image.png" width="1000">

- In the SQL Query we will place our topic.

<img src="https://i.ibb.co/7t4jfSg/image.png" width="1000">

- The first rule we are going to create will be to save all the data in a DynamoDB.

<img src="https://i.ibb.co/nRm3WNy/image.png" width="1000">

- Press "Create a new resource" to create the table where we will save the data.

<img src="https://i.ibb.co/Hn4TYS2/image.png" width="1000">

- For our table we will use the following parameters, I suggest that you use these specifically, since at production level all the device numbers will be different and in the "Time" column we are going to implement a special TIMESTAMP function.

<img src="https://i.ibb.co/ZWR8GcG/image.png" width="1000">

The Sort Key value special function in the sortkey setup is:

    ${parse_time("yyyy.MM.dd G 'at' HH:mm:ss z", timestamp() )}

- Once this is finished, we will have finished the first rule. In this case, because the rule for the lambda uses a different SQL query, we will no longer add any more actions to this rule.

## Lambda:

- To create a new rule but using the following SQL Query.

<img src="https://i.ibb.co/7t4jfSg/image.png" width="1000">

- We will add to this rule the following action:

<img src="https://i.ibb.co/n3H5576/image.png" width="1000">

- Press the "Create a new Lambda Function" button:

<img src="https://i.ibb.co/5sLHqy2/image.png" width="1000">

- We configure the lambda in the following way and create it:

<img src="https://i.ibb.co/68j2BXJ/image.png" width="1000">

- Once the lambda has been created we go down to the Execution role section and press the View the YOURROLE button on the IAM console to be able to add the SNS police to the SMS:

<img src="https://i.ibb.co/K9QRFc4/image.png" width="1000">

- We add the SNS service  
    - AmazonSNSFullAccess 

<img src="https://i.ibb.co/xJV8jxX/image.png" width="1000">

- Once that is finished, we select the lambda in our rule to finish configuring the lambda trigger.

<img src="https://i.ibb.co/zh8Fq0C/image.png" width="1000">

- Before programming the Lambda we will have to configure the SMS service through SNS.

<img src="https://i.ibb.co/RbjHG8c/image.png" width="1000">

- Press the "Create Topic" button to create our message service.

<img src="https://i.ibb.co/fNhCPfh/image.png" width="1000">

- Give the Topic a title and create it.

<img src="https://i.ibb.co/YDZXHC5/image.png" width="1000">

- Save the ARN number, since we are going to need it to configure the lambda.

<img src="https://i.ibb.co/NpBxLj1/image.png" width="1000">

- Click "Create subscription".

<img src="https://i.ibb.co/bvdLmBW/image.png" width="1000">

- Select as "Protocol" SMS and in Endpoint put your cell number (International dialing).

<img src="https://i.ibb.co/Kw1F5SW/image.png" width="1000">

- Done, we have finished creating the necessary services to use the lambda correctly, now we return to the lambda and copy the code in the Lambda Code folder and paste it into your Lambda.

<img src="https://i.ibb.co/tC9h9KZ/image.png" width="1000">

- The most important part of the code is the Thresholds, each of them was obtained from the following references.

- Max Accel Limit: https://web.archive.org/web/20170104164718/http://www.au.af.mil/au/aupress/digital/pdf/book/b_0113_brulle_engineering_space_age.pdf
- Max Pressure on Flight: https://www.who.int/ith/mode_of_travel/cab/en/
- Max Degrees: 45 degrees maximum static friction before the dog slips
- Max Magnetic Field: https://www.who.int/peh-emf/publications/facts/fs322/en/
- Min and Max, Temperature and Humidity: http://www.dartmouth.edu/~cushman/courses/engs44/comfort.pdf

# IoT Things:

Since we have all our platform ready, we have to create the accesses to communicate with it. So we will have to create two Things in this case, the first is for our Helium Kit and the other will be for the NodeRed UI.

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

- With this, we have the entire cloud backend of the project, so now we can focus on the frontend.

# Node-Red Setup:

- Node Red is a tool for NodeJS where we can integrate services easily, without code and, of course, create excellent dashboards.

- NodeJS installation guide: https://www.guru99.com/download-install-node-js.html

- NodeRED installation guide: https://nodered.org/docs/getting-started/windows

- NodeRED installation guide: https://flows.nodered.org/node/node-red-dashboard

- The file "flows.json" in the folder "Node-RED Flow", has all the information to import the flow into your NodeRED.

<img src = "https://i.ibb.co/c11ZJT8/image.png" width = "400">
<img src = "https://i.ibb.co/nBL3M23/image.png" width = "400">

- Once that is done we will edit the MQTT node to enter our credentials.

<img src = "https://i.ibb.co/SyM0X7S/image.png" width = "600">

- Set Server and Port.

<img src = "https://i.ibb.co/WHrcHCd/image.png" width = "600">

- Press in the pencil in TSL configuration to add the certificates.

- Note: RootCA certificate inside "Certs" folder.

<img src = "https://i.ibb.co/nMgtkRN/image.png" width = "600">

- If everything works fine press the "Deploy" button and enter the following URL to check the Dashboard.

http://localhost:1880/ui

<img src = "https://i.ibb.co/SKPbtM3/image.png" width = "800">

- The device's real-time location map is at:

http://localhost:1880/worldmap/

<img src = "https://i.ibb.co/ydhWQVs/image.png" width = "800">

### Explanation for nodes:

- This node receives the broker's payloads, filters according to the sensor which graph it has to go to and sends it to graph and deploy the adress in the world map.

<img src = "https://i.ibb.co/DD4WD7v/image.png" width = "800">

# Product:

<img src="https://i.ibb.co/XxL85ZT/20200609-003412.jpg" width="1000">
<img src="https://i.ibb.co/gJrrtx1/20200609-003442.jpg" width="1000">

All the solution in action:

<img src = "https://i.ibb.co/b3jg4Sj/ezgif-com-video-to-gif-2.gif" width = "800">

UI:

http://localhost:1880/ui

<img src = "https://i.ibb.co/SKPbtM3/image.png" width = "800">

- The device's real-time location map is at:

http://localhost:1880/worldmap/

<img src = "https://i.ibb.co/ydhWQVs/image.png" width = "800">

# Demo:

This my DEMO:

Video: Click on the image:

[![Demo](https://i.ibb.co/Tbq1r7Y/Logo.png)](https://youtu.be/m8bSZlNu_z4)

Sorry github does not allow embed videos.

* [Table of Contents](#table-of-contents)

