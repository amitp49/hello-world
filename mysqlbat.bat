@echo off
for /f %%f in ('dir /b C:\Users\amitp49\Downloads\Unzip') do (
	echo %%~nf
	mysql -e "use nsewebdata; CREATE table  %%~nf (INSTRUMENT text,SYMBOL text,EXPIRY_DT text,STRIKE_PR real,OPTION_TYP text,OPEN real,HIGH real,LOW real,CLOSE real,SETTLE_PR real,CONTRACTS real,VAL_INLAKH real,OPEN_INT real,CHG_IN_OI real,TIMESTAMP text);" -u root --password=root
	mysql -e "use nsewebdata; LOAD DATA LOCAL INFILE 'C:\\Users\\amitp49\\Downloads\\Unzip\\%%~nf.csv' INTO TABLE %%~nf fields TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES;" -u root --password=root
)
