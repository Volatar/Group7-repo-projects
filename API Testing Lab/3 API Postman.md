# API Testing With Postman
## Introduction to Postman
Postman is an API platform that provides tools for building, testing, and using APIs.
It can make HTTP requests, save environments for later, alongside convert API code into languages like Python and JavaScript.
All of this functionality is handled by a simple and easy-to-use user interface.
As a result, Postman is used by millions of API developers every year for all their API needs.

## How to Setup Postman
1. First, you must download Postman to be able to use it.
   Whilst there is a variety of Postman products to use, we are just going to download the free version provided.
   [Click here for the link](https://www.postman.com/downloads/)
   
   ![postman-webpage](https://github.com/Volatar/Group7-repo-projects/assets/94473147/d8337177-4a7c-47b2-b381-e116378fbf9a)

2. After downloading Postman from that link, you must now install it.
   Simply click on the setup file you downloaded should install everything.
3. You will be presented with a menu that will ask you to sign up or create an account.
   You can create an account or you can select an option towards the bottom of the window to skip this process.
   It should be noted that if you do not have an account associated with your Postman application, you will be limited in certain actions you can do with Postman and your UI will be different.

## How to Test With Postman
To keep things simple and to work with the basic API template we have used throughout this lab, we are going to focus on using HTTP requests with Postman.
If you did not create an account with Postman, this will be possible but will be slightly different.
The requests should be the same, but you will not be able to create collections and workspaces or take advantage of templates.
You should however still be able to follow along.

### Step-By-Step
1. You should be in a default workspace, you can either create a new one or use the current one.
   However, you will want to create a new collection, in this case, a REST API basics template is perfect or you can create your own with a blank template.
   
   ![postman-createcollection](https://github.com/Volatar/Group7-repo-projects/assets/94473147/95f1bb16-9b53-487b-9a14-dd8eb8f71b19)

   If you use the blank template you will have to create your own requests.
   In this example, it is recommended you use the REST API basics template.
2. You should now be presented or create 4 requests, a GET request, a POST request, a PUT request, and finally a DEL request.
   Each of the API request methods should be familiar, with a GET retrieving data, a POST adding data, a PUT updating data, and a DEL deleting data in the API.
   Let's start with the simplest request, the GET request.
3. To modify the GET request, simply select it.
   First, you will want to provide the request with the API's URL.
   For our tutorial, you can use our simple API, simply by pasting `http://127.0.0.1:5000/iceCream`.

   ![postman-url](https://github.com/Volatar/Group7-repo-projects/assets/94473147/18881a07-57df-4547-9fce-86a5536afd36)

   You will also want to actually retrieve something specific.
   In this case, let us retrieve the 4th flavor on the menu.
   Add `/4` to the end of the URL and click Send.
   
   ![postman-send](https://github.com/Volatar/Group7-repo-projects/assets/94473147/b73541f5-9d49-42b0-9b98-20ea1eedeb97)

   You should receive a dictionary containing the flavor "Cookies and Creme" unless the API was recently modified.
   
   ![postman-return](https://github.com/Volatar/Group7-repo-projects/assets/94473147/01a741bb-b248-47ac-a52a-b2cc0ac88761)

4. Now let us move on to something a little more complicated, the POST method.
   First, you will want to select the POST method in your collection and then enter the same URL from the GET method, except instead of `/4` use `/6`.
   To keep this tutorial simple and to work similarly to the API requests in Python, we will then select the Body tab below the URL.
   From there you might want to select the form-data bubble to ensure that your parameters are clear and make sense, though any format you feel comfortable with should work.
   On form-data, you want to **double-click** on the sections in the table below the first row, this will allow you to select the key and its value.

   ![postman-body](https://github.com/Volatar/Group7-repo-projects/assets/94473147/023d59f6-2a9a-4a3f-ae91-91aadc3f3b7c)

   In this case, the key should be `name` and the value can be whatever flavor you want.
   After entering the key and its value into the body, you can now click the Send button, and your request should process and return the flavor you entered (We used Rocky Road as an Example).
5. Next, use the PUT request method.
   This method will follow the same details as mentioned in step #4.
   The main exception is that you should be updating the current menu item to another flavor.
   Therefore, under the body tab, you should change the value to `Butter Pecan`.
   Once you send this request it will return the new flavor, replacing the flavor you came up with before.
6. Finally let's get rid of the 6th flavor, with the DEL request method.
   In this case, you will not have to add anything under the body tab, just keep the same URL from steps #4 and #5.
   Once you have sent the request, you will be returned a message saying `"Item is deleted from the menu"`.

This should give a basic idea of how to run HTTP requests and interact with our simple API lab template.
Feel free to experiment with the requests presented and interact with the API.

