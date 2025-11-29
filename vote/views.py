from django.shortcuts import render
from .models import Leader

# --- Translations ---
translations = {
    "intro": {
        "English": "Hi, welcome to our support chatbot. Politics can bring unresolved grief, trauma, and difficult emotions. This space is here to help you find support and guidance. Please choose your preferred language: English, Afrikaans, isiZulu, isiXhosa, Sesotho, Setswana, Sepedi, Xitsonga, Tshivenda, isiNdebele, or SiSwati."
    },

    "menu": {
        "English": "What do you need help with: food, shelter, safety, a social worker, education, psychologist, case follow-up, or request a call back?",
        "Afrikaans": "Waarmee het jy hulp nodig: kos, skuiling, veiligheid, 'n maatskaplike werker, onderwys, sielkundige, saak-opvolging, of versoek 'n terugbel?",
        "isiZulu": "Udinga usizo ngani: ukudla, indawo yokuhlala, ukuphepha, umphathi wezenhlalakahle, imfundo, udokotela wezengqondo, ukulandela icala, noma cela ukubuyiselwa emuva?",
        "isiXhosa": "Ufuna uncedo ngantoni: ukutya, indawo yokuhlala, ukhuseleko, umphathi wezenhlalakahle, imfundo, ugqirha wezengqondo, ukulandela ityala, okanye cela umnxeba?",
        "Sesotho": "O hloka thuso ka eng: dijo, bolulo, polokeho, mosebeletsi oa sechaba, thuto, setsebi sa kelello, ho latela nyeoe, kapa kopa ho letsetsoa hape?",
        "Setswana": "O tlhoka thuso ka eng: dijo, bolulo, tshireletso, modiri wa loago, thuto, setsebi sa maikutlo, go latela kgang, kgotsa kopa go letsetsiwa gape?",
        "Sepedi": "O hloka thušo ka eng: dijo, bolulo, tshireletšo, modiri wa setšhaba, thuto, setsebi sa monagano, go latela kgang, goba kopa gore o letsetšwe gape?",
        "Xitsonga": "U lava mpfuno eka yini: swakudya, ndhawu yo tshama, vuhlayiseki, mushandzisi wa vaaki, dyondzo, dokodela wa mianakanyo, ku landzela mhaka, kumbe kopa ku fona nakambe?",
        "Tshivenda": "Ni khou ṱoḓa thuso kha: zwiḽiwa, vhudzulo, vhulungoni, mushumeli wa vhathu, vhuḓidini, dokodela wa ṱhanziela, u tevhela siaṱari, kana ni kopa u vhidzwa hafhu?",
        "isiNdebele": "Ufuna usizo ngani: ukudla, indawo yokuhlala, ukuphepha, umphathi wezenhlalakahle, imfundo, udokotela wezengqondo, ukulandela icala, noma cela ukubuyiselwa emuva?",
        "SiSwati": "Ufuna lusito ngani: kudla, indzawo yekuhlala, kuphepha, umsebenti wesintfu, imfundvo, dokotela wekwati kwengcondvo, kulandzela licala, noma cela kutsi ubuyiselwe emuva?"
    },

    "resources": {
        "English": {
            "food": "For urgent food support:<br><a href='https://www.foodforwardsa.org/' target='_blank' class='btn btn-sm btn-success mt-2'>Visit Website</a>",
            "shelter": "For shelter:<br><a href='https://www.haven.org.za/' target='_blank' class='btn btn-sm btn-info mt-2'>Visit Website</a>",
            "safety": "For safety:<br><a href='https://jhbchildwelfare.org.za/' target='_blank' class='btn btn-sm btn-info mt-2'>Visit Website</a>",
            "psychologist": "For mental health support:<br><a href='https://www.lifelinejhb.org.za/' target='_blank' class='btn btn-sm btn-primary mt-2'>Visit Website</a>",
            "social_worker": "For social worker support:<br><a href='https://www.dsd.gov.za' target='_blank' class='btn btn-sm btn-warning mt-2'>Visit Website</a>",
            "education": "For child and education services:<br><a href='https://graduates24.com/' target='_blank' class='btn btn-sm btn-secondary mt-2'>Visit Website</a>",
            "case": "For legal or case follow-ups:<br><a href='https://www.justice.gov.za/' target='_blank' class='btn btn-sm btn-info mt-2'>Visit SAPS</a><br><a href='https://www.justice.gov.za' target='_blank' class='btn btn-sm btn-dark mt-2'>Visit Justice Dept</a>",
            "call_back": "To request a call back, please provide your details."
        },
        "Afrikaans": {
            "food": "Vir dringende voedselondersteuning:<br><a href='https://www.foodforwardsa.org/' target='_blank' class='btn btn-sm btn-success mt-2'>Besoek Webwerf</a>",
            "shelter": "Vir skuiling<br><a href='https://www.haven.org.za/' target='_blank' class='btn btn-sm btn-info mt-2'>Besoek Webwerf</a>",
            "safety": "Vir veiligheid:<br><a href='https://jhbchildwelfare.org.za/' target='_blank' class='btn btn-sm btn-info mt-2'>Besoek Webwerf</a>",
            "psychologist": "Vir geestesgesondheidsondersteuning:<br><a href='https://www.lifelinejhb.org.za/' target='_blank' class='btn btn-sm btn-primary mt-2'>Besoek Webwerf</a>",
            "social_worker": "Vir maatskaplike werk-ondersteuning:<br><a href='https://www.dsd.gov.za' target='_blank' class='btn btn-sm btn-warning mt-2'>Besoek Webwerf</a>",
            "education": "Vir kinder- en onderwysdienste:<br><a href='https://graduates24.com/' target='_blank' class='btn btn-sm btn-secondary mt-2'>Besoek Webwerf</a>",
            "case": "Vir regshulp of saak-opvolging:<br><a href='https://www.justice.gov.za/' target='_blank' class='btn btn-sm btn-info mt-2'>Besoek SAPD</a><br><a href='https://www.justice.gov.za' target='_blank' class='btn btn-sm btn-dark mt-2'>Besoek Justisie</a>",
            "call_back": "Om 'n terugbel te versoek, verskaf asseblief jou besonderhede."
        },
        "isiZulu": {
            "food": "Usizo lwezokudla oluphuthumayo:<br><a href='https://www.foodforwardsa.org/' target='_blank' class='btn btn-sm btn-success mt-2'>Vakashela iwebhusayithi</a>",
            "shelter": "Indawo yokuhlala:<br><a href='https://www.haven.org.za/' target='_blank' class='btn btn-sm btn-info mt-2'>Vakashela iwebhusayithi</a>",
            "safety": "Indawo ukuphepha:<br><a href='https://jhbchildwelfare.org.za/' target='_blank' class='btn btn-sm btn-info mt-2'>Vakashela iwebhusayithi</a>",
            "psychologist": "Ukwesekwa kwengqondo:<br><a href='https://www.lifelinejhb.org.za/' target='_blank' class='btn btn-sm btn-primary mt-2'>Vakashela iwebhusayithi</a>",
            "social_worker": "Ukwesekwa ngumphathi wezenhlalakahle:<br><a href='https://www.dsd.gov.za' target='_blank' class='btn btn-sm btn-warning mt-2'>Vakashela iwebhusayithi</a>",
            "education": "Ukwesekwa kwezingane nemfundo:<br><a href='https://graduates24.com/' target='_blank' class='btn btn-sm btn-secondary mt-2'>Vakashela iwebhusayithi</a>",
            "case": "Ulandelo lwamacala noma usizo lwezomthetho:<br><a href='https://www.justice.gov.za/' target='_blank' class='btn btn-sm btn-info mt-2'>Vakashela i-SAPS</a><br><a href='https://www.justice.gov.za' target='_blank' class='btn btn-sm btn-dark mt-2'>Vakashela uMnyango Wezobulungiswa</a>",
            "call_back": "Ukucela ukubuyiselwa emuva, sicela unikeze imininingwane yakho." 
        },
        "isiXhosa": {
            "food": "Uncedo lokutya olungxamisekileyo:<br><a href='https://www.foodforwardsa.org/' target='_blank' class='btn btn-sm btn-success mt-2'>Vizite iWebhusayithi</a>",
            "shelter": "Indawo yokuhlala:<br><a href='https://www.haven.org.za/' target='_blank' class='btn btn-sm btn-info mt-2'>Vizite iWebhusayithi</a>",
            "safety": "Indawo yokhuseleko:<br><a href='https://jhbchildwelfare.org.za/' target='_blank' class='btn btn-sm btn-info mt-2'>Vizite iWebhusayithi</a>",
            "psychologist": "Uncedo lwezengqondo:<br><a href='https://www.lifelinejhb.org.za/' target='_blank' class='btn btn-sm btn-primary mt-2'>Vizite iWebhusayithi</a>",
            "social_worker": "Uncedo kumsebenzi wezenhlalakahle:<br><a href='https://www.dsd.gov.za' target='_blank' class='btn btn-sm btn-warning mt-2'>Vizite iWebhusayithi</a>",
            "education": "Uncedo lwabantwana kunye nemfundo:<br><a href='https://graduates24.com/' target='_blank' class='btn btn-sm btn-secondary mt-2'>Vizite iWebhusayithi</a>",
            "case": "Ukulandela ityala okanye uncedo lwezomthetho:<br><a href='https://www.justice.gov.za/' target='_blank' class='btn btn-sm btn-info mt-2'>Vizite i-SAPS</a><br><a href='https://www.justice.gov.za' target='_blank' class='btn btn-sm btn-dark mt-2'>Vizite iSebe lezoBulungisa</a>",
            "call_back": "Ukucela umnxeba, nceda unikeze iinkcukacha zakho."
        },
        "Sesotho": {
            "food": "Thuso ea lijo hang-hang:<br><a href='https://www.foodforwardsa.org/' target='_blank' class='btn btn-sm btn-success mt-2'>Etela Webosaete</a>",
            "shelter": "Bolulo:<br><a href='https://www.haven.org.za/' target='_blank' class='btn btn-sm btn-info mt-2'>Etela Webosaete</a>",
            "safety": "Polokeho:<br><a href='https://jhbchildwelfare.org.za/' target='_blank' class='btn btn-sm btn-info mt-2'>Etela Webosaete</a>",
            "psychologist": "Thuso ea kelello:<br><a href='https://www.lifelinejhb.org.za/' target='_blank' class='btn btn-sm btn-primary mt-2'>Etela Webosaete</a>",
            "social_worker": "Thuso ea mosebeletsi oa sechaba:<br><a href='https://www.dsd.gov.za' target='_blank' class='btn btn-sm btn-warning mt-2'>Etela Webosaete</a>",
            "education": "Thuso ea bana le thuto:<br><a href='https://graduates24.com/' target='_blank' class='btn btn-sm btn-secondary mt-2'>Etela Webosaete</a>",
            "case": "Ho latela nyeoe kapa thuso ea molao:<br><a href='https://www.justice.gov.za/' target='_blank' class='btn btn-sm btn-info mt-2'>Etela SAPS</a><br><a href='https://www.justice.gov.za' target='_blank' class='btn btn-sm btn-dark mt-2'>Etela Lefapha la Toka</a>",
            "call_back": "Ho kopa ho letsetsoa hape, ka kopo fana ka lintlha tsa hau."
        },
        "Setswana": {
            "food": "Thuso ya dijo ka bonako:<br><a href='https://www.foodforwardsa.org/' target='_blank' class='btn btn-sm btn-success mt-2'>Etela Webosaete</a>",
            "shelter": "Bolulo:<br><a href='https://www.haven.org.za/' target='_blank' class='btn btn-sm btn-info mt-2'>Etela Webosaete</a>",
            "safety": "Tshireletso:<br><a href='https://jhbchildwelfare.org.za/' target='_blank' class='btn btn-sm btn-info mt-2'>Etela Webosaete</a>",
            "psychologist": "Thuso ya tlhaloganyo:<br><a href='https://www.lifelinejhb.org.za/' target='_blank' class='btn btn-sm btn-primary mt-2'>Etela Webosaete</a>",
            "social_worker": "Thuso ya modiri wa loago:<br><a href='https://www.dsd.gov.za' target='_blank' class='btn btn-sm btn-warning mt-2'>Etela Webosaete</a>",
            "education": "Thuso ya bana le thuto:<br><a href='https://graduates24.com/' target='_blank' class='btn btn-sm btn-secondary mt-2'>Etela Webosaete</a>",
            "case": "Go latela kgang kgotsa thuso ya molao:<br><a href='https://www.justice.gov.za/' target='_blank' class='btn btn-sm btn-info mt-2'>Etela SAPS</a><br><a href='https://www.justice.gov.za' target='_blank' class='btn btn-sm btn-dark mt-2'>Etela Lefapha la Toka</a>",
            "call_back": "Go kopa go letsetsiwa gape, ka kopo neela dintlha tsa gago."
        },
        "Sepedi": {
            "food": "Thušo ya dijo ka pela:<br><a href='https://www.foodforwardsa.org/' target='_blank' class='btn btn-sm btn-success mt-2'>Etela Webosaete</a>",
            "shelter": "Bolulo:<br><a href='https://www.haven.org.za/' target='_blank' class='btn btn-sm btn-info mt-2'>Etela Webosaete</a>",
            "safety": "Tshireletso:<br><a href='https://jhbchildwelfare.org.za/' target='_blank' class='btn btn-sm btn-info mt-2'>Etela Webosaete</a>",
            "psychologist": "Thušo ya monagano:<br><a href='https://www.lifelinejhb.org.za/' target='_blank' class='btn btn-sm btn-primary mt-2'>Etela Webosaete</a>",
            "social_worker": "Thušo ya modiri wa setšhaba:<br><a href='https://www.dsd.gov.za' target='_blank' class='btn btn-sm btn-warning mt-2'>Etela Webosaete</a>",
            "education": "Thušo ya bana le thuto:<br><a href='https://graduates24.com/' target='_blank' class='btn btn-sm btn-secondary mt-2'>Etela Webosaete</a>",
            "case": "Go latela kgang goba thušo ya molao:<br><a href='https://www.justice.gov.za/' target='_blank' class='btn btn-sm btn-info mt-2'>Etela SAPS</a><br><a href='https://www.justice.gov.za' target='_blank' class='btn btn-sm btn-dark mt-2'>Etela Lefapha la Toka</a>",
            "call_back": "Go kopa go letsetšwa gape, ka kopo neela dintlha tša gago."
        },
        "Xitsonga": {
            "food": "Mpfuno wa swakudya hi xihatla:<br><a href='https://www.foodforwardsa.org/' target='_blank' class='btn btn-sm btn-success mt-2'>Vaka Sayiti</a>",
            "shelter": "Ndhawu yo tshama:<br><a href='https://www.haven.org.za/' target='_blank' class='btn btn-sm btn-info mt-2'>Vaka Sayiti</a>",
            "safety": "Ndhawu yo vuhlayiseki:<br><a href='https://jhbchildwelfare.org.za/' target='_blank' class='btn btn-sm btn-info mt-2'>Vaka Sayiti</a>",
            "psychologist": "Mpfuno wa mianakanyo:<br><a href='https://www.lifelinejhb.org.za/' target='_blank' class='btn btn-sm btn-primary mt-2'>Vaka Sayiti</a>",
            "social_worker": "Mpfuno wa mushandzisi wa vaaki:<br><a href='https://www.dsd.gov.za' target='_blank' class='btn btn-sm btn-warning mt-2'>Vaka Sayiti</a>",
            "education": "Mpfuno wa vana na dyondzo:<br><a href='https://graduates24.com/' target='_blank' class='btn btn-sm btn-secondary mt-2'>Vaka Sayiti</a>",
            "case": "Ku landzela mhaka kumbe mpfuno wa nawu:<br><a href='https://www.justice.gov.za/' target='_blank' class='btn btn-sm btn-info mt-2'>Vaka SAPS</a><br><a href='https://www.justice.gov.za' target='_blank' class='btn btn-sm btn-dark mt-2'>Vaka Departemente ya Nawu</a>",
            "call_back": "Ku kombela ku foniwa nakambe, hi kombela u nyika vuxokoxoko bya wena."
        },
        "Tshivenda": {
            "food": "Thuso ya zwiḽiwa nga u ṱavhanya:<br><a href='https://www.foodforwardsa.org/' target='_blank' class='btn btn-sm btn-success mt-2'>Fhedza Website</a>",
            "shelter": "Vhudzulo:<br><a href='https://www.haven.org.za/' target='_blank' class='btn btn-sm btn-info mt-2'>Fhedza Website</a>",
            "safety": "Vhulungoni:<br><a href='https://jhbchildwelfare.org.za/' target='_blank' class='btn btn-sm btn-info mt-2'>Fhedza Website</a>",
            "psychologist": "Thuso ya ṱhanziela ya monagano:<br><a href='https://www.lifelinejhb.org.za/' target='_blank' class='btn btn-sm btn-primary mt-2'>Fhedza Website</a>",
            "social_worker": "Thuso ya mushumeli wa vhathu:<br><a href='https://www.dsd.gov.za' target='_blank' class='btn btn-sm btn-warning mt-2'>Fhedza Website</a>",
            "education": "Thuso ya vhana na vhuḓidini:<br><a href='https://graduates24.com/' target='_blank' class='btn btn-sm btn-secondary mt-2'>Fhedza Website</a>",
            "case": "U tevhela siaṱari kana thuso ya mulayo:<br><a href='https://www.justice.gov.za/' target='_blank' class='btn btn-sm btn-info mt-2'>Fhedza SAPS</a><br><a href='https://www.justice.gov.za' target='_blank' class='btn btn-sm btn-dark mt-2'>Fhedza Muhasho wa Vhulungoni</a>",
            "call_back": "U kopa u vhidzwa hafhu, ni kombela ni nyite vhuṱanzi haṋu."
        },
        "isiNdebele": {
            "food": "Usizo lokudla oluphuthumayo:<br><a href='https://www.foodforwardsa.org/' target='_blank' class='btn btn-sm btn-success mt-2'>Vakashela iwebhusayithi</a>",
            "shelter": "Indawo yokuhlala:<br><a href='https://www.haven.org.za/' target='_blank' class='btn btn-sm btn-info mt-2'>Vakashela iwebhusayithi</a>",
            "safety": "Ukuphepha:<br><a href='https://jhbchildwelfare.org.za/' target='_blank' class='btn btn-sm btn-info mt-2'>Vakashela iwebhusayithi</a>",
            "psychologist": "Usizo lwezengqondo:<br><a href='https://www.lifelinejhb.org.za/' target='_blank' class='btn btn-sm btn-primary mt-2'>Vakashela iwebhusayithi</a>",
            "social_worker": "Usizo lomsebenzi wezenhlalakahle:<br><a href='https://www.dsd.gov.za' target='_blank' class='btn btn-sm btn-warning mt-2'>Vakashela iwebhusayithi</a>",
            "education": "Usizo lwezingane nemfundo:<br><a href='https://graduates24.com/' target='_blank' class='btn btn-sm btn-secondary mt-2'>Vakashela iwebhusayithi</a>",
            "case": "Ukulandela icala noma usizo lwezomthetho:<br><a href='https://www.justice.gov.za/' target='_blank' class='btn btn-sm btn-info mt-2'>Vakashela i-SAPS</a><br><a href='https://www.justice.gov.za' target='_blank' class='btn btn-sm btn-dark mt-2'>Vakashela uMnyango Wezobulungiswa</a>",
            "call_back": "Ukucela ukubuyiselwa emuva, sicela unikeze imininingwane yakho."
        },
        "SiSwati": {
            "food": "Lusito lwekudla loluphutfumele:<br><a href='https://www.foodforwardsa.org/' target='_blank' class='btn btn-sm btn-success mt-2'>Vakashela iwebhusayithi</a>",
            "shelter": "Indzawo yekuhlala:<br><a href='https://www.haven.org.za/' target='_blank' class='btn btn-sm btn-info mt-2'>Vakashela iwebhusayithi</a>",
            "safety": "Indzawo yekuphepha:<br><a href='https://jhbchildwelfare.org.za/' target='_blank' class='btn btn-sm btn-info mt-2'>Vakashela iwebhusayithi</a>",
            "psychologist": "Lusito lwekucabanga/ingcondvo:<br><a href='https://www.lifelinejhb.org.za/' target='_blank' class='btn btn-sm btn-primary mt-2'>Vakashela iwebhusayithi</a>",
            "social_worker": "Lusito lwemsebenti wesintfu:<br><a href='https://www.dsd.gov.za' target='_blank' class='btn btn-sm btn-warning mt-2'>Vakashela iwebhusayithi</a>",
            "education": "Lusito lwevana nemfundvo:<br><a href='https://graduates24.com/' target='_blank' class='btn btn-sm btn-secondary mt-2'>Vakashela iwebhusayithi</a>",
            "case": "Kulandzelwa kwegcwala noma lusito lwemthetho:<br><a href='https://www.justice.gov.za/' target='_blank' class='btn btn-sm btn-info mt-2'>Vakashela SAPS</a><br><a href='https://www.justice.gov.za' target='_blank' class='btn btn-sm btn-dark mt-2'>Vakashela Umnyango Wezobulungiswa</a>",
            "call_back": "Kucela kubuyiselwa emuva, sicela unikeze imininingwane yakho."
        }
    },

    "follow_up": {
        "English": "Is there anything else you need? (yes / no)",
        "Afrikaans": "Is daar nog iets waarmee jy hulp benodig? (ja / nee)",
        "isiZulu": "Ingabe kukhona okunye okudingayo? (yebo / cha)",
        "isiXhosa": "Ingaba kukho enye into oyidingayo? (ewe / hayi)",
        "Sesotho": "Na ho na le ntho e ’ngoe eo u e hlokang? (ee / che)",
        "Setswana": "A go na le sengwe se sengwe se o se tlhokang? (ee / nnyaa)",
        "Sepedi": "Na go na le sengwe se sengwe seo o se nyakago? (ee / aowa)",
        "Xitsonga": "Xana ku na swin’wana leswi u swi lavaka? (ee / e-e)",
        "Tshivenda": "Ni khou ṱoḓa zwinwe? (ee / hai)",
        "isiNdebele": "Kukhona okunye okudingayo? (yebo / cha)",
        "SiSwati": "Kukhona lokunye lokudzingako? (yebo / cha)"
    },

    "goodbye": {
        "English": "Thank you for reaching out. Remember, politics can be stressful but your wellbeing matters. Goodbye.",
        "Afrikaans": "Dankie dat jy uitgereik het. Onthou, politiek kan stresvol wees maar jou welstand maak saak. Totsiens.",
        "isiZulu": "Ngiyabonga ngokuxhumana. Khumbula, ezombusazwe zingaba nzima kodwa impilo yakho ibalulekile. Hamba kahle.",
        "isiXhosa": "Enkosi ngokunxibelelana. Khumbula, ezopolitiko zinokuba nzima kodwa impilo yakho ibalulekile. Hamba kakuhle.",
        "Sesotho": "Rea leboha ka ho ikopanya. Hopola, lipolotiki li ka ba thata empa bophelo ba hao bo bohlokoa. Tsamaya hantle.",
        "Setswana": "Re leboga ka go ikopanya. Gopola, dipolotiki di ka nna thata mme boitekanelo jwa gago bo botlhokwa. Tsamaya sentle.",
        "Sepedi": "Re leboga ka go ikopanya. Gopola, dipolotiki di ka ba thata eupša bophelo bja gago bo bohlokwa. Tsamaya gabotse.",
        "Xitsonga": "Hi khensa ku tihlanganisa. Tsundzuka, tipolitiki ti nga va to tika kambe vutomi bya wena byi na nkoka. Famba kahle.",
        "Tshivenda": "Ro livhuwa u kwama. Humbulani, zwa politiki zwi nga vha zwi tshinyana fhedzi vhutshilo haṋu ho khwaṱhisa. Fhambani zwavhudi.",
        "isiNdebele": "Siyabonga ngokuxhumana. Khumbula, ezombusazwe zingaba nzima kodwa impilo yakho ibalulekile. Hamba kahle.",
        "SiSwati": "Siyabonga ngekuxhumana. Khumbula, ezombusazwe tingaba nzima kodvwa kuphila kwakho kubalulekile. Hamba kahle."
    }
}


