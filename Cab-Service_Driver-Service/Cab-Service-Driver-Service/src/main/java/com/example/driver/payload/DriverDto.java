package com.example.driver.payload;

import com.fasterxml.jackson.annotation.JsonIgnore;
import lombok.Data;

import java.time.LocalDateTime;

@Data
public class DriverDto {
    private Long driverId;
    private String username;
    @JsonIgnore
    private String password;
    private String email;
    private Boolean availability;
    private String role = "ROLE_DRIVER";

}
