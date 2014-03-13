The task is to build a django webserver with admin panel, 2 tables, and a simple API interface:

1. Create 2 tables as models in Django.
Employees:
id
first name,
last name,
department_id

Departments:
id,
name

2. Allow the Admin panel to add/update/delete and search these tables.
3. Write an API interface on top op Django, where the results are in JSON format:
a) get_users - returns a list of the users, with their department name
b) get_user - receives as key the user's ID, and returns the user with it's department name.

--
Example:
```bash
curl http://127.0.0.1:8000/api/get_users/
```

```bash
curl http://127.0.0.1:8000/api/get_users/
```
