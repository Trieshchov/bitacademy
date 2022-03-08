ALTER TABLE planeten ADD ID int NOT NULL AUTO_INCREMENT PRIMARY KEY;
ALTER TABLE planeten ADD Diameter int(11) NOT NULL;
ALTER TABLE planeten ADD Afstand int(11) NOT NULL;
ALTER TABLE planeten ADD Massa int(11) NOT NULL;
ALTER TABLE planeten ADD Bezoekdatum int(11);

TRUNCATE planeten;

INSERT INTO planeten (naam, Diameter, Afstand, Massa, Bezoekdatum) VALUES ('Moon','3474','384400','0', '1969');

INSERT INTO planeten (naam, Diameter, Afstand, Massa)
VALUES ('Zon', '1392000', '0', '332946'), 
('Mercurius', '4880', '57910000', '0'),
('Venus', '12104', '108208930', '1'),
('Mars', '1275', '149597870', '1'),
('Aarde', '6794', '227936640', '0');


UPDATE planeten SET naam = 'Teenalp' WHERE ID = 4;
DELETE FROM planeten WHERE naam = 4;

ALTER TABLE planeten ADD CONSTRAINT Mars NOT NULL AUTO_INCREMENT PRIMARY KEY (ID);