fenix_python_sdk
================

Install the sdk:

Create a configurations file:

How to use it:
- Instatiate an API object in your code
<code>api = FenixAPI()</code>
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
