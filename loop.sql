DO $$
DECLARE
    char_lvl  phase.level%TYPE;
	
BEGIN
    FOR char_lvl IN SELECT UNNEST(ARRAY[1, 90])
    LOOP
		INSERT INTO phase (level, rised)
		VALUES 
			(1, 'N'),
			(90, 'N')
		ON CONFLICT (level, rised) DO NOTHING;
	END LOOP;
	
    FOR char_lvl IN SELECT UNNEST(ARRAY[20, 40, 50, 60, 70, 80])
    LOOP
        INSERT INTO phase (level, rised)
        VALUES 
            (char_lvl, 'N'),
            (char_lvl, 'Y')
        ON CONFLICT (level, rised) DO NOTHING;
    END LOOP;
	
END;
$$;

