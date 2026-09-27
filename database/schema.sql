CREATE TABLE users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100),
    password VARCHAR(255),
    role VARCHAR(20)
);
CREATE TABLE assets(
    id INT AUTO_INCREMENT PRIMARY KEY,
    asset_name VARCHAR(100),
    asset_type VARCHAR(50),
    location VARCHAR(50),
    status VARCHAR(50)
);
CREATE TABLE security_rules(
    id INT AUTO_INCREMENT PRIMARY KEY,
    port INT,
    protocol VARCHAR(20),
    action VARCHAR(20)
);
CREATE TABLE vpcs(
    id INT AUTO_INCREMENT PRIMARY KEY,
    vpc_name VARCHAR(100),
    subnet VARCHAR(100)
);
CREATE TABLE alerts(
    id INT AUTO_INCREMENT PRIMARY KEY,
    message TEXT,
    severity VARCHAR(20)
);
CREATE TABLE logs(
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    activity TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);