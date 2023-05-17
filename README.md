# <img src=https://user-images.githubusercontent.com/122404051/235878740-0f447969-b786-41de-93ca-a4528a4db470.gif width="48" height="48" >  Restaurant-Recommendation-Model
Built a web-based recommendation model using machine learning algorithms to recommend optimal restaurant locations and prices based on user preferences for cuisine, location, and price.
Used Jupyter Notebook to train the machine learning algorithms, and implemented the model using Flask web framework.
Developed a user-friendly web page using HTML and CSS to display the recommendation results.
Utilized libraries such as Scikit-Learn, importnb, and Pandas to perform data processing, modeling, and web development tasks.

<br>
<br>
<p align="center"><a><img src="https://user-images.githubusercontent.com/122404051/235915776-95efe711-5076-4b7b-8f2b-493893cce0f0.jpg" width="420" height="35"></a></p>

##  <img src="https://user-images.githubusercontent.com/106439762/181935629-b3c47bd3-77fb-4431-a11c-ff8ba0942b63.gif" width="48" height="48"> **Folder Structure Guide**

| Files/Folder| Description |
| ------------- | ------------- |
| **.ipynb Folder** | This folder includes the Jupyter Notebook files that were utilized to make Machine Learning models  |
| **Dataset Folder** | Within this folder, there are two CSV tables that were acquired by scraping data from the web and used in this project to create ML prediction models  |
| **Presentation Folder** | This folder contains the presentation in pdf format.  |
| **Deployment Folder** | This folder contains flask deployment file |
| **Web-page Folder** | This folder comprises HTML and CSS files, which are used to generate our webpage. |
| **CSS Data Files Folder** | It contains all the files that are used for styling our webpage, like background images, etc |
| **Pickle Folder** | It contains all the pickle files of both the models. |

<br>
<p align="center"><img src="https://user-images.githubusercontent.com/122404051/235923506-3e8b5280-f760-44d3-af9b-9da55946b26a.gif"
 width="400" ></p>
 
 ##  <img src=https://user-images.githubusercontent.com/106439762/178803205-47a08ce7-2187-4f96-b301-a2b68690619a.gif width="48" height="48" > Prior Knowledge <br>
<br>
<p align="center"><a><img src="https://user-images.githubusercontent.com/122404051/235928491-09398424-2c7c-45f8-a0d5-f452320d015c.jpg" width="1050" height="35"></a></p>


<br>

## <img src=https://user-images.githubusercontent.com/106439762/178804195-d9db61fb-b2cf-4c8f-bfc3-214cfe0f534c.gif width="48" height="48" > Quick Summary

      1. The Price prediction model is created on Decision Tree and Location prediction model is created on Random Forest as accuracy for both of these was best than others.
  ![1](https://github.com/dhananjay-metangale/Restaurant-Recommendation-Model/assets/122404051/b79ba0b1-33ee-4a9b-94e9-a8632834d035)
	
  ![2](https://github.com/dhananjay-metangale/Restaurant-Recommendation-Model/assets/122404051/7340adf7-d4c7-4be4-827e-94006daddc2d)

    2. Both of these models take three parameters, two of which are provided by the user they are Cuisine and Price For One and it takes the third parameter from the insights that is the Average Price For One of that location
  
  ![3](https://github.com/dhananjay-metangale/Restaurant-Recommendation-Model/assets/122404051/8b85a816-1923-484c-be9f-847af1fb41d2)
  
  ![4](https://github.com/dhananjay-metangale/Restaurant-Recommendation-Model/assets/122404051/5aec2398-89cb-4514-8818-49640bc22ce1)
    
    3. All of this inputs are taken from the html landing page using flask and then is compare with pkl file and is later predicted.
  
  	a) HTML code for Main Page
  
  ![5](https://github.com/dhananjay-metangale/Restaurant-Recommendation-Model/assets/122404051/c2f64321-44c6-444a-a8b1-9f6c9d2fbd8b)

  	b) HTML code for Prediction Page
  
  ![6](https://github.com/dhananjay-metangale/Restaurant-Recommendation-Model/assets/122404051/90c7072d-4e05-49ac-a9ae-ba32d7af783d)
  	
	c) Css Code For both Pages
  
  ![7](https://github.com/dhananjay-metangale/Restaurant-Recommendation-Model/assets/122404051/9a1e0871-7272-418b-9b13-d8ebb3213d6a)
  
    4. We connected all the Notebooks to a main Python file using a library  'importnb'
    
    5. Later when all the Notebooks were connected, we used flask to deploy the model on Web Page
    
   ![8](https://github.com/dhananjay-metangale/Restaurant-Recommendation-Model/assets/122404051/5a489943-f98d-4888-820d-b40321784c5e)
   ![9](https://github.com/dhananjay-metangale/Restaurant-Recommendation-Model/assets/122404051/c7349cbe-c2a6-4d47-b66e-4d420c69027c)

    
    6. Flask was used to Get and post the data on webpage
	
## <img src="https://user-images.githubusercontent.com/122404051/235936187-301b427a-9f69-4c72-8d3e-e289a50c3a59.png" width="48" height="48"/> Landing Page Screenshot
![landing page](https://user-images.githubusercontent.com/122404051/235935721-faca695c-97ea-4591-a633-ee1bfd2a052b.jpg)

## <img src="https://user-images.githubusercontent.com/122404051/235936187-301b427a-9f69-4c72-8d3e-e289a50c3a59.png" width="48" height="48"/> Prediction Page Screenshot
![predction page](https://user-images.githubusercontent.com/122404051/235935916-78179f03-339e-49db-814e-a185e5cd3a2d.jpeg)
