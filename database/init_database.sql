create table if not exists tbl_fund(
    fund_id SERIAL PRIMARY KEY,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITHOUT TIME ZONE,
    status BOOLEAN DEFAULT 't',
    document_id VARCHAR(64) NOT NULL,
    validate_fund decimal(10,2) NOT NULL
);


create table if not exists tbl_transaction(
    transaction_id SERIAL PRIMARY KEY,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITHOUT TIME ZONE,
    status BOOLEAN DEFAULT 't',
    amount decimal(10,2) NOT NULL,
    fund_id int not NULL,
    FOREIGN KEY (fund_id) REFERENCES tbl_fund(fund_id)
);

