# Java Repository Analysis Report

> Generated: 2026-11-01T12:51:51.439+05:30 | Repository: cab-service-userservice | Coverage: partial

## 1. Executive summary
Single Spring Boot (Java 17) Maven module implementing a Driver Service. Exposes REST endpoints under `/api/driver` for create/read/update/delete/list drivers and change availability. Uses Spring Data JPA + MySQL; schema management is via Hibernate `ddl-auto=update`.

## 2. Repository scope and coverage
- Root module: `Cab-Service_Driver-Service/Cab-Service-Driver-Service`
- Inspected: all `src/main/java`, `pom.xml`, `src/main/resources/application.properties`
- Excluded: `**/target/**` (generated build output)
- Gaps: no `@FeignClient` types found; no Spring Security configuration found.

## 3. Technology stack and modules
- Spring Boot 3.3.1 (`pom.xml` lines 5–10)
- Java 17 (`pom.xml` lines 29–33)
- Spring Web + Spring Data JPA (`pom.xml` lines 35–42)
- MySQL JDBC (`pom.xml` lines 50–54) and JDBC URL config (`application.properties` lines 5–6)
- Spring Cloud (Eureka + OpenFeign) (`pom.xml` lines 74–81; `Application.java` lines 12–15)

## 4. Architecture and component relationships
Layered flow: `DriverController` → `DriverServiceImpl` → `DriverDaoImpl` → `DriverRepository` → DB.

## 5. Class/package inventory summary
Key classes: `Application`, `DriverController`, `DriverService(+Impl)`, `DriverDao(+Impl)`, `DriverRepository`, `Driver`, `BaseEntity`, `GlobalExceptionHandler`, `DriverDto`.

## 6. REST/API inventory
Base mapping: `/api/driver` (`DriverController.java` lines 18–20)
- POST `/add` (`DriverController.java` 28–31)
- GET `/{driverId}` (`DriverController.java` 33–36)
- DELETE `/{driverId}` (`DriverController.java` 38–41)
- PUT `/update/{driverId}` (`DriverController.java` 43–47)
- GET `/all` (`DriverController.java` 49–52)
- PUT `/change-status/{driverId}` (`DriverController.java` 54–57)
- GET `/name/{username}` (`DriverController.java` 59–62)

## 7. Business rules catalogue
- Uniqueness on create: email + username (reject) (`DriverDaoImpl.java` 33–38)
- Hash password on create using PasswordEncoder/BCrypt (`DriverDaoImpl.java` 40; `Application.java` 26–29)
- Default availability=true on create (`DriverDaoImpl.java` 41)
- Id-based operations throw `UserNotFoundException` when missing (`DriverDaoImpl.java` 49–53, 62–65, 80–83, 104–107)

## 8. End-to-end data flows
Create driver: POST → uniqueness checks → bcrypt hash + availability default → `save` → map to `DriverDto`.

## 9. Persistence/entity/database mapping
- Entity: `Driver` mapped to table `drives` (`Driver.java` 8–12)
- Repository: `DriverRepository extends JpaRepository` with derived queries (`DriverRepository.java` 8–13)
- No migrations found; Hibernate `ddl-auto=update` configured (`application.properties` line 9)

## 10. External integrations and messaging
- MySQL (JPA/JDBC)
- Eureka client configured (`application.properties` line 12)
- OpenFeign enabled but no concrete clients found

## 11. Validation and exception handling
`GlobalExceptionHandler` maps domain exceptions and validation failures to `ExceptionDto` (`GlobalExceptionHandler.java` 19–55).

## 12. Security observations
Confirmed: password hashing on create (BCrypt).
Confirmed risk: `/api/driver/name/{username}` returns `Optional<Driver>`; `Driver` includes `password` without `@JsonIgnore` (`DriverController.java` 59–62; `Driver.java` 15–22).

## 13. Technical risks and recommendations
- Entity exposure (High, confirmed): return `DriverDto` from API-007.
- `ddl-auto=update` (High, potential): use migrations + prod-safe `ddl-auto`.
- Audit fields `updatable=false` for last-modified (Medium, potential): review (`BaseEntity.java` 26–31).

## 14. Evidence index
See: `DriverController.java`, `DriverDaoImpl.java`, `Driver.java`, `BaseEntity.java`, `GlobalExceptionHandler.java`, `pom.xml`, `application.properties`, and `analysis/java-code-analysis/java-inventory.json`.

## 15. Limitations and unresolved questions
- No migration/DDL artifacts.
- No security/authz configuration present.
- No Feign clients present to trace outbound HTTP calls.