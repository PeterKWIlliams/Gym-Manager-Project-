DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS staff;
DROP TABLE IF EXISTS members;

CREATE TABLE staff(
   id SERIAL NUMBER KEY 
   first_name VARCHAR(255),
   last_name VARCHAR(255),
   postion VARCHAR(255)
   type VARCHAR(255)
);
CREATE TABLE members(
   
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),

);


CREATE TABLE classes(
   id SERIAL NUMBER KEY, 
   staff_id SERIAL REFERENCES staff(id),
   name VARCHAR(255),
   duration VARCHAR(255)



);
CREATE TABLE bookings(
   id SERIAL NUMBER KEY
   member_id SERIAL REFERENCES member(id)
   classes_id SERIAL REFERENCES classes(id)

);
                 
                                                                              