-- Creator:       MySQL Workbench 8.0.18/ExportSQLite Plugin 0.1.0
-- Author:        Mike
-- Caption:       Sakila Full
-- Project:       Name of the project
-- Changed:       2022-08-08 12:37
-- Created:       Jan 09, 2008
PRAGMA foreign_keys = OFF;

-- Schema: new_schema1
ATTACH "new_schema1.sdb" AS "new_schema1";
BEGIN;
CREATE TABLE "new_schema1"."borrowers"(
  "borrowerid" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  "fname" VARCHAR(45) NOT NULL,
  "lname" VARCHAR(45) NOT NULL,
  "email" VARCHAR(45) NOT NULL,
  "password" VARCHAR(45) NOT NULL,
  "phonenumber" INTEGER NOT NULL,
  "address1" VARCHAR(45) NOT NULL,
  "address2" VARCHAR(45),
  "suburb" VARCHAR(45),
  "city" VARCHAR(45) NOT NULL,
  "postcode" INTEGER NOT NULL
);
CREATE TABLE "new_schema1"."books"(
  "bookid" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  "title" VARCHAR(45) NOT NULL,
  "author" VARCHAR(45) NOT NULL
);
CREATE TABLE "new_schema1"."books_borrowed"(
  "books_borrowedid" INTEGER PRIMARY KEY NOT NULL,
  "bookid" INTEGER NOT NULL,
  "borrowerid" INTEGER NOT NULL,
  "date_borrowed" DATE NOT NULL,
  "due_date" DATE NOT NULL,
  "date_returned" DATE,
  CONSTRAINT "bookid"
    FOREIGN KEY("bookid")
    REFERENCES "books"("bookid"),
  CONSTRAINT "borrowerid"
    FOREIGN KEY("borrowerid")
    REFERENCES "borrowers"("borrowerid")
);
CREATE INDEX "new_schema1"."books_borrowed.bookid_idx" ON "books_borrowed" ("bookid");
CREATE INDEX "new_schema1"."books_borrowed.borrowerid_idx" ON "books_borrowed" ("borrowerid");
COMMIT;
