insert into tbl_client (names, address, mail)
values
('Alejandro Valdivia', 'Jr Napo 1035', 'alejandro@gmail.com');

insert into tbl_payment_method 
(number, expiration_date, cvv_static, validate_fund, client_id) 
values
('7777777777777777', '01/30', '234', 1000.00, 1);