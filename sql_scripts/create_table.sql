create table if not exists mkb(
	id SERIAL PRIMARY KEY,
	code VARCHAR(28) NOT NULL,
	name VARCHAR(250) NOT NULL);


create table if not exists rbSpeciality(
	id SERIAL PRIMARY KEY,
	code VARCHAR(28) NOT NULL,
	name VARCHAR(250) NOT NULL);


create table if not exists rbService(
	id SERIAL PRIMARY KEY,
	code VARCHAR(28) NOT NULL,
	name VARCHAR(450) NOT NULL);