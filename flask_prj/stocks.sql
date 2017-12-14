CREATE TABLE Stocks(stk_id INTEGER PRIMARY KEY AUTOINCREMENT, stk_name VARCHAR(150), stk_symbol VARCHAR(40), stk_last_price FLOAT, stk_change FLOAT, stk_change_percentage FLOAT, stk_timestamp VARCHAR(25), stk_msdate NUMBER, stk_volume INTEGER, stk_change_ytd FLOAT);
ALTER TABLE Stocks ADD COLUMN stk_change_percent_ytd FLOAT;
ALTER TABLE Stocks ADD COLUMN stk_high FLOAT;
ALTER TABLE Stocks ADD COLUMN stk_low FLOAT;
ALTER TABLE Stocks ADD COLUMN stk_open FLOAT;

CREATE TABLE Users(usr_id INTEGER PRIMARY KEY AUTOINCREMENT, usr_name VARCHAR(50), usr_amount FLOAT, usr_stocks NUMBER, usr_age NUMBER, usr_address VARCHAR(150), usr_phone NUMBER, usr_email VARCHAR(75));
ALTER TABLE Users ADD COLUMN usr_user_name VARCHAR(35);
ALTER TABLE Users ADD COLUMN usr_password VARCHAR(50);
ALTER TABLE Users ADD COLUMN usr_status VARCHAR(10);


INSERT INTO Users VALUES(1, 'Danny Boyle', 10000, 0, 21, 'Dennis Morris Street, Domlur, Bangalore', 3755422, 'samuel_2wait@gmail.com', 'simson', 'gregory_49', 'user');

CREATE TABLE Transactions(trn_id INTEGER PRIMARY KEY AUTOINCREMENT, trn_user_id NUMBER, trn_symbol VARCHAR(15), trn_stocks NUMBER, trn_stock_last_price FLOAT, trn_total FLOAT, trn_timestamp VARCHAR(30));
ALTER TABLE Transactions ADD COLUMN trn_status VARCHAR(10);
