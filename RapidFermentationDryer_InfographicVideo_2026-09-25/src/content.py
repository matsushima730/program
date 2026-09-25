# -*- coding: utf-8 -*-
"""急速発酵乾燥装置 解説動画（図解版）の台本と画面の文言。日本語・英語。

方針
- 「ERS」「環境リサイクルシステム」と、元動画のERSロゴ（緑の三矢印）は使わない
- 装置名: 急速発酵乾燥装置 / Rapid Fermentation and Drying System（device-master の英訳に合わせる）
- 社名: 日本語版＝有限会社松和メンテナンス、英語版＝SHOWAM ORGANIC PRODUCTS INC.（brand/guidelines.md）
- 数値・処理時間・温度・削減量は入れない（資料間で値が割れていて要仕様確認のため）。
  出典は brand/infographics/projects/rapid-fermentation-* と device-master の CATALOG/README
"""
import json
from pathlib import Path

CHAPTERS = {
    "ja": ["", "課題", "仕組み", "工程と管理", "資源化", "価値"],
    "en": ["", "The challenge", "How it works", "Process & control", "Into resources", "Value"],
}

DEVICE = {"ja": "急速発酵乾燥装置", "en": "Rapid Fermentation and Drying System"}

# 読みの直し（TTS に渡す直前だけ。画面・字幕の表記は変えない）。gemini-narration の共通辞書に追加する分
READINGS_JA = {
    "急速発酵乾燥装置": "きゅうそくはっこうかんそうそうち",
    "有機性廃棄物": "ゆうきせいはいきぶつ",
    "土着菌": "どちゃくきん",
    "浸出水": "しんしゅつすい",
    "敷料": "しきりょう",
    "処理槽": "しょりそう",
    "槽": "そう",
    "凝縮器": "ぎょうしゅくき",
    "気液分離器": "きえきぶんりき",
    "気液分離": "きえきぶんり",
    "撹拌羽根": "かくはんばね",
    "羽根": "はね",
    "残さ": "ざんさ",
    "家畜のふん": "かちくのふん",
    "土壌改良材": "どじょうかいりょうざい",
    "二酸化炭素": "にさんかたんそ",
    "100度": "ひゃくど",
    "沸点": "ふってん",
    "有限会社松和メンテナンス": "ゆうげんがいしゃ、ショウワメンテナンス",
    "二本立て": "にほんだて",
    "市場": "いちば",
}

