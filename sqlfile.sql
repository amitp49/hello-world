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
        CONVERT(substr(TABLE_NAME,3,2),UNSIGNED INTEGER) AS daynum,
        CONVERT(substr(TABLE_NAME,8,4),UNSIGNED INTEGER) AS yearnum,
		TABLE_ROWS
     FROM INFORMATION_SCHEMA.TABLES 
     WHERE TABLE_SCHEMA = 'nsewebdata'
     order by yearpart,monthnum,daypart;


#SELECT * FROM nsewebdata.fo04MAY2009bhav where symbol='BANKNIFTY' and INSTRUMENT='OPTIDX' and EXPIRY_DT like '%MAY%' and OPEN!=0 and
#OPTION_TYP = "PE" and 
#STRIKE_PR < (SELECT OPEN FROM nsewebdata.fo04MAY2009bhav where symbol='BANKNIFTY' and INSTRUMENT='FUTIDX' and EXPIRY_DT like '%MAY%') and
#STRIKE_PR > (SELECT OPEN FROM nsewebdata.fo04MAY2009bhav where symbol='BANKNIFTY' and INSTRUMENT='FUTIDX' and EXPIRY_DT like '%MAY%') - 200
#order by STRIKE_PR desc;

UPDATE `nsewebdata`.`expiry`
SET
Date =REPLACE(Date,'/','-');


SELECT * FROM nsewebdata.fo18MAY2005bhav where symbol='NIFTY' and EXPIRY_DT like '%MAY%';

#SELECT * FROM nsewebdata.fo04MAY2009bhav where symbol='BANKNIFTY' and INSTRUMENT='OPTIDX' and EXPIRY_DT like '%MAY%' and OPEN!=0 and
#OPTION_TYP = "CE" and 
#STRIKE_PR > (SELECT OPEN FROM nsewebdata.fo04MAY2009bhav where symbol='BANKNIFTY' and INSTRUMENT='FUTIDX' and EXPIRY_DT like '%MAY%') and
#STRIKE_PR < (SELECT OPEN FROM nsewebdata.fo04MAY2009bhav where symbol='BANKNIFTY' and INSTRUMENT='FUTIDX' and EXPIRY_DT like '%MAY%') + 200
#order by STRIKE_PR desc;


SELECT STRIKE_PR,OPEN,CLOSE,CLOSE-OPEN FROM nsewebdata.fo03oct2016bhav where symbol='BANKNIFTY' and INSTRUMENT='OPTIDX' and EXPIRY_DT like '%oct%' and OPEN!=0 and             OPTION_TYP = 'CE' and             STRIKE_PR > 19511.15 and             STRIKE_PR < 19631.15             order by STRIKE_PR desc

SELECT SUBSTRING_INDEX( Date, '-', 1 ),
SUBSTRING(SUBSTRING_INDEX(Date, '-', 2),CHAR_LENGTH(SUBSTRING_INDEX(Date, '-', 1))+2),
SUBSTRING_INDEX( Date, '-', -1 ),
Date from nsewebdata.expiry;

update nsewebdata.expiry
set
Datepart =  SUBSTRING_INDEX( Date, '-', 1 ),
Monthpart = SUBSTRING(SUBSTRING_INDEX(Date, '-', 2),CHAR_LENGTH(SUBSTRING_INDEX(Date, '-', 1))+2),
Yearpart = SUBSTRING_INDEX( Date, '-', -1 )
where Datepart=0;

SELECT CONCAT(LPAD(SUBSTRING_INDEX( Date, '-', 1 ), 2, '0'), "-" , 
		IF(SUBSTRING(SUBSTRING_INDEX(Date, '-', 2),CHAR_LENGTH(SUBSTRING_INDEX(Date, '-', 1))+2) = 1, 'Jan',
        IF(SUBSTRING(SUBSTRING_INDEX(Date, '-', 2),CHAR_LENGTH(SUBSTRING_INDEX(Date, '-', 1))+2) = 2,'Feb',
        IF(SUBSTRING(SUBSTRING_INDEX(Date, '-', 2),CHAR_LENGTH(SUBSTRING_INDEX(Date, '-', 1))+2) = 3,'Mar', 
        IF(SUBSTRING(SUBSTRING_INDEX(Date, '-', 2),CHAR_LENGTH(SUBSTRING_INDEX(Date, '-', 1))+2) = 4,'Apr', 
        IF(SUBSTRING(SUBSTRING_INDEX(Date, '-', 2),CHAR_LENGTH(SUBSTRING_INDEX(Date, '-', 1))+2) = 5,'May',  
        IF(SUBSTRING(SUBSTRING_INDEX(Date, '-', 2),CHAR_LENGTH(SUBSTRING_INDEX(Date, '-', 1))+2) = 6,'Jun', 
        IF(SUBSTRING(SUBSTRING_INDEX(Date, '-', 2),CHAR_LENGTH(SUBSTRING_INDEX(Date, '-', 1))+2) = 7,'Jul', 
        IF(SUBSTRING(SUBSTRING_INDEX(Date, '-', 2),CHAR_LENGTH(SUBSTRING_INDEX(Date, '-', 1))+2) = 8,'Aug', 
        IF(SUBSTRING(SUBSTRING_INDEX(Date, '-', 2),CHAR_LENGTH(SUBSTRING_INDEX(Date, '-', 1))+2) = 9,'Sep',  
        IF(SUBSTRING(SUBSTRING_INDEX(Date, '-', 2),CHAR_LENGTH(SUBSTRING_INDEX(Date, '-', 1))+2) = 10,'Oct', 
        IF(SUBSTRING(SUBSTRING_INDEX(Date, '-', 2),CHAR_LENGTH(SUBSTRING_INDEX(Date, '-', 1))+2) = 11,'Nov',
        IF(SUBSTRING(SUBSTRING_INDEX(Date, '-', 2),CHAR_LENGTH(SUBSTRING_INDEX(Date, '-', 1))+2) = 12, 'Dec','XXX')))))))))))) ,
        "-",SUBSTRING_INDEX( Date, '-', -1 )),
        Date FROM nsewebdata.expiry;
