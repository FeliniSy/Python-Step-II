create database AAPL_2025
go

use AAPL_2025;
go

IF NOT EXISTS (
    SELECT * 
    FROM sysobjects 
    WHERE name='stock_daily_data' 
    AND xtype='U'
)   

BEGIN

create table stock_daily_data(
			id int identity(1,1) primary key,
			symbol nvarchar(10),
			date dateTime,
			open_price float,
			high_price float,
			low_price float,
			close_price float,
			volume int,
			daily_change_percentage float,
			extraction_timestamp datetime default getdate()
);
END
go