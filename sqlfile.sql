#Create database nsewebnfo;
#use nsewebnfo;
#CREATE TABLE NIFTY (INSTRUMENT text,SYMBOL text,EXPIRY_DT text,STRIKE_PR real,OPTION_TYP text,OPEN real,HIGH real,LOW real,CLOSE real,SETTLE_PR real,CONTRACTS real,VAL_INLAKH real,OPEN_INT real,CHG_IN_OI real,TIMESTAMP text)
#create database nsewebdata;
#use nsewebdata;
#CREATE table fo01APR2010bhav (INSTRUMENT text,SYMBOL text,EXPIRY_DT text,STRIKE_PR real,OPTION_TYP text,OPEN real,HIGH real,LOW real,CLOSE real,SETTLE_PR real,CONTRACTS real,VAL_INLAKH real,OPEN_INT real,CHG_IN_OI real,TIMESTAMP text)
#select count(*) from nifty;
SET @rank=0;
SELECT @rank:=@rank+1 AS rank,
TABLE_NAME,substr(TABLE_NAME,3,9) as fulldate,
		substr(TABLE_NAME,3,2) as daypart,
		substr(TABLE_NAME,5,3) as monthpart ,
		substr(TABLE_NAME,8,4) as yearpart ,
        IF(substr(TABLE_NAME,5,3) = 'JAN', 1, 
        IF(substr(TABLE_NAME,5,3) = 'FEB', 2,
        IF(substr(TABLE_NAME,5,3) = 'MAR', 3,
        IF(substr(TABLE_NAME,5,3) = 'APR', 4,
        IF(substr(TABLE_NAME,5,3) = 'MAY', 5, 
        IF(substr(TABLE_NAME,5,3) = 'JUN', 6,
        IF(substr(TABLE_NAME,5,3) = 'JUL', 7,
        IF(substr(TABLE_NAME,5,3) = 'AUG', 8,
        IF(substr(TABLE_NAME,5,3) = 'SEP', 9, 
        IF(substr(TABLE_NAME,5,3) = 'OCT', 10,
        IF(substr(TABLE_NAME,5,3) = 'NOV', 11,
        IF(substr(TABLE_NAME,5,3) = 'DEC', 12,0)))))))))))) as monthnum,
		TABLE_ROWS
     FROM INFORMATION_SCHEMA.TABLES 
     WHERE TABLE_SCHEMA = 'nsewebdata'
     order by yearpart,monthnum,daypart;
