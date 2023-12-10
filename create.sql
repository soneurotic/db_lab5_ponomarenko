CREATE TABLE character
(
  character_name VARCHAR(50) NOT NULL,
  element VARCHAR(25) NOT NULL,
  rarity INT NOT NULL,
  PRIMARY KEY (character_name)
);

CREATE TABLE phase
(
  level INT NOT NULL,
  rised CHAR(1) NOT NULL,
  PRIMARY KEY (level, rised)
);

CREATE TABLE weapon
(
  weapon_name VARCHAR(50) NOT NULL,
  rarity INT NOT NULL,
  max_atk INT NOT NULL,
  substat_type VARCHAR(25),
  max_substat VARCHAR(10),
  PRIMARY KEY (weapon_name)
);

CREATE TABLE is_at
(
  character_name VARCHAR(50) NOT NULL,
  level INT NOT NULL,
  rised CHAR(1) NOT NULL,
  base_HP INT NOT NULL,
  base_ATK INT NOT NULL,
  base_DEF INT NOT NULL,
  PRIMARY KEY (character_name, level, rised),
  FOREIGN KEY (character_name) REFERENCES character(character_name),
  FOREIGN KEY (level, rised) REFERENCES phase(level, rised)
);

CREATE TABLE has
(
  character_name VARCHAR(50) NOT NULL,
  weapon_type VARCHAR(25) NOT NULL,
  weapon_name VARCHAR(50) NOT NULL,
  PRIMARY KEY (character_name, weapon_name),
  FOREIGN KEY (character_name) REFERENCES character(character_name),
  FOREIGN KEY (weapon_name) REFERENCES weapon(weapon_name)
);