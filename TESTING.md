<p align="center">
  <img src="./documentation/chalk_logo_white.png" alt="Chalk Talk Logo" width="200"/>
</p>

<a name="top"></a>
# Chalk Talk DRF API Testing
This is the TESTING file for the [Chalk Talk Django Rest Framework API](https://chalk-talk-api-7f804e82f4b9.herokuapp.com/).

[Chalk Talk React Frontend Live Link](https://chalk-talk-react-444e4f93c93c.herokuapp.com/)

[Chalk Talk React Frontend Github Repo](https://github.com/SophieTiger/chalk-talk)

Return back to the [README.md](./README.md) file.

## Table of Contents


## Manual Testing
This document outlines the comprehensive testing process for Chalk Talk's backend API, built using Django REST Framework. The main goal of testing is to ensure that all parts of the API work correctly and securely. I've created a set of careful tests for each endpoint.
These tests check if users can access the right information, create and change their own data. I want to make sure that everyone can use the API as intended, whether they're adding a post, interacting with the community or creating personal records. By running these tests, I aim to catch any problems early and make the API reliable and user-friendly.

### Authentication Endpoints
| Endpoint | Method | CRUD Operation | Description | Expected Result | Actual Result | Pass/Fail |
|----------|--------|----------------|-------------|-----------------|---------------|-----------|
| `/dj-rest-auth/login/` | POST | Create | Log in a user and obtain authentication tokens | User logged in, tokens returned | User logged in, tokens returned | PASS |
| `/dj-rest-auth/logout/`| POST | Delete | Log out a user and invalidate tokens | User logged out, tokens invalidated | User logged out, tokens invalidated | PASS |
| `/dj-rest-auth/registration/` | POST | Create | Register a new user | User registered, details returned | User registered, details returned | PASS |

### Profile Endpoints
| Endpoint | Method | CRUD Operation | Description | Expected Result | Actual Result | Pass/Fail |
|----------|--------|----------------|-------------|-----------------|---------------|-----------|
| `/profiles/` | GET | Read | Retrieve a list of profiles | List of profiles returned | List of profiles returned | PASS |
| `/profiles/<id>/` | GET | Read | Retrieve a specific profile by ID | Profile details returned | Profile details returned | PASS |
| `/profiles/<id>/` | PUT | Update | Update a specific profile by ID | Profile updated, updated details returned | Profile updated, updated details returned | PASS |
| `/profiles/<id>/` | PATCH | Update | Partially update a specific profile by ID | Profile partially updated, updated details returned | Profile partially updated, updated details returned | PASS |

### Post Endpoints
| Endpoint | Method | CRUD Operation | Description | Expected Result | Actual Result | Pass/Fail |
|----------|--------|----------------|-------------|-----------------|---------------|-----------|
| `/posts/` | GET | Read | Retrieve a list of posts | List of posts returned | List of posts returned | PASS |
| `/posts/` | POST | Create | Create a new post | Post created, details returned | Post created, details returned | PASS |
| `/posts/<id>/` | GET | Read | Retrieve a specific post by ID | Post details returned | Post details returned | PASS |
| `/posts/<id>/` | PUT | Update | Update a specific post by ID | Post updated, updated details returned | Post updated, updated details returned | PASS |
| `/posts/<id>/` | PATCH | Update | Partially update a specific post by ID | Post partially updated, updated details returned | Post partially updated, updated details returned | PASS |
| `/posts/<id>/` | DELETE | Delete | Delete a specific post by ID | Post deleted | Post deleted | PASS |

### Comment Endpoints
| Endpoint | Method | CRUD Operation | Description | Expected Result | Actual Result | Pass/Fail |
|----------|--------|----------------|-------------|-----------------|---------------|-----------|
| `/comments/` | GET | Read | Retrieve a list of comments | List of comments returned | List of comments returned | PASS |
| `/comments/` | POST | Create | Create a new comment | Comment created, details returned | Comment created, details returned | PASS |
| `/comments/<id>/` | GET | Read | Retrieve a specific comment by ID | Comment details returned | Comment details returned | PASS |
| `/comments/<id>/` | PUT | Update | Update a specific comment by ID | Comment updated, updated details returned | Comment updated, updated details returned | PASS |
| `/comments/<id>/` | PATCH | Update | Partially update a specific comment by ID | Comment partially updated, updated details returned | Comment partially updated, updated details returned | PASS |
| `/comments/<id>/` | DELETE | Delete | Delete a specific comment by ID | Comment deleted | Comment deleted | PASS |

### Like Endpoints
| Endpoint | Method | CRUD Operation | Description | Expected Result | Actual Result | Pass/Fail |
|----------|--------|----------------|-------------|-----------------|---------------|-----------|
| `/likes/` | GET | Read | Retrieve a list of likes | List of likes returned | List of likes returned | PASS |
| `/likes/` | POST | Create | Create a new like | Like created, details returned | Like created, details returned | PASS |
| `/likes/<id>/` | DELETE | Delete | Delete a specific like by ID | Like deleted | Like deleted | PASS |

### Follower Endpoints
| Endpoint | Method | CRUD Operation | Description | Expected Result | Actual Result | Pass/Fail |
|----------|--------|----------------|-------------|-----------------|---------------|-----------|
| `/followers/` | GET | Read | Retrieve a list of followers | List of followers returned | List of followers returned | PASS |
| `/followers/` | POST | Create | Follow a user | Follow successful | Follow successful | PASS |
| `/followers/<id>/` | DELETE | Delete | Unfollow a user by ID | Unfollow successful | Unfollow successful | PASS |

### Personal Records Endpoints
| Endpoint | Method | CRUD Operation | Description | Expected Result | Actual Result | Pass/Fail |
|----------|--------|----------------|-------------|-----------------|---------------|-----------|
| `/personalrecords/` | GET | Read | Retrieve a list of personal records | List of personal records returned | List of personal records returned | PASS |
| `/personalrecords/` | POST | Create | Create a new personal record | Personal record created, details returned | Personal record created, details returned | PASS |
| `/personalrecords/<id>/` | GET | Read | Retrieve a specific personal record by ID | Personal record details returned | Personal record details returned | PASS |
| `/personalrecords/<id>/` | PUT | Update | Update a specific personal record by ID | Personal record updated, updated details returned | Personal record updated, updated details returned | PASS |
| `/personalrecords/<id>/` | PATCH | Update | Partially update a specific personal record by ID | Personal record partially updated, updated details returned | Personal record partially updated, updated details returned | PASS |
| `/personalrecords/<id>/` | DELETE | Delete | Delete a specific personal record by ID | Personal record deleted | Personal record deleted | PASS |

## Automated Testing
### Post API Tests
### Profile Model Tests
### Comment Model Tests
### Followers Model Tests
### Like Model Tests
### Personal Records Model Tests
### Running the Tests
## Python Validation
### chalk-talk-api Project Python Validation Results
### Profile Module Python Validation Results
### Posts Module Python Validation Results
### Comments Module Python Validation Results
### Followers Module Python Validation Results
### Likes Module Python Validation Results
### Personal Records Module Python Validation Results


[Back to top](#top)