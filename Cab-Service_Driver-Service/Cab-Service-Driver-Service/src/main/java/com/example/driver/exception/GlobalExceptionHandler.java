package com.example.driver.exception;

import com.example.driver.payload.ExceptionDto;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.HttpStatusCode;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.context.request.WebRequest;
import org.springframework.web.servlet.mvc.method.annotation.ResponseEntityExceptionHandler;

import java.time.LocalDate;

@ControllerAdvice
public class GlobalExceptionHandler extends ResponseEntityExceptionHandler {

    @ExceptionHandler(Exception.class)
    public final ResponseEntity<ExceptionDto> handleAllExceptions(Exception ex, WebRequest request) {
        ExceptionDto exRes = new ExceptionDto(LocalDate.now(), ex.getMessage(),
                request.getDescription(false), HttpStatus.INTERNAL_SERVER_ERROR.toString());
        return new ResponseEntity<>(exRes, HttpStatus.INTERNAL_SERVER_ERROR);
    }

    @ExceptionHandler(RuntimeException.class)
    public final ResponseEntity<ExceptionDto> handleRuntimeExceptions(RuntimeException ex, WebRequest request) {
        ExceptionDto exRes = new ExceptionDto(LocalDate.now(), ex.getMessage(),
                request.getDescription(false), HttpStatus.BAD_REQUEST.toString());
        return new ResponseEntity<>(exRes, HttpStatus.BAD_REQUEST);
    }

    @ExceptionHandler(UserAlreadyPresentException.class)
    public final ResponseEntity<ExceptionDto> handleUserAlreadyPresentException(Exception ex, WebRequest request) {
        ExceptionDto exRes = new ExceptionDto(LocalDate.now(), ex.getMessage(),
                request.getDescription(false), HttpStatus.BAD_REQUEST.toString());
        return new ResponseEntity<>(exRes, HttpStatus.BAD_REQUEST);
    }

    @ExceptionHandler(UserNotFoundException.class)
    public final ResponseEntity<ExceptionDto> handleUserNotFoundException(Exception ex, WebRequest request) {
        ExceptionDto exRes = new ExceptionDto(LocalDate.now(), ex.getMessage(),
                request.getDescription(false), HttpStatus.NOT_FOUND.toString());
        return new ResponseEntity<>(exRes, HttpStatus.NOT_FOUND);
    }


    @Override
    protected ResponseEntity<Object> handleMethodArgumentNotValid(MethodArgumentNotValidException ex, HttpHeaders headers, HttpStatusCode status, WebRequest request) {
        String message = ex.getFieldError().getDefaultMessage();
        ExceptionDto er = new ExceptionDto(LocalDate.now(), message,
                request.getDescription(false),
                status.toString());
        return new ResponseEntity<>(er,HttpStatus.BAD_REQUEST);
    }

}
