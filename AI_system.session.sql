-- CREATE TABLE User (
--     user_id INT AUTO_INCREMENT PRIMARY KEY,
--     username VARCHAR(50) UNIQUE NOT NULL,
--     password VARCHAR(100) NOT NULL,
--     name VARCHAR(100) NOT NULL,
--     email VARCHAR(100) UNIQUE NOT NULL
-- );

-- CREATE TABLE Restaurant (
--     restaurant_id INT AUTO_INCREMENT PRIMARY KEY,
--     name VARCHAR(100) NOT NULL,
--     latitude DOUBLE NOT NULL,
--     longitude DOUBLE NOT NULL,
--     phone VARCHAR(20),
--     category VARCHAR(50),
--     address TEXT
-- );

CREATE TABLE Menu (
    menu_id INT AUTO_INCREMENT PRIMARY KEY,
    restaurant_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    price INT NOT NULL,
    image_url VARCHAR(255),
    FOREIGN KEY (restaurant_id) REFERENCES Restaurant(restaurant_id)
);

CREATE TABLE Review (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    restaurant_id INT NOT NULL,
    rating FLOAT NOT NULL,
    content TEXT,
    source VARCHAR(50),
    review_url TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (restaurant_id) REFERENCES Restaurant(restaurant_id)
);

-- CREATE TABLE Preference (
--     preference_id INT AUTO_INCREMENT PRIMARY KEY,
--     user_id INT NOT NULL,
--     category VARCHAR(50),
--     FOREIGN KEY (user_id) REFERENCES User(user_id)
-- );
