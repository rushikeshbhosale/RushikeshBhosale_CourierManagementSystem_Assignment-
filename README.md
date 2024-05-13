# Courier Management System

## Introduction
Welcome to the Courier Management System project! This project aims to implement a comprehensive system for managing courier operations, including customer orders, courier assignments, package tracking, employee management, and more. The system is designed to be scalable, efficient, and user-friendly, providing robust functionalities for both customers and administrative staff.

## Technologies Used - 
- **Python**
- **MySQL**
- **GIT**

## Project Structure
The project follows a modular structure, with different components organized into packages:

- **entity**: Contains entity classes representing real-world entities such as users, couriers, employees, locations, and payments. These classes encapsulate data and behavior related to each entity.
- **dao**: Contains service provider interfaces (SPIs) and their implementations for interacting with the database. This package handles database operations such as CRUD (Create, Read, Update, Delete) operations, data retrieval, and data manipulation.
- **exception**: Contains user-defined exceptions that are thrown and handled within the application. These exceptions help in handling error scenarios gracefully and provide meaningful feedback to users.
- **util**: Contains utility classes for database connection management and property file handling. These classes facilitate establishing connections to the database and retrieving database configuration properties.
- **main**: Contains the main module of the application, which demonstrates the functionalities in a menu-driven console application. Users interact with the system through this module, accessing various features and functionalities.

## Database Design
The database schema for the Courier Management System consists of several tables representing different entities such as users, couriers, employees, locations, and payments. Relationships between these tables are defined using foreign keys to maintain data integrity. Sample data is inserted into the tables to simulate real-world scenarios.

## Queries and Functionalities
The project implements a wide range of SQL queries and functionalities to perform operations such as data retrieval, aggregation, filtering, and joining. These functionalities cover various use cases related to customer orders, courier assignments, package tracking, employee management, and payment processing.

## Control Flow Statements
The project includes implementations of control flow statements such as if-else statements, switch-case statements, and loops to manage order status, parcel categorization, user authentication, and courier assignment logic.

## Collections and Data Structures
Python data structures such as lists and dictionaries are used to enhance the Courier Management System by providing dynamic data storage and efficient data retrieval capabilities. These data structures are utilized for storing and accessing courier, employee, and location information.

## Exception Handling
The project incorporates exception handling mechanisms to gracefully handle error scenarios and provide meaningful feedback to users. Custom exceptions are defined and raised within the application to handle scenarios such as tracking number not found and invalid employee ID.

## Database Interaction
The application interacts with a SQL database to store and retrieve data related to courier management operations. Database connection management is handled using utility classes, and database operations are performed using DAO classes. Features such as data insertion, retrieval, and report generation are implemented using database queries.
