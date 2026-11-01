package com.example.driver.controller;

import com.example.driver.entity.Driver;
import com.example.driver.exception.UserAlreadyPresentException;
import com.example.driver.exception.UserNotFoundException;
import com.example.driver.payload.DriverDto;
import com.example.driver.payload.UpdateDriverDetailsDto;
import com.example.driver.repository.DriverRepository;
import com.example.driver.service.DriverService;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/api/driver")
public class DriverController {

    @Autowired
    DriverService driverService;

    @Autowired
    DriverRepository repository;

    @PostMapping("/add")
    public ResponseEntity<DriverDto> addOneDriver(@Valid @RequestBody Driver driver) throws UserAlreadyPresentException {
        return driverService.addOneDriver(driver);
    }

    @GetMapping("/{driverId}")
    public ResponseEntity<DriverDto> getDriverById(@PathVariable("driverId") Long driverId) throws UserNotFoundException {
        return driverService.getDriverById(driverId);
    }

    @DeleteMapping("/{driverId}")
    public ResponseEntity<DriverDto> deleteDriverUsingId(@PathVariable("driverId") Long driverId) throws UserNotFoundException {
        return driverService.deleteDriverById(driverId);
    }

    @PutMapping("/update/{driverId}")
    public ResponseEntity<DriverDto> updateDriverDetails(@PathVariable("driverId") Long driverId, @RequestBody UpdateDriverDetailsDto updateDriverDetailsDto) throws UserNotFoundException, UserAlreadyPresentException {
        return driverService.updateDriverDetails(driverId, updateDriverDetailsDto);

    }

    @GetMapping("/all")
    public ResponseEntity<List<DriverDto>> getAllDriver() {
        return driverService.getAllDriverDetails();
    }

    @PutMapping("/change-status/{driverId}")
    public ResponseEntity<DriverDto> updateDriverStatus(@PathVariable("driverId") Long driverId, @RequestBody DriverDto driverDto) throws UserNotFoundException {
        return driverService.updateDriverStatus(driverId, driverDto);
    }

    @GetMapping("/name/{username}")
    public Optional<Driver> getDriverByName(@PathVariable("username") String username){
        return driverService.getDriverByName(username);
    }


}
