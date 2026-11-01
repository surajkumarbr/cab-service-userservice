package com.example.driver.payload;

import lombok.AllArgsConstructor;
import lombok.Data;

import java.time.LocalDate;

@Data
@AllArgsConstructor
public class ExceptionDto {
    private LocalDate timestamp;
    private String message;
    private String details;
    private String httpCodeMessage;
}
