# {Back-end User Interface for Future Clients}
A user-friendly way to import information about your company that will render appropriately for clients to see.
 

# Technologies Used
* Django
* Python
	* CSS Framework: Bootstrap
* posgreSQL

# Approach Taken
I had to decide the appropriate form thats a that would needed to be grouped 

### Sprint1 - Setup 
Brainstorm approach.
Acquire as much information from client as possible.
Create trello board and label the sprints with their distintive colors
Developed wireframes of the application
Created views structure based on wireframe
create Imgur account to store images

### Sprint2 - Backend 
Basic frontend pages with directions on where the data should be rendered
Create Models appropriate for site.
Using django's admin site - create a theme tailored to the  specific company.
Also using django's admin site - created forms to group together specific model fields, and rendered them with 
Basic error handling for input forms to prevent odd data entries

### Sprint3 - Frontend 
Revisited components and revised some routes for better User flow
Created basic styles all the pages
Fix bugs that are 

# Issues/Unresolve problems
* Learning MongoDb on the fly while pushing towards a deadline
 	* We had a slight learning curve when it came to learning a new db technology
    * Figuring out delete routes with node and making it sure we are passing the appropriate data objects was a challenge
* Styling React pages can be a chore when using a CSS framwork!
* We left some work on the table as we did not quite get the Quiz mode working
* Make Quiz mode be able to turn code into snippets
* Flesh out a delete route for Cards 
* Have a feature where users can share their cards with the community


# How to get your own {FlashDash}?
If you'd like to set this project up on your own local server: 
* Fork and clone this repository
* Run `npm install` to install dependencies in both client and main project folder
  * Create a react build with `npm run build`  in the /client folder
  * Use `nodemon` to run the application
* Setup your database with Mongodb 
* Create .env file, inside set a "JWT_SECRET=wordOfyourchoice".
* To have a view of your database, use Mongo Compass or Robo 3T to manage the data in your MongoDb.


# Backlog for future development
Add advance styling so the app has a more evernote or Google keep theme
