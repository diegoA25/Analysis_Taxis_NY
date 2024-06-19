select vendorid,
date_trunc('hour', lpep_pickup_datetime) AS pickup_hour,
avg(passenger_count) as avg_passenger_count,
sum(passenger_count) as total_passenger_count,
avg(trip_distance) as avg_trip_distance,
sum(trip_distance) as total_trip_distance,
avg(fare_amount) as avg_fare_amount,
sum(fare_amount) as total_fare_amount,
count(*) as total_trips
from nyt.green_taxi_trips
where lpep_pickup_date >= '01-01-2020'
group by vendorid, pickup_hour