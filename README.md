fenix_python_sdk
================

Install the sdk:
- Clone this repo
- Run setup file
<code>python setup.py install</code>

Create a configurations file in your application project root:
- Copy file fenixedu.sample.ini to a new one called fenixedu.ini
<code>cp fenixedu.sample.ini fenixedu.ini</code>
- Fill the fields as needed

How to use it:
- In your source code file:
- Import python sdk
<code>import fenix</code>
- Instatiate an API object in your code
<code>api = fenix.FenixAPISingleton()</code>
- Get the authentication url
<code>url = api.get_authentication_url()</code>
- Redirect your user to that url
- It will redirect the user to a url like:
<code>redirect_uri?code=[code]</code>
- Get the code parameter in url and do:
<code>api.setCode(code)</code>
- It will request an access token and returns no erros if everything is fine
-Start using the api like this:
<code>person = api.getPerson()</code>
