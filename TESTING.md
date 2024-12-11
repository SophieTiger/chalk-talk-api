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
| /dj-rest-auth/login/ | POST | Create | Log in a user and obtain authentication tokens | User logged in, tokens returned | User logged in, tokens returned | PASS |
| /dj-rest-auth/logout/ | POST | Delete | Log out a user and invalidate tokens | User logged out, tokens invalidated | User logged out, tokens invalidated | PASS |
| /dj-rest-auth/registration/ | POST | Create | Register a new user | User registered, details returned | User registered, details returned | PASS |

### Profile Endpoints
### Post Endpoints
### Comment Endpoints
### Daily Routine Endpoints
### Like Endpoints
### Follower Endpoints
### Personal Records Endpoints
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