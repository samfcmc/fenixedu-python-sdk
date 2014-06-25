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

<code>client = fenixedu.FenixEduAPISingleton()</code>

* Get the authentication url

<code>url = client.get_authentication_url()</code>

* Redirect your user to that url

* It will redirect the user to a url like:

<code>redirect_uri?code=CODE</code>
* Get the code parameter in url and get an object with the user details:

<code>user = client.get_user_by_code(CODE)</code>

* It will request an access token and returns no erros if everything is fine

* This user object now can be used to make requests that belong to the private scope like:

<code>person = client.get_person(user)</code>

### Examples

#### Get degrees
<code>degrees = client.get_degrees()</code>

#### Get spaces
<code>spaces = client.get_spaces()</code>

#### Get information about the user
<code>person = client.get_person(user)</code>

#### Get user's classes calendar
<code>classes = client.get_person_calendar_classes(user)</code>

#### Get user's payments
<code>payments = client.get_person_payments(user)</code>

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

* GET /person -> <code>get_person(user)</code>

* GET /person/calendar/classes -> <code>get_person_classes_calendar(user)</code>

* GET /person/calendar/evaluations -> <code>get_person_evaluations_calendar(user)</code>

* GET /person/courses -> <code>get_person_courses(user, [academicTerm])</code>

* GET /person/evaluations -> <code>get_person_evaluations(user)</code>

* GET /person/payments -> <code>get_person_payments(user)</code>

* PUT /person/evaluations/{id} -> <code>enrol_in_evaluation(id, user, [enrol_action])</code>

* GET /person/curriculum -> <code>get_person_curriculum(user)</code>

#### More info about all available endpoints in <a href="http://fenixedu.org/dev/api/">FenixEdu API website</a>
