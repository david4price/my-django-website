# my-django-website

This is my main website which will contain in the future my django projects, currently it has only one project.

The current project is based on my previous python project(parking-lot-automation), but now in web version with user interface. 

The website consists of two menu types:
- The first type is for ‘superuser’ which contains: parking lot setup and creation, updating the parking lot name, area and hourly charge rate or even       deleting it. All this can be only accessed by a ‘superuser’ account. In order to create a new ‘superuser’ you need to register as a regular user and       then a ‘superuser’ can change your permissions for a ‘superuser’. The regular creation of a ‘superuser’ isn’t possible because of a usage of a custom       user   model.
- The second type is for ‘user’ which contains: activation of parking with choosing the wanted parking lot or browsing the home menu and filtering by the     wanted area. Ending the parking session through the users profile which he can see all his active tickets. Upon ending the parking session the sub total   amount will be added to the users ‘balance’ which can be seen in the users profile. 

For now the user profile picture doesn’t load and it appears empty, can’t seem to understand why.
