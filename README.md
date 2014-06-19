fenix_python_sdk
================

##Installation
<code>pip install fenixedu_api_sdk</code>


## Configuration

* Create a configurations file in your application project root:

* Clone this repo or just download fenixedu.sample.ini file</b>

* Copy file fenixedu.sample.ini to a new one called fenixedu.ini

<code>cp fenixedu.sample.ini fenixedu.ini</code>

* Move it to your project's root

<code>mv fenixedu.ini project_dir</code>

* Edit fenixedu.ini file according to your app info


## Usage

* Import python sdk

<code>import fenixedu</code>

* Instatiate an API object in your source code

<code>api = fenixedu.FenixEduAPISingleton()</code>

* Get the authentication url

<code>url = api.get_authentication_url()</code>

* Redirect your user to that url

* It will redirect the user to a url like:

<code>redirect_uri?code=[code]</code>
* Get the code parameter in url and do:

<code>api.set_code(code)</code>

* It will request an access token and returns no erros if everything is fine

* Start using the api like this:

<code>person = api.get_person()</code>



<b>Multiple users using the same client</b>
<br>
As you have noticed, the client is a singleton. So you can't use with it if you have multiple users using your application at the same time (like a web application).
<br>
To use it with with multiple users:
<br>
- Instatiate a user object
<br>
<code>user = fenix.User()</code>
<br>
- When you get the code from the api (After the user logged in), you can pass the user object to set_code method like this:
<br>
<code>api.set_code(code, user)</code>
<br>
- After this, if nothing goes wrong, the user object will contain the access token, refresh token, etc.
<br>
- Now, you can use the private methods with that user. Example:
<br>
<code>person = api.get_person(user=user)</code>
<br>
- You can instatiate as many users as you want. If you don't instatiate an user, the FenixAPISingleton will use a singleton user object.
<br>

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
GET /academicterms -> <code>get_academic_terms</code>
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
GET /person -> <code>get_person([user])</code>
<br>
GET /person/calendar/classes -> <code>get_person_classes_calendar([user])</code>
<br>
GET /person/calendar/evaluations -> <code>get_person_evaluations_calendar([user])</code>
<br>
GET /person/courses -> <code>get_person_courses([sem], [year], [user])</code>
<br>
GET /person/evaluations -> <code>get_person_evaluations([user])</code>
<br>
GET /person/payments -> <code>get_person_payments([user])</code>
<br>
PUT /person/evaluations/{id} -> <code>enrol_in_evaluation(id, [enrol_action], [user])</code>
<br>
GET /person/curriculum -> <code>get_person_curriculum([user])</code>
<br>

More info about all available endpoints in <a href="http://fenixedu.org/dev/api/">FenixEdu API website</a>
