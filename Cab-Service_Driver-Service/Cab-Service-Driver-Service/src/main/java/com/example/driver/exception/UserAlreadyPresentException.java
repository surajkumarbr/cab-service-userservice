package com.example.driver.exception;

public class UserAlreadyPresentException extends Exception {
    public UserAlreadyPresentException(String msg) {
        super(msg);
    }
}
