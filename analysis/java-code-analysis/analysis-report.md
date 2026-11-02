# Java Repository Analysis Report

> Generated: 2026-11-02T13:42:39.855+05:30 | Repository: cab-service-userservice | Coverage: complete

## 1. Executive Summary
This repository contains a single Spring Boot 3.3.1 (Java 17) module implementing a Driver service.
It exposes 7 REST endpoints under `/api/driver` and persists `Driver` entities to a MySQL datasource via Spring Data JPA.

Notable confirmed risks:
- `spring.jpa.hibernate.ddl-auto=update` (schema drift risk) (Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/resources/application.properties:8-9)
- `GET /api/driver/name/{username}` returns the `Driver` entity which contains a `password` field (possible hash exposure) (Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/controller/DriverController.java:59-62, Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/entity/Driver.java:17-22)

## 2. Repository Scope and Coverage
- Repository root: `C:\ADLC\DA\cca_distributed_agentic_framework\custom_agent_helper_worker\custom_agent_helper_worker\cache\src_k3a6nvgv`
- Module reviewed: `Cab-Service-Driver-Service` (`Cab-Service_Driver-Service/Cab-Service-Driver-Service`)
- Inventory artifact: `analysis/java-code-analysis/java-inventory.json`
- Excluded from semantic review: build output directories (e.g., `**/target/**`)

## 3. Technology Stack (evidence-backed)
| Technology | Version | Evidence |
|---|---:|---|
| Spring Boot | 3.3.1 | `Cab-Service_Driver-Service/Cab-Service-Driver-Service/pom.xml:5-10` |
| Java | 17 | `Cab-Service_Driver-Service/Cab-Service-Driver-Service/pom.xml:29-33` |
| Spring Web | (via BOM) | `Cab-Service_Driver-Service/Cab-Service-Driver-Service/pom.xml:39-42`, `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/controller/DriverController.java:18-65` |
| Spring Data JPA | (via BOM) | `Cab-Service_Driver-Service/Cab-Service-Driver-Service/pom.xml:35-38`, `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/repository/DriverRepository.java:8-13` |
| MySQL Connector/J | runtime | `Cab-Service_Driver-Service/Cab-Service-Driver-Service/pom.xml:50-54`, `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/resources/application.properties:3-6` |
| Bean Validation | (via BOM) | `Cab-Service_Driver-Service/Cab-Service-Driver-Service/pom.xml:70-73`, `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/entity/Driver.java:15-20`, `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/controller/DriverController.java:28-31`, `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/exception/GlobalExceptionHandler.java:48-54` |
| ModelMapper | 2.4.4 | `Cab-Service_Driver-Service/Cab-Service-Driver-Service/pom.xml:65-69`, `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/Application.java:21-24`, `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/dao/impl/DriverDaoImpl.java:121-127` |
| Eureka Client | (via BOM) | `Cab-Service_Driver-Service/Cab-Service-Driver-Service/pom.xml:74-77`, `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/resources/application.properties:12` |
| OpenFeign | (via BOM) | `Cab-Service_Driver-Service/Cab-Service-Driver-Service/pom.xml:78-81`, `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/Application.java:12-15` |

## 4. Architecture and Component Relationships
Observed call path layering:
`DriverController` ? `DriverServiceImpl` ? `DriverDaoImpl` ? `DriverRepository` ? MySQL.

Evidence:
- Controller mappings: `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/controller/DriverController.java:18-65`
- Service delegation: `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/service/impl/DriverServiceImpl.java:17-55`
- DAO persistence + rules: `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/dao/impl/DriverDaoImpl.java:31-113`
- Repository derived queries: `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/repository/DriverRepository.java:8-13`

## 5. REST/API Inventory
| ID | Method | Path | Controller method | Key DAO method | Evidence |
|---|---|---|---|---|---|
| API-DRIVER-001 | POST | /api/driver/add | addOneDriver | DriverDaoImpl#addOneDriver | `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/controller/DriverController.java:28-31`, `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/dao/impl/DriverDaoImpl.java:31-44` |
| API-DRIVER-002 | GET | /api/driver/{driverId} | getDriverById | DriverDaoImpl#getDriverById | `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/controller/DriverController.java:33-36`, `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/dao/impl/DriverDaoImpl.java:49-57` |
| API-DRIVER-003 | DELETE | /api/driver/{driverId} | deleteDriverUsingId | DriverDaoImpl#deleteDriverById | `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/controller/DriverController.java:38-41`, `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/dao/impl/DriverDaoImpl.java:61-69` |
| API-DRIVER-004 | PUT | /api/driver/update/{driverId} | updateDriverDetails | DriverDaoImpl#updateDriverDetails | `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/controller/DriverController.java:43-47`, `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/dao/impl/DriverDaoImpl.java:73-89` |
| API-DRIVER-005 | GET | /api/driver/all | getAllDriver | DriverDaoImpl#getAllDriverDetails | `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/controller/DriverController.java:49-52`, `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/dao/impl/DriverDaoImpl.java:95-99` |
| API-DRIVER-006 | PUT | /api/driver/change-status/{driverId} | updateDriverStatus | DriverDaoImpl#updateDriverStatus | `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/controller/DriverController.java:54-57`, `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/dao/impl/DriverDaoImpl.java:103-112` |
| API-DRIVER-007 | GET | /api/driver/name/{username} | getDriverByName | DriverDaoImpl#getDriverByName | `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/controller/DriverController.java:59-62`, `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/dao/impl/DriverDaoImpl.java:116-118` |

## 6. Business Rules (implemented)
- Reject create if email exists: `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/dao/impl/DriverDaoImpl.java:33-35`
- Reject create if username exists: `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/dao/impl/DriverDaoImpl.java:36-38`
- Hash password on create (BCrypt): `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/Application.java:26-29`, `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/dao/impl/DriverDaoImpl.java:40`
- Default availability=true on create: `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/dao/impl/DriverDaoImpl.java:41`
- Guard missing driverId (throw UserNotFoundException): `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/dao/impl/DriverDaoImpl.java:50-53`, `62-65`, `80-83`, `104-107`
- Update details updates username/email only: `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/dao/impl/DriverDaoImpl.java:84-89`

## 7. Persistence / DB Mapping
- `Driver` entity maps to table `drives`: `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/entity/Driver.java:9-24`
- Auditing fields are defined in `BaseEntity`: `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/entity/BaseEntity.java:15-31`
- No migration tooling files were found; schema appears managed by Hibernate `ddl-auto=update`: `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/resources/application.properties:8-9`

## 8. Validation, Exceptions, and Error Mapping
- Validation errors mapped to 400 by global handler: `Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/exception/GlobalExceptionHandler.java:48-54`

## 9. Limitations
- No runtime/deployment manifests or environment profiles were analyzed.
- No explicit authentication/authorization configuration (e.g., SecurityFilterChain) was found in inventoried production sources.
