
-- SHARES, commands - SHARES commands and it's syntax
-- Basically anything that starts with "COMMAND USAGE/SYNTAX ..."

DELETE from shares_kb WHERE keywords LIKE '%command%';

INSERT INTO shares_kb
(prompt, keywords, completion)
VALUES
    ('Command to move up or down in a PNR (MT/MB/MD/MU)',
     'command, syntax, MT, MB, MD, MU',
     ''),
    ('Command to check availability for flights (A)',
     'command, syntax, A',
     '')





