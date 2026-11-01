package com.example.driver.repository;

import com.example.driver.entity.Driver;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface DriverRepository extends JpaRepository<Driver, Long> {
    boolean existsByEmail(String email);

    boolean existsByUsername(String username);

    Optional<Driver> findByUsername(String username);



}
