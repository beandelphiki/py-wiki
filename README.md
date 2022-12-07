
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
- High Availability: In order to make this highly available in a completely open-source environment with your own home-grown systems there's a few options that you could attach this to.
    - Public Cloud (i.e. AWS)
    - On Prem (Your own private Datacenter with Kubernetes (K8))



