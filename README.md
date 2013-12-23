fenix_python_sdk
================

<b>Installation</b>
<br>
<code>pip install fenix_api_sdk</code>
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
<code>api.set_code(code)</code>
<br>
- It will request an access token and returns no erros if everything is fine
<br>
- Start using the api like this:
<br>
<code>person = api.get_person()</code>

<b>Available methods</b>
<br>
[x] - Optional parameters
<br>
- All endpoint in FenixEdu API have a method in this sdk
<br>
- <b> Mapping between FenixAPISingleton api methods and original api endpoints </b>
<br>
API endpoint -> SDK FenixAPISingleton Methods
<br>
<b>- Public methods </b>
<br>
GET /about -> <code>get_about</code>
<br>
GET /courses/{id} -> <code>get_course(id)</code>
<br>
GET /courses/{id}/evaluations -> <code>get_course_evaluations(id)</code>
<br>
GET /courses/{id}/groups -> <code>get_course_groups(id)</code>
<br>
GET /courses/{id}/schedule ->  <code>get_course_schedule(id)</code>
<br>
GET /courses/{id}/students ->  <code>get_course_students(id)</code>
<br>
GET /degrees -> <code>get_degrees([year])</code>
<br>
GET /degrees/{id} ->  <code>get_degree(id, [year])</code>
<br>
GET /degrees/{id}/courses -> <code>get_degree_courses(id, [year])</code>
<br>
GET /spaces -> <code>get_spaces()</code>
<br>
GET /spaces/{id} -> <code>get_space(id,[day])</code>
<br>
<b>- Private methods (You need to get an access token before calling one of this methods)</b>
<br>
GET /person -> <code>get_person()</code>
<br>
GET /person/calendar/classes -> <code>get_classes_calendar()</code>
<br>
GET /person/calendar/evaluations -> <code>get_evaluations_calendar()</code>
<br>
GET /person/courses -> <code>get_courses([sem], [year])</code>
<br>
GET /person/evaluations -> <code>get_evaluations()</code>
<br>
GET /person/payments -> <code>get_payments()</code>
<br>
PUT /person/evaluations/{id} -> <code>enrol_in_evaluation(id, [enrol_action])</code>
<br>
GET /person/curriculum -> <code>get_curriculum()</code>
<br>

More info about all available endpoints in <a href="http://fenixedu.org/dev/api/">FenixEdu API website</a>
