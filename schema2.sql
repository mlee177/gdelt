DROP TABLE IF EXISTS gdelt.eventcode;

CREATE TABLE gdelt.eventcode(
id varchar(4)  NOT NULL,
description VARCHAR(255),
PRIMARY KEY (id)
);
