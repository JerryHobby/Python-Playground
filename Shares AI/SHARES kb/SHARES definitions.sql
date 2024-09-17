
-- SHARES, definitions - any term found in shares or in a PNR
-- any component of a pnr
-- any airline abbreviation
-- basically any question that starts with "WHAT IS ..."

DELETE from shares_kb WHERE keywords LIKE '%definition%';

INSERT INTO shares_kb
    (prompt, keywords, completion)
VALUES
    ('What is SHARES?',
     'SHARES, definition',
     ''),
    ('What is the history of SHARES?',
     'SHARES, definition, history',
     ''),
    ('Who uses SHARES?',
     'SHARES, definition, users',
     ''),
    ('What is a PNR?',
     'SHARES, definition, passenger name record(PNR)',
     ''),
    ('What is a Fare Quote?',
     'SHARES, definition, fare quote (FQTR)',
     ''),
    ('What is a work area?',
     'SHARES, definition, work area',
     ''),
    ('What is an SOM (start of message)?',
     'SHARES, definition, keyboard, som',
     ''),
    ('What is UNMR?',
     'SHARES, definition, unaccompanied minor (UNMR)',
     ''),
    ('What is an ITIN?',
     'SHARES, definition, itinerary (ITIN), segment',
     ''),
    ('What is an OSI?',
     'SHARES, definition, other service information (OSI)',
     ''),
    ('What is an SSR?',
     'SHARES, definition, special service request (SSR)',
     ''),
    ('What is a FONE field?',
     'SHARES, definition, fone, phone',
     ''),
    ('What is a comment field)?',
     'SHARES, definition, comment',
     ''),
    ('What is a UNMR?',
     'SHARES, definition, unaccompanied minor (UNMR)',
     ''),
    ('What is a TCP?',
     'SHARES, definition, to complete a party (TCP)',
     ''),
    ('What is a SHARES keyboard?',
     'SHARES, definition, keyboard',
     ''),
    ('What does it mean to "get control" or "push control"?',
     'SHARES, definition, control of ticket',
     ''),
    ('What is OA?',
     'SHARES, definition, other airline (OA)',
     ''),
    ('What is EZR?',
     'SHARES, definition, EZR software program',
     ''),
    ('What is Navigator?',
     'SHARES, definition, Navigator software program',
     '')









