0x00. AirBnB clone - The console

![The AirBnB](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240212%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240212T185439Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a255e39fa5668794dab5f1bb65d9cb5b0eeaca371d45792554defa1c9aa8dd2a)

Welcome to the AirBnB clone project!

Before starting, please read the AirBnB concept page.

This is a project done my partner Ryan Kibet and I.

First step: Write a command interpreter to manage our AirBnB objects.

- This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help us to:

- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine


We want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object
