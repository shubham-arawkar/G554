-- INSERT INTO employee VALUES ('Cecilia', 'F', 'Kolonsky', NULL, '1960-04-05', '6357 Windy Lane, Katy, TX', 'F', 28000, NULL, 4);
-- #1048 - Column 'ssn' cannot be null [PRIMARY KEY can't be null]

INSERT INTO employee VALUES ('Alicia', 'J', 'Zelaya', '999887777', '1960-04-05', '6357 Windy Lane, Katy, TX', 'F', 28000, '987654321', 4);

-- INSERT INTO employee VALUES ('Cecilia', 'F', 'Kolonsky', '677678989', '1960-04-05', '6357 Windswept, Katy, TX', 'F', 28000, '987654321', 7);
-- #1062 - Duplicate entry '677678989' for key 'PRIMARY'

-- INSERT INTO employee VALUES ('Cecilia', 'F', 'Kolonsky', '677678989', '1960-04-05', '6357 Windy Lane, Katy, TX', 'F', 28000, NULL, 4);
-- #1062 - Duplicate entry '677678989' for key 'PRIMARY'

DELETE FROM works_on WHERE essn = '999887777' and pno = 10;

DELETE FROM employee WHERE ssn = '999887777';

DELETE FROM employee WHERE ssn = '333445555';

UPDATE employee SET salary = 28000 WHERE ssn = '999887777';

UPDATE employee SET dno = 1 WHERE ssn = '999887777';

UPDATE employee SET dno = 7 WHERE ssn = '999887777';

UPDATE employee SET ssn = '987654321' WHERE ssn = '999887777';

