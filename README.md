# Book Reservation Web Application with an Analytics Dashboard made with Django

Authentication
![webapp2](https://user-images.githubusercontent.com/68674002/145207803-1c2da859-cb15-435f-947a-d21e836cd29e.PNG)

Dashboard
![webapp3](https://user-images.githubusercontent.com/68674002/145208468-dec2a7bd-6dd2-45fd-9b8e-d1d3d1264fc6.PNG)

Reserving books for students
![webapp5](https://user-images.githubusercontent.com/68674002/145208472-370590e7-9371-472a-8fa2-7c73f44c6e38.PNG)
![webapp4](https://user-images.githubusercontent.com/68674002/145208470-882480ca-22dd-43de-bde5-3634c8e905b7.PNG)




### Requirements
Getting Started - One time setup

Clone this Repo using the HTTPS method


### Installing

Have a later version of Java installed (11+)

Install an Eclipse IDE with JEE and Web app (JSF, JPA) features. [Eclipse 2020-03](https://www.eclipse.org/downloads/packages/release/2020-03/r)

Install the wlp server folder https://openliberty.io/start/ Scroll down and install the zip (Version=20.0.0.11, All GA Features). Save it in a secure location


Once you start Eclipse navigate to Eclipse MarketPlace and search for `liberty`. The first two that pop up should be `IBM Liberty Developer Tools 20.0.0.9` and `IBM WebSphere Application Server Liberty Developer Tools Beta 20.0.0.9`. Install both of these tools
All plugins should install without error

Import the project into eclipse
File > Import > General > Projects from Folder or Archive > Directory…
Select PerfMgmtStore and PerfMgmtStoreEar and click finish


Now you need to add the version of Java we are using for the project

In your browser go to the link:
https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html
And install the:
Java SE Development Kit 8u172

Change the Java Build Path for the project:
Confirm your path by navigating to it in the terminal. It should look something like this:
“/Library/Java/JavaVirtualMachines/jdk1.8.0_172.jdk/Contents/Home/”
What we need to do is add 5 security files to repo




In eclipse, under the Package Explorer section on the right:
Right click PerfMgmtStore> Properties > Java Build Path > Libraries > JRE System Library > Installed JREs > Add > MACOS X VM

Copy your java path to the JRE home and rename it to Java SE 1.8.0_172. Once you click finish select that java version and click Apply and Close


Add the liberty Server in Eclipse:
Navigate to Windows > Show View > Other > Server > Servers > Finish
Severs tab > create a new server > IBM > Liberty Server > Path > Select the installed wlp server > finish

Go back to the server panel > expand Liberty Server > Open Server Configuration > Source > locate the line with “fileset” and edit the start of the path to match your local setup. 
Then right click Liberty Server again > Start

Navigate to Performance-Management/PerfMgmtStoreBuild/defaultServer/resources/security and copy the 5 files then paste them in wlp/usr/servers/defaultServer/resources/security/


# You need to set environment variables to the current shell to initialize the secrets volume.
```
# Vault prod address
export VAULT_ADDR=https://vserv-us.sos.ibm.com:8200

# Analytics Prod (New project) SECRET ROLE AND ID
export VAULT_SECRET_ID=<provided secret id>
export VAULT_ROLE_ID=<provided role id>

# Vault login path, the URL we authenticate at
export VAULT_LOGIN_PATH=/v1/auth/approle/login

# StoreFront prod Vault instance
export STOREFRONT_VAULT_PATH=/v1/generic/project/ne-ant-ai-analytics/storefront/prod

# BlueArgus prod Vault instance
export BLUEARGUS_VAULT_PATH=/v1/generic/project/ne-ant-ai-analytics/blueargus/prod

```

`source ~/.bash_profile`


Under the Servers tab
Go to Liberty Server at localhost and add these to your server.env file


`VAULT_ADDR=https://vserv-us.sos.ibm.com:8200
VAULT_SECRET_ID=<provided secret id>
VAULT_ROLE_ID=<provided role id>
VAULT_LOGIN_PATH=/v1/auth/approle/login
STOREFRONT_VAULT_PATH=/v1/generic/project/ne-ant-ai-analytics/storefront/prod `
