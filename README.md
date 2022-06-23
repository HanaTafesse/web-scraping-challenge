# web-scraping-challenge

# Missions_to_Mars_full_page

![Missions_to_Mars_full_page](/Missions_to_Mars/Missions_to_Mars_Images/Missions_to_Mars_full_page.png)

## Part  1: Scraping

Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

* Create a Jupyter Notebook file called `mission_to_mars.ipynb`. Use this file to complete all your scraping and analysis tasks. The following information outlines what you need to scrape.

![Missions_to_Mars](/Missions_to_Mars/mission_to_mars.ipynb)

### NASA Mars News

* Scrape the [Mars News Site](https://redplanetscience.com/) and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

![Latest latest News Title and Paragraph](/Missions_to_Mars/Missions_to_Mars_Images/Latest_Mars_News.png)

### JPL Mars Space Images—Featured Image

* Visit the URL for the Featured Space Image site [here](https://spaceimages-mars.com).

* Use Splinter to navigate the site and find the image URL for the current Featured Mars Image, then assign the URL string to a variable called `featured_image_url`.

![Featured_Mars_Image](/Missions_to_Mars/Missions_to_Mars_Images/Featured_Mars_Image.png)

### Mars Facts

* Visit the [Mars Facts webpage](https://galaxyfacts-mars.com) and use Pandas to scrape the table containing facts about the planet including diameter, mass, etc.

![Mars_Facts_table](/Missions_to_Mars/Missions_to_Mars_Images/Mars_Facts_table.png)

### Mars Hemispheres

* Visit the [astrogeology site](https://marshemispheres.com/) to obtain high-resolution images for each hemisphere of Mars.

* You will need to click each of the links to the hemispheres in order to find the image URL to the full-resolution image.

* ![Mars_Hemispheres](/Missions_to_Mars/Missions_to_Mars_Images/Mars_Hemispheres.png)

## Part 2: MongoDB and Flask Application

Use MongoDB with Flask templating to create a new HTML page that displays all the information that was scraped from the URLs above.

![Mars_db.mars_data](/Missions_to_Mars/Missions_to_Mars_Images/mars_db.mars_data.png)

* Start by converting your Jupyter notebook into a Python script called `scrape_mars.py` by using a function called `scrape`. This function should  execute all your scraping code from above and return one Python dictionary containing all the scraped data.

* ![MongoDB/scrape_mars.py](/Missions_to_Mars/scrape_mars.py)


* Create a template HTML file called `index.html` that will take the Mars data dictionary and display all the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.

![Flask Application/app.py](/Missions_to_Mars/app.py)

![Index Template/index.html](/Missions_to_Mars/templates/index.html)