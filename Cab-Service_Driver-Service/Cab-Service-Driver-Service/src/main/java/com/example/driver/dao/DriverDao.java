package com.example.driver.dao;

import com.example.driver.entity.Driver;
import com.example.driver.exception.UserAlreadyPresentException;
import com.example.driver.exception.UserNotFoundException;
import com.example.driver.payload.DriverDto;
import com.example.driver.payload.UpdateDriverDetailsDto;
import org.springframework.http.ResponseEntity;

import java.util.List;
import java.util.Optional;

public interface DriverDao {
    ResponseEntity<DriverDto> addOneDriver(Driver driver) throws UserAlreadyPresentException;

    ResponseEntity<DriverDto> getDriverById(Long driverId) throws UserNotFoundException;

    ResponseEntity<DriverDto> deleteDriverById(Long driverId) throws UserNotFoundException;

    ResponseEntity<DriverDto> updateDriverDetails(Long driverId, UpdateDriverDetailsDto updateDriverDetailsDto) throws UserAlreadyPresentException, UserNotFoundException;

    ResponseEntity<List<DriverDto>> getAllDriverDetails();

    ResponseEntity<DriverDto> updateDriverStatus(Long driverId, DriverDto driverDto) throws UserNotFoundException;

    Optional<Driver> getDriverByName(String username);
}
