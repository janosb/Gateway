--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'SQL_ASCII';
SET standard_conforming_strings = off;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET escape_string_warning = off;

--
-- Name: odetta; Type: DATABASE; Schema: -; Owner: -
--

CREATE DATABASE odetta WITH TEMPLATE = template0 ENCODING = 'SQL_ASCII' LC_COLLATE = 'C' LC_CTYPE = 'C';


\connect odetta

SET statement_timeout = 0;
SET client_encoding = 'SQL_ASCII';
SET standard_conforming_strings = off;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET escape_string_warning = off;

--
-- Name: plpgsql; Type: PROCEDURAL LANGUAGE; Schema: -; Owner: -
--

CREATE OR REPLACE PROCEDURAL LANGUAGE plpgsql;


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    username character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(75) NOT NULL,
    password character varying(128) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    is_superuser boolean NOT NULL,
    last_login timestamp with time zone NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- Name: chi2test; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE chi2test (
    fname character varying(200),
    chi2dof real,
    chi2dof_bin real,
    dof integer,
    dofb integer
);


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    user_id integer NOT NULL,
    content_type_id integer,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


--
-- Name: django_site; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE django_site (
    id integer NOT NULL,
    domain character varying(100) NOT NULL,
    name character varying(50) NOT NULL
);


--
-- Name: django_site_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE django_site_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: django_site_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE django_site_id_seq OWNED BY django_site.id;


--
-- Name: filters; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE filters (
    filter_id smallint,
    name character varying(40)
);


--
-- Name: fluxvals; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE fluxvals (
    spec_id bigint NOT NULL,
    wavelength real NOT NULL,
    luminosity double precision,
    photon_count real,
    flux_id bigint
);


--
-- Name: lcvals; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE lcvals (
    lc_id bigint,
    t_expl real,
    b_landolt real,
    r_landolt real,
    i_landolt real,
    ux_landolt real,
    v_landolt real
);


--
-- Name: lightcurves; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE lightcurves (
    model_id bigint,
    lc_id bigint,
    theta real,
    phi real,
    b_lan_max real,
    r_lan_max real,
    i_lan_max real,
    ux_lan_max real,
    v_lan_max real,
    t_b_lan_max real,
    t_r_lan_max real,
    t_i_lan_max real,
    t_ux_lan_max real,
    t_v_lan_max real
);


--
-- Name: meta_dd2d; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE meta_dd2d (
    modelname character varying(40),
    mass_wd real,
    percent_carbon real,
    percent_oxygen real,
    n_ignit integer,
    r_min_ignit real,
    cos_alpha real,
    stdev real,
    ka_min real,
    rho_min real,
    rho_max real,
    pub_id integer,
    model_id smallint
);


--
-- Name: meta_nsm1d; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE meta_nsm1d (
    pub_id bigint NOT NULL,
    model_id bigint,
    modelname character varying(40),
    m_ej real,
    beta real,
    n real,
    delta real,
    composition character varying(4)
);


--
-- Name: meta_pi1d; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE meta_pi1d (
    pub_id bigint NOT NULL,
    model_id bigint,
    modelname character varying(15),
    t_expl real,
    mass real,
    star_type character varying(2)
);


--
-- Name: publications; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE publications (
    modeltype character varying(40),
    modeldim smallint,
    date_entered date,
    citation character varying(200),
    type character varying(10),
    pub_id smallint,
    is_public boolean,
    fullname character varying(40),
    shortname character varying(20),
    metatype character varying(20),
    summary character varying(200),
    url character varying(100)
);


--
-- Name: spectra; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE spectra (
    model_id bigint,
    spec_id bigint,
    t_expl real,
    mu real,
    phi real,
    metatype character varying(20)
);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY django_site ALTER COLUMN id SET DEFAULT nextval('django_site_id_seq'::regclass);


--
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions_group_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_key UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_content_type_id_codename_key; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_key UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_user_id_group_id_key; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_key UNIQUE (user_id, group_id);


--
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_user_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_key UNIQUE (user_id, permission_id);


--
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type_app_label_model_key; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_key UNIQUE (app_label, model);


--
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: django_site_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY django_site
    ADD CONSTRAINT django_site_pkey PRIMARY KEY (id);


--
-- Name: auth_group_permissions_group_id; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX auth_group_permissions_group_id ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX auth_group_permissions_permission_id ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX auth_permission_content_type_id ON auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX auth_user_groups_group_id ON auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX auth_user_groups_user_id ON auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_permission_id ON auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_user_id ON auth_user_user_permissions USING btree (user_id);


--
-- Name: django_admin_log_content_type_id; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX django_admin_log_content_type_id ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX django_admin_log_user_id ON django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX django_session_expire_date ON django_session USING btree (expire_date);


