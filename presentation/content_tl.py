# -*- coding: utf-8 -*-
"""Tagalog / Filipino content pack."""

BRAND = "Showa Maintenance Co., Ltd.  ·  SHOWAM ORGANIC PRODUCTS INC."

PACK = {
    "lang": "tl",
    "cjk": False,
    "brand": BRAND,
    "deck_title": "Paglilinis ng Organikong Basura at Paggawa ng Organikong Pataba sa pamamagitan ng Rapid Fermentation-Drying",

    "title": {
        "org": "Showa Maintenance Co., Ltd. / SHOWAM ORGANIC PRODUCTS INC.",
        "title": "Paglilinis ng Organikong Basura at\nPaggawa ng Organikong Pataba",
        "subtitle": "Tungo sa Circular GX Agriculture Model sa Angeles City",
        "tagline": "Presentasyon ng Teknolohiya sa Pamamahala ng Solidong Basura",
        "footer": "Pulong ng Provincial Solid Waste Management Board — Ika-2 Quarter 2026",
    },

    "agenda": {
        "kicker": "AGENDA",
        "title": "Daloy ng Presentasyon Ngayon (mga 30 minuto)",
        "bullets": [
            "1. Panimula sa kumpanya",
            "2. Pinagmulan: dalawang hamon — organikong basura at suplay ng pataba",
            "▶ Video 1  Paano gumagana ang rapid fermentation-drying (~3 min)",
            "3. Ang teknolohiya at proseso ng paglilinis",
            "4. Pagpapatunay ng pagbawas ng GHG (Angeles City)",
            "▶ Video 2  Ang circular GX agriculture model (~3 min)",
            "5. Plano at roadmap ng proyektong FS",
            "6. Buod",
        ],
        "note": "Pinagsasama namin ang paliwanag sa slides at dalawang maikling video.",
    },

    "sec_company": {"no": "1", "title": "Panimula sa Kumpanya", "sub": "Dala ang karanasan ng Japan sa basura tungo sa organikong pataba sa Pilipinas"},
    "company": {
        "kicker": "COMPANY",
        "title": "Pag-ikot ng organikong yaman sa dalawang base",
        "lh": "Showa Maintenance Co., Ltd. (Japan)",
        "left": [
            "Itinatag noong 1991 sa Toyohashi, Aichi Prefecture",
            "Isang SME sa pangangalap, transport at paglilinis ng industriyal na basura",
            "May karanasan sa organikong basura — tira ng pagkain at agrikultura",
            "Tinitingnan ang basura bilang yaman, hindi lamang itatapon",
        ],
        "rh": "SHOWAM ORGANIC PRODUCTS INC. (Pilipinas)",
        "right": [
            "Nakabase sa Angeles City, Pampanga",
            "Gumagawa, nagbebenta at nag-eexport ng organikong pataba mula 2018",
            "Organikong pataba mula sa tira ng tubo (sugarcane residue)",
            "May Halal at Organic-JAS certification, at record ng export sa Japan",
        ],
    },

    "sec_bg": {"no": "2", "title": "Pinagmulan at Hamon", "sub": "Problema sa basura sa lungsod at problema sa pataba sa agrikultura"},
    "background": {
        "kicker": "BACKGROUND",
        "title": "Dalawang hamon sa lipunan na sabay na umiiral",
        "bullets": [
            "Higit 61,000 tonelada ng solidong basura ang nalilikha bawat araw sa Pilipinas",
            "Sa ilalim ng mga panuntunang naglilimita sa pagsunog, nagpapatuloy ang pag-asa sa landfill",
            "Ang anaerobic na pagkabulok ng organiko sa landfill ay naglalabas ng methane (CH₄)",
            "Sa agrikultura, patuloy ang pag-asa sa angkat, mataas na presyo, at pagkasira ng lupa",
            "Sa isang pampublikong palengke sa Angeles City, mga 10 t/araw na organikong basura",
        ],
        "note": "Simula namin: maaari bang lutasin nang sabay ang paglilinis ng basura at suplay ng pataba?",
    },
    "dual": {
        "kicker": "ANG HAMON",
        "title": "Lungsod at sakahan — dalawang hamon, isang teknolohiya",
        "lh": "Hamon ng lungsod (basura)",
        "left": [
            "Lumiliit na kapasidad ng landfill",
            "Emisyon ng methane mula sa landfill",
            "Panganib sa kalusugan at kapaligiran",
        ],
        "rh": "Hamon ng agrikultura (pataba)",
        "right": [
            "Mataas na presyo at pag-asa sa angkat na kemikal na pataba",
            "Pagkasira at pag-asido ng lupa",
            "Kakulangan ng abot-kaya at de-kalidad na organikong pataba",
        ],
    },

    "cue1": {"no": "▶", "title": "Video 1  Paano gumagana ang rapid fermentation-drying", "sub": "Mula organikong basura tungong pataba sa loob ng mga 24 oras (~3 min)"},

    "sec_tech": {"no": "3", "title": "Ang Teknolohiya", "sub": "Ang rapid fermentation-drying unit at proseso nito"},
    "tech_spec": {
        "kicker": "TECHNOLOGY",
        "title": "Mga pangunahing katangian ng rapid fermentation-drying unit",
        "bullets": [
            "Saradong aerobic high-speed fermentation (uri ng bioreactor)",
            "Gumagamit ng katutubong aerobic microbes; naproseso ang halo-halong basura sa mga 24 oras",
            "Mas mabilis kaysa karaniwang composting (2–6 buwan)",
            "Dahil sarado, mababa ang amoy at zero-wastewater ang disenyo",
            "Kapasidad na mga 10 t/araw (akma sa basura ng palengke)",
        ],
        "note": "Ang produkto ay limitado sa organikong pataba lamang. Ang plastik at iba pang di-akmang materyal ay awtomatikong inihihiwalay sa proseso.",
    },
    "tech_proc": {
        "kicker": "PROCESS",
        "title": "Ang proseso: mula input hanggang organikong pataba",
        "steps": [
            ("1  Input", ["Tanggapin ang basura", "Iayos ang halumigmig", "Idagdag at haluin ang mikrobyo"], 0),
            ("2  Ferment & dry", ["Mga 24 oras", "Aerobic sa 40–70°C", "Tuloy-tuloy na halo, pagsingaw"], 1),
            ("3  Pagsala (in-line)", ["Vibrating screen", "Magnetic / air separation", "Plastik, awtomatikong hiwalay"], 2),
            ("4  Organikong pataba", ["Mga 20% ng input", "~2 t/araw, ~500 t/taon", "Nakukuhang de-kalidad na pataba"], 0),
        ],
        "caption": "Zero-wastewater, mababang amoy, walang pagsunog. Awtomatikong inihihiwalay ang plastik at iba pang di-akma; ang organiko lamang ang nagiging pataba.",
    },
    "tech_cmp": {
        "kicker": "COMPARISON",
        "title": "Paghahambing sa karaniwang pamamaraan",
        "headers": ["Aytem", "Teknolohiyang ito", "Composting", "BSF (insekto)"],
        "rows": [
            ["Tagal ng proseso", "Mga 24 oras", "2–6 buwan", "2–4 linggo"],
            ["Amoy", "Napakababa (sarado)", "Malakas (bukas)", "Katamtaman"],
            ["Tatag ng kalidad", "Mataas (madaling kontrolin)", "Mababa–gitna (pana-panahon)", "Depende sa insekto"],
            ["Halong basura", "Oo (walang paunang sala)", "Organiko lang", "Tira ng pagkain lang"],
            ["Batas (RA8749)", "Sumusunod (walang sunog)", "Sumusunod", "Sumusunod"],
            ["Gamit ng produkto", "Organikong pataba", "Compost", "Pakain / compost"],
        ],
        "note": "Madaling i-deploy kahit kulang ang imprastraktura sa pagsala; mapapatakbo ng mga 2–3 lokal na tauhan.",
    },
    "tech_out": {
        "kicker": "OUTPUT",
        "title": "Ang produkto: de-kalidad na organikong pataba",
        "bullets": [
            "Mayaman sa organic carbon, pinapabuti ang istruktura ng lupa",
            "Slow-release na sustansya (N-P-K) para sa tuloy-tuloy na ani",
            "Pinabubuti ang pagtataglay ng tubig at hangin sa tropikong lupa",
            "100% organikong pagpapayaman ng lupa, walang asa sa kemikal",
            "Pamamahala ng kalidad tungo sa rehistro ng pataba sa Pilipinas (FPA)",
        ],
        "note": "Ang produkto ay limitado sa organikong pataba lamang.",
    },

    "sec_ghg": {"no": "4", "title": "Pagpapatunay ng Pagbawas ng GHG", "sub": "Pagtataya para sa isang pampublikong palengke sa Angeles City"},
    "ghg_method": {
        "kicker": "GHG — METHOD",
        "title": "Mga palagay (ayon sa IPCC 2006 Guidelines)",
        "headers": ["Parameter", "Halaga", "Sanggunian / batayan"],
        "rows": [
            ["Basurang napoproseso", "10 t/araw", "Sinukat sa palengke (paunang survey)"],
            ["Araw ng operasyon", "250 araw/taon", "5 araw/linggo"],
            ["Bahaging organiko", "60–70%", "Estadistika ng basura sa ASEAN (IPCC)"],
            ["CH₄ emission factor", "0.06 t-CH₄/t", "IPCC 2006 Vol.5"],
            ["GWP (CH₄)", "28", "IPCC AR5 (100 taon)"],
            ["MCF correction", "0.8", "Ipinapalagay na unmanaged landfill"],
        ],
        "note": "Pormula: 10 t/araw × 250 araw × organiko (60–70%) × 0.06 × 28 × 0.8 = mga 2,016–2,352 t-CO₂e/taon",
    },
    "ghg_result": {
        "kicker": "GHG — RESULT",
        "title": "Pagbawas mula sa pag-iwas sa landfill methane",
        "number": "2,016–2,352",
        "unit": "t-CO₂e / taon (naiwasang landfill methane)",
        "caption": "Iniiwasan ng aerobic high-speed fermentation ang methane mula sa anaerobic na pagkabulok, mula sa ugat.",
        "sub": "Mula sa isang palengke lamang. Inaasahang kontribusyon sa NDC ng Pilipinas (target 2030).",
    },

    "sec_model": {"no": "5", "title": "Circular GX Model at Proyektong FS", "sub": "Isang feasibility study (FS) sa Angeles City"},
    "cue2": {"no": "▶", "title": "Video 2  Ang circular GX agriculture model", "sub": "Ang buong ikot na ginagawang yaman ang basura (~3 min)"},
    "model_flow": {
        "kicker": "CIRCULAR MODEL",
        "title": "Ang circular GX agriculture model",
        "steps": [
            ("Palengke", ["Organikong basura", "~10 t/araw"], 1),
            ("Ferment-dry", ["~24 oras", "naging yaman"], 0),
            ("Pataba", ["~2 t/araw", "de-kalidad"], 2),
            ("Lokal na sakahan", ["sa mga", "magsasaka"], 0),
            ("Balik-palengke", ["produkto, sa", "back-haul"], 1),
        ],
        "caption": "Sa paggamit ng back-haul ng mga sasakyang naghahatid sa palengke, nananatiling mura at low-carbon ang lohistika habang lumalawak ang network.",
    },
    "fs_obj": {
        "kicker": "FS — OBJECTIVES",
        "title": "Ano ang patutunayan ng proyektong FS",
        "bullets": [
            "Aktwal na dami, komposisyon at sistema ng koleksyon ng basura",
            "Pagiging akma ng teknolohiya at performance sa lokal na kondisyon",
            "Bilang ng pagbawas ng GHG mula sa pag-iwas sa landfill",
            "Kalidad, demand at marketability ng organikong pataba",
            "Ang modelo ng kita at viability ng negosyo",
        ],
        "note": "FS = feasibility study. Tinitiyak nito ang mga kondisyon para sa susunod na yugto (demonstrasyon, pagkatapos ay komersyal).",
    },
    "fs_road": {
        "kicker": "ROADMAP",
        "title": "Roadmap ng negosyo",
        "headers": ["Panahon", "Yugto", "Pangunahing gawain"],
        "rows": [
            ["2026–2027", "FS study", "Field survey, technical verification, GHG estimate, marketability"],
            ["2027–2028", "Pilot at rehistro ng pataba", "Treatment trials, pagsusuri ng kalidad, paghahanda sa rehistro"],
            ["2028–2029", "Pagpapatunay ng regional model", "Pagtapos ng operasyon; plano ng pagpapalawak sa kalapit na lungsod"],
            ["2029 →", "Komersyal at mas malawak", "Komersyal sa Angeles City → buong Luzon at ASEAN"],
        ],
    },
    "policy": {
        "kicker": "POLICY ALIGNMENT",
        "title": "Pagkakatugma sa pambansa at lokal na patakaran",
        "bullets": [
            "RA10068 (Organic Agriculture Act): kaayon ng pagsulong ng organikong pataba",
            "RA8749 (Clean Air Act): isang paglilinis na walang pagsunog",
            "RA9003 (Solid Waste Management Act): binabawasan ang asa sa landfill, may recovery",
            "NDC ng Pilipinas (2030): tumutulong sa layunin sa GHG sa pag-iwas sa landfill methane",
        ],
    },
    "kpi": {
        "kicker": "EXPECTED OUTCOMES",
        "title": "Inaasahang resulta",
        "lh": "Pag-ikot ng yaman",
        "left": [
            "Produksyon ng pataba: ~500 t/taon sa unang taon → ~2,000 t/taon sa ika-5 taon",
            "Basurang napoproseso: ~2,500 t/taon (10 t/araw × 250 araw)",
            "Mas mababang landfill rate (tungo sa zero waste)",
        ],
        "rh": "Kapaligiran at komunidad",
        "right": [
            "Pagbawas ng GHG: ~2,016–2,352 t-CO₂e/taon (naiwasang landfill methane)",
            "Unti-unting paglawak ng suplay ng pataba sa lokal na magsasaka",
            "Mas mababang asa sa kemikal; mas kaunting pagkasira ng lupa",
        ],
    },

    "summary": {
        "kicker": "SUMMARY",
        "title": "Buod",
        "bullets": [
            "Ginagawang pataba ng rapid fermentation-drying ang organikong basura sa mga 24 oras",
            "Sarado, mababang amoy, zero-wastewater, walang pagsunog; awtomatikong hiwalay ang plastik",
            "Tinatayang 2,016–2,352 t-CO₂e/taon na pagbawas para sa Angeles City",
            "Isang circular GX model na sabay na lumulutas sa basura at suplay ng pataba",
            "Patutunayan ng proyektong FS ang feasibility at epekto sa bilang",
        ],
        "note": None,
    },
    "closing": {
        "title": "Basura, gawing yaman. Halaga, dalhin sa agrikultura.",
        "subtitle": "Isang circular GX agriculture model sa rapid fermentation-drying",
        "tagline": "Maraming salamat sa inyong pakikinig.",
        "org": "Showa Maintenance Co., Ltd. / SHOWAM ORGANIC PRODUCTS INC.",
        "footer": BRAND,
    },

    "v1": [
        {"kind": "title", "dur": 7, "title": "Paano gumagana ang rapid fermentation-drying",
         "subtitle": "Organikong basura tungong pataba sa ~24 oras",
         "srt": "Tingnan natin kung paano gumagana ang teknolohiyang rapid fermentation-drying — ginagawang organikong pataba ang organikong basura sa loob ng mga dalawampu't apat na oras."},
        {"kind": "point", "dur": 13, "step": "STEP 1", "head": "1  Input",
         "bullets": ["Tanggapin ang basura at iayos ang halumigmig", "Idagdag ang katutubong aerobic microbes at haluin"],
         "srt": "Una, tinatanggap ang organikong basurang nakalap mula sa palengke at iba pa, inaayos ang halumigmig, at idinaragdag ang katutubong aerobic microbes saka hinahalo."},
        {"kind": "point", "dur": 14, "step": "STEP 2", "head": "2  Ferment & dry (~24 h)",
         "bullets": ["Saradong aerobic high-speed fermentation", "Nabubulok sa 40–70°C na may tuloy-tuloy na halo", "Zero-wastewater, mababang amoy"],
         "srt": "Sunod, sa loob ng saradong unit, nagaganap ang aerobic high-speed fermentation. Umaakyat ang temperatura sa apatnapu hanggang pitumpung digri, tuloy-tuloy na hinahalo, at sumisingaw ang tubig. Walang wastewater at pinipigil ang amoy. Tumatagal ito ng mga dalawampu't apat na oras."},
        {"kind": "point", "dur": 13, "step": "STEP 3", "head": "3  Pagsala (in-line)",
         "bullets": ["Vibrating screen, magnetic at air separation", "Plastik at iba pang di-akma, awtomatikong hiwalay", "Organiko lamang ang nakukuha"],
         "srt": "Sa proseso, awtomatikong inihihiwalay ng vibrating screen at ng magnetic at air separation ang plastik at iba pang di-akmang materyal, kaya organiko na lamang ang natitira na magiging pataba."},
        {"kind": "point", "dur": 13, "step": "STEP 4", "head": "4  Organikong pataba",
         "bullets": ["Mga 20% ng input (~2 t/araw) ang nakukuha", "Natatapos bilang de-kalidad na organikong pataba", "Limitado sa organikong pataba lamang"],
         "srt": "Sa huli, mga dalawampung porsyento ng input — humigit-kumulang dalawang tonelada bawat araw — ang nakukuha bilang de-kalidad na organikong pataba. Limitado sa organikong pataba lamang ang produkto."},
        {"kind": "flow", "dur": 11, "title": "Ang proseso sa isang sulyap",
         "steps": [("1 Input", ["Organiko", "+ mikrobyo"], 0), ("2 Ferment-dry", ["~24 h", "40–70°C"], 1),
                   ("3 Pagsala", ["Plastik,", "awto-alis"], 2), ("4 Pataba", ["~2 t/araw", "nakuha"], 0)],
         "caption": "Mula input hanggang pataba, natatapos ang buong proseso sa loob ng isang saradong unit.",
         "srt": "Mula input hanggang sa pagkuha ng pataba, natatapos ang buong prosesong ito sa loob ng iisang saradong unit."},
        {"kind": "big", "dur": 9, "top": "Ang karaniwang composting ay 2–6 buwan. Ang teknolohiyang ito —",
         "number": "24", "unit": "oras lang", "caption": "Malaking pagbawas sa tagal ng proseso.",
         "srt": "Ang karaniwang composting ay tumatagal ng dalawa hanggang anim na buwan. Pinaikli ito ng teknolohiyang ito sa mga dalawampu't apat na oras."},
        {"kind": "title", "dur": 7, "title": "Sarado · mababang amoy · zero-wastewater · walang sunog",
         "subtitle": "Kayang prosesuhin ang halong basura nang diretso",
         "srt": "Sarado ito at mababa ang amoy, walang wastewater, at hindi umaasa sa pagsunog. Kahit halong basurang mahirap pag-uri-uriin nang maaga ay kayang prosesuhin nang diretso."},
    ],

    "v2": [
        {"kind": "title", "dur": 7, "title": "Ang circular GX agriculture model",
         "subtitle": "Tungo sa demonstrasyon sa Angeles City",
         "srt": "Ngayon, tingnan natin ang circular GX agriculture model — isang konseptong nakatuon sa demonstrasyon sa Angeles City."},
        {"kind": "point", "dur": 11, "step": "NGAYON", "head": "Isang tuwid na daloy",
         "bullets": ["Karamihan ng organikong basura ng palengke ay napupunta sa landfill", "Naglalabas ng methane ang landfill"],
         "srt": "Sa kasalukuyan, karamihan ng organikong basura mula sa palengke ay napupunta sa landfill, kung saan, habang nabubulok, naglalabas ito ng methane."},
        {"kind": "flow", "dur": 13, "title": "Ang circular GX agriculture model",
         "steps": [("Palengke", ["Organiko", "~10 t/araw"], 1), ("Ferment-dry", ["~24 h", "yaman"], 0),
                   ("Pataba", ["~2 t/araw"], 2), ("Sakahan", ["sa magsasaka"], 0), ("Balik-palengke", ["sa back-haul"], 1)],
         "caption": "Ginagawang pataba ang basura at ibinabalik sa lokal na agrikultura — isang ikot.",
         "srt": "Sa modelong ito, ang organikong basura ng palengke ay ginagawang pataba sa pamamagitan ng rapid fermentation-drying, inihahatid sa lokal na sakahan, at bumabalik ang produkto sa palengke — isang saradong ikot."},
        {"kind": "big", "dur": 12, "top": "Pagtataya para sa isang palengke sa Angeles City (ayon sa IPCC 2006)",
         "number": "2,016–2,352", "unit": "t-CO₂e / taon (naiwasang landfill methane)",
         "caption": "Iniiwasan ang methane mula sa landfill, mula sa ugat.",
         "srt": "Para sa isang palengke sa Angeles City, ang pag-iwas sa landfill methane ay tinatayang magbabawas ng mga dalawang libo hanggang dalawang libo tatlong daan limampung tonelada ng CO2-equivalent bawat taon, batay sa IPCC dalawang libo't anim na guidelines."},
        {"kind": "point", "dur": 11, "step": "VALUE 1", "head": "Pataba para sa komunidad",
         "bullets": ["De-kalidad na organikong pataba sa lokal na sakahan", "Mas mababang asa sa kemikal at pagkasira ng lupa"],
         "srt": "Ang organikong patabang nagagawa ay inihahatid sa lokal na sakahan, tumutulong na bawasan ang pag-asa sa kemikal na pataba at pabagalin ang pagkasira ng lupa."},
        {"kind": "point", "dur": 11, "step": "VALUE 2", "head": "Low-carbon na lohistika",
         "bullets": ["Gamitin ang back-haul ng mga sasakyang naghahatid sa palengke", "Palawakin ang network habang mababa ang dagdag na gastos"],
         "srt": "Sa transport, ginagamit ang back-haul ng mga sasakyang naghahatid ng gulay sa palengke, pinapalawak ang network habang mababa ang karagdagang gastos."},
        {"kind": "flow", "dur": 11, "title": "Mula FS hanggang komersyalisasyon",
         "steps": [("FS study", ["2026–2027"], 0), ("Pilot", ["2027–2028"], 1),
                   ("Rehiyonal", ["2028–2029"], 2), ("Komersyal", ["2029 →"], 0)],
         "caption": "Tiyakin ang kondisyon sa FS, pagkatapos pilot, komersyal, at mas malawak.",
         "srt": "Una, tinitiyak ng FS study ang mga kondisyon; pagkatapos ay pilot at regional verification, sinusundan ng komersyal na operasyon at mas malawak na pagpapakalat."},
        {"kind": "title", "dur": 7, "title": "Basura, gawing yaman. Halaga, dalhin sa agrikultura.",
         "subtitle": "Isang circular GX agriculture model",
         "srt": "Basura, gawing yaman; halaga, dalhin sa agrikultura — ito ang circular GX agriculture model na ninanais namin."},
    ],

    "script": [
        ("Panimula (~1 min)",
         "Ngayon, ipakikilala namin ang aming gawain sa paglilinis ng organikong basura at paggawa ng organikong pataba sa pamamagitan ng rapid fermentation-drying. "
         "Bukod sa slides, gagamit kami ng dalawang maikling video, sa loob ng mga tatlumpung minuto."),
        ("1. Panimula sa kumpanya (~4 min)",
         "Dalawa ang aming base: ang Showa Maintenance, itinatag noong 1991 sa Toyohashi, Aichi Prefecture, Japan, "
         "at ang aming lokal na kumpanya sa Pilipinas, ang SHOWAM ORGANIC PRODUCTS INC., sa Angeles City, Pampanga. "
         "Sa Japan, kami ay nangangalap, naghahatid at naglilinis ng industriyal na basura, at nakaipon ng karanasan sa organikong basura gaya ng tira ng pagkain at agrikultura. "
         "Sa Pilipinas, mula 2018, gumagawa, nagbebenta at nag-eexport kami ng organikong pataba mula sa tira ng tubo, "
         "may Halal at Organic-JAS certification, at may record ng export sa Japan."),
        ("2. Pinagmulan at hamon (~4 min)",
         "Higit 61,000 tonelada ng solidong basura ang nalilikha bawat araw sa Pilipinas, at sa ilalim ng mga panuntunang naglilimita sa pagsunog, nagpapatuloy ang pag-asa sa landfill. "
         "Ang anaerobic na pagkabulok ng organiko sa landfill ay humahantong sa methane. "
         "Sa agrikultura, ang pag-asa sa angkat, mataas na presyo, at pagkasira ng lupa ay mga agarang isyu. "
         "Sa isang pampublikong palengke sa Angeles City, mga 10 tonelada bawat araw ang organikong basura. "
         "Itinanong namin kung maaaring sabayang lutasin ang paglilinis ng basura at suplay ng pataba. "
         "Tingnan natin sa maikling video kung paano gumagana ang teknolohiya."),
        ("▶ Video 1 (~3 min)", "I-play ang video tungkol sa kung paano gumagana ang rapid fermentation-drying."),
        ("3. Ang teknolohiya (~6 min)",
         "Ulitin natin ang teknolohiya. Ang saradong aerobic high-speed fermentation ay naglilinis ng halong organikong basura sa mga 24 oras. "
         "Kung saan ang karaniwang composting ay 2–6 buwan, ito ay mas mabilis, may mababang amoy at zero-wastewater. "
         "May apat na yugto ang proseso: input, ferment-dry, pagsala, at pataba. "
         "Ang plastik at iba pang di-akmang materyal ay awtomatikong inihihiwalay, at ang produkto ay limitado sa organikong pataba lamang. "
         "Ang produkto ay de-kalidad na organikong pataba, mayaman sa organic carbon, na may slow-release na sustansyang nagpapabuti sa tropikong lupa."),
        ("4. Pagpapatunay ng pagbawas ng GHG (~4 min)",
         "Sunod, ang pagbawas ng GHG. Para sa isang pampublikong palengke sa Angeles City — mga 10 t/araw na organikong basura — tinaya namin ayon sa IPCC 2006 Guidelines. "
         "Sa palagay na 250 araw ng operasyon, 60–70% na organiko, emission factor na 0.06, GWP 28 at MCF 0.8, "
         "ang pag-iwas sa landfill methane ay nagbubunga ng mga 2,016–2,352 t-CO₂e bawat taon. "
         "Ito ay para sa isang palengke lamang, at inaasahan ang kontribusyon sa NDC ng Pilipinas. "
         "Ngayon, tingnan natin ito bilang ikot ng buong komunidad sa maikling video."),
        ("▶ Video 2 (~3 min)", "I-play ang video tungkol sa circular GX agriculture model."),
        ("5. Plano at roadmap ng proyektong FS (~4 min)",
         "Patutunayan namin ang feasibility ng konseptong ito sa isang FS study. "
         "Titiyakin namin sa bilang ang aktwal na basura, akma ng teknolohiya, pagbawas ng GHG, kalidad at marketability ng pataba, at ang modelo ng kita. "
         "Mula sa FS noong 2026–2027, susulong kami sa pilot at regional verification tungo sa komersyal na operasyon, saka mas malawak na pagpapakalat sa Luzon at ASEAN. "
         "Kaayon ang modelo ng Organic Agriculture Act, Clean Air Act, Solid Waste Management Act, at ng NDC ng Pilipinas."),
        ("6. Buod (~1 min)",
         "Sa buod: ginagawang pataba ng rapid fermentation-drying ang organikong basura sa mga 24 oras, "
         "at ang pag-iwas sa landfill methane ay inaasahang magdudulot ng malaking pagbawas ng GHG. "
         "Sa pamamagitan ng proyektong FS, patutunayan namin ang circular GX agriculture model na sabay na lumulutas sa basura at suplay ng pataba. "
         "Maraming salamat sa inyong pakikinig."),
    ],
}
