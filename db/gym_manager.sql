DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS gym_classes;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS staff;

CREATE TABLE staff(
   id SERIAL NUMBER KEY 
   first_name VARCHAR(255),
   last_name VARCHAR(255),
   job_postion VARCHAR(255),
   
);

CREATE TABLE members(
   
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    date_of_birth VARCHAR(255),
    gender VARCHAR(255),
    notes TEXT,
    contact_info_email VARCHAR(255),
    contact_info_number VARCHAR(255),
    membership_type VARCHAR(255)
    );


CREATE TABLE gym_classes(
   id SERIAL NUMBER KEY, 
   class_name VARCHAR(255),
   duration VARCHAR(255),
   staff_id SERIAL REFERENCES staff(id)



);

CREATE TABLE bookings(
   id SERIAL NUMBER KEY
   member_id SERIAL REFERENCES member(id)
   gym_classes_id SERIAL REFERENCES gym_classes(id)

);
                 
                                                                              