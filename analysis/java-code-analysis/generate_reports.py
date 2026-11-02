import json
from pathlib import Path

# Static-analysis timestamp supplied by user
GENERATED_AT = "2026-11-02T13:58:44.338+05:30"
REPO_NAME = "surajkumarbr/cab-service-userservice (analyzed module: Cab-Service-Driver-Service)"

# Repo-relative paths
POM   = "Cab-Service_Driver-Service/Cab-Service-Driver-Service/pom.xml"
APP   = "Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/Application.java"
CTRL  = "Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/controller/DriverController.java"
DAO   = "Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/dao/impl/DriverDaoImpl.java"
REPO  = "Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/repository/DriverRepository.java"
ENTITY= "Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/entity/Driver.java"
BASE  = "Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/entity/BaseEntity.java"
EXH   = "Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/exception/GlobalExceptionHandler.java"
DTO   = "Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/payload/DriverDto.java"
UPD   = "Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/payload/UpdateDriverDetailsDto.java"
PROPS = "Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/resources/application.properties"

# Verified line ranges from grep output (do not invent beyond file bounds)
LINES = {
  APP: (12, 30),
  CTRL: (18, 65),
  DAO: (21, 128),
  REPO: (8, 17),
  ENTITY: (8, 24),
  BASE: (15, 34),
  EXH: (16, 57),
  DTO: (8, 18),
  UPD: (6, 10),
}


def ev(path, symbol=None, method=None, line_start=None, line_end=None, note=""):
    return {
        "path": path,
        "symbol": symbol,
        "method": method,
        "line_start": line_start,
        "line_end": line_end,
        "note": note,
    }