SCENES = [
    {
        "id": "s01_title", "chapter": 0,
        "ja": {
            "screen": {"kicker": "有機性廃棄物の資源化技術", "title": "急速発酵乾燥装置",
                       "sub": "水分の多い有機性廃棄物を、乾いた資源へ", "note": "背景画像はイメージです"},
            "lines": [
                "生ごみや家畜のふんなど、水分の多い有機性廃棄物。",
                "急速発酵乾燥装置は、これを密閉した槽の中で、乾燥と発酵を組み合わせて処理し、扱いやすい乾いた資源に変えます。",
                "この動画では、装置の仕組みと工程、そして資源として活かすまでの流れをご紹介します。",
            ]},
        "en": {
            "screen": {"kicker": "Turning organic waste into resources", "title": "Rapid Fermentation and Drying System",
                       "sub": "From wet organic waste to a dry resource", "note": "Background image for illustration only"},
            "lines": [
                "Food waste, livestock manure and other organic waste often contain a lot of water.",
                "The Rapid Fermentation and Drying System treats this waste inside a sealed vessel, combining drying and fermentation to turn it into a dry, easy-to-handle resource.",
                "This video explains how the system works, the steps of the process, and how the output can be put to use.",
            ]},
    },
    {
        "id": "s02_risks", "chapter": 1,
        "ja": {
            "screen": {"heading": "水分の多い有機性廃棄物が抱える4つのリスク",
                       "center": "水分の多い\n有機性廃棄物",
                       "cards": [
                           {"icon": "wind", "title": "悪臭", "text": "においが周囲に広がる"},
                           {"icon": "bug", "title": "衛生", "text": "虫や病原菌が増えやすい"},
                           {"icon": "droplets", "title": "浸出水", "text": "汚れた水が土や水路にしみ出す"},
                           {"icon": "cloud", "title": "温室効果ガス", "text": "積み上げや埋立でメタンが出やすい"},
                       ]},
            "lines": [
                "水分の多い有機性廃棄物は、そのまま置いておくと、いくつもの問題を生みます。",
                "においが周囲に広がり、虫や病原菌が増えやすくなります。",
                "汚れた水がしみ出して、土や水路を汚すおそれもあります。",
                "さらに、積み上げたり埋め立てたりすると、温室効果ガスであるメタンが出やすくなります。",
            ]},
        "en": {
            "screen": {"heading": "Four risks of wet organic waste",
                       "center": "Wet\norganic waste",
                       "cards": [
                           {"icon": "wind", "title": "Odor", "text": "Smells spread to the surroundings"},
                           {"icon": "bug", "title": "Hygiene", "text": "Insects and pathogens multiply"},
                           {"icon": "droplets", "title": "Leachate", "text": "Dirty liquid seeps into soil and water"},
                           {"icon": "cloud", "title": "Greenhouse gas", "text": "Piles and landfills release methane"},
                       ]},
            "lines": [
                "Left as it is, wet organic waste causes several problems.",
                "Odors spread, and insects and pathogens multiply more easily.",
                "Contaminated liquid can seep out and pollute soil and waterways.",
                "And when it is piled up or landfilled, it tends to release methane, a potent greenhouse gas.",
            ]},
    },
    {
        "id": "s03_methane", "chapter": 1,
        "ja": {
            "screen": {"heading": "メタンが出るのは、酸素が足りないとき",
                       "left": {"title": "積み上げ・埋立", "steps": ["内側まで空気が届かない", "酸素が足りない状態で分解", "メタン（CH₄）が出やすい"]},
                       "right": {"title": "かき混ぜて空気に触れさせる", "steps": ["空気が行き渡る", "酸素がある状態で分解", "主に CO₂ と水蒸気になる"]},
                       "banner": "急速発酵乾燥装置は、この「空気に触れさせながら分解する」状態を密閉した槽の中でつくる"},
            "lines": [
                "メタンは、有機物が、酸素の足りない状態で分解されるときに多く発生します。",
                "積み上げたごみの内側や埋立地の中は、空気が届きにくく、まさにこの状態です。",
                "一方、かき混ぜて空気に触れさせながら分解すれば、発生するのは主に二酸化炭素と水蒸気になります。",
                "急速発酵乾燥装置は、この、空気に触れさせながら分解する状態を、密閉した槽の中でつくります。",
            ]},
        "en": {
            "screen": {"heading": "Methane forms when oxygen runs short",
                       "left": {"title": "Piled up or landfilled", "steps": ["Air cannot reach the inside", "Breaks down without enough oxygen", "Methane (CH₄) is released"]},
                       "right": {"title": "Mixed and exposed to air", "steps": ["Air reaches all the material", "Breaks down with oxygen", "Mainly CO₂ and water vapor"]},
                       "banner": "The system creates these aerobic conditions inside a sealed vessel"},
            "lines": [
                "Methane is produced mainly when organic matter breaks down without enough oxygen.",
                "Inside a waste pile or a landfill, air cannot reach easily. These are exactly those conditions.",
                "If the material is mixed and exposed to air as it breaks down, what comes out is mainly carbon dioxide and water vapor.",
                "The Rapid Fermentation and Drying System creates these aerobic conditions inside a sealed vessel.",
            ]},
    },
    {
        "id": "s04_overview", "chapter": 2,
        "ja": {
            "screen": {"heading": "処理の全体像：投入から資源化まで",
                       "nodes": [
                           {"icon": "basket", "title": "投入", "text": "投入口（ホッパ）"},
                           {"icon": "settings-cog", "title": "急速発酵乾燥装置", "text": "密閉・減圧・加温・撹拌"},
                           {"icon": "filter", "title": "選別", "text": "回転式ふるいで異物を除く"},
                           {"icon": "seedling", "title": "資源化", "text": "有機肥料・土壌改良材など"},
                       ],
                       "vapor": {"title": "蒸気", "text": "冷やして水に戻し、回収"},
                       "air": {"title": "排気", "text": "脱臭してから排出"}},
            "lines": [
                "まず、処理の全体像を見てみましょう。",
                "有機性廃棄物は、投入口のホッパから装置に入り、密閉した槽の中で、加温と撹拌を受けながら、乾燥と発酵が進みます。",
                "処理を終えた乾燥物は、回転式のふるいで異物を取り除き、資源として使える形に整えます。",
                "一方、原料から出た水分は蒸気として取り出され、冷やして水に戻して回収します。",
            ]},
        "en": {
            "screen": {"heading": "The whole process: from intake to resource",
                       "nodes": [
                           {"icon": "basket", "title": "Intake", "text": "Feed hopper"},
                           {"icon": "settings-cog", "title": "The system", "text": "Sealed, depressurized, heated, mixed"},
                           {"icon": "filter", "title": "Screening", "text": "Rotating screen removes foreign matter"},
                           {"icon": "seedling", "title": "Resources", "text": "Organic fertilizer, soil conditioner, etc."},
                       ],
                       "vapor": {"title": "Vapor", "text": "Cooled and recovered as water"},
                       "air": {"title": "Exhaust air", "text": "Deodorized before release"}},
            "lines": [
                "First, an overview of the whole process.",
                "Organic waste enters the system through the feed hopper. Inside the sealed vessel, it is heated and mixed while drying and fermentation proceed.",
                "The dried output then passes through a rotating screen that removes foreign matter and prepares it for use as a resource.",
                "Meanwhile, the moisture from the waste is drawn off as vapor, cooled, and recovered as water.",
            ]},
    },
    {
        "id": "s05_two_actions", "chapter": 2,
        "ja": {
            "screen": {"heading": "中核となる2つのはたらき",
                       "a": {"title": "水分を取り除く", "text": "槽の中を減圧し、比較的低い温度で水を蒸発させる"},
                       "b": {"title": "土着菌を活性化する", "text": "原料にもともといる微生物が、有機物を分解・発酵させる"},
                       "from": "水分の多い原料", "to": "乾いた処理物"},
            "lines": [
                "装置の中心には、二つのはたらきがあります。",
                "一つは、水分を取り除くこと。槽の中の圧力を下げることで、比較的低い温度でも水を蒸発させます。",
                "もう一つは、土着菌、つまり原料にもともといる微生物のはたらきを活発にすることです。微生物が有機物を分解し、発酵が進みます。",
                "この二つを組み合わせることで、水分の多い原料を、短い時間で乾いた処理物に変えていきます。",
            ]},
        "en": {
            "screen": {"heading": "Two core actions",
                       "a": {"title": "Remove water", "text": "Lower pressure lets water evaporate at a relatively low temperature"},
                       "b": {"title": "Activate indigenous microbes", "text": "Microbes already in the waste break down and ferment organic matter"},
                       "from": "Wet feedstock", "to": "Dry product"},
            "lines": [
                "Two actions sit at the heart of the system.",
                "The first is removing water. Lowering the pressure inside the vessel lets water evaporate at a relatively low temperature.",
                "The second is activating indigenous microbes, the microorganisms already present in the waste. They break down organic matter as fermentation proceeds.",
                "Combining the two turns wet feedstock into a dry product in a short time.",
            ]},
    },
    {
        "id": "s06_boiling", "chapter": 2,
        "ja": {
            "screen": {"heading": "圧力を下げると、水は低い温度で沸騰する",
                       "x": "まわりの圧力", "y": "水の沸点", "low": "低い", "high": "高い",
                       "p_atm": "大気圧（ふだんの沸点）", "p_mtn": "高い山の上", "p_vac": "減圧した槽の中",
                       "callout": "原料を高温にしすぎずに、水分を取り除ける", "note": "概念図"},
            "lines": [
                "ここで、減圧のしくみを少し詳しく見てみます。",
                "水が沸騰する温度は、まわりの圧力によって変わります。圧力が低いほど、水は低い温度で沸騰します。",
                "高い山の上で、お湯が100度より低い温度で沸くのと同じ原理です。",
                "槽の中を減圧することで、原料を高温にしすぎずに、水分を効率よく取り除くことができます。",
            ]},
        "en": {
            "screen": {"heading": "Lower pressure, lower boiling point",
                       "x": "Surrounding pressure", "y": "Boiling point of water", "low": "Low", "high": "High",
                       "p_atm": "Atmospheric pressure (normal boiling point)", "p_mtn": "On a high mountain", "p_vac": "Inside the depressurized vessel",
                       "callout": "Removes moisture without overheating the material", "note": "Conceptual"},
            "lines": [
                "Let's take a closer look at how reduced pressure helps.",
                "The temperature at which water boils depends on the surrounding pressure. The lower the pressure, the lower the boiling point.",
                "It is the same reason water boils below 100 degrees Celsius on a high mountain.",
                "By reducing the pressure in the vessel, the system removes moisture efficiently without overheating the material.",
            ]},
    },
    {
        "id": "s07_cutaway", "chapter": 2,
        "ja": {
            "screen": {"heading": "装置の断面：密閉・加温・撹拌",
                       "inlet": "投入口", "outlet": "排出口", "vapor": "蒸気の出口",
                       "callouts": ["外周のジャケットから加温", "中空の回転軸と羽根からも加温", "らせん状の羽根が原料を循環・混合", "蒸気は上部から吸い出す"],
                       "note": "構成の一例（概念図）"},
            "lines": [
                "装置の本体は、横向きに置かれた密閉型の処理槽です。",
                "構成の一例として、熱は、槽の外側を包むジャケット、中空の回転軸、そして撹拌羽根の、三つの経路から原料に伝わります。",
                "らせん状の羽根が、原料を槽の中で循環させ、温度と水分のむらを小さくします。",
                "発生した蒸気は、槽の上部から吸い出され、次の回収工程へ送られます。",
            ]},
        "en": {
            "screen": {"heading": "Inside the vessel: sealed, heated, mixed",
                       "inlet": "Feed inlet", "outlet": "Discharge", "vapor": "Vapor outlet",
                       "callouts": ["Heated from the outer jacket", "Also heated through the hollow shaft and paddles", "Spiral paddles circulate and mix the material", "Vapor is drawn out from the top"],
                       "note": "Example configuration (conceptual)"},
            "lines": [
                "The main unit is a sealed, horizontal processing vessel.",
                "In one typical configuration, heat reaches the material through three paths: a jacket around the vessel, a hollow rotating shaft, and the mixing paddles themselves.",
                "Spiral paddles keep the material circulating through the vessel, evening out temperature and moisture.",
                "The vapor that is released is drawn out from the top of the vessel and sent on to the recovery stage.",
            ]},
    },
    {
        "id": "s08_three_stages", "chapter": 3,
        "ja": {
            "screen": {"heading": "乾燥と発酵を切り替える3段階の運転",
                       "stages": [
                           {"no": "1", "title": "初期乾燥", "text": "減圧して、原料の水分を減らす", "mode": "減圧"},
                           {"no": "2", "title": "発酵", "text": "外の空気を取り入れ、微生物が有機物を分解", "mode": "通気"},
                           {"no": "3", "title": "仕上げ乾燥", "text": "再び減圧して乾かし、取り出す", "mode": "減圧"},
                       ],
                       "moisture": "原料の水分（イメージ）",
                       "note": "各段階の時間と温度は、原料の種類と量に合わせて案件ごとに設定"},
            "lines": [
                "運転は、大きく三つの段階に分かれます。",
                "最初の段階では、槽の中を減圧して、原料の水分を減らします。",
                "次の段階では、外の空気を取り入れて、微生物が有機物を分解する発酵を進めます。",
                "最後に、もう一度減圧して仕上げの乾燥を行い、乾いた処理物として取り出します。",
                "各段階の時間や温度は、原料の種類と量に合わせて、案件ごとに設定します。",
            ]},
        "en": {
            "screen": {"heading": "Three stages: dry, ferment, dry",
                       "stages": [
                           {"no": "1", "title": "Initial drying", "text": "Depressurize to reduce moisture", "mode": "Low pressure"},
                           {"no": "2", "title": "Fermentation", "text": "Bring in outside air; microbes break down organic matter", "mode": "Aeration"},
                           {"no": "3", "title": "Finishing dry", "text": "Depressurize again, dry, and discharge", "mode": "Low pressure"},
                       ],
                       "moisture": "Moisture in the material (illustrative)",
                       "note": "Stage times and temperatures are set for each project, based on the feedstock"},
            "lines": [
                "Operation is divided into three main stages.",
                "In the first stage, the vessel is depressurized to reduce the moisture in the feedstock.",
                "In the second stage, outside air is brought in so that microbes can break down the organic matter through fermentation.",
                "Finally, the pressure is lowered again for a finishing dry, and the material is discharged as a dry product.",
                "The time and temperature of each stage are set for each project, based on the type and amount of feedstock.",
            ]},
    },
    {
        "id": "s09_water", "chapter": 3,
        "ja": {
            "screen": {"heading": "蒸気から水を回収する流れ",
                       "vessel": "処理槽", "steam": "蒸気",
                       "cond": {"title": "凝縮器", "text": "冷やして水に戻す"},
                       "sep": {"title": "気液分離器", "text": "水と空気に分ける"},
                       "water": "回収水", "pump": {"title": "真空ポンプ", "text": "吸引して脱臭へ"},
                       "note": "回収した水や熱の再利用は、設置場所の条件に合わせて検討"},
            "lines": [
                "原料から取り出した水分は、どうなるのでしょうか。",
                "槽から吸い出された蒸気は、凝縮器で冷やされて、水に戻ります。",
                "続く気液分離器で、水と空気に分けられ、水は回収水として取り出されます。",
                "回収した水や熱を、どこまで再利用できるかは、設置する場所の条件に合わせて検討します。",
            ]},
        "en": {
            "screen": {"heading": "Recovering water from vapor",
                       "vessel": "Vessel", "steam": "Vapor",
                       "cond": {"title": "Condenser", "text": "Cools vapor back into water"},
                       "sep": {"title": "Gas-liquid separator", "text": "Splits water and air"},
                       "water": "Recovered water", "pump": {"title": "Vacuum pump", "text": "Draws air on to deodorizing"},
                       "note": "Reuse of recovered water and heat is studied for each site"},
            "lines": [
                "So what happens to the water taken out of the waste?",
                "Vapor drawn from the vessel is cooled in a condenser and turns back into water.",
                "A gas-liquid separator then splits the flow into water and air, and the water is collected as recovered water.",
                "How far the recovered water and heat can be reused is studied for each site, based on local conditions.",
            ]},
    },
    {
        "id": "s10_odor", "chapter": 3,
        "ja": {
            "screen": {"heading": "においを広げにくくする流れ",
                       "steps": [
                           {"icon": "lock", "title": "密閉した処理槽"},
                           {"icon": "snowflake", "title": "凝縮"},
                           {"icon": "tornado", "title": "気液分離"},
                           {"icon": "filter", "title": "ろ過・脱臭"},
                           {"icon": "wind", "title": "吸引・排出"},
                       ],
                       "odor": "においを含む空気",
                       "compare_a": "屋外で積み上げる方式", "compare_b": "密閉した槽で処理する方式",
                       "compare_a_text": "においが周囲に広がりやすい", "compare_b_text": "においを含む空気を経路の中で処理"},
            "lines": [
                "においへの対策も、同じ流れの中に組み込まれています。",
                "処理中の槽は密閉されていて、においを含んだ空気が外に漏れにくい構造です。",
                "蒸気は凝縮と気液分離を経て、残った空気は、ろ過による脱臭を通してから、吸引して排出します。",
                "屋外で積み上げる方式と比べて、においを周囲に広げにくいのが特長です。",
            ]},
        "en": {
            "screen": {"heading": "Keeping odors contained",
                       "steps": [
                           {"icon": "lock", "title": "Sealed vessel"},
                           {"icon": "snowflake", "title": "Condensation"},
                           {"icon": "tornado", "title": "Gas-liquid separation"},
                           {"icon": "filter", "title": "Filtration & deodorizing"},
                           {"icon": "wind", "title": "Suction & release"},
                       ],
                       "odor": "Odorous air",
                       "compare_a": "Outdoor piles", "compare_b": "Sealed-vessel treatment",
                       "compare_a_text": "Odors spread easily", "compare_b_text": "Odorous air is treated along the way"},
            "lines": [
                "Odor control is built into the same flow.",
                "The vessel stays sealed during treatment, so odorous air does not easily escape.",
                "Vapor passes through condensation and gas-liquid separation, and the remaining air is deodorized by filtration before it is drawn out and released.",
                "Compared with piling waste outdoors, this design makes it harder for odors to spread.",
            ]},
    },
    {
        "id": "s11_outlets", "chapter": 3,
        "ja": {
            "screen": {"heading": "密閉処理の3つの出口",
                       "input": "投入した\n有機性廃棄物",
                       "outs": [
                           {"title": "乾燥した処理物", "text": "選別して資源に"},
                           {"title": "回収水", "text": "蒸気を凝縮した水"},
                           {"title": "排気", "text": "脱臭してから排出"},
                       ],
                       "check": "出口が限られ、量と質を測って記録しやすい",
                       "note": "概念図：割合は原料の水分や種類で変わる"},
            "lines": [
                "密閉した槽で処理するため、入ったものの行き先がはっきりしています。",
                "出口は三つ。乾燥した処理物、蒸気から回収した水、そして脱臭してから出す排気です。",
                "それぞれの量の割合は、原料の水分や種類によって変わります。",
                "出口が限られているので、量や質を測って記録しやすく、管理にも役立ちます。",
            ]},
        "en": {
            "screen": {"heading": "Three outlets of a sealed process",
                       "input": "Organic\nwaste in",
                       "outs": [
                           {"title": "Dried product", "text": "Screened and used as a resource"},
                           {"title": "Recovered water", "text": "Condensed from the vapor"},
                           {"title": "Exhaust air", "text": "Deodorized before release"},
                       ],
                       "check": "Few outlets: easy to measure and record",
                       "note": "Conceptual: shares vary with the feedstock"},
            "lines": [
                "Because treatment takes place in a sealed vessel, it is clear where everything goes.",
                "There are three outlets: the dried product, water recovered from the vapor, and exhaust air that is deodorized before release.",
                "The share of each depends on the moisture content and type of feedstock.",
                "With only a few outlets, quantities and quality are easy to measure and record, which helps management.",
            ]},
    },
    {
        "id": "s12_monitor", "chapter": 3,
        "ja": {
            "screen": {"heading": "運転を見守る5つの指標",
                       "gauges": ["温度", "圧力", "水分", "におい", "処理物の状態"],
                       "gauge_icons": ["temperature", "gauge", "droplet", "wind", "eye"],
                       "qc_title": "品質の確認",
                       "qc": ["試料の採取", "縮分", "記録", "分析", "判定"]},
            "lines": [
                "安定した運転のために、五つの指標を見守ります。",
                "温度、圧力、水分、におい、そして処理物の状態です。",
                "処理物は試料を採って分析し、記録を残したうえで、使い道に合う品質かどうかを判定します。",
            ]},
        "en": {
            "screen": {"heading": "Five indicators to watch",
                       "gauges": ["Temperature", "Pressure", "Moisture", "Odor", "Product condition"],
                       "gauge_icons": ["temperature", "gauge", "droplet", "wind", "eye"],
                       "qc_title": "Quality check",
                       "qc": ["Sampling", "Subsampling", "Recording", "Analysis", "Judgment"]},
            "lines": [
                "Five indicators are monitored to keep operation stable.",
                "Temperature, pressure, moisture, odor, and the condition of the product.",
                "Samples of the product are taken, analyzed and recorded, and the results are used to judge whether the quality suits its intended use.",
            ]},
    },
    {
        "id": "s13_inputs_outputs", "chapter": 4,
        "ja": {
            "screen": {"heading": "受け入れる原料と、資源としての行き先",
                       "in_title": "受け入れる原料の候補", "out_title": "資源としての行き先の候補",
                       "inputs": [
                           {"icon": "salad", "title": "生ごみ・食品残さ"},
                           {"icon": "pig", "title": "家畜のふん"},
                           {"icon": "wheat", "title": "農作物の残さ"},
                           {"icon": "carrot", "title": "市場の野菜くず"},
                           {"icon": "building-factory-2", "title": "食品工場の残さ"},
                       ],
                       "outputs": [
                           {"icon": "seedling", "title": "有機肥料"},
                           {"icon": "shovel", "title": "土壌改良材"},
                           {"icon": "home", "title": "家畜の敷料"},
                           {"icon": "grain", "title": "飼料"},
                           {"icon": "flame", "title": "燃料の原料"},
                       ],
                       "note": "受け入れの可否と利用先は、品質試験・法規制・地域のルールで確認します"},
            "lines": [
                "受け入れる原料の候補は、生ごみや食品残さ、家畜のふん、農作物の残さ、市場から出る野菜くずなど、幅広い有機性廃棄物です。",
                "処理物の行き先としては、有機肥料や土壌改良材のほか、家畜の敷料や飼料、燃料の原料などが考えられます。",
                "どの原料を受け入れ、どこに使えるかは、品質試験と、その地域の法規制やルールに合わせて確認します。",
            ]},
        "en": {
            "screen": {"heading": "Feedstocks in, resources out",
                       "in_title": "Candidate feedstocks", "out_title": "Possible uses",
                       "inputs": [
                           {"icon": "salad", "title": "Food waste & residues"},
                           {"icon": "pig", "title": "Livestock manure"},
                           {"icon": "wheat", "title": "Crop residues"},
                           {"icon": "carrot", "title": "Market vegetable waste"},
                           {"icon": "building-factory-2", "title": "Food factory residues"},
                       ],
                       "outputs": [
                           {"icon": "seedling", "title": "Organic fertilizer"},
                           {"icon": "shovel", "title": "Soil conditioner"},
                           {"icon": "home", "title": "Animal bedding"},
                           {"icon": "grain", "title": "Animal feed"},
                           {"icon": "flame", "title": "Fuel feedstock"},
                       ],
                       "note": "Acceptance and uses are confirmed through quality tests, regulations and local rules"},
            "lines": [
                "Candidate feedstocks cover a wide range of organic waste: food waste and food residues, livestock manure, crop residues, and vegetable waste from markets.",
                "Possible uses for the product include organic fertilizer and soil conditioner, as well as animal bedding, animal feed, and fuel feedstock.",
                "Which feedstocks can be accepted, and where the product can be used, is confirmed through quality testing and local laws and rules.",
            ]},
    },
    {
        "id": "s14_loop", "chapter": 4,
        "ja": {
            "screen": {"heading": "地域の中で資源がめぐる",
                       "nodes": [
                           {"icon": "trash", "title": "有機性廃棄物", "text": "家庭・市場・農場"},
                           {"icon": "settings-cog", "title": "急速発酵乾燥装置", "text": "乾燥と発酵"},
                           {"icon": "package", "title": "有機肥料・土壌改良材", "text": "資源として出荷"},
                           {"icon": "plant-2", "title": "農地・土づくり", "text": "土に戻す"},
                           {"icon": "apple", "title": "作物・食卓", "text": "地域の食へ"},
                       ],
                       "center": "ごみとして処分していたものを\n地域でめぐる資源に"},
            "lines": [
                "処理物を有機肥料として地域の農地に戻せば、資源の循環が生まれます。",
                "家庭や市場、農場から出た有機性廃棄物が、装置で資源に変わり、土づくりに使われ、育った作物がまた食卓に届きます。",
                "ごみとして処分していたものが、地域の中でめぐる資源になります。",
            ]},
        "en": {
            "screen": {"heading": "Resources circulating locally",
                       "nodes": [
                           {"icon": "trash", "title": "Organic waste", "text": "Homes, markets, farms"},
                           {"icon": "settings-cog", "title": "The system", "text": "Drying and fermentation"},
                           {"icon": "package", "title": "Fertilizer & soil conditioner", "text": "Shipped as a resource"},
                           {"icon": "plant-2", "title": "Farmland", "text": "Back into the soil"},
                           {"icon": "apple", "title": "Crops & tables", "text": "Local food"},
                       ],
                       "center": "What was disposed of\nbecomes a local resource"},
            "lines": [
                "Returning the product to local farmland as organic fertilizer creates a resource loop.",
                "Organic waste from homes, markets and farms becomes a resource in the system and is used to build healthy soil, and the crops grown there return to people's tables.",
                "What used to be disposed of as waste becomes a resource that circulates within the community.",
            ]},
    },
    {
        "id": "s15_ghg_boundary", "chapter": 4,
        "ja": {
            "screen": {"heading": "温室効果ガスは、この範囲で算定する",
                       "chain": ["原料の発生", "収集・運搬", "装置での処理", "資源としての利用"],
                       "chain_icons": ["trash", "truck", "settings-cog", "seedling"],
                       "boundary": "算定の範囲",
                       "added_title": "加える排出", "added": ["運搬の燃料", "処理に使う電力・熱"],
                       "compare_title": "比べる対象", "compare": "埋立などの処分", "avoided": "避けられるメタン",
                       "note": "具体的な削減量は、案件ごとにこの範囲で算定します"},
            "lines": [
                "温室効果ガスの削減効果は、まず、どこからどこまでを数えるかを決めて評価します。",
                "原料が発生してから、運搬、装置での処理、そして資源としての利用までを、一つの範囲として捉えます。",
                "運搬の燃料や、処理に使う電力と熱による排出を足し合わせ、埋立などの処分で出るはずだったメタンが避けられた分と比べます。",
                "具体的な削減量は、案件ごとに、この範囲で算定します。",
            ]},
        "en": {
            "screen": {"heading": "Where greenhouse gas accounting begins and ends",
                       "chain": ["Waste generated", "Collection & transport", "Treatment in the system", "Use as a resource"],
                       "chain_icons": ["trash", "truck", "settings-cog", "seedling"],
                       "boundary": "Accounting boundary",
                       "added_title": "Emissions added", "added": ["Transport fuel", "Electricity & heat for treatment"],
                       "compare_title": "Compared with", "compare": "Landfill or similar disposal", "avoided": "Methane avoided",
                       "note": "Actual reductions are calculated for each project within this boundary"},
            "lines": [
                "Greenhouse gas reductions are evaluated by first deciding exactly what to count.",
                "The boundary runs from where the waste is generated, through transport and treatment in the system, to its use as a resource.",
                "Emissions from transport fuel and from the electricity and heat used in treatment are added up, and compared with the methane that landfilling or similar disposal would otherwise have released.",
                "The actual reduction is calculated for each project within this boundary.",
            ]},
    },
    {
        "id": "s16_value", "chapter": 5,
        "ja": {
            "screen": {"heading": "処理と資源、二つの価値",
                       "a": {"icon": "trash", "title": "処理の価値", "text": "廃棄物の処理を引き受け、排出する側の負担を減らす", "tag": "処理委託費"},
                       "b": {"icon": "seedling", "title": "資源の価値", "text": "処理物を有機肥料などの資源として届ける", "tag": "有機肥料などの販売"},
                       "base": "二本立てで、続けやすい事業へ"},
            "lines": [
                "この仕組みは、二つの価値を生みます。",
                "一つは、廃棄物の処理を引き受ける価値。排出する側にとっては、処理の負担を減らすことにつながります。",
                "もう一つは、処理物を、有機肥料などの資源として届ける価値です。",
                "処理と資源の二本立てで、事業として続けやすい形を目指します。",
            ]},
        "en": {
            "screen": {"heading": "Two kinds of value",
                       "a": {"icon": "trash", "title": "Treatment value", "text": "Taking on waste treatment eases the burden on those who generate it", "tag": "Treatment fees"},
                       "b": {"icon": "seedling", "title": "Resource value", "text": "Delivering the product as a resource, such as organic fertilizer", "tag": "Sales of fertilizer and more"},
                       "base": "Two pillars for a business that can last"},
            "lines": [
                "This system creates two kinds of value.",
                "The first is taking on waste treatment, which eases the burden on those who generate the waste.",
                "The second is delivering the product as a resource, such as organic fertilizer.",
                "With treatment and resources as two pillars, the aim is a model that can be sustained as a business.",
            ]},
    },
    {
        "id": "s17_stakeholders", "chapter": 5,
        "ja": {
            "screen": {"heading": "関わる人と、めぐる価値",
                       "center": "急速発酵乾燥装置",
                       "nodes": [
                           {"icon": "building-store", "title": "排出者", "text": "家庭・市場・食品工場・畜産農家"},
                           {"icon": "building-bank", "title": "自治体", "text": "仕組みを支える"},
                           {"icon": "settings-cog", "title": "運営事業者", "text": "装置を動かす"},
                           {"icon": "tractor", "title": "農家", "text": "資源を使う"},
                           {"icon": "users", "title": "地域の利用者", "text": "作物や資源を利用する"},
                       ]},
            "lines": [
                "導入には、多くの関係者が関わります。",
                "廃棄物を出す、家庭や市場、食品工場、畜産農家。仕組みを支える自治体。装置を動かす運営事業者。資源を使う農家、そして地域の利用者です。",
                "それぞれが役割を担うことで、廃棄物の処理と資源の活用が、地域の中で一つにつながります。",
            ]},
        "en": {
            "screen": {"heading": "Stakeholders and shared value",
                       "center": "The system",
                       "nodes": [
                           {"icon": "building-store", "title": "Waste generators", "text": "Homes, markets, food factories, livestock farms"},
                           {"icon": "building-bank", "title": "Local government", "text": "Supports the scheme"},
                           {"icon": "settings-cog", "title": "Operator", "text": "Runs the system"},
                           {"icon": "tractor", "title": "Farmers", "text": "Use the resources"},
                           {"icon": "users", "title": "Local community", "text": "Uses the crops and resources"},
                       ]},
            "lines": [
                "Many stakeholders are involved in putting the system to work.",
                "Households, markets, food factories and livestock farms that generate waste; the local government that supports the scheme; the operator that runs the system; and the farmers and local users who use the resources.",
                "With each playing its part, waste treatment and resource use are linked together within the community.",
            ]},
    },
    {
        "id": "s18_closing", "chapter": 0,
        "ja": {
            "screen": {"message": "有機性廃棄物を、地域の資源に。", "title": "急速発酵乾燥装置",
                       "logo": "logo-ja.png", "company": "有限会社松和メンテナンス",
                       "note": "図はすべて説明用の概念図です。数値・仕様は案件ごとに確認します。背景画像はイメージです。"},
            "lines": [
                "急速発酵乾燥装置は、有機性廃棄物を、地域で活かせる資源に変えます。",
                "ご覧いただき、ありがとうございました。",
            ]},
        "en": {
            "screen": {"message": "Turning organic waste into local resources.", "title": "Rapid Fermentation and Drying System",
                       "logo": "logo-sopi.png", "company": "SHOWAM ORGANIC PRODUCTS INC.",
                       "note": "All diagrams are conceptual illustrations. Figures and specifications are confirmed for each project. Background image for illustration only."},
            "lines": [
                "The Rapid Fermentation and Drying System turns organic waste into resources that communities can put to use.",
                "Thank you for watching.",
            ]},
    },
]


def dump(path="build/content.json"):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    data = {"chapters": CHAPTERS, "device": DEVICE, "scenes": SCENES}
    Path(path).write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    return data


if __name__ == "__main__":
    d = dump()
    for lang in ("ja", "en"):
        n = sum(len(s[lang]["lines"]) for s in SCENES)
        c = sum(len(x) for s in SCENES for x in s[lang]["lines"])
        print(lang, "lines", n, "chars", c)
    # 禁止語の確認
    txt = json.dumps(d, ensure_ascii=False)
    for bad in ("ERS", "環境リサイクル", "Environmental Recycling", "株式会社松和", "MAINTENANDE"):
        assert bad not in txt, bad
    print("banned words: none")
