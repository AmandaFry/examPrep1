-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema tfprac1
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema tfprac1
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `tfprac1` DEFAULT CHARACTER SET utf8 ;
USE `tfprac1` ;

-- -----------------------------------------------------
-- Table `tfprac1`.`Users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tfprac1`.`Users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(75) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tfprac1`.`Trips`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tfprac1`.`Trips` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tripOrganizer_id` INT NOT NULL,
  `destination` VARCHAR(45) NULL,
  `plan` VARCHAR(45) NULL,
  `start_date` DATE NULL,
  `end_date` DATE NULL,
  `created_at` DATETIME NULL,
  `updaetd_at` DATETIME NULL,
  PRIMARY KEY (`id`, `tripOrganizer_id`),
  INDEX `fk_Trips_Users_idx` (`tripOrganizer_id` ASC),
  CONSTRAINT `fk_Trips_Users`
    FOREIGN KEY (`tripOrganizer_id`)
    REFERENCES `tfprac1`.`Users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tfprac1`.`trip_friends`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tfprac1`.`trip_friends` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `trips_id` INT NOT NULL,
  `friends_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`, `trips_id`),
  INDEX `fk_table3_Trips1_idx` (`trips_id` ASC),
  INDEX `fk_trip_friends_Users1_idx` (`friends_id` ASC),
  CONSTRAINT `fk_table3_Trips1`
    FOREIGN KEY (`trips_id`)
    REFERENCES `tfprac1`.`Trips` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_trip_friends_Users1`
    FOREIGN KEY (`friends_id`)
    REFERENCES `tfprac1`.`Users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
