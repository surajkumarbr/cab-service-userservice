package com.example.driver.payload;

import lombok.Data;

@Data
public class UpdateDriverDetailsDto {
    private String username;
    private String password;
    private String email;
}