language_aliases = {
    "english": "English", "afrikaans": "Afrikaans",
    "zulu": "isiZulu", "isizulu": "isiZulu",
    "xhosa": "isiXhosa", "isixhosa": "isiXhosa",
    "sesotho": "Sesotho", "setswana": "Setswana", "tswana": "Setswana",
    "sepedi": "Sepedi", "northern sotho": "Sepedi",
    "xitsonga": "Xitsonga", "tsonga": "Xitsonga",
    "tshivenda": "Tshivenda", "venda": "Tshivenda",
    "isindebele": "isiNdebele", "ndebele": "isiNdebele",
    "siswati": "SiSwati", "swati": "SiSwati"
}

affirmations = [
    "You are stronger than you think.",
    "Your voice matters in politics.",
    "Taking care of your mental health is powerful.",
    "Change begins with small steps.",
    "You are not alone in this journey.",
    "Healing takes time, and that’s okay.",
    "It’s brave to ask for help.",
    "Your feelings are valid.",
    "Every day is a chance to grow.",
    "You deserve peace and safety."
]

resources = [
    {"name": "SADAG", "phone": "0800 567 567", "whatsapp": "076 882 2775", "url": "https://www.sadag.org"},
    {"name": "LifeLine South Africa", "phone": "0861 322 322", "url": "https://lifelinesa.co.za"},
    {"name": "Childline South Africa", "phone": "0800 055 555", "url": "https://www.childlinesa.org.za"},
    {"name": "Department of Social Development", "url": "https://www.dsd.gov.za"},
    {"name": "Child Welfare South Africa", "url": "https://www.childwelfaresa.org.za"},
    {"name": "Department of Justice", "url": "https://www.justice.gov.za"},
    {"name": "SAPS Victim Support", "url": "https://www.saps.gov.za"},
]

