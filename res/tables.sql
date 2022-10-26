PRAGMA encoding="UTF-8";

-- DROP TABLE IF EXISTS subjects;
-- DROP TABLE IF EXISTS students;
-- DROP TABLE IF EXISTS academicHistory;
-- DROP TABLE IF EXISTS classification;

CREATE TABLE IF NOT EXISTS subjects(
    code INTEGER PRIMARY KEY NOT NULL UNIQUE,
    name TEXT NOT NULL UNIQUE,
    school TEXT,
    department TEXT,
    credits TEXT,
    language TEXT);

CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    lastName TEXT,
    career TEXT,
    bornDate TEXT,
    entryDate TEXT,
    placeOrigin TEXT,
    email TEXT,
    enrollQuantity INTEGER,
    photograph TEXT);

CREATE TABLE IF NOT EXISTS academicHistory(
    code INTEGER,
    id INTEGER,
    finalNote FLOAT,
    credits INTEGER,
    PRIMARY KEY (code, id)
    FOREIGN KEY (code) REFERENCES subjects(code),
    FOREIGN KEY (id) REFERENCES students(id)
    );

CREATE TABLE IF NOT EXISTS classification(
    student_id INTEGER,
    name TEXT,
    lastName TEXT,
    amountSubjects INTEGER,
    creditSum INTEGER,
    average INTEGER
    );