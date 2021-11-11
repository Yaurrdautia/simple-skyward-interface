import skywrd

#initializes the library with the parameters.
skywrd.setup("helloworld","helloworld")

#logs into account and grabs the string that has the session id in it.
session = skywrd.get_login()

#gets the html for the whole page.
html = skywrd.get_gradbook_html(session)

#gets the names of the teachers and cources as a list.
teachers = skywrd.get_teachers(html)

print(teachers)
