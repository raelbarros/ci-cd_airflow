-- Table: public.carriers

-- DROP TABLE public.carriers;

CREATE TABLE IF NOT EXISTS public.carriers
(
    id integer NOT NULL DEFAULT nextval('carriers_id_seq'::regclass),
    cnpj character varying(255) COLLATE pg_catalog."default" DEFAULT NULL::character varying,
    cdvtex character varying(255) COLLATE pg_catalog."default" DEFAULT NULL::character varying,
    dest_dir character varying(255) COLLATE pg_catalog."default" DEFAULT NULL::character varying,
    created_at timestamp with time zone NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp with time zone NOT NULL DEFAULT CURRENT_TIMESTAMP,
    placa character varying(10) COLLATE pg_catalog."default",
    excep_csv boolean NOT NULL DEFAULT false,
    street_address character varying(150) COLLATE pg_catalog."default",
    street_number integer,
    complement character varying(100) COLLATE pg_catalog."default",
    neighborhood character varying(100) COLLATE pg_catalog."default",
    city character varying(100) COLLATE pg_catalog."default",
    state character varying(2) COLLATE pg_catalog."default",
    postal_code integer,
    codigo_municipio integer,
    CONSTRAINT carriers_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public.carriers
    OWNER to arpyia;

GRANT ALL ON TABLE public.carriers TO arpyia;

GRANT SELECT, UPDATE, DELETE, INSERT ON TABLE public.carriers TO israelb_sauter;

GRANT ALL ON TABLE public.carriers TO sylvio;

GRANT SELECT ON TABLE public.carriers TO tableu_leitura;

GRANT INSERT, SELECT, UPDATE, DELETE ON TABLE public.carriers TO tomaslacarte;

GRANT UPDATE, DELETE, SELECT, INSERT ON TABLE public.carriers TO ygom_sauter;