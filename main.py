import psycopg2
import matplotlib.pyplot as plt
from textwrap import wrap

username = 'postgres'
password = 'postgres'
database = 'lab_5'
host = 'localhost'
port = '5432'

query_1 = '''
SELECT character_name, max_atk AS weapon_max_atk 
FROM Characters_WeaponPotential
'''
query_2 = '''
SELECT weapon_type, weapon_count 
FROM WeaponType_to_WeaponCount
'''

query_3 = '''
SELECT character_name, character_base_atk, weapon_max_atk 
FROM AtkPotentialForBuilds
	ORDER BY character_base_atk + weapon_max_atk
'''

view_1 = '''
CREATE OR REPLACE VIEW Characters_WeaponPotential AS
	SELECT character_name, weapon_name, rarity, weapon_type, max_atk, substat_type, max_substat FROM has
	LEFT JOIN weapon USING(weapon_name)
'''

view_2 = '''
CREATE OR REPLACE VIEW WeaponType_to_WeaponCount AS
SELECT weapon_type, COUNT(weapon_type) AS weapon_count FROM is_at 
	LEFT JOIN character USING(character_name)
	LEFT JOIN has USING(character_name)
		WHERE level > 40
			GROUP BY weapon_type
'''

view_3 = '''
CREATE OR REPLACE VIEW AtkPotentialForBuilds AS
SELECT is_at.character_name, level, rised, base_atk AS character_base_atk, 
	   element, character.rarity, weapon.weapon_name, weapon_type, 
	   (weapon.rarity) AS weapon_rarity, max_atk AS weapon_max_atk, substat_type, max_substat
	   FROM is_at 
			LEFT JOIN character USING(character_name)
			LEFT JOIN has USING(character_name)
			LEFT JOIN weapon USING(weapon_name)
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))

with conn:
    print("Database opened successfully")
    cur = conn.cursor()

    cur.execute(view_1)
    cur.execute(view_2)
    cur.execute(view_3)

    # Запит 1
    cur.execute(query_1)
    characters = []
    atk = []

    char_to_weaponATK = dict()

    for row in cur:
        characters.append(row[0])
        atk.append(row[1])

    for el in list(zip(characters, atk)):
        char_to_weaponATK.update({el[0]: char_to_weaponATK.get(el[0], []) + [el[1]]})

    plt.figure(figsize=(20, 8))
    plt.subplot(131)

    cmap1 = plt.cm.get_cmap("hsv", len(char_to_weaponATK) + 1)

    bar_width = 0.5
    bar_padding = 1.0

    for i, (k, v) in enumerate(char_to_weaponATK.items()):
        x_positions = [pos + i * (bar_width + bar_padding) for pos in range(len(v))]
        plt.bar(x_positions, v, width=bar_width, color=cmap1(i), label=k)

    plt.title("\n".join(wrap('Максимальна атака зброї, якою споряджені персонажі', 40)))
    plt.xlabel('Персонажі')
    plt.xticks([])
    plt.legend(loc='best', bbox_to_anchor=(1, 0.6))
    plt.ylabel('Атака, од.')

    # Запит 2
    cur.execute(query_2)

    weapon_type = []
    freq = []

    for row in cur:
        weapon_type.append(row[0])
        freq.append(row[1])

    plt.subplot(132)
    plt.pie(freq, labels=weapon_type, autopct='%1.1f%%')
    plt.title("\n".join(wrap('Частка використання зброї, що припадає на кожен тип зброї '
                             'використовуваний персонажами, що мають рівень вище 40', 40)))

    # Запит 3
    cur.execute(query_3)
    char_names = []
    base_max = []

    for row in cur:
        char_names.append(row[0])
        base_max.append((row[1], row[2]))

    data = dict()

    for el in list(zip(char_names, base_max)):
        data.update({el[0]: data.get(el[0], []) + [el[1]]})

    plt.subplot(133)
    cmap2 = plt.cm.get_cmap("hsv", len(data) + 1)

    for i, (k, v) in enumerate(data.items()):
        value_atk1 = [value[0] for value in v]
        value_atk2 = [value[1] for value in v]
        plt.scatter(value_atk1, value_atk2, color=cmap2(i), label=k)

    plt.title("\n".join(wrap('Базова атака персонажа + максимальна атака зброї', 40)))
    plt.xlabel('character_base_atk')
    plt.ylabel('weapon_max_atk')
    plt.legend(loc='best', bbox_to_anchor=(1, 0.6))

    plt.tight_layout()
    plt.savefig('new_graphs.png')

    plt.show()