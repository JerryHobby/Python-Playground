

-- SHARES, procedures - Processes such as "how do I assign seats
-- Basically anything that starts with "HOW DO I ..."



DELETE from shares_kb WHERE keywords LIKE '%procedure%';

INSERT INTO shares_kb
(prompt, keywords, completion)
VALUES
    ('How do I sign into SHARES?',
     'procedure',
     ''),
    ('How do I switch work areas?',
     'procedure',
     ''),
    ('How do I sign out of SHARES?',
     'procedure',
     ''),
    ('How do I open a PNR/RECLOC?',
     'procedure',
     ''),
    ('How do I ignore changes to a PNR?',
     'procedure',
     ''),

    ('How do I move up or down in a PNR?',
     'procedure',
     ''),
    ('How do I display or update the itinerary?',
     'procedure',
     ''),
    ('How do I display or update  the passengers?',
     'procedure',
     ''),
    ('How do I display or update  the phone fields?',
     'procedure',
     ''),
    ('How do I display or update  the OSI fields?',
     'procedure',
     ''),
    ('How do I display or update  the SSR fields?',
     'procedure',
     ''),
    ('How do I display or update  the seat assignments?',
     'procedure',
     ''),

    ('How do I display or update the fare quote?',
     'procedure',
     ''),
    ('How do I display the tickets?',
     'procedure',
     ''),
    ('How do I display the OA (other airline/carrier) PNR/RECLOC',
     'procedure',
     ''),
    ('How do I divide a PNR?',
     'procedure',
     ''),
    ('How do I price a PNR?',
     'procedure',
     ''),
    ('How do I display or update',
     'procedure',
     '')

-- # unmr
-- # get control
-- # push control
-- # shares keyboard
-- # ja - pass rider information
-- # line formats
--