--
-- Name: flux_idx; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX flux_idx ON fluxvals USING btree (spec_id);


--
-- Name: fluxvals_spec_id_idx; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX fluxvals_spec_id_idx ON fluxvals USING btree (spec_id);


--
-- Name: spectra_spec_id_idx; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX spectra_spec_id_idx ON spectra USING btree (spec_id);


--
-- Name: auth_group_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_fkey FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: content_type_id_refs_id_728de91f; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT content_type_id_refs_id_728de91f FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_content_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_fkey FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_fkey FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: group_id_refs_id_3cea63fe; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT group_id_refs_id_3cea63fe FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_id_refs_id_831107f1; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT user_id_refs_id_831107f1 FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_id_refs_id_f2045483; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT user_id_refs_id_f2045483 FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: public; Type: ACL; Schema: -; Owner: -
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM pgsql;
GRANT ALL ON SCHEMA public TO pgsql;
GRANT USAGE ON SCHEMA public TO PUBLIC;
GRANT USAGE ON SCHEMA public TO odetta_user;
GRANT ALL ON SCHEMA public TO odetta_admin;


--
-- Name: auth_group; Type: ACL; Schema: public; Owner: -
--

REVOKE ALL ON TABLE auth_group FROM PUBLIC;
REVOKE ALL ON TABLE auth_group FROM odetta_admin;
GRANT ALL ON TABLE auth_group TO odetta_admin;
GRANT SELECT ON TABLE auth_group TO odetta_user;


--
-- Name: auth_group_permissions; Type: ACL; Schema: public; Owner: -
--

REVOKE ALL ON TABLE auth_group_permissions FROM PUBLIC;
REVOKE ALL ON TABLE auth_group_permissions FROM odetta_admin;
GRANT ALL ON TABLE auth_group_permissions TO odetta_admin;
GRANT SELECT ON TABLE auth_group_permissions TO odetta_user;


--
-- Name: auth_permission; Type: ACL; Schema: public; Owner: -
--

REVOKE ALL ON TABLE auth_permission FROM PUBLIC;
REVOKE ALL ON TABLE auth_permission FROM odetta_admin;
GRANT ALL ON TABLE auth_permission TO odetta_admin;
GRANT SELECT ON TABLE auth_permission TO odetta_user;


--
-- Name: auth_user; Type: ACL; Schema: public; Owner: -
--

REVOKE ALL ON TABLE auth_user FROM PUBLIC;
REVOKE ALL ON TABLE auth_user FROM odetta_admin;
GRANT ALL ON TABLE auth_user TO odetta_admin;
GRANT SELECT ON TABLE auth_user TO odetta_user;


--
-- Name: auth_user_groups; Type: ACL; Schema: public; Owner: -
--

REVOKE ALL ON TABLE auth_user_groups FROM PUBLIC;
REVOKE ALL ON TABLE auth_user_groups FROM odetta_admin;
GRANT ALL ON TABLE auth_user_groups TO odetta_admin;
GRANT SELECT ON TABLE auth_user_groups TO odetta_user;


--
-- Name: auth_user_user_permissions; Type: ACL; Schema: public; Owner: -
--

REVOKE ALL ON TABLE auth_user_user_permissions FROM PUBLIC;
REVOKE ALL ON TABLE auth_user_user_permissions FROM odetta_admin;
GRANT ALL ON TABLE auth_user_user_permissions TO odetta_admin;
GRANT SELECT ON TABLE auth_user_user_permissions TO odetta_user;


--
-- Name: chi2test; Type: ACL; Schema: public; Owner: -
--

REVOKE ALL ON TABLE chi2test FROM PUBLIC;
REVOKE ALL ON TABLE chi2test FROM odetta_admin;
GRANT ALL ON TABLE chi2test TO odetta_admin;
GRANT SELECT ON TABLE chi2test TO odetta_user;


--
-- Name: django_admin_log; Type: ACL; Schema: public; Owner: -
--

REVOKE ALL ON TABLE django_admin_log FROM PUBLIC;
REVOKE ALL ON TABLE django_admin_log FROM odetta_admin;
GRANT ALL ON TABLE django_admin_log TO odetta_admin;
GRANT SELECT ON TABLE django_admin_log TO odetta_user;


--
-- Name: django_content_type; Type: ACL; Schema: public; Owner: -
--

REVOKE ALL ON TABLE django_content_type FROM PUBLIC;
REVOKE ALL ON TABLE django_content_type FROM odetta_admin;
GRANT ALL ON TABLE django_content_type TO odetta_admin;
GRANT SELECT ON TABLE django_content_type TO odetta_user;


