#### Airbnb Clone Practise

adding mysql
We have 6 tables.

User has one to many relationship with place
User has one to many relationship with review
place has one to many relationship with review
city has one to many relationship with place
state has one to many relationship with city
placeamenity will be a table created later on, it has one to many relationship with place and amenity

Note:

<ol>
    <li> A user can have many places (many airbnbs at different places) </li>
    <li> A user can write many reviews </li>
    <li> A place can have one owner (user) </li>
    <li> A place can have many reviews </li>
    <li> A city can many places </li>
    <li> A state can have many cities </li>
    <li> placeamenity table is created with place id primary key amd amenity primary key compound key, it has one to many relationship with place and amenity </li>

</ol>