def main():
    repo_root = str(Path(".").resolve())
    out_dir = Path("analysis") / "java-code-analysis"
    out_dir.mkdir(parents=True, exist_ok=True)

    report = {
        "report_metadata": {
            "generated_at": GENERATED_AT,
            "agent": "java-code-analyst",
            "skill_version": "java-code-analysis@1.0",
        },
        "repository": {"root": repo_root, "name": REPO_NAME},
        "coverage": {
            "status": "partial",
            "modules": [
                {
                    "name": "Cab-Service-Driver-Service",
                    "status": "inspected",
                    "notes": "Single Maven module found in this workspace snapshot. target/ build output excluded from semantic review.",
                }
            ],
        },
        "technology_stack": [
            {"name": "Java", "version": "17", "evidence": [ev(POM, "pom.xml", None, 29, 32, "java.version=17")]} ,
            {"name": "Spring Boot", "version": "3.3.1", "evidence": [ev(POM, "pom.xml", None, 5, 10, "spring-boot-starter-parent=3.3.1")]} ,
            {"name": "Spring Cloud", "version": "2023.0.2", "evidence": [ev(POM, "pom.xml", None, 29, 92, "spring-cloud.version and dependencyManagement import")]} ,
            {"name": "Spring Web (MVC)", "version": None, "evidence": [ev(POM, "pom.xml", None, 39, 42, "spring-boot-starter-web")]} ,
            {"name": "Spring Data JPA", "version": None, "evidence": [ev(POM, "pom.xml", None, 35, 38, "spring-boot-starter-data-jpa")]} ,
            {"name": "MySQL JDBC", "version": None, "evidence": [
                ev(POM, "pom.xml", None, 50, 54, "mysql-connector-j runtime"),
                ev(PROPS, "application.properties", None, 3, 7, "JDBC url/user configured; password redacted")
            ]} ,
            {"name": "Eureka Client", "version": None, "evidence": [
                ev(POM, "pom.xml", None, 74, 77, "spring-cloud-starter-netflix-eureka-client"),
                ev(PROPS, "application.properties", None, 12, 12, "eureka.instance.hostname")
            ]} ,
            {"name": "OpenFeign", "version": None, "evidence": [
                ev(POM, "pom.xml", None, 78, 81, "spring-cloud-starter-openfeign"),
                ev(APP, "com.example.driver.Application", None, 12, 15, "@EnableFeignClients")
            ]} ,
            {"name": "ModelMapper", "version": "2.4.4", "evidence": [
                ev(POM, "pom.xml", None, 65, 69, "modelmapper=2.4.4"),
                ev(APP, "com.example.driver.Application", "modelMapper", 21, 24, "ModelMapper bean")
            ]} ,
            {"name": "BCrypt password hashing", "version": None, "evidence": [
                ev(APP, "com.example.driver.Application", "passwordEncoder", 26, 29, "BCryptPasswordEncoder bean")
            ]} ,
        ],
        "modules": [
            {
                "name": "Cab-Service-Driver-Service",
                "path": "Cab-Service_Driver-Service/Cab-Service-Driver-Service",
                "build_system": "maven",
            }
        ],
        "architecture": {
            "style": "Spring MVC layered: controller -> service -> DAO -> repository -> JPA entity",
            "components": [
                {"name": "DriverController", "type": "controller", "path": CTRL},
                {"name": "DriverServiceImpl", "type": "service", "path": "Cab-Service_Driver-Service/Cab-Service-Driver-Service/src/main/java/com/example/driver/service/impl/DriverServiceImpl.java"},
                {"name": "DriverDaoImpl", "type": "dao", "path": DAO},
                {"name": "DriverRepository", "type": "repository", "path": REPO},
                {"name": "Driver", "type": "entity", "path": ENTITY},
                {"name": "GlobalExceptionHandler", "type": "exception-handler", "path": EXH},
            ],
            "relationships": [
                {"from": "DriverController", "to": "DriverService", "type": "calls"},
                {"from": "DriverServiceImpl", "to": "DriverDao", "type": "delegates"},
                {"from": "DriverDaoImpl", "to": "DriverRepository", "type": "uses"},
            ],
            "notes": [
                "Service layer is mostly delegation; DAO contains most business logic.",
                "OpenFeign enabled but no @FeignClient declarations were found in this snapshot (outbound calls not traceable).",
            ],
        },
        "classes": [
            {
                "name": "Application",
                "qualified_name": "com.example.driver.Application",
                "type": "class",
                "path": APP,
                "responsibility": "Spring Boot entry point; enables JPA auditing and Feign; defines ModelMapper and PasswordEncoder beans.",
                "evidence": [ev(APP, "com.example.driver.Application", None, *LINES[APP], "Annotations and @Bean methods")],
            },
            {
                "name": "DriverController",
                "qualified_name": "com.example.driver.controller.DriverController",
                "type": "class",
                "path": CTRL,
                "responsibility": "REST endpoints under /api/driver.",
                "evidence": [ev(CTRL, "DriverController", None, *LINES[CTRL], "@RestController + mappings")],
            },
            {
                "name": "DriverDaoImpl",
                "qualified_name": "com.example.driver.dao.impl.DriverDaoImpl",
                "type": "class",
                "path": DAO,
                "responsibility": "Implements business rules (uniqueness checks, password hashing, availability default) and persistence operations.",
                "evidence": [ev(DAO, "DriverDaoImpl", None, *LINES[DAO], "DAO methods")],
            },
            {
                "name": "DriverRepository",
                "qualified_name": "com.example.driver.repository.DriverRepository",
                "type": "interface",
                "path": REPO,
                "responsibility": "Spring Data JPA repository for Driver (derived query methods).",
                "evidence": [ev(REPO, "DriverRepository", None, *LINES[REPO], "existsByEmail/existsByUsername/findByUsername")],
            },
            {
                "name": "Driver",
                "qualified_name": "com.example.driver.entity.Driver",
                "type": "class",
                "path": ENTITY,
                "responsibility": "JPA entity for drivers, including password, availability and default role.",
                "evidence": [ev(ENTITY, "Driver", None, *LINES[ENTITY], "@Entity @Table and fields")],
            },
            {
                "name": "BaseEntity",
                "qualified_name": "com.example.driver.entity.BaseEntity",
                "type": "class",
                "path": BASE,
                "responsibility": "Auditing base entity with created/updated timestamps and principals.",
                "evidence": [ev(BASE, "BaseEntity", None, *LINES[BASE], "@MappedSuperclass auditing")],
            },
            {
                "name": "GlobalExceptionHandler",
                "qualified_name": "com.example.driver.exception.GlobalExceptionHandler",
                "type": "class",
                "path": EXH,
                "responsibility": "Maps domain/validation exceptions to ExceptionDto.",
                "evidence": [ev(EXH, "GlobalExceptionHandler", None, *LINES[EXH], "@ControllerAdvice")],
            },
            {
                "name": "DriverDto",
                "qualified_name": "com.example.driver.payload.DriverDto",
                "type": "class",
                "path": DTO,
                "responsibility": "DTO for responses; hides password via @JsonIgnore.",
                "evidence": [ev(DTO, "DriverDto", None, *LINES[DTO], "@JsonIgnore password")],
            },
        ],
        "apis": [
            {
                "id": "API-DRIVER-001",
                "http_method": "POST",
                "path": "/api/driver/add",
                "controller": "com.example.driver.controller.DriverController",
                "method": "addOneDriver",
                "service_calls": [
                    "DriverService.addOneDriver",
                    "DriverDaoImpl.addOneDriver",
                    "DriverRepository.existsByEmail",
                    "DriverRepository.existsByUsername",
                    "PasswordEncoder.encode",
                    "DriverRepository.save",
                ],
                "request_type": "com.example.driver.entity.Driver",
                "response_type": "org.springframework.http.ResponseEntity<com.example.driver.payload.DriverDto>",
                "evidence": [
                    ev(CTRL, "DriverController", "addOneDriver", 28, 31, "Controller mapping"),
                    ev(DAO, "DriverDaoImpl", "addOneDriver", 31, 45, "Uniqueness checks + encode + availability default + save"),
                ],
            },
            {
                "id": "API-DRIVER-002",
                "http_method": "GET",
                "path": "/api/driver/{driverId}",
                "controller": "com.example.driver.controller.DriverController",
                "method": "getDriverById",
                "service_calls": ["DriverService.getDriverById", "DriverDaoImpl.getDriverById", "DriverRepository.findById"],
                "request_type": None,
                "response_type": "org.springframework.http.ResponseEntity<com.example.driver.payload.DriverDto>",
                "evidence": [
                    ev(CTRL, "DriverController", "getDriverById", 33, 36, "Controller mapping"),
                    ev(DAO, "DriverDaoImpl", "getDriverById", 49, 58, "Throws UserNotFoundException if missing"),
                ],
            },
            {
                "id": "API-DRIVER-003",
                "http_method": "DELETE",
                "path": "/api/driver/{driverId}",
                "controller": "com.example.driver.controller.DriverController",
                "method": "deleteDriverUsingId",
                "service_calls": ["DriverService.deleteDriverById", "DriverDaoImpl.deleteDriverById", "DriverRepository.delete"],
                "request_type": None,
                "response_type": "org.springframework.http.ResponseEntity<com.example.driver.payload.DriverDto>",
                "evidence": [
                    ev(CTRL, "DriverController", "deleteDriverUsingId", 38, 41, "Controller mapping"),
                    ev(DAO, "DriverDaoImpl", "deleteDriverById", 61, 70, "Deletes after existence check"),
                ],
            },
            {
                "id": "API-DRIVER-004",
                "http_method": "PUT",
                "path": "/api/driver/update/{driverId}",
                "controller": "com.example.driver.controller.DriverController",
                "method": "updateDriverDetails",
                "service_calls": ["DriverService.updateDriverDetails", "DriverDaoImpl.updateDriverDetails", "DriverRepository.save"],
                "request_type": "com.example.driver.payload.UpdateDriverDetailsDto",
                "response_type": "org.springframework.http.ResponseEntity<com.example.driver.payload.DriverDto>",
                "evidence": [
                    ev(CTRL, "DriverController", "updateDriverDetails", 43, 47, "Controller mapping"),
                    ev(DAO, "DriverDaoImpl", "updateDriverDetails", 73, 90, "Updates username/email and saves"),
                ],
            },
            {
                "id": "API-DRIVER-005",
                "http_method": "GET",
                "path": "/api/driver/all",
                "controller": "com.example.driver.controller.DriverController",
                "method": "getAllDriver",
                "service_calls": ["DriverService.getAllDriverDetails", "DriverDaoImpl.getAllDriverDetails", "DriverRepository.findAll"],
                "request_type": None,
                "response_type": "org.springframework.http.ResponseEntity<java.util.List<com.example.driver.payload.DriverDto>>",
                "evidence": [
                    ev(CTRL, "DriverController", "getAllDriver", 49, 52, "Controller mapping"),
                    ev(DAO, "DriverDaoImpl", "getAllDriverDetails", 95, 100, "Maps entities to DTOs"),
                ],
            },
            {
                "id": "API-DRIVER-006",
                "http_method": "PUT",
                "path": "/api/driver/change-status/{driverId}",
                "controller": "com.example.driver.controller.DriverController",
                "method": "updateDriverStatus",
                "service_calls": ["DriverService.updateDriverStatus", "DriverDaoImpl.updateDriverStatus", "DriverRepository.save"],
                "request_type": "com.example.driver.payload.DriverDto",
                "response_type": "org.springframework.http.ResponseEntity<com.example.driver.payload.DriverDto>",
                "evidence": [
                    ev(CTRL, "DriverController", "updateDriverStatus", 54, 57, "Controller mapping"),
                    ev(DAO, "DriverDaoImpl", "updateDriverStatus", 103, 113, "Updates availability and saves"),
                ],
            },
            {
                "id": "API-DRIVER-007",
                "http_method": "GET",
                "path": "/api/driver/name/{username}",
                "controller": "com.example.driver.controller.DriverController",
                "method": "getDriverByName",
                "service_calls": ["DriverService.getDriverByName", "DriverDaoImpl.getDriverByName", "DriverRepository.findByUsername"],
                "request_type": None,
                "response_type": "java.util.Optional<com.example.driver.entity.Driver>",
                "evidence": [
                    ev(CTRL, "DriverController", "getDriverByName", 59, 62, "Returns Optional<Driver> directly"),
                    ev(DAO, "DriverDaoImpl", "getDriverByName", 115, 119, "findByUsername")
                ],
            },
        ],
        "business_rules": [
            {
                "id": "BR-001",
                "name": "Driver email must be unique on creation",
                "description": "Create-driver rejects a request when an existing Driver uses the same email.",
                "conditions": ["driverRepository.existsByEmail(email) returns true"],
                "actions": ["Throw UserAlreadyPresentException (mapped to HTTP 400)"] ,
                "confidence": "high",
                "evidence": [
                    ev(DAO, "DriverDaoImpl", "addOneDriver", 33, 35, "existsByEmail check"),
                    ev(EXH, "GlobalExceptionHandler", "handleUserAlreadyPresentException", 33, 38, "Maps to 400")
                ],
            },
            {
                "id": "BR-002",
                "name": "Driver username must be unique on creation",
                "description": "Create-driver rejects a request when an existing Driver uses the same username.",
                "conditions": ["driverRepository.existsByUsername(username) returns true"],
                "actions": ["Throw UserAlreadyPresentException (mapped to HTTP 400)"] ,
                "confidence": "high",
                "evidence": [ev(DAO, "DriverDaoImpl", "addOneDriver", 36, 38, "existsByUsername check")],
            },
            {
                "id": "BR-003",
                "name": "Persisted driver passwords are stored hashed (BCrypt)",
                "description": "Before persisting a new Driver, the raw password is encoded via PasswordEncoder (BCryptPasswordEncoder bean).",
                "conditions": ["Creating driver via POST /api/driver/add"],
                "actions": ["driver.password = passwordEncoder.encode(rawPassword)"],
                "confidence": "high",
                "evidence": [
                    ev(APP, "Application", "passwordEncoder", 26, 29, "BCryptPasswordEncoder bean"),
                    ev(DAO, "DriverDaoImpl", "addOneDriver", 40, 42, "encode() invoked before save")
                ],
            },
            {
                "id": "BR-004",
                "name": "New drivers default to available",
                "description": "When creating a driver, availability is set to true before persistence.",
                "conditions": ["Creating driver via POST /api/driver/add"],
                "actions": ["driver.availability = true"],
                "confidence": "high",
                "evidence": [ev(DAO, "DriverDaoImpl", "addOneDriver", 41, 44, "Sets availability(true)")],
            },
            {
                "id": "BR-005",
                "name": "Validation failures return HTTP 400 with field message",
                "description": "On create, validation failures return a 400 ExceptionDto containing the first field error message.",
                "conditions": ["@Valid request body fails constraints (@NotEmpty etc.)"],
                "actions": ["GlobalExceptionHandler.handleMethodArgumentNotValid returns 400 with ExceptionDto(message=fieldError.defaultMessage)"],
                "confidence": "high",
                "evidence": [
                    ev(CTRL, "DriverController", "addOneDriver", 28, 31, "@Valid on request body"),
                    ev(ENTITY, "Driver", None, 15, 18, "@NotEmpty constraints"),
                    ev(EXH, "GlobalExceptionHandler", "handleMethodArgumentNotValid", 48, 55, "400 mapping")
                ],
            },
        ],
        "data_flows": [
            {
                "name": "Create driver",
                "steps": [
                    "HTTP POST /api/driver/add",
                    "DriverController.addOneDriver -> DriverServiceImpl.addOneDriver -> DriverDaoImpl.addOneDriver",
                    "DAO checks uniqueness (email, username)",
                    "DAO hashes password and sets availability=true",
                    "DAO saves via DriverRepository.save and returns DriverDto",
                ],
                "evidence": [
                    ev(CTRL, "DriverController", "addOneDriver", 28, 31, "Entry point"),
                    ev(DAO, "DriverDaoImpl", "addOneDriver", 31, 45, "Implementation")
                ],
            },
            {
                "name": "Change driver availability",
                "steps": [
                    "HTTP PUT /api/driver/change-status/{driverId}",
                    "DAO loads Driver by id; if missing throws UserNotFoundException",
                    "DAO sets availability from request DTO and saves",
                ],
                "evidence": [
                    ev(CTRL, "DriverController", "updateDriverStatus", 54, 57, "Entry point"),
                    ev(DAO, "DriverDaoImpl", "updateDriverStatus", 103, 113, "Implementation")
                ],
            },
        ],
        "persistence": {
            "entities": [
                {
                    "name": "Driver",
                    "qualified_name": "com.example.driver.entity.Driver",
                    "table": "drives",
                    "evidence": [ev(ENTITY, "Driver", None, 9, 22, "@Table(name=drives) and fields")],
                },
                {
                    "name": "BaseEntity",
                    "qualified_name": "com.example.driver.entity.BaseEntity",
                    "table": None,
                    "evidence": [ev(BASE, "BaseEntity", None, *LINES[BASE], "Auditing fields")],
                },
            ],
            "repositories": [
                {
                    "name": "DriverRepository",
                    "qualified_name": "com.example.driver.repository.DriverRepository",
                    "entity": "Driver",
                    "methods": ["existsByEmail", "existsByUsername", "findByUsername"],
                    "evidence": [ev(REPO, "DriverRepository", None, 8, 14, "Repository methods")],
                }
            ],
            "migrations": [],
            "notes": [
                "No Flyway/Liquibase migrations were found in this snapshot.",
                "application.properties indicates Hibernate ddl-auto=update (dev-friendly; risky for prod without profiles).",
            ],
        },
        "integrations": [
            {"name": "MySQL", "type": "database", "direction": "outbound", "evidence": [ev(PROPS, "application.properties", None, 3, 6, "Datasource JDBC config")]},
            {"name": "Eureka", "type": "service-discovery", "direction": "outbound", "evidence": [ev(POM, "pom.xml", None, 74, 77, "Eureka client dependency")]} ,
            {"name": "OpenFeign", "type": "http-client-framework", "direction": "outbound", "evidence": [ev(APP, "Application", None, 12, 15, "@EnableFeignClients")]} ,
        ],
        "security": {
            "observations": [
                {
                    "description": "Passwords are BCrypt-hashed before persisting new drivers.",
                    "status": "confirmed",
                    "evidence": [
                        ev(APP, "Application", "passwordEncoder", 26, 29, "BCryptPasswordEncoder bean"),
                        ev(DAO, "DriverDaoImpl", "addOneDriver", 40, 42, "encode() before save"),
                    ],
                },
                {
                    "description": "DriverDto.password is excluded from JSON responses via @JsonIgnore.",
                    "status": "confirmed",
                    "evidence": [ev(DTO, "DriverDto", None, 10, 16, "@JsonIgnore on password")],
                },
                {
                    "description": "GET /api/driver/name/{username} returns Driver entity directly; entity includes password field and is not annotated to suppress serialization.",
                    "status": "confirmed",
                    "evidence": [
                        ev(CTRL, "DriverController", "getDriverByName", 59, 62, "Returns Optional<Driver>"),
                        ev(ENTITY, "Driver", None, 17, 20, "password field present")
                    ],
                },
            ],
            "not_assessed": [
                "Authentication/authorization: no SecurityFilterChain/@EnableWebSecurity config classes were found in this snapshot.",
                "CORS/CSRF configuration.",
            ],
        },
        "technical_risks": [
            {
                "id": "TR-001",
                "description": "Sensitive data exposure: /api/driver/name/{username} returns Driver entity including password.",
                "severity": "high",
                "status": "confirmed",
                "evidence": [
                    ev(CTRL, "DriverController", "getDriverByName", 59, 62, "Entity returned directly"),
                    ev(ENTITY, "Driver", None, 17, 20, "password field")
                ],
                "recommendation": "Return DriverDto (or a safe response type) instead of Driver; ensure password is never serialized; return 404 when not found.",
            },
            {
                "id": "TR-002",
                "description": "Schema drift risk: Hibernate ddl-auto=update and generate-ddl=true are configured.",
                "severity": "medium",
                "status": "confirmed",
                "evidence": [ev(PROPS, "application.properties", None, 8, 10, "ddl-auto=update; generate-ddl=true")],
                "recommendation": "Adopt Flyway/Liquibase and use profiles; set ddl-auto=validate/none in prod.",
            },
            {
                "id": "TR-003",
                "description": "Auditing last-modified columns are marked updatable=false, likely preventing updates from being persisted.",
                "severity": "medium",
                "status": "confirmed",
                "evidence": [ev(BASE, "BaseEntity", None, 26, 31, "updatedAt/updateBy updatable=false")],
                "recommendation": "Remove updatable=false for @LastModifiedDate/@LastModifiedBy fields or confirm intended DB behavior.",
            },
            {
                "id": "TR-004",
                "description": "UpdateDriverDetailsDto includes password but update flow does not update/encode password.",
                "severity": "low",
                "status": "confirmed",
                "evidence": [
                    ev(UPD, "UpdateDriverDetailsDto", None, *LINES[UPD], "password field present"),
                    ev(DAO, "DriverDaoImpl", "updateDriverDetails", 84, 89, "Only username/email updated")
                ],
                "recommendation": "Remove password from the DTO or implement a dedicated change-password endpoint with BCrypt encoding.",
            },
        ],
        "recommendations": [
            {
                "priority": "high",
                "description": "Do not return JPA entities from controllers; return DTOs that exclude sensitive fields.",
                "rationale": "Prevents accidental password exposure and enforces a stable API contract.",
            },
            {
                "priority": "medium",
                "description": "Move schema management to migrations and use environment-specific profiles.",
                "rationale": "ddl-auto=update is risky outside development; migrations provide controlled, reviewable changes.",
            },
            {
                "priority": "medium",
                "description": "Review auditing column mutability for last-modified fields.",
                "rationale": "Current mapping may prevent updatedAt/updateBy from persisting.",
            },
        ],
        "limitations": [
            "Single-module snapshot; no additional modules were present in this workspace.",
            "No OpenAPI/Swagger specs found; API inventory derived from Spring MVC annotations.",
            "No DB migration scripts found; schema inferred from JPA annotations and Hibernate configuration.",
            "Static analysis only; runtime behavior and profile overrides not executed.",
        ],
    }

    (out_dir / "analysis-report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    md_lines = []
    md_lines.append("# Java Repository Analysis Report")
    md_lines.append("")
    md_lines.append(f"> Generated: {GENERATED_AT} | Repository: {REPO_NAME} | Coverage: {report['coverage']['status']}")
    md_lines.append("")
    md_lines.append("## Executive summary")
    md_lines.append("Single Spring Boot driver-service module exposing REST endpoints under `/api/driver` with MySQL persistence via Spring Data JPA.")
    md_lines.append("Business logic is primarily implemented in `DriverDaoImpl`.")
    md_lines.append("")
    md_lines.append("High-priority finding: `GET /api/driver/name/{username}` returns the `Driver` entity (includes `password`) instead of a safe DTO.")
    md_lines.append("")

    md_lines.append("## Technology stack")
    for t in report["technology_stack"]:
        md_lines.append(f"- {t['name']} {('('+t['version']+')') if t['version'] else ''}")
    md_lines.append("")

    md_lines.append("## REST API inventory")
    for a in report["apis"]:
        md_lines.append(f"- {a['http_method']} {a['path']} -> {a['controller']}#{a['method']}")
    md_lines.append("")

    md_lines.append("## Business rules (implemented)")
    for r in report["business_rules"]:
        md_lines.append(f"- {r['id']}: {r['name']} (confidence: {r['confidence']})")
    md_lines.append("")

    md_lines.append("## Technical risks")
    for r in report["technical_risks"]:
        md_lines.append(f"- {r['id']} [{r['severity']}/{r['status']}]: {r['description']}")
        md_lines.append(f"  Recommendation: {r['recommendation']}")
    md_lines.append("")

    md_lines.append("## Evidence index (high-signal)")
    md_lines.append(f"- `{CTRL}`:18-65 (controller mappings)")
    md_lines.append(f"- `{DAO}`:21-128 (DAO business logic)")
    md_lines.append(f"- `{ENTITY}`:8-24 (entity mapping)")
    md_lines.append(f"- `{EXH}`:16-57 (exception mapping)")
    md_lines.append("")

    md_lines.append("## Limitations")
    for l in report["limitations"]:
        md_lines.append(f"- {l}")
    md_lines.append("")

    (out_dir / "analysis-report.md").write_text("\n".join(md_lines), encoding="utf-8")


if __name__ == "__main__":
    main()