--
-- Name: django_session; Type: ACL; Schema: public; Owner: -
--

REVOKE ALL ON TABLE django_session FROM PUBLIC;
REVOKE ALL ON TABLE django_session FROM odetta_admin;
GRANT ALL ON TABLE django_session TO odetta_admin;
GRANT SELECT ON TABLE django_session TO odetta_user;


--
-- Name: django_site; Type: ACL; Schema: public; Owner: -
--

REVOKE ALL ON TABLE django_site FROM PUBLIC;
REVOKE ALL ON TABLE django_site FROM odetta_admin;
GRANT ALL ON TABLE django_site TO odetta_admin;
GRANT SELECT ON TABLE django_site TO odetta_user;


--
-- Name: filters; Type: ACL; Schema: public; Owner: -
--

REVOKE ALL ON TABLE filters FROM PUBLIC;
REVOKE ALL ON TABLE filters FROM odetta_admin;
GRANT ALL ON TABLE filters TO odetta_admin;
GRANT SELECT ON TABLE filters TO odetta_user;


--
-- Name: fluxvals; Type: ACL; Schema: public; Owner: -
--

REVOKE ALL ON TABLE fluxvals FROM PUBLIC;
REVOKE ALL ON TABLE fluxvals FROM odetta_admin;
GRANT ALL ON TABLE fluxvals TO odetta_admin;
GRANT SELECT ON TABLE fluxvals TO odetta_user;


--
-- Name: lcvals; Type: ACL; Schema: public; Owner: -
--

REVOKE ALL ON TABLE lcvals FROM PUBLIC;
REVOKE ALL ON TABLE lcvals FROM odetta_admin;
GRANT ALL ON TABLE lcvals TO odetta_admin;
GRANT SELECT ON TABLE lcvals TO odetta_user;


--
-- Name: lightcurves; Type: ACL; Schema: public; Owner: -
--

REVOKE ALL ON TABLE lightcurves FROM PUBLIC;
REVOKE ALL ON TABLE lightcurves FROM odetta_admin;
GRANT ALL ON TABLE lightcurves TO odetta_admin;
GRANT SELECT ON TABLE lightcurves TO odetta_user;


--
-- Name: meta_dd2d; Type: ACL; Schema: public; Owner: -
--

REVOKE ALL ON TABLE meta_dd2d FROM PUBLIC;
REVOKE ALL ON TABLE meta_dd2d FROM odetta_admin;
GRANT ALL ON TABLE meta_dd2d TO odetta_admin;
GRANT SELECT ON TABLE meta_dd2d TO odetta_user;


--
-- Name: meta_nsm1d; Type: ACL; Schema: public; Owner: -
--

REVOKE ALL ON TABLE meta_nsm1d FROM PUBLIC;
REVOKE ALL ON TABLE meta_nsm1d FROM odetta_admin;
GRANT ALL ON TABLE meta_nsm1d TO odetta_admin;
GRANT SELECT ON TABLE meta_nsm1d TO odetta_user;


--
-- Name: meta_pi1d; Type: ACL; Schema: public; Owner: -
--

REVOKE ALL ON TABLE meta_pi1d FROM PUBLIC;
REVOKE ALL ON TABLE meta_pi1d FROM odetta_admin;
GRANT ALL ON TABLE meta_pi1d TO odetta_admin;
GRANT SELECT ON TABLE meta_pi1d TO odetta_user;


--
-- Name: publications; Type: ACL; Schema: public; Owner: -
--

REVOKE ALL ON TABLE publications FROM PUBLIC;
REVOKE ALL ON TABLE publications FROM odetta_admin;
GRANT ALL ON TABLE publications TO odetta_admin;
GRANT SELECT ON TABLE publications TO odetta_user;


--
-- Name: spectra; Type: ACL; Schema: public; Owner: -
--

REVOKE ALL ON TABLE spectra FROM PUBLIC;
REVOKE ALL ON TABLE spectra FROM odetta_admin;
GRANT ALL ON TABLE spectra TO odetta_admin;
GRANT SELECT ON TABLE spectra TO odetta_user;


--
-- Name: DEFAULT PRIVILEGES FOR TABLES; Type: DEFAULT ACL; Schema: public; Owner: -
--

ALTER DEFAULT PRIVILEGES FOR ROLE pgsql IN SCHEMA public REVOKE ALL ON TABLES  FROM PUBLIC;
ALTER DEFAULT PRIVILEGES FOR ROLE pgsql IN SCHEMA public REVOKE ALL ON TABLES  FROM pgsql;
ALTER DEFAULT PRIVILEGES FOR ROLE pgsql IN SCHEMA public GRANT ALL ON TABLES  TO odetta_admin;


--
-- PostgreSQL database dump complete
--

