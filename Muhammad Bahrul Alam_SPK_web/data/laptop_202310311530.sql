--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0
-- Dumped by pg_dump version 16.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: laptop; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.laptop (
    id integer,
    "Merk" text,
    ram text,
    memori_internal text,
    processor text,
    layar text,
    baterai_mah text,
    "Harga" text
);


ALTER TABLE public.laptop OWNER TO postgres;

--
-- Data for Name: laptop; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.laptop (id, "Merk", ram, memori_internal, processor, layar, baterai_mah, "Harga") FROM stdin;
1	HP 14S	8 GB	256 GB	Intel Core i5	14 inci	10000Mah	Rp.12000000
2	ASUS VivoBook 15	16 GB	512 GB	AMD Ryzen 7	15.6 inci	8000Mah	Rp.18000000
3	Dell XPS 13	12 GB	1 TB	Intel Core i7	13.3 inci	12000Mah	Rp.20000000
4	ASUS VivoBook 15	4 GB	256 GB	Intel Celeron	15 inci	6000Mah	Rp.4000000
5	Apple MacBook Air	16 GB	512 GB	Apple M1	13 inci	14000Mah	Rp.22500000
6	Lenovo Ideapad 15	8 GB	256 GB	AMD Ryzen 5	15.6 inci	9000Mah	Rp.10800000
7	MSI GS75 Stealth	32 GB	2 TB	Intel Core i9	17.3 inci	8000Mah	Rp.30000000
8	Lenovo ThinkPad 14	8 GB	512 GB	AMD Ryzen 3	14 inci	7000Mah	Rp.8400000
9	Laptop Acer Aspire A515	16 GB	1 TB	Intel Core i7	15.6 inci	10000Mah	Rp.15600000
10	Dell Inspiron 13	8 GB	256 GB	Intel Core i5	13.3 inci	12000Mah	Rp.17000000
\.


--
-- PostgreSQL database dump complete
--

