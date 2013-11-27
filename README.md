fenix_python_sdk
================

<b>Instalation</b>
<br>
- Install the dependencies with pip
<br>
<code>pip install -r reqs.txt</code>
<br>
- Install the fenix module
<br>
<code>python setup.py install</code>
<br>

<b>Configuration</b>
Create a configurations file in your application project root:
<br>
- Copy file fenixedu.sample.ini to a new one called fenixedu.ini
<br>
<code>cp fenixedu.sample.ini fenixedu.ini</code>
<br>
- Move it to your project's root
<br>
<code>mv fenixedu.ini project_dir</code>
<br>
- Edit fenixedu.ini file according to your app info
<br>

<b>Usage:</b>
<br>
- Import python sdk
<br>
<code>import fenix</code>
<br>
- Instatiate an API object in your source code
<br>
<code>api = fenix.FenixAPISingleton()</code>
<br>
- Get the authentication url
<br>
<code>url = api.get_authentication_url()</code>
<br>
- Redirect your user to that url
<br>
- It will redirect the user to a url like:
<br>
<code>redirect_uri?code=[code]</code>
- Get the code parameter in url and do:
<br>
<code>api.setCode(code)</code>
<br>
- It will request an access token and returns no erros if everything is fine
<br>
-Start using the api like this:
<br>
<code>person = api.get_person()</code>
