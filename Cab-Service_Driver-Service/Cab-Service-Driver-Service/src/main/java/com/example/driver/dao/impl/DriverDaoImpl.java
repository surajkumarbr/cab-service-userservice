package com.example.driver.dao.impl;

import com.example.driver.dao.DriverDao;
import com.example.driver.entity.Driver;
import com.example.driver.exception.UserAlreadyPresentException;
import com.example.driver.exception.UserNotFoundException;
import com.example.driver.payload.DriverDto;
import com.example.driver.payload.UpdateDriverDetailsDto;
import com.example.driver.repository.DriverRepository;
import org.modelmapper.ModelMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Component;

import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

@Component
public class DriverDaoImpl implements DriverDao {
    @Autowired
    DriverRepository driverRepository;
    @Autowired
    ModelMapper modelMapper;
    @Autowired
    PasswordEncoder passwordEncoder;

    @Override
    public ResponseEntity<DriverDto> addOneDriver(Driver driver) throws UserAlreadyPresentException {

        if (driverRepository.existsByEmail(driver.getEmail())) {
            throw new UserAlreadyPresentException("Driver Already Present With Email: " + driver.getEmail());
        }
        if (driverRepository.existsByUsername(driver.getUsername())) {
            throw new UserAlreadyPresentException("Driver Already Present With UserName: " + driver.getUsername());
        }
//        Driver driver = mapToEntity(driverDto);
        driver.setPassword(passwordEncoder.encode(driver.getPassword()));
        driver.setAvailability(true);
        Driver savedDriver = driverRepository.save(driver);
        DriverDto dto = mapToDto(savedDriver);
        return new ResponseEntity<>(dto, HttpStatus.CREATED);

    }

    @Override
    public ResponseEntity<DriverDto> getDriverById(Long driverId) throws UserNotFoundException {
        Optional<Driver> byId = driverRepository.findById(driverId);
        if (byId.isEmpty()) {
            throw new UserNotFoundException("Driver not found with given user id: " + driverId);
        }
        Driver driver = byId.get();
        DriverDto dto = mapToDto(driver);

        return new ResponseEntity<>(dto, HttpStatus.OK);
    }

    @Override
    public ResponseEntity<DriverDto> deleteDriverById(Long driverId) throws UserNotFoundException {
        Optional<Driver> byId = driverRepository.findById(driverId);
        if (byId.isEmpty()) {
            throw new UserNotFoundException("Driver not found with given user id: " + driverId);
        }
        Driver driver = byId.get();
        driverRepository.delete(driver);
        DriverDto driverDto = mapToDto(driver);
        return new ResponseEntity<>(driverDto, HttpStatus.OK);
    }

    @Override
    public ResponseEntity<DriverDto> updateDriverDetails(Long driverId, UpdateDriverDetailsDto updateDriverDetailsDto) throws UserAlreadyPresentException, UserNotFoundException {
//        if (driverRepository.existsByEmail(updateDriverDetailsDto.getEmail())) {
//            throw new UserAlreadyPresentException("Driver Already Present With Email: " + updateDriverDetailsDto.getEmail());
//        }
//        if (driverRepository.existsByUsername(updateDriverDetailsDto.getUsername())) {
//            throw new UserAlreadyPresentException("Driver Already Present With UserName: " + updateDriverDetailsDto.getUsername());
//        }
        Optional<Driver> byId = driverRepository.findById(driverId);
        if (byId.isEmpty()) {
            throw new UserNotFoundException("Driver not found with given user id: " + driverId);
        }
        Driver driver = byId.get();
        driver.setUsername(updateDriverDetailsDto.getUsername());
        driver.setEmail(updateDriverDetailsDto.getEmail());
        Driver saved = driverRepository.save(driver);
        DriverDto driverDto = mapToDto(saved);
        return new ResponseEntity<>(driverDto, HttpStatus.OK);


    }

    @Override
    public ResponseEntity<List<DriverDto>> getAllDriverDetails() {
        List<Driver> all = driverRepository.findAll();
        List<DriverDto> driverDtoList =
                all.stream().map(m -> mapToDto(m)).collect(Collectors.toList());
        return new ResponseEntity<>(driverDtoList, HttpStatus.OK);
    }

    @Override
    public ResponseEntity<DriverDto> updateDriverStatus(Long driverId, DriverDto driverDto) throws UserNotFoundException {
        Optional<Driver> byId = driverRepository.findById(driverId);
        if (byId.isEmpty()) {
            throw new UserNotFoundException("Driver not found with given user id: " + driverId);
        }
        Driver driver = byId.get();
        driver.setAvailability(driverDto.getAvailability());
        Driver saved = driverRepository.save(driver);
        DriverDto dto = mapToDto(saved);
        return new ResponseEntity<>(dto, HttpStatus.OK);
    }

    @Override
    public Optional<Driver> getDriverByName(String username) {
        Optional<Driver> byUsername = driverRepository.findByUsername(username);
        return byUsername;
    }

    public Driver mapToEntity(DriverDto driverDto) {
        return modelMapper.map(driverDto, Driver.class);
    }

    public DriverDto mapToDto(Driver driver) {
        return modelMapper.map(driver, DriverDto.class);
    }
}
