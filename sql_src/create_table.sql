DROP TABLE IF EXISTS nyt.green_taxi_trips;

CREATE TABLE IF NOT EXISTS nyt.green_taxi_trips
(
    trip_id serial primary key,
    vendorid SMALLINT NOT NULL,
    lpep_pickup_datetime TIMESTAMP NOT NULL,
    lpep_pickup_date DATE NOT NULL,
    lpep_dropoff_datetime TIMESTAMP NOT NULL,
    store_and_fwd_flag CHAR(1) NULL,
    ratecodeid SMALLINT NULL,
    pulocationid SMALLINT NOT NULL,
    dolocationid SMALLINT NOT NULL,
    passenger_count SMALLINT NULL,
    trip_distance NUMERIC(8,2) NOT NULL,
    fare_amount NUMERIC(8,2) NOT NULL,
    extra NUMERIC(5,2) NOT NULL,
    mta_tax NUMERIC(3,2) NOT NULL,
    tip_amount NUMERIC(6,2) NOT NULL,
    tolls_amount NUMERIC(6,2) NOT NULL,
    ehail_fee SMALLINT NULL,
    improvement_surcharge NUMERIC(3,2) NOT NULL,
    total_amount NUMERIC(8,2) NOT NULL,
    payment_type SMALLINT NOT NULL,
    trip_type SMALLINT NOT NULL,
    congestion_surcharge NUMERIC(5,2)
);

CREATE INDEX idx_lpep_pickup_date ON nyt.green_taxi_trips (lpep_pickup_date);