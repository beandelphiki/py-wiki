
# **PyWiki**
This allows you to do searches in Wikipedia and grab short descriptions of entries. This is a Flask-based endpoint so you need that installed on your system. <br /><br />


## **Requirements**
This is run in Python. I built this using the latest version of Python (``` version 3.11.0```).  You will need to run pip (or pip3 if that's your jam). The following libraries need to be installed on your system to have successfull execution:

|Module|Pip Command|Version|
|---| --- | ---|
|Flask| ```pip install flask```| latest|
|Requests| ```pip install requests```|latest|
<br /><br /> <br />

## **How to Run Locally**
Once you have verified that you installed Flask, you should have the Flask command available to you. Flask is **required** for this to execute properly on your local device. You also need to verify that port 5000 is open on your machine; you can optionally change this in the folder ```\pywiki-main\handler.py```. You can verify Flask is working properly on your machine by running the following command: <br />

```[command prompt]% Flask --version``` <br />

You should see something like this: <br />

```
Python 3.11.0
Flask 2.2.2
Werkzeug 2.2.2
```

To run this in a locally go to the pywiki-main directory, and simply type in the following: <br />
```
flask --app  handler --debug  run
```

This will fire up a local server pointed to ```127.0.0.1:5000``` <br /> <br />

Open your browser and simply type in the following to your address bar : ``` http://127.0.0.1:5000/[titlepage name]/countryCode/[countryCode]/descriptor/['Short Description' in the desired language]```
<br /><br /> <br />
## HTTP Request Information: <br />
- Format of the request: <br />
    - ```[titlepage name]```: this refers to the title of the page you're interested in. For example, in the URL, if you are interested in information on Yoshua Bengio, you would type in ```Yoshua_Bengio```. Notice the ```_``` character. The endpoint will parse this out as needed but it is needed in the request to make it work. 
    - ```[countryCode]```: Use a valid Country Code supported by Wikipedia. For example, a valid country code for English would be ```en``` and so forth. The API will try to find the article in the default language of that country code. For example, ```en``` would bring back English; ```es``` would bring back Spanish content and so forth.
    - ```['Short Description' in the desired language]```: In order to get the short description you need to provide the short description in the language that you are looking for in the content. For example in english this is simply ```short_description``` in the URL. This can vary from language to language so this requires a bit of knowledge of the language that you want the short description in since it apparently seems to vary from page to page and language to lanugage. In general, the descriptor in the return result in the content block is simply ```short description``` or the equivalent in whatever language you are interested in. If there is no short description found you will get a friendly message telling you to check again.
- Sample output of a good request:
    - ***URL Request*** : ``` http://127.0.0.1:5000/Yoshua_Bengio/countryCode/en/descriptor/short_description ```
    - ***Sample response*** :  Canadian computer scientist
- Sample output of a bad request:
    - ***URL Request*** : ``` http://127.0.0.1:5000/Yoshua_Bengio/countryCode/zh/descriptor/short_description ```
    - ***Sample response*** :  That descriptor doesn't exist with this current combination; Check your Country Code or Article Spelling
<br /><br /> <br />
## Hypothetical Future State: <br />
There’s a few items related to reliability that could cause an API to not be available. In cloud-native applications this is usually solved by using some sort of Gateway. For example, AWS has API Gateway for this purpose. It allows for things like authorization and scaling with load automatically. That being said, it is only available in the context of AWS, for example. There are other cloud platforms with similar technologies. How can we solve for this in an open-source setting where transparency is important? We first have to consider some scenarios that we need to solve for and technologies that we can use overcome this issue. 

### Potential challenges to  availability and reliability:

- Security breaches/authorization issues
-  The API becomes flooded with traffic (intentionally or unintentionally)
-  The Server that it’s running on goes down or becomes unreliable
-  The service that the API calls becomes slow or unavailable
- Users in different parts of the world have issues connecting to it



### Potential Solutions:

-  Security breaches/authorization issues: This API currently lacks authorization. In a potential future version it would make sense to have authorization either implemented here or in an API Gateway type setup that enforces HTTPS with custom SSL. Additionally, it might make sense to have some sort of Web application and API protection firewall paired with a Web application firewall that would inspect the traffic and look for patterns in access. Together with some code changes and infrastructure changes we could protect the endpoints.
-  The API becomes flooded with traffic (intentionally or unintentionally): This is highly related to the first point. A mechanism with an API Gateway paired with a Web Application Firewall should help alleviate some of these issues. Also, this is where proper design of the infrastructure comes in place. A load balancer should also be looked at to validate that all of the legitimate  traffic coming in is routed to the right place. There are various schemes that could followed (Weighted, geolocation based, manually done (not ideal), Done on a schedule, etc.). Based on the anticipated use, the team would have to decide a scheme; Maybe even adopting a hybrid approach that is dynamic and based on usage or other factors. There’s different ways to attack this problem but it should be considered in any deployment.
-  The Server that it’s running on goes down or becomes unreliable: Instead of running this on one server, I would run a K8 cluster with auto-scaling options in enabled spread across different regions with Load balancers in front of them. If possible I would even consider edge locations as well to see if this makes sense based on where my users are. Wrapped up in docker and deployed on K8 there are a few options for scaling HPA and VPA. Horizontal Pod Autoscaler is more or less the software approach to managing the pods and you can write it to look at various factors. Vertical Pod Autoscaler looks at the hardware utilization and scales as needed but this requires the pod to be restarted which would mean some downtime depending on how many pods you have. With redundancy built in, these can be orchestrated.
-  The service that the API calls becomes slow or unavailable: I would primarily attack this issue with caching. Caching responses locally for the most used API endpoints. It might make sense to cache responses pretty often throughout the day if you expect the data to change frequently; especially in the case of a very busy endpoint or topic/
-  Users in different parts of the world have issues connecting to it: I would look at implementing edge locations in different regions around the world. Bringing the data closer to your users would decrease on latency and ease the access to different people. 



