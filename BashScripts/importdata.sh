#!bin/bash
    FILES="/Users/amitp/IdeaProjects/KiteProg/Mod1/Dump/Unzip2009/*"
    for f in $FILES
    do
        #unzip $f -d ../Dump/Unzip2001

        echo  ${f%.*} | rev | cut -d"/" -f1 | rev
        #mongoimport -d nsewebfno -c $(echo  ${f%.*} | rev | cut -d"/" -f1 | rev) --type csv --file "$f" --headerline
        sleep 0.1
        mysql -e "use nsewebdata; CREATE table $(echo  ${f%.*} | rev | cut -d"/" -f1 | rev) (INSTRUMENT text,SYMBOL text,EXPIRY_DT text,STRIKE_PR real,OPTION_TYP text,OPEN real,HIGH real,LOW real,CLOSE real,SETTLE_PR real,CONTRACTS real,VAL_INLAKH real,OPEN_INT real,CHG_IN_OI real,TIMESTAMP text)" -u root --password=root
        mysql  -e "USE nsewebdata; LOAD DATA LOCAL INFILE '"$f"' INTO TABLE $(echo  ${f%.*} | rev | cut -d"/" -f1 | rev) fields TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES" -u root --password=root
    done