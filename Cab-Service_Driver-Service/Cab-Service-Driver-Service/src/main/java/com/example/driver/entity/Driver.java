package com.example.driver.entity;

import jakarta.persistence.*;
import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotEmpty;
import lombok.Data;

@Data
@Entity
@Table(name = "drives")
public class Driver extends BaseEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long driverId;
    @NotEmpty(message = "user name should not be null")
    private String username;
    @NotEmpty(message = "password should not be nul")
    private String password;
    @Email
    private String email;
    private Boolean availability;
    private String role = "ROLE_DRIVER";

}
