
# Image gallery

Simple image gallery for storing images with tags

##  Built in
- Django 
- Django Rest Framework 
- Docker


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

See sample .env file
## Run Locally

Clone the project

```bash
  git clone https://github.com/Persepha/image-gallery.git
```

Go to the project directory

```bash
  cd image-gallery
```

Build the images and run the containers:

```bash
  docker compose -f docker-compose.local.yml up -d --build
```

Test it out at http://localhost:8000. The "app" folder is mounted into the container and your code changes apply automatically.


## Related

Here are some related projects

Front end part of project

[Frontend image gallery](https://github.com/Persepha/image-gallery-frontend)


## API Reference

### Users API

#### Get all users

```http
  GET /auth/users/
```

#### Get user profile info

```http
  GET /auth/users/${username}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`      | `string` | **Required**. Username to fetch |

#### Get authorized user`s profile

```http
  GET /auth/user/
```

#### Register user

```http
  POST /auth/registration/
```

| Data | Type     | Description     |
| :-------- | :------- | :------- |
| `username`      | `string` | **Required**     |
| `password1`      | `string` | **Required**     |
| `password2`      | `string` | **Required**     |
| `email`      | `string` |    |

#### Login user

```http
  POST /auth/login/
```

| Data | Type     | Description     |
| :-------- | :------- | :------- |
| `username`      | `string` | **Required**     |
| `password`      | `string` | **Required**     |


#### Logout user

```http
  POST /auth/logout/
```

### Gallery API

#### Get all images from gallery

```http
  GET /api/v1/images/
```

#### Create image

```http
  POST /api/v1/images/create/
```

| Data | Type     | Description     |
| :-------- | :------- | :------- |
| `name`      | `string` | **Required**     |
| `url`      | `url` | **Required**     |
| `slug`      | `slug` |      |
| `tags`      | `string` |     |


#### Get image detail info

```http
  GET /api/v1/images/${slug}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `slug`      | `slug` | **Required**. Image slug to fetch |


#### Update image info

```http
  POST /api/v1/images/${slug}/update/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `slug`      | `slug` | **Required**. Image slug to update |

| Data | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` |   |
| `url`      | `url` |     |
| `slug`      | `slug` |      |
| `tags`      | `string` |     |


#### Delete image

```http
  DELETE /api/v1/images/${slug}/delete/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `slug`      | `slug` | **Required**. Image slug to delete |