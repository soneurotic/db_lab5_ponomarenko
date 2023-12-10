import csv
import random
import psycopg2

username = 'postgres'
password = 'postgres'
database = 'lab_5'
host = 'localhost'
port = '5432'

INPUT_CSV_FILE_1 = 'C:/Users/alexa/OneDrive/Рабочий стол/пм/databases/SQL/LR3/Genshin_Impact_All_Character_Stat.csv'
INPUT_CSV_FILE_2 = 'C:/Users/alexa/OneDrive/Рабочий стол/пм/databases/SQL/LR3/genshin_weapons_v2.csv'

query_01 = '''
CREATE TABLE IF NOT EXISTS character
(
  character_name VARCHAR(50) NOT NULL,
  element VARCHAR(25) NOT NULL,
  rarity INT NOT NULL,
  PRIMARY KEY (character_name)
)
'''

query_02 = '''
CREATE TABLE IF NOT EXISTS is_at
(
  character_name VARCHAR(50) NOT NULL,
  level INT NOT NULL,
  rised CHAR(1) NOT NULL,
  base_HP INT NOT NULL,
  base_ATK INT NOT NULL,
  base_DEF INT NOT NULL,
  PRIMARY KEY (character_name, level, rised),
  FOREIGN KEY (character_name) REFERENCES character_test(character_name),
  FOREIGN KEY (level, rised) REFERENCES phase(level, rised)
)
'''

query_03 = '''
CREATE TABLE IF NOT EXISTS has
(
  character_name VARCHAR(50) NOT NULL,
  weapon_type VARCHAR(25) NOT NULL,
  weapon_name VARCHAR(50) NOT NULL,
  PRIMARY KEY (character_name, weapon_name),
  FOREIGN KEY (character_name) REFERENCES character(character_name),
  FOREIGN KEY (weapon_name) REFERENCES weapon(weapon_name)
)
'''

query_04 = '''
CREATE TABLE IF NOT EXISTS weapon
(
  weapon_name VARCHAR(50) NOT NULL,
  rarity INT NOT NULL,
  max_atk INT NOT NULL,
  substat_type VARCHAR(25),
  max_substat VARCHAR(10),
  PRIMARY KEY (weapon_name)
)
'''

query_11 = '''
INSERT INTO character (character_name, element, rarity) VALUES (%s, %s, %s)
ON CONFLICT (character_name) DO NOTHING
'''

query_12 = '''
INSERT INTO is_at (character_name, level, rised, base_HP, base_ATK, base_DEF) VALUES (%s, %s, %s, %s, %s, %s)
ON CONFLICT (character_name, level, rised) DO NOTHING
'''

query_13 = '''
INSERT INTO has (character_name, weapon_type, weapon_name) VALUES (%s, %s, %s)
ON CONFLICT (character_name, weapon_name) DO NOTHING
'''

query_14 = '''
INSERT INTO weapon (weapon_name, rarity, max_atk) VALUES (%s, %s, %s) 
ON CONFLICT (weapon_name) DO NOTHING
'''

conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
    cur = conn.cursor()

    cur.execute(query_01)
    cur.execute(query_02)

    with open(INPUT_CSV_FILE_1, 'r') as inf1, open(INPUT_CSV_FILE_2, 'r') as inf2:
        char_reader = csv.DictReader(inf1)
        weapon_reader = csv.DictReader(inf2)

        all_weapons = [(row['weapon_name'], row['type'], row['max_atk'], int(row['rarity'][0])) for row in weapon_reader]
        sorted_weapons_by_type = {}

        classifier = map(lambda x: (x[1], (x[0], x[2], x[3])), all_weapons)

        for el in classifier:
            sorted_weapons_by_type.update({el[0]: sorted_weapons_by_type.get(el[0], []) + [el[1]]})

        char_lvl_comp_prev, char_name_prev = None, None

        for idx, row in enumerate(char_reader):
            if idx == 42:
                break

            character_name = row['Character']
            level = row['Lv']
            rarity = row['Rarity']
            element = row['Element']
            weapon_type = row['Weapon']

            weapon = random.choice(sorted_weapons_by_type[weapon_type])
            weapon_name, max_atk, weapon_rarity = weapon[0], weapon[1], weapon[2]

            lst = list(sorted_weapons_by_type[weapon_type])
            lst.remove(weapon)

            sorted_weapons_by_type.update({weapon_type: lst})

            char_lvl_comb = (character_name, level)
            rised = ['N','Y'][char_lvl_comb == char_lvl_comp_prev]
            char_lvl_comp_prev = char_lvl_comb

            base_HP = row['Base HP']
            base_ATK = row['Base ATK']
            base_DEF = row['Base DEF']

            char_values = (character_name, element, rarity)
            is_at_values = (character_name, level, rised, base_HP, base_ATK, base_DEF)

            has_values = (character_name, weapon_type, weapon_name)
            weapon_values = (weapon_name, weapon_rarity, max_atk)

            if character_name != char_name_prev:
                cur.execute(query_11, char_values)

            char_name_prev = character_name

            cur.execute(query_12, is_at_values)

            cur.execute(query_14, weapon_values)
            cur.execute(query_13, has_values)

    conn.commit()