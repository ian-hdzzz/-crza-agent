"""Domain layer — pure Python, stdlib only. No framework imports.

Slot 1: CRZ//A firm knowledge as typed constants.
This is the ONLY source of truth for firm information.
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
# Firm identity
# ---------------------------------------------------------------------------

FIRM_NAME = "CRZ//A Abogados (Cuenca Reyes Zavala y Asociados)"
FOUNDED_YEARS_AGO = 12

FIRM_TAGLINE = "Think Global, Act Local, Be Local."
FIRM_DESCRIPTION = (
    "Firma de estrategia, inteligencia comercial y servicios jurídicos "
    "internacionales. Asesoramos a clientes e inversionistas en 3 continentes, "
    "4 países, +87 ciudades. Profesionales comprometidos con la innovación "
    "constante y la excelencia en la prestación de servicios jurídicos."
)

# ---------------------------------------------------------------------------
# Practice areas
# ---------------------------------------------------------------------------

PRACTICE_AREAS = [
    "Derecho Corporativo",
    "Inversión Extranjera y Comercio Internacional",
    "Litigio Civil, Mercantil y Administrativo",
    "Comercio Exterior y Cumplimiento T-MEC",
    "Derecho Aduanero (IMMEX, PROSEC, OEA, RFE)",
    "Telecomunicaciones y Tecnología (TIC's)",
    "Energético y Ambiental",
    "Propiedad Intelectual",
    "MASC — Mediación y Métodos Alternativos de Solución de Controversias",
    "Impuestos y Seguridad Social",
    "Ciberseguridad y Protección de Datos Personales",
    "Migración Corporativa Internacional",
    "Laboral Corporativo",
    "Derecho Bursátil y Mercado de Valores",
    "Cabildeo Político, Legislativo y Asuntos Gubernamentales",
    "Inteligencia Comercial y Apertura de Mercado",
]

# ---------------------------------------------------------------------------
# International desks
# ---------------------------------------------------------------------------

DESKS = {
    "Mexico (Sede Principal)": (
        "Ciudad de México. Operamos desde hace 12 años como Firma de Estrategia, "
        "Apertura y expansión de mercado y Servicios Jurídicos Internacionales."
    ),
    "US Desk (Austin, Texas)": (
        "Abarcamos una red de cobertura y área de influencia en los Estados Unidos "
        "de América, en Austin Texas asesorando operaciones cross-border, reshoring, "
        "smartshoring y relocalización de empresas. Nuestra red abarca la "
        "Mexico-Texas Chamber of Commerce (fundadores), condado de Travis, Austin TX "
        "y Ciudad de México; somos consejeros de la Texas-European Chamber of Commerce; "
        "socios de Texas Global y aliados de South Texas Advanced Manufacturing "
        "Partnership (STAMP)."
    ),
    "Oficina España (Oviedo)": (
        "Desde 2015 contamos con oficina en el noreste de España, en la Ciudad de "
        "Oviedo, capital de Asturias, y mantenemos presencia física con nuestros "
        "delegados en todo el país. Somos Proveedores de Servicios Jurídicos "
        "Internacionales de la Red Exterior de ASTUREX (España)."
    ),
    "China Desk (Tianjin / Beijing)": (
        "En 2018 firmamos un Joint Venture con la Red Global Mx, Organismo autónomo "
        "de la Secretaría de Relaciones Exteriores, para asesorar empresas chinas "
        "que desean hacer negocios en México. Operamos a través del Centro de "
        "Cooperación y Negocios México-China (CCNMC)."
    ),
}

# ---------------------------------------------------------------------------
# Credentials and recognitions
# ---------------------------------------------------------------------------

CREDENTIALS = [
    "Primera y única firma legal mexicana miembro permanente de la World Free Zones Organization (WFZO) — Emiratos Árabes Unidos (1,600+ miembros, 140 países).",
    "Firma Líder Diamante en Comercio Exterior 2020–2026 — Tops México.",
    "Firma Líder Diamante en Inversión Extranjera 2020–2026 — Tops México.",
    "Firma Líder Platino en Litigio — Tops México.",
    "Empresa Mexicana del Año 2021 y The Law Award Winners 2021 — Latin American Quality Institute.",
    "Proveedor de Servicios Jurídicos Internacionales — Red Exterior de ASTUREX (España).",
    "Presencia y participación en foros del BID, Dubai Chamber, The Economist Events, Bolsa Mexicana de Valores.",
]

# ---------------------------------------------------------------------------
# Team
# ---------------------------------------------------------------------------

TEAM = {
    "Socios": [
        {
            "name": "Mauricio Jaramillo Reyes",
            "role": "Socio Fundador & Director General",
            "focus": "Inversión Extranjera, Comercio Internacional, Proyectos Internacionales",
            "highlights": "Representante en México de ASTUREX España. Secretario de la Junta Directiva de la Texas-Europe Chamber of Commerce (TECC) en Austin TX. Ponente invitado por el BID, Dubai Chamber y The Economist Events.",
        },
        {
            "name": "Bernardo Camacho Zavala",
            "role": "Socio Fundador & Administrador",
            "focus": "Litigio Civil, Financiero, Administrativo, Telecomunicaciones",
            "highlights": "Certificado en Negociación Litigiosa por la Universidad de Berkeley (International Legal Certificate). Participó en la sección 'Doing Business in México' del Banco Mundial.",
        },
        {
            "name": "Dr. Arturo Flores López",
            "role": "Gobernanza e Internacionalización",
            "focus": "Paradiplomacia de negocios y relocalización empresarial",
            "highlights": "Doctorado por la Universidad de York, Reino Unido. Post-doctorado por la UNAM. Director del programa ECOSCIM, financiado por el Newton Fund del Reino Unido.",
        },
    ],
    "Of Counsel": [
        {
            "name": "Iván Díaz",
            "role": "Ciberseguridad y Peritaje Informático",
            "focus": "CISO con 19+ años de trayectoria. Certificaciones CISSP, CISA, CISM, ISO 27001:2022, CIPM-IAPP. Perito registrado ante el Poder Judicial de la Federación.",
        },
        {
            "name": "Marlene Díaz",
            "role": "Protección de Datos y Privacidad",
            "focus": "Máster en Derecho de las TICs (Universidad Carlos III de Madrid). 15 años en España y Latinoamérica. Especialista en RGPD de la UE.",
        },
        {
            "name": "Pablo Aguirre",
            "role": "Marketing Internacional y Enlace Asia",
            "focus": "Marketing internacional y penetración en mercados asiáticos. Enlace en Beijing.",
        },
    ],
    "Directores": [
        {
            "name": "Mathieu Julien",
            "role": "Director de Migración Corporativa Internacional",
            "focus": "Consultor de inmigración canadiense certificado (ICCRC). +10 años de experiencia. Programas EB-5, Golden Visa Portugal, ciudadanía caribeña. Habla 4 idiomas.",
        },
        {
            "name": "Manuel Gaviño",
            "role": "Director Laboral Corporativo y Seguridad Social",
            "focus": "Inspecciones STPS, litigio fiscal y administrativo. Sectores automotriz, construcción, telecomunicaciones, tecnología.",
        },
        {
            "name": "León Ernesto Urbilla Suazo",
            "role": "Director de Materia Bursátil",
            "focus": "Ex Director General Adjunto en emisiones de la CNBV. Especialista en delitos financieros y mercado de valores.",
        },
        {
            "name": "Juan Carlos Prieto Williams",
            "role": "Director de Telecomunicaciones y Consultoría Digital",
            "focus": "Socio Fundador de Williams Advisers International. Embajador de TELCEL. Doble nacionalidad, bilingüe.",
        },
    ],
    "Gerentes": [
        {
            "name": "María Espinosa",
            "role": "Gerente de Contratos Tecnológicos y Gobernanza de TI",
            "focus": "CLM, Gobernanza TI, Compliance. Experiencia en Genpact, DXC Technology, Motorola Solutions.",
        },
        {
            "name": "Liv Espinosa",
            "role": "Gerente del Área Ambiental y Anticorrupción",
            "focus": "Derecho Ambiental, Energético y Compliance. Universidad Aix en Provence, Francia. Maestría en Administración Pública (BUAP). ISO 37001.",
        },
    ],
}

# ---------------------------------------------------------------------------
# Contact
# ---------------------------------------------------------------------------

CONTACT = {
    "email_general": "contacto@crza.com.mx",
    "email_bernardo": "bzavala@crza.com.mx",
    "phone_bernardo": "55 2139 5193",
    "website": "https://crza.com.mx",
    "address": "Ciudad de México, México",
}

# ---------------------------------------------------------------------------
# Compiled system-prompt knowledge block (Slot 2: static context injection)
# ---------------------------------------------------------------------------

def build_knowledge_block() -> str:
    """Returns the firm knowledge formatted for injection into the system prompt.
    Pure function — deterministic, no I/O."""

    teams_text = ""
    for category, members in TEAM.items():
        teams_text += f"\n  {category}:\n"
        for m in members:
            teams_text += f"    - {m['name']} ({m['role']}): {m.get('focus','')}\n"
            if m.get("highlights"):
                teams_text += f"      {m['highlights']}\n"

    desks_text = ""
    for desk, desc in DESKS.items():
        desks_text += f"  • {desk}: {desc}\n\n"

    creds_text = "\n".join(f"  • {c}" for c in CREDENTIALS)
    areas_text = ", ".join(PRACTICE_AREAS)

    return f"""
=== CONOCIMIENTO SOBRE {FIRM_NAME} ===

IDENTIDAD:
{FIRM_DESCRIPTION}
Lema: "{FIRM_TAGLINE}"
Años de trayectoria: {FOUNDED_YEARS_AGO}

ÁREAS DE PRÁCTICA:
{areas_text}

PRESENCIA INTERNACIONAL:
{desks_text}

RECONOCIMIENTOS Y CREDENCIALES:
{creds_text}

EQUIPO:
{teams_text}

CONTACTO:
  • Email general: {CONTACT['email_general']}
  • Email Bernardo Camacho: {CONTACT['email_bernardo']}
  • Teléfono: {CONTACT['phone_bernardo']}
  • Sitio web: {CONTACT['website']}
"""
