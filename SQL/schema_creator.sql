CREATE TABLE transfers (
    index INT NOT NULL,
    name VARCHAR(60)   NOT NULL,
    position VARCHAR(40)   NOT NULL,
    age INT   NOT NULL,
    team_from VARCHAR(40)   NOT NULL,
    league_from VARCHAR(40)   NOT NULL,
    team_to VARCHAR(40)   NOT NULL,
    league_to VARCHAR(40)   NOT NULL,
    season VARCHAR(40)   NOT NULL,
    market_value INT   NOT NULL,
    transfer_fee INT   NOT NULL,
    CONSTRAINT pk_transfers PRIMARY KEY (
        index
     )
);

CREATE TABLE league_countries (
    league_name VARCHAR(35)   NOT NULL,
    country VARCHAR(30)   NOT NULL,
    CONSTRAINT pk_league_countries PRIMARY KEY (
        league_name
     )
);

CREATE TABLE locations (
    country VARCHAR(35)   NOT NULL,
    country_code VARCHAR(10)   NOT NULL,
    latitude VARCHAR(30)   NOT NULL,
    longitude VARCHAR(30)   NOT NULL,
    CONSTRAINT pk_locations PRIMARY KEY (
        country
     )
);

ALTER TABLE transfers ADD CONSTRAINT fk_transfers_league_from FOREIGN KEY(league_from)
REFERENCES league_countries (league_name);

ALTER TABLE transfers ADD CONSTRAINT fk_transfers_league_to FOREIGN KEY(league_to)
REFERENCES league_countries (league_name);

ALTER TABLE league_countries ADD CONSTRAINT fk_league_countries_country FOREIGN KEY(country)
REFERENCES locations (country);