# --- News page ---
# --- News page ---
def sa_politics_news(request):
    articles = [
        {
            "title": "Explore your next President, but first check‑in on your mental health!",
            "description": "Please click on the link below for our Politics Chatbot, Affirmations and Resources:",
            "url": "/chatbot/"
        }
    ]
    leaders = Leader.objects.all()
    return render(request, "sa_politics_news.html", {"articles": articles, "leaders": leaders})

# --- Home view (optional, points to news) ---
def home_view(request):
    return sa_politics_news(request)

def chatbot_view(request):
    if "conversation" not in request.session:
        request.session["language"] = None
        request.session["conversation"] = [
            {"sender": "bot", "text": translations["intro"]["English"], "new": True}
        ]
        request.session["awaiting_yes_no"] = False

    conversation = request.session["conversation"]
    language = request.session["language"]

    # Multilingual keyword mapping
    resource_keywords = {
        "food": ["food", "kos", "ukudla", "ukutya", "dijo", "swakudya", "zwiḽiwa", "kudla"],
        "shelter": ["shelter", "skuiling", "indawo yokuhlala", "bolulo", "ndhawu yo tshama", "vhudzulo", "indzawo yekuhlala"],
        "safety": ["safety", "veiligheid", "ukuphepha", "vuhlayiseki", "polokeho", "tshireletso", "vhulungoni", "kuphepha"],
        "psychologist": [
            "psychologist", "sielkundige", "udokotela wezengqondo", "ugqirha wezengqondo",
            "setsebi sa kelello", "setsebi sa maikutlo", "setsebi sa monagano",
            "dokodela wa mianakanyo", "dokodela wa ṱhanziela", "dokotela wekwati kwengcondvo"
        ],
        "social_worker": [
            "social worker", "maatskaplike werker", "umphathi wezenhlalakahle", "mosebeletsi oa sechaba",
            "modiri wa loago", "modiri wa setšhaba", "mushandzisi wa vaaki", "mushumeli wa vhathu", "umsebenti wesintfu"
        ],
        "education": ["education", "onderwys", "imfundo", "thuto", "dyondzo", "vhuḓidini", "imfundvo"],
        "case": ["case", "saak", "icala", "ityala", "nyeoe", "kgang", "mhaka", "siaṱari", "licala"],
        "call_back": [
            "call back", "callback", "terugbel", "ukubuyiselwa emuva", "umnxeba", "ho letsetsoa hape",
            "go letsetsiwa gape", "go letsetšwa gape", "ku foniwa nakambe", "u vhidzwa hafhu", "kubuyiselwa emuva"
        ],
    }

    yes_keywords = {"yes", "ja", "yebo", "ewe", "ee"}
    no_keywords = {"no", "nee", "cha", "hayi", "che", "nnyaa", "aowa", "e-e", "hai"}

    if request.method == "POST":
        if "clear_chat" in request.POST:
            request.session["language"] = None
            request.session["conversation"] = [
                {"sender": "bot", "text": translations["intro"]["English"], "new": True}
            ]
            request.session["awaiting_yes_no"] = False
            conversation = request.session["conversation"]
            language = request.session["language"]
        else:
            user_message = request.POST.get("user_message", "").strip()
            if user_message:
                conversation.append({"sender": "you", "text": user_message})
                lower = user_message.lower()

                # If we are waiting for yes/no
                if request.session.get("awaiting_yes_no", False):
                    for msg in conversation:
                        if msg["sender"] == "bot":
                            msg["new"] = False

                    if lower in yes_keywords:
                        bot_reply = translations["menu"][language]
                        conversation.append({"sender": "bot", "text": bot_reply, "new": True})
                        request.session["awaiting_yes_no"] = False
                    elif lower in no_keywords:
                        bot_reply = translations["goodbye"][language]
                        conversation.append({"sender": "bot", "text": bot_reply, "new": True})
                        request.session["awaiting_yes_no"] = False
                    else:
                        conversation.append({"sender": "bot", "text": translations["follow_up"][language], "new": True})

                    request.session["conversation"] = conversation
                    request.session["language"] = language

                # Language selection flow
                elif language is None:
                    for msg in conversation:
                        if msg["sender"] == "bot":
                            msg["new"] = False

                    if lower in language_aliases:
                        request.session["language"] = language_aliases[lower]
                        language = request.session["language"]
                        bot_reply = translations["menu"][language]
                    else:
                        bot_reply = "Please type one of the languages listed."
                    conversation.append({"sender": "bot", "text": bot_reply, "new": True})

                else:
                    # Handle help options
                    matched_option = None
                    for option, keywords in resource_keywords.items():
                        if any(k in lower for k in keywords):
                            matched_option = option
                            break

                    if matched_option:
                        bot_reply = translations["resources"][language][matched_option]
                        for msg in conversation:
                            if msg["sender"] == "bot":
                                msg["new"] = False
                        conversation.append({"sender": "bot", "text": bot_reply, "new": True})
                        conversation[-1]["new"] = False
                        conversation.append({"sender": "bot", "text": translations["follow_up"][language], "new": True})
                        request.session["awaiting_yes_no"] = True

                    elif lower in yes_keywords:
                        bot_reply = translations["menu"][language]
                        for msg in conversation:
                            if msg["sender"] == "bot":
                                msg["new"] = False
                        conversation.append({"sender": "bot", "text": bot_reply, "new": True})
                        request.session["awaiting_yes_no"] = False

                    elif lower in no_keywords:
                        bot_reply = translations["goodbye"][language]
                        for msg in conversation:
                            if msg["sender"] == "bot":
                                msg["new"] = False
                        conversation.append({"sender": "bot", "text": bot_reply, "new": True})
                        request.session["awaiting_yes_no"] = False

                    else:
                        bot_reply = translations["menu"][language]
                        for msg in conversation:
                            if msg["sender"] == "bot":
                                msg["new"] = False
                        conversation.append({"sender": "bot", "text": bot_reply, "new": True})

        request.session["conversation"] = conversation
        request.session["language"] = language

    # ✅ Only one return at the end
    return render(request, "chatbot.html", {
        "conversation": request.session["conversation"],
        "affirmations": affirmations,
        "resources": resources
    })

    # Multilingual keyword mapping (all resources for all languages)
    resource_keywords = {
        "food": ["food", "kos", "ukudla", "ukutya", "dijo", "swakudya", "zwiḽiwa", "kudla"],
        "shelter": ["shelter", "skuiling", "safety", "indawo yokuhlala", "bolulo", "ndhawu yo tshama", "vhudzulo", "indzawo yekuhlala"],
        "psychologist": [
            "psychologist", "sielkundige", "udokotela wezengqondo", "ugqirha wezengqondo",
            "setsebi sa kelello", "setsebi sa maikutlo", "setsebi sa monagano",
            "dokodela wa mianakanyo", "dokodela wa ṱhanziela", "dokotela wekwati kwengcondvo"
        ],
        "social_worker": [
            "social worker", "maatskaplike werker", "umphathi wezenhlalakahle", "mosebeletsi oa sechaba",
            "modiri wa loago", "modiri wa setšhaba", "mushandzisi wa vaaki", "mushumeli wa vhathu", "umsebenti wesintfu"
        ],
        "education": ["education", "onderwys", "imfundo", "thuto", "dyondzo", "vhuḓidini", "imfundvo"],
        "case": ["case", "saak", "icala", "ityala", "nyeoe", "kgang", "mhaka", "siaṱari", "licala"],
        "call_back": [
            "call back", "callback", "terugbel", "ukubuyiselwa emuva", "umnxeba", "ho letsetsoa hape",
            "go letsetsiwa gape", "go letsetšwa gape", "ku foniwa nakambe", "u vhidzwa hafhu", "kubuyiselwa emuva"
        ],
    }

    # Yes/No across languages
    yes_keywords = {"yes", "ja", "yebo", "ewe", "ee"}
    no_keywords = {"no", "nee", "cha", "hayi", "che", "nnyaa", "aowa", "e-e", "hai"}

    if request.method == "POST":
        if "clear_chat" in request.POST:
            request.session["language"] = None
            request.session["conversation"] = [
                {"sender": "bot", "text": translations["intro"]["English"], "new": True}
            ]
            request.session["awaiting_yes_no"] = False
            conversation = request.session["conversation"]
            language = request.session["language"]
        else:
            user_message = request.POST.get("user_message", "").strip()
            if user_message:
                conversation.append({"sender": "you", "text": user_message})
                lower = user_message.lower()

                # If we are waiting for yes/no, handle that first
                if request.session.get("awaiting_yes_no", False):
                    # Clear 'new' from previous bot messages
                    for msg in conversation:
                        if msg["sender"] == "bot":
                            msg["new"] = False

                    if lower in yes_keywords:
                        # Show the menu again (in chosen language)
                        bot_reply = translations["menu"][language]
                        conversation.append({"sender": "bot", "text": bot_reply, "new": True})
                        request.session["awaiting_yes_no"] = False
                    elif lower in no_keywords:
                        # Goodbye (in chosen language)
                        bot_reply = translations["goodbye"][language]
                        conversation.append({"sender": "bot", "text": bot_reply, "new": True})
                        request.session["awaiting_yes_no"] = False
                    else:
                        # Invalid answer → re-ask yes/no (in chosen language)
                        conversation.append({"sender": "bot", "text": translations["follow_up"][language], "new": True})

                    request.session["conversation"] = conversation
                    request.session["language"] = language

                    return render(request, "chatbot.html", {
                        "conversation": conversation,
                        "affirmations": affirmations,
                        "resources": resources
                    })

                # Language selection flow
                if language is None:
                    # Clear 'new' flags
                    for msg in conversation:
                        if msg["sender"] == "bot":
                            msg["new"] = False

                    if lower in language_aliases:
                        request.session["language"] = language_aliases[lower]
                        language = request.session["language"]
                        bot_reply = translations["menu"][language]
                    else:
                        bot_reply = "Please type one of the languages listed."
                    conversation.append({"sender": "bot", "text": bot_reply, "new": True})

                else:
                    # Handle help options using multilingual keyword mapping
                    matched_option = None
                    for option, keywords in resource_keywords.items():
                        if any(k in lower for k in keywords):
                            matched_option = option
                            break

                    if matched_option:
                        # Reply with the resource in chosen language (button intact)
                        bot_reply = translations["resources"][language][matched_option]
                        # Clear 'new' flags on previous bot messages
                        for msg in conversation:
                            if msg["sender"] == "bot":
                                msg["new"] = False
                        conversation.append({"sender": "bot", "text": bot_reply, "new": True})
                        # Freeze resource reply (no typing effect), animate follow-up only
                        conversation[-1]["new"] = False
                        conversation.append({"sender": "bot", "text": translations["follow_up"][language], "new": True})
                        request.session["awaiting_yes_no"] = True

                    elif lower in yes_keywords:
                        bot_reply = translations["menu"][language]
                        # Clear 'new' flags
                        for msg in conversation:
                            if msg["sender"] == "bot":
                                msg["new"] = False
                        conversation.append({"sender": "bot", "text": bot_reply, "new": True})
                        request.session["awaiting_yes_no"] = False

                    elif lower in no_keywords:
                        bot_reply = translations["goodbye"][language]
                        # Clear 'new' flags
                        for msg in conversation:
                            if msg["sender"] == "bot":
                                msg["new"] = False
                        conversation.append({"sender": "bot", "text": bot_reply, "new": True})
                        request.session["awaiting_yes_no"] = False

                    else:
                        # Default: show menu again for unknown input
                        bot_reply = translations["menu"][language]
                        # Clear 'new' flags
                        for msg in conversation:
                            if msg["sender"] == "bot":
                                msg["new"] = False
                        conversation.append({"sender": "bot", "text": bot_reply, "new": True})

        request.session["conversation"] = conversation
        request.session["language"] = language

    return render(request, "chatbot.html", {
        "conversation": request.session["conversation"],
        "affirmations": affirmations,
        "resources": resources
    })
