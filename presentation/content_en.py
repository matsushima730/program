# -*- coding: utf-8 -*-
"""English content pack."""

BRAND = "Showa Maintenance Co., Ltd.  ·  SHOWAM ORGANIC PRODUCTS INC."

PACK = {
    "lang": "en",
    "cjk": False,
    "brand": BRAND,
    "deck_title": "Organic Waste Treatment & Organic Fertilizer via Rapid Fermentation-Drying",

    "title": {
        "org": "Showa Maintenance Co., Ltd. / SHOWAM ORGANIC PRODUCTS INC.",
        "title": "Organic Waste Treatment &\nOrganic Fertilizer Production",
        "subtitle": "Toward a Circular GX Agriculture Model in Angeles City",
        "tagline": "Presentation of Solid Waste Management Technology",
        "footer": "Provincial Solid Waste Management Board Meeting — 2nd Quarter 2026",
    },

    "agenda": {
        "kicker": "AGENDA",
        "title": "Today's Flow (about 30 minutes)",
        "bullets": [
            "1. Company introduction",
            "2. Background: two challenges — organic waste and fertilizer supply",
            "▶ Video 1  How the rapid fermentation-drying technology works (~3 min)",
            "3. The technology and treatment process",
            "4. Verifying the GHG reduction (Angeles City)",
            "▶ Video 2  The circular GX agriculture model (~3 min)",
            "5. The FS project plan and roadmap",
            "6. Summary",
        ],
        "note": "We combine slide-based explanation with two short videos.",
    },

    "sec_company": {"no": "1", "title": "Company Introduction", "sub": "Bringing Japanese waste-management expertise to organic fertilizer in the Philippines"},
    "company": {
        "kicker": "COMPANY",
        "title": "Circulating organic resources across two bases",
        "lh": "Showa Maintenance Co., Ltd. (Japan)",
        "left": [
            "Founded 1991 in Toyohashi, Aichi Prefecture",
            "An SME engaged in industrial-waste collection, transport and treatment",
            "Hands-on expertise with organic waste — food and agricultural residues",
            "A mindset that treats waste as a resource, not just disposal",
        ],
        "rh": "SHOWAM ORGANIC PRODUCTS INC. (Philippines)",
        "right": [
            "Based in Angeles City, Pampanga",
            "Manufacturing, selling and exporting organic fertilizer since 2018",
            "Organic fertilizer made from sugarcane residue",
            "Halal- and Organic-JAS-certified, with a record of export to Japan",
        ],
    },

    "sec_bg": {"no": "2", "title": "Background & Challenge", "sub": "An urban waste problem and an agricultural fertilizer problem"},
    "background": {
        "kicker": "BACKGROUND",
        "title": "Two social challenges exist at the same time",
        "bullets": [
            "The Philippines generates more than 61,000 tons of solid waste per day",
            "Under rules that restrict incineration, reliance on landfill continues",
            "Anaerobic decomposition of organics in landfills releases methane (CH₄)",
            "In agriculture, import dependence, high prices and soil degradation persist",
            "One public market in Angeles City alone produces about 10 t/day of organic waste",
        ],
        "note": "Our starting point: can we solve waste treatment and fertilizer supply together, as one?",
    },
    "dual": {
        "kicker": "THE CHALLENGE",
        "title": "City and farm — two challenges, one technology",
        "lh": "Urban challenge (waste)",
        "left": [
            "Pressure on landfill capacity",
            "Methane emissions from landfills",
            "Public-health and environmental risks",
        ],
        "rh": "Agricultural challenge (fertilizer)",
        "right": [
            "High prices and import dependence for chemical fertilizer",
            "Soil degradation and acidification",
            "A shortage of affordable, high-quality organic fertilizer",
        ],
    },

    "cue1": {"no": "▶", "title": "Video 1  How rapid fermentation-drying works", "sub": "From organic waste to organic fertilizer in about 24 hours (~3 min)"},

    "sec_tech": {"no": "3", "title": "The Technology", "sub": "The rapid fermentation-drying unit and its process"},
    "tech_spec": {
        "kicker": "TECHNOLOGY",
        "title": "Key features of the rapid fermentation-drying unit",
        "bullets": [
            "Enclosed aerobic high-speed fermentation (bioreactor type)",
            "Uses indigenous aerobic microbes to treat mixed organic waste in about 24 hours",
            "Far faster than conventional composting (2–6 months)",
            "Enclosed design means low odor and a zero-wastewater design",
            "Capacity of about 10 t/day (matched to the market's waste volume)",
        ],
        "note": "The output is limited to organic fertilizer. Plastics and other unsuitable materials are automatically separated within the process.",
    },
    "tech_proc": {
        "kicker": "PROCESS",
        "title": "The process: from input to organic fertilizer",
        "steps": [
            ("1  Input", ["Receive waste", "Adjust moisture", "Add & mix microbes"], 0),
            ("2  Ferment & dry", ["About 24 hours", "Aerobic at 40–70°C", "Continuous mixing, evaporation"], 1),
            ("3  Sorting (in-line)", ["Vibrating screen", "Magnetic / air separation", "Plastics auto-separated"], 2),
            ("4  Organic fertilizer", ["About 20% of input", "~2 t/day, ~500 t/year", "Recovered as quality fertilizer"], 0),
        ],
        "caption": "Zero wastewater, low odor, no incineration. Plastics and other unsuitable items are automatically separated; only the organic fraction becomes fertilizer.",
    },
    "tech_cmp": {
        "kicker": "COMPARISON",
        "title": "Comparison with conventional methods",
        "headers": ["Item", "This technology", "Composting", "BSF (insects)"],
        "rows": [
            ["Treatment time", "About 24 hours", "2–6 months", "2–4 weeks"],
            ["Odor", "Very low (enclosed)", "Strong (open-air)", "Moderate"],
            ["Quality stability", "High (easy to control)", "Low–mid (seasonal)", "Depends on insects"],
            ["Mixed waste", "Yes (no pre-sorting)", "Organics only", "Food scraps only"],
            ["Regulation (RA8749)", "Compliant (non-incin.)", "Compliant", "Compliant"],
            ["Use of output", "Organic fertilizer", "Compost", "Feed / compost"],
        ],
        "note": "Easy to deploy even where sorting infrastructure is limited; can be operated by about 2–3 local staff.",
    },
    "tech_out": {
        "kicker": "OUTPUT",
        "title": "The output: high-quality organic fertilizer",
        "bullets": [
            "Rich in organic carbon, improving soil structure",
            "Slow-release nutrients (N-P-K) for sustained crop yield",
            "Improves water retention and aeration in tropical soils",
            "100% organic soil-building, without reliance on chemicals",
            "Quality management aimed at Philippine fertilizer registration (FPA)",
        ],
        "note": "The output is limited to organic fertilizer.",
    },

    "sec_ghg": {"no": "4", "title": "Verifying GHG Reduction", "sub": "An estimate for a public market in Angeles City"},
    "ghg_method": {
        "kicker": "GHG — METHOD",
        "title": "Assumptions (per IPCC 2006 Guidelines)",
        "headers": ["Parameter", "Value", "Source / basis"],
        "rows": [
            ["Waste treated", "10 t/day", "Measured at the public market (pre-survey)"],
            ["Operating days", "250 days/year", "Assumes 5 days/week"],
            ["Organic fraction", "60–70%", "ASEAN urban-waste statistics (IPCC)"],
            ["CH₄ emission factor", "0.06 t-CH₄/t", "IPCC 2006 Vol.5"],
            ["GWP (CH₄)", "28", "IPCC AR5 (100-year)"],
            ["MCF correction", "0.8", "Assumes unmanaged landfill"],
        ],
        "note": "Formula: 10 t/day × 250 days × organic fraction (60–70%) × 0.06 × 28 × 0.8 = about 2,016–2,352 t-CO₂e/year",
    },
    "ghg_result": {
        "kicker": "GHG — RESULT",
        "title": "Reduction from avoiding landfill methane",
        "number": "2,016–2,352",
        "unit": "t-CO₂e / year (landfill methane avoided)",
        "caption": "Aerobic high-speed fermentation avoids methane generation from anaerobic decomposition at its root.",
        "sub": "From a single market only. A meaningful contribution to the Philippines' NDC (2030 target) is expected.",
    },

    "sec_model": {"no": "5", "title": "Circular GX Model & the FS Project", "sub": "A feasibility study (FS) in Angeles City"},
    "cue2": {"no": "▶", "title": "Video 2  The circular GX agriculture model", "sub": "The full loop that turns waste into a resource (~3 min)"},
    "model_flow": {
        "kicker": "CIRCULAR MODEL",
        "title": "The circular GX agriculture model",
        "steps": [
            ("Public market", ["Organic waste", "~10 t/day"], 1),
            ("Rapid ferment-dry", ["Resourced in", "~24 hours"], 0),
            ("Organic fertilizer", ["~2 t/day", "High quality"], 2),
            ("Local farms", ["Supplied to", "farmers"], 0),
            ("Back to market", ["Produce shipped", "via back-haul"], 1),
        ],
        "caption": "Using the back-haul of vehicles that deliver to the market keeps logistics low-cost and low-carbon while widening the supply network.",
    },
    "fs_obj": {
        "kicker": "FS — OBJECTIVES",
        "title": "What the FS project will verify",
        "bullets": [
            "The reality of waste volume, composition and collection",
            "Technical fit and operating performance in local conditions",
            "Quantified GHG reduction from avoiding landfill",
            "Quality, demand and marketability of the organic fertilizer",
            "The revenue model and business viability",
        ],
        "note": "FS = feasibility study. It sets the conditions needed to move to the next stage (demonstration, then commercial operation).",
    },
    "fs_road": {
        "kicker": "ROADMAP",
        "title": "Business roadmap",
        "headers": ["Period", "Phase", "Main activities"],
        "rows": [
            ["2026–2027", "FS study", "Field survey, technical verification, GHG estimate, marketability"],
            ["2027–2028", "Pilot & fertilizer registration", "Treatment trials, quality assessment, registration prep"],
            ["2028–2029", "Regional model verification", "Finalize operations; horizontal-expansion plan to nearby cities"],
            ["2029 →", "Commercial & wider rollout", "Commercialize in Angeles City → Luzon-wide and ASEAN"],
        ],
    },
    "policy": {
        "kicker": "POLICY ALIGNMENT",
        "title": "Alignment with national and local policy",
        "bullets": [
            "RA10068 (Organic Agriculture Act): aligned with promoting organic fertilizer",
            "RA8749 (Clean Air Act): a non-incineration treatment",
            "RA9003 (Solid Waste Management Act): reduces landfill reliance and adds recovery",
            "Philippines' NDC (2030): contributes to GHG goals by avoiding landfill methane",
        ],
    },
    "kpi": {
        "kicker": "EXPECTED OUTCOMES",
        "title": "Expected outcomes",
        "lh": "Resource circulation",
        "left": [
            "Fertilizer output: ~500 t/year in year 1 → ~2,000 t/year by year 5",
            "Waste treated: ~2,500 t/year (10 t/day × 250 days)",
            "Lower landfill rate (toward zero waste)",
        ],
        "rh": "Environment & community",
        "right": [
            "GHG reduction: ~2,016–2,352 t-CO₂e/year (landfill methane avoided)",
            "Gradually expanding organic-fertilizer supply to local farmers",
            "Less dependence on chemical fertilizer; less soil degradation",
        ],
    },

    "summary": {
        "kicker": "SUMMARY",
        "title": "Summary",
        "bullets": [
            "Rapid fermentation-drying turns organic waste into fertilizer in about 24 hours",
            "Enclosed, low-odor, zero-wastewater, non-incineration; plastics auto-separated",
            "An estimated 2,016–2,352 t-CO₂e/year reduction for Angeles City",
            "A circular GX model that solves waste treatment and fertilizer supply together",
            "The FS project will verify feasibility and impact quantitatively",
        ],
        "note": None,
    },
    "closing": {
        "title": "Waste into a resource. Value into agriculture.",
        "subtitle": "A circular GX agriculture model via rapid fermentation-drying",
        "tagline": "Thank you for your attention.",
        "org": "Showa Maintenance Co., Ltd. / SHOWAM ORGANIC PRODUCTS INC.",
        "footer": BRAND,
    },

    "v1": [
        {"kind": "title", "dur": 7, "title": "How rapid fermentation-drying works",
         "subtitle": "Organic waste into organic fertilizer in ~24 hours",
         "srt": "Let's look at how the rapid fermentation-drying technology works — turning organic waste into organic fertilizer in about twenty-four hours."},
        {"kind": "point", "dur": 13, "step": "STEP 1", "head": "1  Input",
         "bullets": ["Receive the waste and adjust its moisture", "Add indigenous aerobic microbes and mix"],
         "srt": "First, organic waste collected from places such as the market is received, its moisture is adjusted, and indigenous aerobic microbes are added and mixed in."},
        {"kind": "point", "dur": 14, "step": "STEP 2", "head": "2  Ferment & dry (~24 h)",
         "bullets": ["Enclosed aerobic high-speed fermentation", "Decomposes at 40–70°C with continuous mixing", "Zero wastewater, low odor"],
         "srt": "Next, inside the sealed unit, aerobic high-speed fermentation takes place. The temperature rises to between forty and seventy degrees, the material is continuously mixed, and moisture is evaporated. There is zero wastewater and odor is suppressed. This takes about twenty-four hours."},
        {"kind": "point", "dur": 13, "step": "STEP 3", "head": "3  Sorting (in-line)",
         "bullets": ["Vibrating screen, magnetic and air separation", "Plastics and other unsuitable items auto-separated", "Only the organic fraction is recovered"],
         "srt": "During the process, a vibrating screen and magnetic and air separation automatically remove plastics and other unsuitable materials, leaving only the organic fraction that becomes fertilizer."},
        {"kind": "point", "dur": 13, "step": "STEP 4", "head": "4  Organic fertilizer",
         "bullets": ["About 20% of input (~2 t/day) recovered", "Finished as high-quality organic fertilizer", "Output limited to organic fertilizer"],
         "srt": "Finally, about twenty percent of the input — roughly two tons a day — is recovered as high-quality organic fertilizer. The output is limited to organic fertilizer."},
        {"kind": "flow", "dur": 11, "title": "The process at a glance",
         "steps": [("1 Input", ["Organic waste", "+ microbes"], 0), ("2 Ferment-dry", ["~24 h", "40–70°C"], 1),
                   ("3 Sorting", ["Plastics", "auto-removed"], 2), ("4 Fertilizer", ["~2 t/day", "recovered"], 0)],
         "caption": "From input to fertilizer, the whole sequence is completed inside one enclosed unit.",
         "srt": "From input through to fertilizer recovery, this whole sequence is completed inside a single, enclosed unit."},
        {"kind": "big", "dur": 9, "top": "Conventional composting takes 2–6 months. This technology —",
         "number": "24", "unit": "hours to treat", "caption": "A dramatic reduction in treatment time.",
         "srt": "Conventional composting takes two to six months. This technology shortens that to about twenty-four hours."},
        {"kind": "title", "dur": 7, "title": "Enclosed · low-odor · zero-wastewater · no incineration",
         "subtitle": "Able to treat mixed waste as it is",
         "srt": "It is enclosed and low-odor, with zero wastewater, and it relies on no incineration. Even mixed waste that is hard to pre-sort can be treated as it is."},
    ],

    "v2": [
        {"kind": "title", "dur": 7, "title": "The circular GX agriculture model",
         "subtitle": "Toward a demonstration in Angeles City",
         "srt": "Now, let's look at the circular GX agriculture model — a concept aimed at a demonstration in Angeles City."},
        {"kind": "point", "dur": 11, "step": "TODAY", "head": "A linear flow",
         "bullets": ["Organic waste from the market mostly goes to landfill", "Landfills generate methane"],
         "srt": "Today, most of the organic waste from the market goes to landfill, where, as it decomposes, methane is generated."},
        {"kind": "flow", "dur": 13, "title": "The circular GX agriculture model",
         "steps": [("Market", ["Organic waste", "~10 t/day"], 1), ("Ferment-dry", ["~24 h", "resourced"], 0),
                   ("Fertilizer", ["~2 t/day"], 2), ("Local farms", ["to farmers"], 0), ("Back to market", ["via back-haul"], 1)],
         "caption": "We turn waste into fertilizer and return it to local agriculture, creating a loop.",
         "srt": "In this model, organic waste from the market is turned into fertilizer by rapid fermentation-drying, delivered to local farms, and produce flows back to the market — a closed loop."},
        {"kind": "big", "dur": 12, "top": "Estimate for one market in Angeles City (per IPCC 2006)",
         "number": "2,016–2,352", "unit": "t-CO₂e / year (landfill methane avoided)",
         "caption": "Methane from landfill is avoided at its root.",
         "srt": "For a single market in Angeles City, avoiding landfill methane is estimated to reduce emissions by about two thousand to two thousand three hundred fifty tons of CO2-equivalent per year, based on the IPCC twenty-oh-six guidelines."},
        {"kind": "point", "dur": 11, "step": "VALUE 1", "head": "Fertilizer to the community",
         "bullets": ["High-quality organic fertilizer to local farms", "Less chemical-fertilizer dependence and soil degradation"],
         "srt": "The organic fertilizer produced is delivered to local farms, helping to reduce dependence on chemical fertilizer and to slow soil degradation."},
        {"kind": "point", "dur": 11, "step": "VALUE 2", "head": "Low-carbon logistics",
         "bullets": ["Use the back-haul of vehicles delivering to the market", "Widen the supply network while holding down extra cost"],
         "srt": "For transport, we use the back-haul of the vehicles that deliver vegetables to the market, widening the supply network while keeping additional cost low."},
        {"kind": "flow", "dur": 11, "title": "From FS to commercialization",
         "steps": [("FS study", ["2026–2027"], 0), ("Pilot", ["2027–2028"], 1),
                   ("Regional", ["2028–2029"], 2), ("Commercial", ["2029 →"], 0)],
         "caption": "Fix the conditions in the FS, then pilot, commercial operation, and wider rollout.",
         "srt": "First the FS study fixes the conditions; then a pilot and regional verification, followed by commercial operation and a wider rollout."},
        {"kind": "title", "dur": 7, "title": "Waste into a resource. Value into agriculture.",
         "subtitle": "A circular GX agriculture model",
         "srt": "Waste into a resource, value into agriculture — this is the circular GX agriculture model we aim for."},
    ],

    "script": [
        ("Opening (~1 min)",
         "Today we introduce our work on treating organic waste and producing organic fertilizer through rapid fermentation-drying. "
         "Alongside the slides, we will use two short videos, in about thirty minutes."),
        ("1. Company introduction (~4 min)",
         "We operate from two bases: Showa Maintenance, founded in 1991 in Toyohashi, Aichi Prefecture, Japan, "
         "and our local company in the Philippines, SHOWAM ORGANIC PRODUCTS INC., in Angeles City, Pampanga. "
         "In Japan we collect, transport and treat industrial waste, building hands-on expertise with organic waste such as food and agricultural residues. "
         "In the Philippines, since 2018, we have manufactured, sold and exported organic fertilizer from sugarcane residue, "
         "with Halal and Organic-JAS certification and a record of export to Japan."),
        ("2. Background & challenge (~4 min)",
         "The Philippines generates more than 61,000 tons of solid waste per day, and under rules that restrict incineration, reliance on landfill continues. "
         "Anaerobic decomposition of organics in landfills leads to methane. "
         "In agriculture, import dependence, high prices and soil degradation are pressing issues. "
         "One public market in Angeles City produces about 10 tons a day of organic waste. "
         "We asked whether waste treatment and fertilizer supply could be solved together, as one. "
         "Let's see how the technology works in a short video."),
        ("▶ Video 1 (~3 min)", "Play the video on how rapid fermentation-drying works."),
        ("3. The technology (~6 min)",
         "Let me restate the technology. Enclosed aerobic high-speed fermentation treats mixed organic waste in about 24 hours. "
         "Where conventional composting takes 2–6 months, this is far faster, with low odor and zero wastewater. "
         "The process has four stages: input, ferment-dry, sorting, and fertilizer. "
         "Plastics and other unsuitable items are automatically separated within the process, and the output is limited to organic fertilizer. "
         "That output is a high-quality organic fertilizer, rich in organic carbon, with slow-release nutrients that improve tropical soils."),
        ("4. Verifying GHG reduction (~4 min)",
         "Next, the GHG reduction. For a public market in Angeles City — about 10 t/day of organic waste — we estimated per the IPCC 2006 Guidelines. "
         "Assuming 250 operating days, 60–70% organic fraction, an emission factor of 0.06, GWP 28 and MCF 0.8, "
         "avoiding landfill methane yields about 2,016–2,352 t-CO₂e per year. "
         "This is for a single market only, and a contribution to the Philippines' NDC can be expected. "
         "Now, let's see this as a community-wide loop in a short video."),
        ("▶ Video 2 (~3 min)", "Play the video on the circular GX agriculture model."),
        ("5. FS project plan and roadmap (~4 min)",
         "We will verify the feasibility of this concept in an FS study. "
         "We will quantitatively confirm the waste reality, technical fit, GHG reduction, fertilizer quality and marketability, and the revenue model. "
         "Starting with the FS in 2026–2027, we will move through a pilot and regional verification toward commercial operation, then a wider rollout across Luzon and ASEAN. "
         "The model aligns with the Organic Agriculture Act, the Clean Air Act, the Solid Waste Management Act, and the Philippines' NDC."),
        ("6. Summary (~1 min)",
         "To summarize: rapid fermentation-drying turns organic waste into fertilizer in about 24 hours, "
         "and avoiding landfill methane is expected to deliver a significant GHG reduction. "
         "Through the FS project, we will verify this circular GX agriculture model that solves waste treatment and fertilizer supply together. "
         "Thank you for your attention."),
    ],
}
