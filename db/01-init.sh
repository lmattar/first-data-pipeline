#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER"  <<-EOSQL
    CREATE USER jjoo;
    CREATE DATABASE jjoo;
    GRANT ALL PRIVILEGES ON DATABASE jjoo TO jjoo;

	CREATE TABLE public.countries
	(
	    country character varying,
	    code character varying,
	    population numeric,
	    gdppc numeric,
	    CONSTRAINT pk_table PRIMARY KEY (code)
	);


	CREATE TABLE public.medals
	(
	    Year numeric,
	    City character varying,
	    Sport character varying,
	    Discipline character varying,
	    Athlete character varying,
	    Country character varying,
	    Gender character varying,
	    Event  character varying,
	    Medal  character varying, 	
	    CONSTRAINT pk_table_medals PRIMARY KEY (Year,Discipline,Athlete,Medal),
	    CONSTRAINT fk_countries FOREIGN KEY (Country)
		REFERENCES public.countries (code)
	);

