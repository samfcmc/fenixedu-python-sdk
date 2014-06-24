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

<code>mv fenixedu.ini PROJECT_DIRECTORY</code>

* Edit fenixedu.ini file according to your app info


## Usage

### Authentication

* Import python sdk

<code>import fenixedu</code>

* Instatiate an API object in your source code

<code>api = fenixedu.FenixEduAPISingleton()</code>

* Get the authentication url

<code>url = api.get_authentication_url()</code>

* Redirect your user to that url

* It will redirect the user to a url like:

<code>redirect_uri?code=CODE</code>
* Get the code parameter in url and do:

<code>api.set_code(CODE)</code>

* It will request an access token and returns no erros if everything is fine

* Start using the api like this:

<code>person = api.get_person()</code>

### Multiple users using the same client
* As you have noticed, the client is a singleton. So you can't use with it if you have multiple users using your application at the same time (like a web application).

* To use it with with multiple users:

* Instatiate a user object

<code>user = fenix.User()</code>

* When you get the code from the api (After the user logged in), you can pass the user object to set_code method like this:

<code>api.set_code(code, user)</code>

* After this, if nothing goes wrong, the user object will contain the access token, refresh token, etc.

* Now, you can use the private methods with that user. Example:

<code>person = api.get_person(user=user)</code>

* You can instatiate as many users as you want. If you don't instatiate an user, the FenixAPISingleton will use a singleton user object.

### Full endpoint list

* '[x]' - Optional parameters

* All endpoint in FenixEdu API have a method in this sdk

* Mapping between FenixAPISingleton api methods and original api endpoints 

* API endpoint -> SDK FenixAPISingleton Methods

#### Public methods 

* GET /about -> <code>get_about</code>

* GET /academicterms -> <code>get_academic_terms</code>

* GET /courses/{id} -> <code>get_course(id)</code>

* GET /courses/{id}/evaluations -> <code>get_course_evaluations(id)</code>

* GET /courses/{id}/groups -> <code>get_course_groups(id)</code>

* GET /courses/{id}/schedule ->  <code>get_course_schedule(id)</code>

* GET /courses/{id}/students ->  <code>get_course_students(id)</code>

* GET /degrees -> <code>get_degrees([year])</code>

* GET /degrees/{id} ->  <code>get_degree(id, [year])</code>

* GET /degrees/{id}/courses -> <code>get_degree_courses(id, [year])</code>

* GET /spaces -> <code>get_spaces()</code>

* GET /spaces/{id} -> <code>get_space(id,[day])</code>

#### Private methods (You need to get an access token before calling one of this methods)</b>

* GET /person -> <code>get_person([user])</code>

* GET /person/calendar/classes -> <code>get_person_classes_calendar([user])</code>

* GET /person/calendar/evaluations -> <code>get_person_evaluations_calendar([user])</code>

* GET /person/courses -> <code>get_person_courses([sem], [year], [user])</code>

* GET /person/evaluations -> <code>get_person_evaluations([user])</code>

* GET /person/payments -> <code>get_person_payments([user])</code>

* PUT /person/evaluations/{id} -> <code>enrol_in_evaluation(id, [enrol_action], [user])</code>

* GET /person/curriculum -> <code>get_person_curriculum([user])</code>

#### More info about all available endpoints in <a href="http://fenixedu.org/dev/api/">FenixEdu API website</a>
