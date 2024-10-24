# Wine quiz
#### Video Demo: https://youtu.be/1qMF6oyl1GU
#### Description:
This is an application to keep track of the questions of an external quiz, it was inspired by  an app that I use that consists on a wine themed quiz, so I based my design choices on their visual identity. It has the function to add new questions with their correct answer and to search the questions in the database so you never miss.

I used python for the backend with flask to handle the routes and HTML, CSS and Javascript for the frontend, with jinja integrating front and backend, and making dynamic templates.

The layout.html file sets up the general appearance of the pages, especially the navbar on top. It won't appear on the landing page, I chose to switch it with buttons centered on screen to improve readability of this page.

home.html is the file for the landing page and it creates the buttons to access the other two pages using jinja to extend layout.html.

On the add_question.html page we have a form with two input text fields, one for the question and another for the answer. After filling them we can submit the form to store its content in our database and will receive a confirmation message.

With the search.html page we can search the database for any questions previously registered in our DB through a form with a text field to be filled with our search parameters. It will redirect us to the search_results.html, wich will acces the DB looking for a question that matches our parameters and bring the results in table form. Here I added the possibility to select a question and delete it when we want to.

Initially I intended to have another page dedicated to delete questions, but along development I realized it would be redundant with search.html, and would only repeat what this page already did.

The quiz.db file was created using sqlite and has one table with four columns (id, question, answer and ascii_question). Since I'm brazilian, I wanted the app to be able to handle special characters like ã, é, ç and others we use in portuguese. So I designed the DB table with two columns that are almost identical, one of them has the questions exactly the way they were submitted on the form, and the ascii_question column has a version of the question without these special characters (only ascii characters). I decided to go this way because my intention is to store only a few questions and because of that storage space won't be a issue.

To look for the questions I used a query that searches on the ascii_question column and returns the results from the question and answer columns.This way I can have the results to be shown correctly when I search for them, with all the special characters, but it will also work if someone types their search parameter without the special characters. For that I treated the search parameter on the backend to contain only ascii characters before passing it ot the query.