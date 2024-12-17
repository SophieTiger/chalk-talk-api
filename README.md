<p align="center">
  <img src="./documentation/chalk_logo_white.png" alt="Chalk Talk Logo" width="200"/>
</p>

<a name="top"></a>
# Chalk Talk API

[Chalk Talk Django REST Framework API Backend live link](https://chalk-talk-api-7f804e82f4b9.herokuapp.com/)

[Chalk Talk React Frontend live link](https://chalk-talk-react-444e4f93c93c.herokuapp.com/)

[Chalk Talk React Frontend GitHub repository](https://github.com/SophieTiger/chalk-talk/)

## Table of Contents

- [Project Goals](#project-goals)
- [Planning](#planning)
  - [Project Overview](#project-overview)
  - [Objectives](#objectives)
  - [Timeline](#timeline)
- [Data Models](#data-models)
- [API Endpoints](#api-endpoints)
- [Frameworks, Libraries, and Dependencies](#frameworks-libraries-and-dependencies)
  - [Django Framework and Extensions](#django-framework-and-extensions)
  - [Database Management](#database-management)
  - [Authentication and Security](#authentication-and-security)
  - [Storage and Image Handling](#storage-and-image-handling)
  - [Application Server](#application-server)
  - [Utility Libraries](#utility-libraries)
- [Testing and Validation](#testing-and-validation)
- [Bugs](#bugs)
- [Deployment](#deployment)
  - [Deployment Steps](#deployment-steps)
- [Cloning and Forking](#cloning-and-forking)
  - [Cloning the Repository](#cloning-the-repository)
  - [Forking the Repository](#forking-the-repository)
- [Credits](#credits)
  - [Code](#code)
  - [Media](#media)
- [Acknowledgements](#acknowledgements)
  - [Inspiration](#inspiration)
  - [Project Guidance](#project-guidance)
  - [README Structure](#readme-structure)
  - [Personal Thanks](#personal-thanks)


## Project Goals
Chalk Talk is designed to be a fitness companion for users of all levels, from beginners to seasoned athletes. The primary goals of the web app are to:

- Deliver a user-friendly and engaging platform where users can create and share posts, follow other users, and make use of personal records and percentage calculation on a daily basis.
- Provide users with tools to use on a daily basis, track personal records, share thoughts and feelings through posts, fostering a supportive and motivating community.
- Ensure a streamlined experience with essential features like personal records documentation, community engagement, and the ability to manage profiles, posts, and comments.

The backend is implemented using Django Rest Framework API for the Chalk Talk Website. It is designed to support both web and future mobile applications providing robust and secure APIs for the Chalk Talk React frontend application, ensuring seamless integration and future scalability.

## Planning
The planning phase for the Chalk Talk project encompasses several key areas to ensure the successful development and deployment of both the backend and frontend components. Here is a comprehensive plan to guide the development process:

### Project Overview
Chalk Talk is a comprehensive fitness platform designed to help users stay connected with their community to get inspired and inspire others on a daily basis. The platform includes features such as personal record documentation, weight percentage calculator, and social interaction to create a supportive and motivating environment for users.

### Objectives
Develop a robust backend API using Django Rest Framework to handle data management and user authentication.
Build an intuitive and responsive frontend using React to provide a seamless user experience.
Integrate key features such as user profiles, posts, comments, likes, personal records, and weight calulation.

### Timeline
- Iteration 1: Backend setup and initial development

  - Set up backend repository.
  - Configure Django Rest Framework for the backend.
  - Set up initial project structure and environment configurations.

- Iteration 2: Finish the backend

  - Implement user registration, login, and logout functionality.
  - Develop user profile creation and editing features.
  - Ensure secure password handling and authentication processes.
  - Develop the functionality for creating, editing, and deleting posts.
  - Implement comments and likes features for posts.
  - Develop personal records features, including creation and management.

- Iteration 3: Backend Bugs solving
  - Going through the backend to solve any bugs and make sure deployment is ok with final settings.

- Iteration 4: Front-end setup

  - Integrate backend API with the frontend.
  - Develop responsive and user-friendly UI components.
  - Apply consistent styling using CSS modules or a CSS framework.

- Iteration 5: Implementing features

  - Develop features for the frontend to retrieve data from backend: Profile, Personal Records, Posts, Comments, Likes  
  - Perform user acceptance testing (UAT) to ensure the platform meets user needs.

- Iteration 6: General testing, bug solving, documentation and final steps

  - Conduct Testing and documentation of all features for backend and frontend.
  - Fix any bugs or issues identified during testing.
  - Going through the frontend to solve any bugs and make sure deployment is ok with final settings.
  - Final deploy of the backend API to a cloud service (e.g., Heroku).
  - Final deploy of the frontend application to a hosting service (e.g., Heroku).
  - Write comprehensive documentation, including setup instructions, API documentation, and user guides.

## Data Models
The Chalk Talk backend project is organized into several key models, each representing different aspects of the Chalk Talk platform. Below is an overview of the primary data models used in the project:

### 1. Profile Model
**Profile:** Stores user-specific information such as username, password, profile image, bio, name and crossfit_experience.

**Fields:**

- owner: ForeignKey to the User model
- created_at: DateTimeField
- updated_at: DateTimeField
- name: CharField
- bio: TextField
- image: ImageField
- crossfit_experience: CharField

### 2. Post Model
**Post:** Represents user-generated content, including fields for the title, content, image, creation date, and owner.

**Fields:**

- owner: ForeignKey to the User model
- created_at: DateTimeField
- updated_at: DateTimeField
- title: CharField
- content: TextField
- image: ImageField
- image_filter: CharField

### 3. Comment Model
**Comment:** Allows users to comment on posts, with fields for the content, creation date, post it belongs to, and owner.

**Fields:**

- owner: ForeignKey to the User model
- post: ForeignKey
- created_at: DateTimeField
- updated_at: DateTimeField
- content: TextField

### 4. Likes Model
**Like:** Tracks which users have liked a particular post.

**Fields:**

- owner: ForeignKey to the User model
- post: ForeignKey
- created_at: DateTimeField

### 5. Follower Model
**Follower:** Manages follower-following relationships between users.

**Fields:**

- owner: ForeignKey to the User model
- followed: ForeignKey
- created_at: DateTimeField

### 6. Personal Record Model
**PersonalRecord:** Represents user-generated content, including fields for owner, exercise, weight, reps, date_achieved and notes.

**Fields:**

- owner: ForeignKey to the User model
- exercise: CharField
- weight: DecimalField
- reps: IntegerField
- date_achieved: DateTimeField
- notes: TextField

## API Endpoints
The Chalk Talk backend provides a RESTful API to interact with the various models. Below is a list of the primary API endpoints for each model, including their respective HTTP methods and descriptions. It covers all the major functionalities such as user authentication, profiles, posts, comments, likes, followers and personal records.

| Endpoint | HTTP Method | CRUD Operation | View Type | Description |
|----------|-------------|----------------|-----------|-------------|
| **Authentication Endpoints** | | | | |
| `/dj-rest-auth/login/` | POST | Create | Auth | Log in a user and obtain authentication tokens. |
| `/dj-rest-auth/logout/` | POST | Delete | Auth | Log out a user and invalidate their authentication tokens. |
| `/dj-rest-auth/registration/` | POST | Create | Auth | Register a new user. |
| **Profile Endpoints** | | | | |
| `/profiles/` | GET | Read | List | Retrieve a list of profiles. |
| | POST | Create | Create | Create a new profile (admin only). |
| `/profiles/<id>/` | GET | Read | Detail | Retrieve a specific profile by ID. |
| | PUT | Update | Update | Update a specific profile by ID. |
| | PATCH | Update | Partial Update | Partially update a specific profile by ID. |
| | DELETE | Delete | Delete | Delete a specific profile by ID (admin only). |
| **Post Endpoints** | | | | |
| `/posts/` | GET | Read | List | Retrieve a list of posts. |
| | POST | Create | Create | Create a new post. |
| `/posts/<id>/` | GET | Read | Detail | Retrieve a specific post by ID. |
| | PUT | Update | Update | Update a specific post by ID. |
| | PATCH | Update | Partial Update | Partially update a specific post by ID. |
| | DELETE | Delete | Delete | Delete a specific post by ID. |
| **Comment Endpoints** | | | | |
| `/comments/` | GET | Read | List | Retrieve a list of comments. |
| | POST | Create | Create | Create a new comment. |
| `/comments/<id>/` | GET | Read | Detail | Retrieve a specific comment by ID. |
| | PUT | Update | Update | Update a specific comment by ID. |
| | PATCH | Update | Partial Update | Partially update a specific comment by ID. |
| | DELETE | Delete | Delete | Delete a specific comment by ID. |
| **Like Endpoints** | | | | |
| `/likes/` | GET | Read | List | Retrieve a list of likes. |
| | POST | Create | Create | Create a new like. |
| `/likes/<id>/` | DELETE | Delete | Delete | Delete a specific like by ID. |
| **Follower Endpoints** | | | | |
| `/followers/` | GET | Read | List | Retrieve a list of followers. |
| | POST | Create | Create | Follow a user. |
| `/followers/<id>/` | DELETE | Delete | Delete | Unfollow a user by ID. |
| **PersonalRecords Endpoints** | | | | |
| `/personalrecords/` | GET | Read | List | Retrieve a list of personal records. |
| | POST | Create | Create | Create a new personal record. |
| `/personalrecords/<id>/` | GET | Read | Detail | Retrieve a specific personal record by ID. |
| | PUT | Update | Update | Update a specific personal record by ID. |
| | PATCH | Update | Partial Update | Partially update a specific personal record by ID. |
| | DELETE | Delete | Delete | Delete a specific personal record by ID. |

## Frameworks, Libraries, and Dependencies
The Chalk Talk project leverages a variety of frameworks, libraries, and dependencies to ensure robust functionality and performance. Below is a detailed list of the key components used:

### Django Framework and Extensions
- **Django** (Django==4.2):

  - A high-level Python web framework that encourages rapid development and clean, pragmatic design. Django handles much of the complexity of web development.

- **Django REST Framework** (djangorestframework==3.15.2):

  - A powerful and flexible toolkit for building Web APIs in Django. It provides various features such as serialization, authentication, and view sets that simplify API development.

- **Django Allauth** (django-allauth==0.54.0):

  - Integrated set of Django applications addressing authentication, registration and account management.

- **Django REST Auth** (dj-rest-auth==2.1.9):

  - Provides a set of REST API endpoints for handling user registration and authentication tasks. It’s built on top of Django Allauth and Django REST Framework.

- **Django Filter** (django-filter==24.3):

  - Simplifies the process of filtering querysets in Django REST Framework.

- **Django CORS Headers** (django-cors-headers==4.6.0):

  - A Django app for handling the server headers required for Cross-Origin Resource Sharing (CORS).

### Database Management
- **dj-database-url** (dj-database-url==0.5.0):

  - Allows you to utilize the DATABASE_URL environment variable to configure your Django application.

- **psycopg2** (psycopg2==2.9.10):

  - PostgreSQL database adapter for Python.

### Authentication and Security
- **djangorestframework-simplejwt** (djangorestframework-simplejwt==5.3.1):

  - Provides JSON Web Token (JWT) authentication for Django REST Framework.

- **oauthlib** (oauthlib==3.2.2):

  - A generic, spec-compliant, thorough implementation of the OAuth request-signing logic for Python.

- **requests-oauthlib** (requests-oauthlib==2.0.0):

  - OAuthlib support for Python-Requests, the ubiquitous HTTP library for Python.

- PyJWT (PyJWT==2.9.0):

  - A Python library which allows you to encode and decode JSON Web Tokens (JWT).

### Storage and Image Handling
- **pillow** (pillow==11.0.0):

  - Python Imaging Library (PIL) fork that supports opening, manipulating, and saving many different image file formats.

- **Cloudinary** (cloudinary==1.41.0):

  - A library that integrates your application with the Cloudinary service for managing media assets such as images.

- **django-cloudinary-storage** (django-cloudinary-storage==0.3.0):

  - Facilitates the integration of Django with Cloudinary for storing media files.

### Application Server
- **Gunicorn** (gunicorn==23.0.0):

  - A Python WSGI HTTP Server for UNIX that serves your Django application and allows it to handle multiple requests simultaneously.

### Utility Libraries
- **asgiref** (asgiref==3.8.1):

  - A reference implementation of ASGI, the emerging Python standard for asynchronous web servers and applications.

- **sqlparse** (sqlparse==0.5.1):

  - A non-validating SQL parser for Python.

- **python3-openid** (python3-openid==3.2.0):

  - A set of Python packages to support OpenID authentication.

- **pytz** (pytz==2024.2):

  - World timezone definitions, modern and historical.

This combination of frameworks, libraries, and dependencies ensures that Chalk Talk is robust, scalable, and secure, providing a seamless user experience. 


## Testing and Validation
For all testing and validation, please refer to the [TESTING.md](./TESTING.md) file.

## Bugs
### Solved Bugs
- **Bug:** All records were always fetched regardless of the user profile being viewed
  - **Fix:** Pass the user ID to the PersonalRecordList in the frontend and use it in the API call.
### Remaining Bugs
- I am not aware of any remaining bugs.

## Deployment
The Chalk Talk project leverages a combination of platforms and services to facilitate its development, deployment, and management.

For version control and collaborative development, GitHub is used to host the project repository, enabling efficient code management and team collaboration. 
GitPod, a cloud-based integrated development environment (IDE), is utilized for coding and testing, providing a consistent and easily accessible development environment.

For hosting and running the application, Heroku, a cloud platform as a service (PaaS), is utilized. It enables seamless deployment, automatic scaling, and management tools for monitoring and maintaining the application.

The Code Institute (CI) database system, which uses PostgreSQL, is employed to store and manage the application's data during development and deployment phases. PostgreSQL is a powerful, open-source object-relational database system that provides robust data management capabilities for the project.

Additionally, Cloudinary, a cloud-based service, is integrated to handle image management, providing an end-to-end solution for storing, optimizing, and delivering media assets for the Chalk Talk platform.

The respective URLs for these platforms and services are as follows:

### GitHub
- **Purpose:** Version control and collaboration.
- **Process:** 
  - The source code for Chalk Talk DRF API is hosted on GitHub. Developers can collaborate, track changes, and manage different versions of the application.
  - The repository is used as the central hub for the project, where all updates and changes are committed and pushed.
- **URL:** [GitHub Repository](https://github.com/SophieTiger/chalk-talk-api)

### Gitpod
- **Purpose:** Online IDE for development.
- **Process:** 
  - Gitpod is used for development and testing. It provides a cloud-based development environment that is pre-configured with the necessary tools and dependencies.
  - Developers can open the GitHub repository in Gitpod and start coding immediately without worrying about local setup.
  - Git commands were used throughout the development to push the code to the Github remote repository. The following git commands were used:
    - git add . - to add the files to the staging area before being committed.
    - git commit -m "commit message" - to commit changes to the local repository queue that are ready for the final step.
    - git push - to push all committed code to the remote repository on Github.
- **URL:** [Gitpod](https://gitpod.io/)

### Heroku
- **Purpose:** Platform as a Service (PaaS) for hosting the application.
- **Process:** 
  - The Chalk Talk DRF API application is deployed on Heroku. Heroku manages the server, deployment, and scaling of the application.
- **URL:** [Heroku Dashboard](https://dashboard.heroku.com/)
- **Setting up on Heroku:** 
  - Create a new app on Heroku.
  - Connect the Heroku app to the GitHub repository.
  - Set up Config Vars in Heroku including DATABASE_URL, SECRET_KEY, CLOUDINARY_URL, ALLOWED_HOST and DISABLE_COLLECTSTATIC=1 (this is temporary and can be removed for the final deployment).
  - Deploy the main branch using the Heroku dashboard or enable automatic deployments for every push to the main branch.

**For deployment, Heroku needs two additional files in order to deploy properly:**
- requirements.txt
- Procfile

**You can install this project's requirements (where applicable) using:**

- `pip install -r requirements.txt`

**If you have your own packages that have been installed, then the requirements file needs to be updated using:**

- `pip freeze --local > requirements.txt`

**The Procfile can be created with the following command:**
  
  - `echo web: gunicorn app_name.wsgi > Procfile` 

**Then add these lines to Procfile**

- `web: gunicorn app_name.wsgi`

- `release: python manage.py makemigrations && python manage.py migrate`

Replace `app_name` with the name of your primary Django app name; the folder where `settings.py` is located.


### CI Database
- **Database Hosting:** The Code Institute (CI) provides PostgreSQL-based database systems specifically for students to use during the development and deployment phases of their projects. PostgreSQL, known for its robustness and reliability, is an advanced, open-source relational database system. It is well-suited for handling complex queries and large volumes of data, making it an excellent choice for web applications.

- **Development Phase:** During development, the CI database allows students to efficiently store, retrieve, and manipulate data required for their applications. It supports various data types and advanced features such as indexing, transactions, and concurrency control, ensuring smooth and effective development processes.

- **Deployment Phase:** When it comes to deployment, the CI database continues to serve as a reliable backend for the application. Students can leverage the database’s capabilities to manage user data, application state, and other critical information with high availability and performance.

- **Accessibility:** The CI database systems are accessible to Code Institute students, providing a consistent and stable environment for learning and project development. This ensures that students have a standardized platform to practice and implement database management techniques, which are crucial skills in the field of web development.

- **Integration:** The PostgreSQL databases provided by CI can be seamlessly integrated with various web frameworks and technologies taught in the course, such as Django. This integration enables students to implement real-world applications with database-driven functionality.

- **To obtain your own PostgreSQL Database:**
  - Download the PostgreSQL installer from the official website. You can visit the official [PostgreSQL download page](https://www.postgresql.org/download/) to find the appropriate installer for your system
  - Run the installer and follow the installation wizard:
    - Choose components to install (at minimum, PostgreSQL Server and Command Line Tools)
    - Select installation directory
    - Set a password for the PostgreSQL superuser (postgres)
    - Choose the port number (default is 5432)
    - Select the locale for the database
  - After installation, you can connect to the database using:
    - SQL Shell (psql): A command-line tool for executing SQL statements
    - pgAdmin: A graphical user interface for managing PostgreSQL databases
  - To create a new database, you can:
    - Use the CREATE DATABASE SQL command in psql
    - Use pgAdmin's graphical interface to create a database
  - Once connected, you can start creating schemas, tables, and working with your database.


### Cloudinary
- **Purpose:** Media management and storage.
- **Process:** Cloudinary is used for storing and managing media files, such as images and videos uploaded by users.
The application is configured to upload media files directly to Cloudinary, where they are stored and served.
- **URL:** [Cloudinary Dashboard](https://cloudinary.com/users/login)
- **Integration:** 
  - Set up a Cloudinary account.
  - Configure the Cloudinary settings in the Django settings file with the API keys provided by Cloudinary.
  - Use Django’s storage backend for Cloudinary to handle media uploads.

## Deployment Steps
- **Clone the Repository:** Clone the GitHub repository to your local machine or open it in Gitpod for development.

- **Configure Environment Variables:** Set up the necessary environment variables in your local .env file or in the Heroku dashboard. These include database URL, Cloudinary API keys, and other sensitive information.

- **Install Dependencies:** Install the required dependencies using `pip install -r requirements.txt`.

- **Run Migrations:** Apply database migrations using python manage.py migrate to set up the PostgreSQL database schema.

- **Test the Application:** Run the application locally or in Gitpod to ensure it works as expected.

- **Deploy to Heroku:** 
  - Push the changes to the GitHub repository, which triggers the continuous deployment to Heroku.
  - Ensure that the Heroku app is properly configured with the necessary environment variables and add-ons.

- **Manage Media Files:** Configure Cloudinary in the Django settings and ensure that media files are uploaded and managed correctly.

## Cloning and Forking
### Cloning the Repository
**Local Setup:**

- Clone the repository: GitHub repository.
  - `git clone https://github.com/SophieTiger/chalk-talk-api.git`
  - Navigate into the project directory: `cd chalk-talk-api`
  - Install dependencies: `pip install -r requirements.txt`
  - Set up local environment variables in a `.env` file.
  - Run migrations: `python manage.py makemigrations` and `python manage.py migrate`
  - Start the development server: `python3 manage.py runserver`

### Forking the Repository
**For Contributions:**
- Fork the repository on [GitHub repository](https://github.com/SophieTiger/chalk-talk-api).
- Clone your forked repository to your local machine.
- Follow the local setup steps as above.
- Make changes and push them back to your fork.
- Create a pull request from your fork back to the original repo.

By following these steps and utilizing the aforementioned platforms, the deployment and management of the Chalk Talk DRF API application are streamlined and efficient, ensuring a robust and scalable application.


## Future Features
In future iterations of this project, it would be beneficial to implement the following features:
- **Profile deletion:** This feature would enhance user autonomy, giving them the ability to manage their presence on the platform more effectively.
- **Programs:** Add programs for Personal training, Bootcamps and Nutrition Coaching to the app according to business needs.
- **Bookings:** Add booking functionality for programs.
- **Notifications:** To let users know when interaction was made to their content, such as likes and comments.
- **Search field for personal records:** To allow users with many PR's to search their records.

## Credits
### Code
The following blogs/tutorials complemented my learning for this project:

- [Django Documentation](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Django Rest Framework JWT Documentation](https://jpadilla.github.io/django-rest-framework-jwt/)
- [Setting up basic Django Project with Cloudinary](https://docs.google.com/document/d/1LCLxWhmW_4VTE4GXsnHgmPUwSPKNT4KyMxSH8agbVqU/edit#heading=h.mpopj7v69qqn)
- Code Institute Moments Walkthrough project

### Media
The following sites were used to gather the photographic media used:

- [Pexels](https://www.pexels.com/)
- [Freepik](https://www.freepik.com/)
- Code Institute for the profile placeholder image
- Chalk Talk Logo was created with [Canva](https://www.canva.com/create/logos/)

## Acknowledgements
The development of Chalk Talk has been a very hard but yet exciting journey, and I am grateful for the inspiration, guidance, and resources that have contributed to the project.

### Inspiration
The Chalk Talk project draws inspiration from two main sources:

- [CHALK IT PRO](https://www.chalkitpro.com/) and their functionality to add personal scores and percentage count.
- **Moments**: This is a walkthrough project provided by Code Institute as part of the PP5 Advanced Frontend curriculum. Moments serves as a foundation, offering a social media-like platform structure. It provided the base for features such as user profiles, posts, comments, followers and likes.

By combining the social aspects of Moments with these fitness-specific features I wanted to create a community-centric approach to allow gyms to use this app to their daily business for comprehensive fitness tracking and community engagement with a personal touch.

### Project Guidance
Moments DJANGO REST DRF API and Moments REACT Walkthrough Project I utilized the Moments Walkthrough Project as a foundational guide. This project provided valuable insights into structuring the application, implementing various features, and ensuring a seamless user experience. The Moments project had several ideas and functionalities similar to what I envisioned for Chalk Talk, which helped streamline my development process.

### README Structure
- The structure and format of the README file was inspired by some fellow students projects: [AmirShkolnik](https://github.com/AmirShkolnik/DivingCenter), [raneem-yad](https://github.com/raneem-yad/wissen) and [SwathiKeshavamurthy](https://github.com/SwathiKeshavamurthy/FitandFine-P5) . The detailed and organized presentation of information in their ReadMe served as a great example for documenting Chalk Talk.
- My own PP4 [Fitness Recipes](https://github.com/SophieTiger/fitness-recipes). This project provided valuable insights into structuring the application, implementing various features, and ensuring a seamless user experience.

### Personal Thanks
- Thanks to my Code Institute mentor, Spencer Bariball, for supporting me in times of need and giving invaluable guidance on this challenging journey!
- Thanks to Kristyna, Cohort facilitator at Code Institute, for always being there to provide all the information needed and for keeping the positive energy up in times of dispare.
- Thanks to my cohort fellow students for all the wise words and for giving invaluable support on this journey.
- Thanks to my family for beliving in me when I lack confidence.

[Back to top](#top)