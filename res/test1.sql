PRAGMA encoding="UTF-8";

DROP TABLE IF EXISTS subjects;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS academicHistory;
DROP TABLE IF EXISTS classification;

CREATE TABLE IF NOT EXISTS subjects(
  id INTEGER PRIMARY KEY NOT NULL UNIQUE,
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
  academicHistoryID INTEGER PRIMARY KEY NOT NULL UNIQUE,
  -- subjectCredits INTEGER
  studentID INTEGER,
  subjectID INTEGER,
  finalNote FLOAT,
  FOREIGN KEY(subjectID)
  REFERENCES subjects(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  FOREIGN KEY(studentID)
  REFERENCES students(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS classification(
  classificationID INTEGER PRIMARY KEY NOT NULL UNIQUE,
  -- studentID INTEGER,
  -- name TEXT,
  -- lastName TEXT,
  studentID INTEGER,
  amountSubjects INTEGER,
  creditSum INTEGER,
  studentAverage INTEGER,
  FOREIGN KEY(studentID)
  REFERENCES students(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
  );

INSERT INTO students(id, name, lastName, career, bornDate, entryDate, placeOrigin, email, enrollQuantity, photograph) VALUES
(1078366418, "Cristian", "Castañeda", "Ciencias de la Computación", "03-10-2004", "01-01-2022", "Bogotá", "crcastanedao", 2, "source.unsplash.com/100x100/"),
(1078366419, "Juan", "Perez", "Medicina", "23-12-2003", "01-01-2022", "Bogotá", "juperez", 2, "source.unsplash.com/100x100/"),
(1078366420, "Maria", "Gomez", "Administración de Empresas", "11-10-2003", "01-01-2022", "Bogotá", "margomez", 2, "source.unsplash.com/100x100/"),
(1078366421, "Camilo", "Gonzalez", "Administración de Empresas", "03-11-2004", "01-01-2022", "Bogotá", "camgonzalez", 2, "source.unsplash.com/100x100/");

INSERT INTO subjects(id, name, school, department, credits, language) VALUES
(001, "Matemáticas", "Ingeniería", "Ingeniería de Sistemas", "4", "Español"),
(002, "Física", "Ingeniería", "Ingeniería de Sistemas", "4", "Español"),
(003, "Química", "Ingeniería", "Ingeniería de Sistemas", "4", "Español"),
(004, "Inglés", "Ingeniería", "Ingeniería de Sistemas", "2", "Inglés"),
(005, "Programación", "Ingeniería", "Ingeniería de Sistemas", "3", "Español"),
(006, "Estructuras de Datos", "Ingeniería", "Ingeniería de Sistemas", "3", "Español"),
(007, "Bases de Datos", "Ingeniería", "Ingeniería de Sistemas", "3", "Español"),
(008, "Sistemas Operativos", "Ingeniería", "Ingeniería de Sistemas", "4", "Español"),
(009, "Arquitectura de Computadores", "Ingeniería", "Ingeniería de Sistemas", "4", "Español"),
(010, "Redes de Computadores", "Ingeniería", "Ingeniería de Sistemas", "4", "Español"),
(011, "Ingeniería de Software", "Ingeniería", "Ingeniería de Sistemas", "4", "Español"),
(012, "Administración de Proyectos", "Ingeniería", "Ingeniería de Sistemas", "4", "Español"),
(013, "Sistemas de Información", "Ingeniería", "Ingeniería de Sistemas", "4", "Español"),
(014, "Ingeniería Económica", "Ingeniería", "Ingeniería de Sistemas", "2", "Español");

INSERT INTO academicHistory(finalNote, subjectID, studentID) VALUES
(4.5, 001, 1078366418),
(4.0, 010, 1078366418),
(2.9, 014, 1078366418),
(4.0, 011, 1078366418),
(3.0, 001, 1078366419),
(2.0, 002, 1078366419),
(5.0, 005, 1078366419),
(4.0, 013, 1078366419),
(3.0, 003, 1078366420),
(3.0, 009, 1078366420),
(5.0, 010, 1078366420),
(4.0, 004, 1078366421),
(4.0, 013, 1078366421),
(4.0, 014, 1078366421);


