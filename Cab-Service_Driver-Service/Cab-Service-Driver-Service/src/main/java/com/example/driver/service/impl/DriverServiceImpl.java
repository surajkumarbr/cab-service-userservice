package com.example.driver.service.impl;

import com.example.driver.dao.DriverDao;
import com.example.driver.entity.Driver;
import com.example.driver.exception.UserAlreadyPresentException;
import com.example.driver.exception.UserNotFoundException;
import com.example.driver.payload.DriverDto;
import com.example.driver.payload.UpdateDriverDetailsDto;
import com.example.driver.service.DriverService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class DriverServiceImpl implements DriverService {
    @Autowired
    DriverDao driverDao;

    @Override
    public ResponseEntity<DriverDto> addOneDriver(Driver driver) throws UserAlreadyPresentException {
        return driverDao.addOneDriver(driver);
    }

    @Override
    public ResponseEntity<DriverDto> getDriverById(Long driverId) throws UserNotFoundException {
        return driverDao.getDriverById(driverId);
    }

    @Override
    public ResponseEntity<DriverDto> deleteDriverById(Long driverId) throws UserNotFoundException {
        return driverDao.deleteDriverById(driverId);
    }

    @Override
    public ResponseEntity<DriverDto> updateDriverDetails(Long driverId, UpdateDriverDetailsDto updateDriverDetailsDto) throws UserNotFoundException, UserAlreadyPresentException {
        return driverDao.updateDriverDetails(driverId, updateDriverDetailsDto);
    }

    @Override
    public ResponseEntity<List<DriverDto>> getAllDriverDetails() {
        return driverDao.getAllDriverDetails();
    }

    @Override
    public ResponseEntity<DriverDto> updateDriverStatus(Long driverId, DriverDto driverDto) throws UserNotFoundException {
        return driverDao.updateDriverStatus(driverId, driverDto);
    }

    @Override
    public Optional<Driver> getDriverByName(String username) {
        return driverDao.getDriverByName(username);
    }

}
