create table mkb(
	id SERIAL PRIMARY KEY,
	code VARCHAR(28) NOT NULL,
	name VARCHAR(250) NOT NULL);


create table rbSpeciality(
	id SERIAL PRIMARY KEY,
	code VARCHAR(28) NOT NULL,
	name VARCHAR(250) NOT NULL);


create table rbService(
	id SERIAL PRIMARY KEY,
	code VARCHAR(28) NOT NULL,
	name VARCHAR(450) NOT NULL);