-------------------------
-- Populate character table
-------------------------
INSERT INTO character(character_name, element, rarity)
VALUES('Bennett', 'Pyro', 4);
INSERT INTO character(character_name, element, rarity)
VALUES('Lisa', 'Electro', 4);
INSERT INTO character(character_name, element, rarity)
VALUES('Qiqi', 'Cryo', 5);
INSERT INTO character(character_name, element, rarity)
VALUES('Kazuha', 'Anemo', 5);
INSERT INTO character(character_name, element, rarity)
VALUES('Zhongli', 'Geo', 5);
INSERT INTO character(character_name, element, rarity)
VALUES('Kokomi', 'Hydro', 5);

--------------------------
-- Populate phase table
--------------------------
INSERT INTO phase(level, rised)
VALUES(20, 'N');
INSERT INTO phase(level, rised)
VALUES(50, 'N');
INSERT INTO phase(level, rised)
VALUES(60, 'Y');
INSERT INTO phase(level, rised)
VALUES(70, 'Y');
INSERT INTO phase(level, rised)
VALUES(80, 'Y');
INSERT INTO phase(level, rised)
VALUES(90, 'N');

------------------------
-- Populate weapon table
------------------------
INSERT INTO weapon(weapon_name, rarity, max_atk, substat_type, max_substat)
VALUES('Dark Iron Sword', 3, 401, 'Elemental', '141');
INSERT INTO weapon(weapon_name, rarity, max_atk, substat_type, max_substat)
VALUES('Hakushin Ring', 4, 565, 'Energy Recharge', '30.60%');
INSERT INTO weapon(weapon_name, rarity, max_atk, substat_type, max_substat)
VALUES('Light of Foliar Incision', 5, 542, 'CRIT DMG', '88.20%');
INSERT INTO weapon(weapon_name, rarity, max_atk, substat_type, max_substat)
VALUES('Primordial Jade Cutter', 5, 542, 'CRIT Rate', '44.10%');
INSERT INTO weapon(weapon_name, rarity, max_atk, substat_type, max_substat)
VALUES('Lithic Spear', 4, 565, 'ATK', '27.60%');
INSERT INTO weapon(weapon_name, rarity, max_atk, substat_type, max_substat)
VALUES('Pocket Grimoire', 2, 243, NULL, NULL);
INSERT INTO weapon(weapon_name, rarity, max_atk, substat_type, max_substat)
VALUES('Luxurious Sea-Lord', 4, 454, 'ATK', '55.10%');
INSERT INTO weapon(weapon_name, rarity, max_atk, substat_type, max_substat)
VALUES('Hunter`s Bow', 1, 185, NULL, NULL);
INSERT INTO weapon(weapon_name, rarity, max_atk, substat_type, max_substat)
VALUES('Aquila Favonia', 5, 674, 'Physical DMG', '41.30%');
INSERT INTO weapon(weapon_name, rarity, max_atk, substat_type, max_substat)
VALUES('Cinnabar Spindle', 4, 454, 'DEF', '69.00%');

----------------------------
-- Populate is_at (character_phase) table
----------------------------
INSERT INTO is_at(character_name, level, rised, base_HP, base_ATK, base_DEF)
VALUES('Bennett', 50, 'N', 6573, 101, 409);
INSERT INTO is_at(character_name, level, rised, base_HP, base_ATK, base_DEF)
VALUES('Lisa', 60, 'Y', 6731, 163, 403);
INSERT INTO is_at(character_name, level, rised, base_HP, base_ATK, base_DEF)
VALUES('Qiqi', 20, 'N', 2498, 58, 186);
INSERT INTO is_at(character_name, level, rised, base_HP, base_ATK, base_DEF)
VALUES('Kazuha', 90, 'N', 13348, 297, 807);
INSERT INTO is_at(character_name, level, rised, base_HP, base_ATK, base_DEF)
VALUES('Zhongli', 70, 'Y', 11940, 204, 599);
INSERT INTO is_at(character_name, level, rised, base_HP, base_ATK, base_DEF)
VALUES('Kokomi', 80, 'Y', 12524, 218, 611);

----------------------------
-- Populate has (character_weapon) table
----------------------------
INSERT INTO has(character_name, weapon_name, weapon_type)
VALUES('Bennett', 'Dark Iron Sword', 'Sword');
INSERT INTO has(character_name, weapon_name, weapon_type)
VALUES('Lisa', 'Hakushin Ring', 'Catalyst');
INSERT INTO has(character_name, weapon_name, weapon_type)
VALUES('Qiqi', 'Aquila Favonia', 'Sword');
INSERT INTO has(character_name, weapon_name, weapon_type)
VALUES('Kazuha', 'Primordial Jade Cutter', 'Sword');
INSERT INTO has(character_name, weapon_name, weapon_type)
VALUES('Zhongli', 'Lithic Spear', 'Polearm');
INSERT INTO has(character_name, weapon_name, weapon_type)
VALUES('Kokomi', 'Pocket Grimoire', 'Catalyst');