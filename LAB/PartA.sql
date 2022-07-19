DROP TABLE Dept;
DROP TABLE Emp;
DROP TABLE Proj;
DROP TABLE Workson;
CREATE TABLE Dept (dno varchar(5) PRIMARY KEY, dname varchar(10),mgreno int);

CREATE TABLE Emp (eno int PRIMARY KEY, ename varchar(10), bdate DATE, title varchar(10), salary int, dno varchar(5) references Dept(dno));

CREATE TABLE Proj (pno int PRIMARY KEY, pname varchar(10), budget int, dno varchar(5) references Dept(dno));

CREATE TABLE Workson ( eno int references Emp(eno),pno int references Proj(pno),resp varchar(10), hours int);

INSERT INTO Dept VALUES('&DNO','&DNAME',&MGRENO);
INSERT INTO Emp VALUES(&eno, '&ename','&bdate','&title',&salary,'&dno');
INSERT INTO Proj VALUES(&PNO,'&PNAME',&BUDGET,'&DNO');
INSERT INTO Workson VALUES(&ENO,&PNO,'&RESP',&HOURS);

Q1. 
SELECT PNO,PNAME FROM PROJ WHERE BUDGET>100000;

Q2.
SELECT * FROM Workson WHERE HOURS<10 AND RESP='MA';

Q3.
SELECT ENO,ENAME FROM EMP WHERE SALARY>35000 AND TITLE IN ('SA','EE');

Q4.
SELECT ENAME FROM EMP WHERE DNO='D1' ORDER BY SALARY DESC;

Q5.
SELECT * FROM DEPT ORDER BY DNAME ASC;