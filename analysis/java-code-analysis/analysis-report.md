# Java Repository Analysis Report

> Generated: 2026-11-02T13:58:44.338+05:30 | Repository: surajkumarbr/cab-service-userservice (analyzed module: Cab-Service-Driver-Service) | Coverage: partial

## Executive summary
Single Spring Boot driver-service module exposing REST endpoints under `/api/driver` with MySQL persistence via Spring Data JPA.
Business logic is primarily implemented in `DriverDaoImpl`.

High-priority finding: `GET /api/driver/name/{username}` returns the `Driver` entity (includes `password`) instead of a safe DTO.

## Technology stack
- Java (17)
- Spring Boot (3.3.1)
- Spring Cloud (2023.0.2)
- Spring Web (MVC) 
- Spring Data JPA 
- MySQL JDBC 
- Eureka Client 
- OpenFeign 
- ModelMapper (2.4.4)
- BCrypt password hashing 

## REST API inventory
- POST /api/driver/add -> com.example.driver.controller.DriverController#addOneDriver
- GET /api/driver/{driverId} -> com.example.driver.controller.DriverController#getDriverById
- DELETE /api/driver/{driverId} -> com.example.driver.controller.DriverController#deleteDriverUsingId
- PUT /api/driver/update/{driverId} -> com.example.driver.controller.DriverController#updateDriverDetails
- GET /api/driver/all -> com.example.driver.controller.DriverController#getAllDriver
- PUT /api/driver/change-status/{driverId} -> com.example.driver.controller.DriverController#updateDriverStatus
- GET /api/driver/name/{username} -> com.example.driver.controller.DriverController#getDriverByName

## Business rules (implemented)
- BR-001: Driver email must be unique on creation (confidence: high)
- BR-002: Driver username must be unique on creation (confidence: high)
- BR-003: Persisted driver passwords are stored hashed (BCrypt) (confidence: high)
- BR-004: New drivers default to available (confidence: high)
- BR-005: Validation failures return HTTP 400 with field message (confidence: high)

## Technical risks
- TR-001 [high/confirmed]: Sensitive data exposure: /api/driver/name/{username} returns Driver entity including password.
  Recommendation: Return DriverDto (or a safe response type) instead of Driver; ensure password is never serialized; return 404 when not found.
- TR-002 [medium/confirmed]: Schema drift risk: Hibernate ddl-auto=update and generate-ddl=true are configured.
  Recommendation: Adopt Flyway/Liquibase and use profiles; set ddl-auto=validate/none in prod.
- TR-003 [medium/confirmed]: Auditing last-modified columns are marked updatable=false, likely preventing updates from being persisted.
  Recommendation: Remove updatable=false for @LastModifiedDate/@LastModifiedBy fields or confirm intended DB behavior.
- TR-004 [low/confirmed]: UpdateDriverDetailsDto includes password but update flow does not update/encode password.
  Recommendation: Remove password from the DTO or implement a dedicated change-password endpoint with BCrypt encoding.

## Evidence index (high-signal)
- `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/controller/DriverController.java`:18-65 (controller mappings)
- `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/dao/impl/DriverDaoImpl.java`:21-128 (DAO business logic)
- `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/entity/Driver.java`:8-24 (entity mapping)
- `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/exception/GlobalExceptionHandler.java`:16-57 (exception mapping)

## Limitations
- Single-module snapshot; no additional modules were present in this workspace.
- No OpenAPI/Swagger specs found; API inventory derived from Spring MVC annotations.
- No DB migration scripts found; schema inferred from JPA annotations and Hibernate configuration.
- Static analysis only; runtime behavior and profile overrides not executed.
