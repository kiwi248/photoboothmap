-- postgis/postgis image installs tiger geocoder + topology by default;
-- we only use core PostGIS geometry types, so drop the rest to keep
-- Alembic autogenerate from picking up their internal tables.
DROP EXTENSION IF EXISTS postgis_tiger_geocoder CASCADE;
DROP EXTENSION IF EXISTS postgis_topology CASCADE;
DROP EXTENSION IF EXISTS fuzzystrmatch CASCADE;
DROP SCHEMA IF EXISTS tiger CASCADE;
DROP SCHEMA IF EXISTS tiger_data CASCADE;
DROP SCHEMA IF EXISTS topology CASCADE;
ALTER DATABASE photoboothmap SET search_path TO "$user", public;
