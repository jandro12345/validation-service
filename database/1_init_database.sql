create table if not exists tbl_client(
    client_id SERIAL PRIMARY KEY,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITHOUT TIME ZONE,
    status BOOLEAN DEFAULT 't',
    names VARCHAR(256) NOT NULL,
    address VARCHAR(128),
    mail VARCHAR(128) NOT NUll,
    CONSTRAINT unique_mail_client UNIQUE (mail)
);


create table if not exists tbl_payment_method(
    payment_method_id SERIAL PRIMARY KEY,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITHOUT TIME ZONE,
    status BOOLEAN DEFAULT 't',
    number VARCHAR(16) NOT NULL,
    expiration_date VARCHAR(10) NOT NULL,
    cvv_static VARCHAR(3) NOT NUll,
    validate_fund decimal(10,2) NOT NULL,
    client_id INT NOT NULL,
    FOREIGN KEY (client_id) REFERENCES tbl_client(client_id),
    CONSTRAINT unique_number_expiration_date_payment UNIQUE (number, expiration_date)
);


create table if not exists tbl_transaction(
    transaction_id SERIAL PRIMARY KEY,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITHOUT TIME ZONE,
    status BOOLEAN DEFAULT 't',
    amount decimal(10,2) NOT NULL,
    payment_method_id int not NULL,
    FOREIGN KEY (payment_method_id) REFERENCES tbl_payment_method(payment_method_id)
);

