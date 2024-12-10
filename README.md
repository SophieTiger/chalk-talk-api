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
  - [Example Requests and Responses](#example-requests-and-responses)
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
### Example Requests and Responses

## Frameworks, Libraries, and Dependencies
### Django Framework and Extensions
### Database Management
### Authentication and Security
### Storage and Image Handling
### Application Server
### Utility Libraries

## Testing and Validation
For all testing and validation, please refer to the [TESTING.md](./TESTING.md) file.

## Bugs
### Solved Bugs
### Known Bugs
### Unknown Bugs

## Deployment
1. GitHub
2. Gitpod
3. Heroku
4. PostGresSQL
5. Cloudinary
### Deployment Steps

## Cloning and Forking
### Cloning the Repository
### Forking the Repository

## Credits
### Code
### Media

## Acknowledgements
### Inspiration
### Project Guidance
### Personal Thanks

[Back to top](#top)