DROP TABLE IF EXISTS gdelt.gdelt;

CREATE TABLE gdelt.gdelt(
id BIGINT NOT NULL AUTO_INCREMENT,
conflict_date DATE,
source_country CHAR(3),
target_country CHAR(3),
cameo_code  int,
num_events int, 
num_arts  int,
quadclass int, 
goldstein float,
source_geo_type int,
source_geo_lat float,
source_geo_long float,
target_geo_type int,    
target_geo_lat float,
target_geo_long float,
action_geo_type int,
action_geo_lat float,
action_geo_long float,
PRIMARY KEY (id)
);
