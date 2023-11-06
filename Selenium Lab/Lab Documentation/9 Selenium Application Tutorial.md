# Selenium Application Tutorial

Selenium is a testing tool that allows for applications and code to be rigorously tested for faults or bugs. 
The application presented in this lab has several tests dedicated to ensuring various facets of the code function on several levels. 
To start, here is a sampling of code from ‘selenium_main.py’:

![img1](https://i.imgur.com/4Tk79TO.jpg)

This test is designed to bounce off another test, so assume that ‘Alien VS Ogre’ is a movie loaded into the cart currently so that we can perform a test with visual example working off of the cart screen, as for other tests, ‘Elven’ will be the movie visual example.

### Test Example 1

Here is the code for that test:

![img2](https://i.imgur.com/Ic8BmQp.jpg)

First and foremost is that when tests are run, the assumed starting point would be the main page, so the first line of code navigates to the Cart page. 
The second line is for automatic screenshots and proof of working tests. 
Then there is an ‘if’ statement, which observes and checks for a button labeled as ‘remove Alien VS Ogre’ in the active cart. 
If the button to remove the movie individually is present and detected, the test clicks the element to remove the movie from the cart. 
Should it not be present, a response is generated to notify the tester. 
The final line serves to screenshot the page after enacting all the tests for another form of proof. 
Here is a visual example of what the test is aiming to accomplish:

![img3](https://i.imgur.com/CECp6Lw.png)

The highlighted portion of the image above shows the exact button the test looks for and identifies. Should it be identified, the button is then pressed, and the cart deletes ‘Alien vs Ogre.’

### Test Example 2

Here is the code for another test:

![img4](https://i.imgur.com/jZShIqy.jpg)

This test works by clicking a present button with an ID of ‘pay,’ and takes a screenshot to ensure the payment screen is reached. 
Once proof is captured, the test attempts to click the button within the payment page to return to the cart, with an ID of ‘return_cart.’ 
As the option to travel to the payment page is located within the cart, this referential image will show the steps undergone by the test:

![img5](https://i.imgur.com/qtm9yaV.png)

The highlighted portion is the button that will be pressed to navigate to the payment screen.
By taking a screenshot, the test has visible proof that the current screen is on payment and should look similar to the following image:

![img6](https://i.imgur.com/VIruo8S.png)

Once the screenshot is obtained, the code will press the button in the image above marked ‘Return to Cart’ to remain within the cart page for further tests.

### Test Example 3

Here is the code for a third and final test:

![img7](https://i.imgur.com/rd20811.jpg)

What this test aims to do is navigate to the payment page, taking a screenshot once it arrives to ensure the correct page is visible. 
Once the page is assured, it simply processes through the payment, which does not actually accept any money, as a simple application designed for this lab. 
The following image shows the payment page and highlights what the test will press in order to succeed:

![img8](https://i.imgur.com/d70joaL.png)

Hopefully through these examples and descriptions, the possibilities provided by Selenium for optimal testing are shown to you clear as day. 
There are many more tests available within the application code for you to observe, so enjoy!