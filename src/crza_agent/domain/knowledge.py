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
# Hub de Inversión & Inteligencia Comercial
# ---------------------------------------------------------------------------

HUB_INVERSION = {
    "identidad_ampliada": (
        "CRZ//A ya no es un despacho legal tradicional. Es una Agencia Promotora de Inversiones "
        "con servicios jurídicos internacionales. El equipo incluye economistas, politólogos, "
        "especialistas en relaciones internacionales y abogados. Operamos bajo los modelos de "
        "Reshoring (repatriación de operaciones), Nearshoring (relocalización estratégica hacia México) "
        "y Smart Shoring (arquitectura híbrida que optimiza costo, talento y riesgo regulatorio). "
        "Acompañamos al inversionista desde la pre-inversión hasta el aftercare, bajo esquema llave en mano."
    ),
    "clientes_referencia": (
        "Al servicio de corporativos Fortune 500 en sectores críticos: metalurgia, energía, "
        "telecomunicaciones e IT. Clientes de referencia incluyen Huawei e Iron Mountain, entre otros."
    ),
    "comercio_exterior_tmec": {
        "descripcion": "Liderazgo en Comercio Exterior y cumplimiento T-MEC.",
        "servicios": [
            "Implantación llave en mano de IMMEX, PROSEC y Draw-Back.",
            "Defensa comercial ante la UPCI: controversias de dumping y subsidios.",
            "Certificación de reglas de origen bajo Capítulo 4 del T-MEC.",
            "Control de Anexos 24 y 31; certificación OEA (Operador Económico Autorizado).",
            "Compliance Laboral — Capítulos 23 y 31 del T-MEC.",
            "Participación activa en mesas de negociación y revisión del T-MEC.",
        ],
    },
    "recintos_fiscalizados_rfe": {
        "descripcion": (
            "Especialistas en Recintos Fiscalizados Estratégicos (RFE) — la zona franca mexicana. "
            "Permiten introducir mercancías extranjeras o nacionales para almacenamiento, distribución, "
            "exhibición, venta o transformación industrial sin pago de impuestos de comercio exterior. "
            "CRZ//A habilitó los dos RFE operativos de referencia: San Luis Potosí y Puerto Chiapas. "
            "Única firma mexicana miembro de la WFZO (World Free Zones Organization)."
        ),
        "servicios": [
            "Estudios de viabilidad física, logística y de mercado.",
            "Gestión jurídica ante SAT y autoridades hacendarias para obtener el decreto fiscal.",
            "Auditorías operacionales para conservar el registro del recinto.",
            "Gobierno corporativo y compliance del RFE.",
        ],
    },
    "infraestructura_energia": {
        "descripcion": (
            "Hub de Construcción y Energía: conectamos fondos soberanos e inversionistas de México, "
            "EE.UU., España y China en proyectos de infraestructura y energía."
        ),
        "servicios": [
            "Asesoría integral ante CRE y SENER para plantas generadoras y campos de extracción.",
            "Workshop Expo CIHAC: creadores del primer taller sobre atracción de capital en construcción.",
            "Red CMIC–ASTUREX: coordinadores de misiones comerciales bilaterales para coinversiones.",
            "Ingeniería ambiental aplicada, auditorías de impacto social y certificaciones de descarbonización.",
            "Transición energética: gestión regulatoria para energías renovables.",
        ],
    },
    "ingenieria_financiera_soft_landing": {
        "descripcion": "Soluciones corporativas integrales para el inversionista extranjero que llega a México.",
        "servicios": [
            "Evaluación económica de proyectos y análisis predictivo de viabilidad financiera.",
            "Reclutamiento y headhunting de personal técnico/directivo alineado a compliance.",
            "Soft landing operativo: contratación laboral, administración contable y fiscal inicial.",
            "Representación en licitaciones públicas y privadas, nacionales e internacionales.",
            "Mediación privada comercial certificada como mecanismo expedito de solución de controversias.",
        ],
    },
    "competitividad_40": {
        "comercio_digital": (
            "Automatización de documentos contractuales (CLM), firmas electrónicas avanzadas con validez "
            "en operaciones aduaneras y e-commerce. Optimización de ecosistemas bajo disciplina regulatoria T-MEC."
        ),
        "mediacion_digital": (
            "Mediadores privados certificados por el Centro de Justicia Alternativa (CJA) de la CDMX. "
            "Los convenios de mediación tienen fuerza legal de cosa juzgada — obligatorios e inmediatos sin juicio previo."
        ),
        "compliance_dei_mente": (
            "Software propietario DEI-MENTE: auditoría y medición empírica de anticorrupción y prevención "
            "de lavado de dinero para personal directivo y operativo. Alineado a ISO 37001. "
            "Oficiales de Cumplimiento Normativo certificados."
        ),
        "inteligencia_artificial": (
            "Regulación, promoción e implementación de Inteligencia Artificial aplicada al derecho, "
            "contratos y cumplimiento normativo. Área en colaboración con Intellexia."
        ),
    },
    "movilidad_global_migracion": {
        "descripcion": (
            "Reubicación de directivos corporativos, gerentes técnicos y familias de alto patrimonio "
            "de manera ágil y legalmente estructurada. Alianza con Horizon Residency & Citizenship "
            "(Mathieu Julien, Director)."
        ),
        "programas": [
            "Visa EB-5 (Estados Unidos) — inversión mínima calificada.",
            "Visa E-2 (Estados Unidos) — en proceso para Mauricio Jaramillo.",
            "Golden Visa Portugal / Unión Europea.",
            "Canadá Start-up Visa y programas de inversionista inmigrante de Quebec.",
            "Gestión exprés de visas de residencia temporal y permanente ante el INM.",
            "Apostillado, homologación internacional y legalización consular de documentos.",
        ],
    },
    "camaras_alianzas": [
        "Mexico–Texas Chamber of Commerce (fundadores del capítulo Valle de México).",
        "Texas–Europe Chamber of Commerce (TECC) — Mauricio Jaramillo es Secretario de la Junta Directiva.",
        "Red Exterior de ASTUREX (España) — Proveedor de Servicios Jurídicos Internacionales desde 2010.",
        "World Free Zones Organization (WFZO) — primera y única firma mexicana. 1,600+ miembros, 140 países.",
        "CMIC (Cámara Mexicana de la Industria de la Construcción) — convenio de colaboración.",
        "Centro de Cooperación y Negocios México–China (CCNMC) — Joint Venture con Red Global Mx (SRE).",
        "Foros: BID, Dubai Chamber, The Economist Events, Bolsa Mexicana de Valores.",
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

    hub = HUB_INVERSION

    # Pilares del hub
    tmec = hub["comercio_exterior_tmec"]
    rfe  = hub["recintos_fiscalizados_rfe"]
    inf  = hub["infraestructura_energia"]
    sl   = hub["ingenieria_financiera_soft_landing"]
    c40  = hub["competitividad_40"]
    mob  = hub["movilidad_global_migracion"]

    def bullet_list(items):
        return "\n".join(f"    - {i}" for i in items)

    hub_text = f"""
IDENTIDAD AMPLIADA (más allá del despacho legal):
  {hub['identidad_ampliada']}

CLIENTES DE REFERENCIA:
  {hub['clientes_referencia']}

COMERCIO EXTERIOR & T-MEC:
  {tmec['descripcion']}
{bullet_list(tmec['servicios'])}

RECINTOS FISCALIZADOS ESTRATÉGICOS (RFE — Zona Franca Mexicana):
  {rfe['descripcion']}
{bullet_list(rfe['servicios'])}

INFRAESTRUCTURA & ENERGÍA:
  {inf['descripcion']}
{bullet_list(inf['servicios'])}

INGENIERÍA FINANCIERA & SOFT LANDING:
  {sl['descripcion']}
{bullet_list(sl['servicios'])}

COMPETITIVIDAD 4.0:
  Comercio Digital: {c40['comercio_digital']}
  Mediación Digital: {c40['mediacion_digital']}
  Compliance DEI-MENTE: {c40['compliance_dei_mente']}
  Inteligencia Artificial: {c40['inteligencia_artificial']}

MOVILIDAD GLOBAL & MIGRACIÓN CORPORATIVA:
  {mob['descripcion']}
{bullet_list(mob['programas'])}

CÁMARAS Y ALIANZAS ESTRATÉGICAS:
{bullet_list(hub['camaras_alianzas'])}
"""

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

HUB DE INVERSIÓN & INTELIGENCIA COMERCIAL:
{hub_text}

EQUIPO:
{teams_text}

CONTACTO:
  • Email general: {CONTACT['email_general']}
  • Email Bernardo Camacho: {CONTACT['email_bernardo']}
  • Teléfono: {CONTACT['phone_bernardo']}
  • Sitio web: {CONTACT['website']}
"""
