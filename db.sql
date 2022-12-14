CREATE DATABASE quotation;
CREATE DATABASE quotation;
CREATE SCHEMA collection;
SET SCHEMA 'collection'

DROP TABLE IF EXISTS collection.euro;
CREATE TABLE collection.euro 
(
	id BIGINT NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	code varchar(255),
	codein varchar(255),
	"name" varchar(255),
	high decimal(10,4),
	low decimal(10,4),
	varBid decimal(10,4),
	pctChange decimal(10,4),
	bid decimal(10,4),
	ask decimal(10,4),
	"timestamp" varchar(255),
	create_date timestamp
);

-- TRUNCATE collection.euro;

SELECT
	*
FROM
	collection.euro;

