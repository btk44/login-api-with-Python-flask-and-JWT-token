CREATE SCHEMA `loginappdb` ;

CREATE TABLE `loginappdb`.`account` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`));

CREATE TABLE `loginappdb`.`refresh_token` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `token` VARCHAR(45) NOT NULL,
  `expires_at` DATETIME NOT NULL,
  `account_id` INT NOT NULL,
  PRIMARY KEY (`id`));


INSERT INTO loginappdb.account (Name, Password) VALUES ('test', 'pbkdf2:sha256:260000$stQ1YeBvroJgOrxt$0d9775283c2401ebb3e9938090bbae8c2d4554e2a426d034e9ae2f652637e95a');

