
# ============================================================
# LEAFVISION AI - TOMATO DISEASE ADVICE
# English + Marathi
# Area unit: Acre
# Sprayer capacity: 15 litres
# ============================================================

SPRAYER_CAPACITY = 15.0

SOURCES = {
    "NIPHM_TOMATO_IPM": "https://niphm.gov.in/IPMPackages/Tomato.pdf",
    "ICAR_KHARIF_2025": (
        "https://icar.gov.in/sites/default/files/Circulars/"
        "ICAR%20En-Kharif%20Agro-Advisories%20for%20Farmers%202025.pdf"
    ),
    "ICAR_LATE_BLIGHT_2026": (
        "https://epubs.icar.org.in/index.php/IndHort/article/view/164935"
    )
}

# ============================================================
# DISEASE DATABASE
# Each disease has its own treatment and prevention.
# Doses are only configured where a reference rate was supplied.
# ============================================================

DISEASES = {

    # 1. BACTERIAL SPOT
    "bacterial spot": {
        "en": {
            "name": "Bacterial Spot",
            "cause": "Bacterial infection",
            "product": "No verified chemical dose configured",
            "solution": "Field sanitation and disease-free seedlings",
            "active_ingredient": "Not specified",
            "purpose": "Reduce bacterial spread and protect healthy leaves.",
            "target": "Bacterial infection and infected plant material.",
            "application": [
                "Remove severely infected leaves.",
                "Dispose of infected plant material safely.",
                "Avoid handling plants when leaves are wet.",
                "Clean pruning tools after handling infected plants.",
                "Ask an agricultural expert before selecting a bactericide."
            ],
            "reference_dose": "No verified current product dose configured.",
            "dose_per_acre": None,
            "water_per_acre": None,
            "unit": "g",
            "fertilizer": "Use balanced NPK nutrition based on soil testing. Fertilizer does not cure bacterial infection.",
            "fertilizer_timing": "Apply basal nutrients during field preparation. Apply later nutrients according to crop stage and soil-test recommendations.",
            "fertilizer_dose": "No disease-specific fertilizer dose. Follow soil-test recommendations.",
            "precautions": [
                "Do not apply unverified antibiotics or pesticides.",
                "Clean tools after handling infected plants.",
                "Avoid moving from infected to healthy plants without cleaning tools.",
                "Follow the label of any approved product."
            ],
            "prevention": [
                "Use disease-free seeds and seedlings.",
                "Avoid overhead irrigation.",
                "Maintain suitable plant spacing.",
                "Remove infected plant debris.",
                "Avoid working among wet plants."
            ],
            "source": "NIPHM Tomato IPM package; verify chemical recommendations locally."
        },
        "mr": {
            "name": "बॅक्टेरियल स्पॉट",
            "cause": "जीवाणूजन्य संसर्ग",
            "product": "पडताळलेला रासायनिक डोस उपलब्ध नाही",
            "solution": "शेताची स्वच्छता आणि रोगमुक्त रोपे",
            "active_ingredient": "निश्चित केलेला नाही",
            "purpose": "जीवाणूंचा प्रसार कमी करणे आणि निरोगी पाने सुरक्षित ठेवणे.",
            "target": "जीवाणूजन्य संसर्ग आणि रोगग्रस्त वनस्पतींचे भाग.",
            "application": [
                "तीव्र रोगग्रस्त पाने काढून टाका.",
                "रोगग्रस्त भाग सुरक्षितपणे नष्ट करा.",
                "पाने ओली असताना झाडांना हाताळणे टाळा.",
                "रोगग्रस्त झाडे हाताळल्यानंतर कात्री आणि साधने स्वच्छ करा.",
                "जीवाणूनाशक निवडण्यापूर्वी कृषी तज्ज्ञांचा सल्ला घ्या."
            ],
            "reference_dose": "सध्याचा पडताळलेला उत्पादन डोस उपलब्ध नाही.",
            "dose_per_acre": None,
            "water_per_acre": None,
            "unit": "g",
            "fertilizer": "माती परीक्षणानुसार संतुलित NPK खत वापरा. खतामुळे जीवाणूजन्य रोग बरा होत नाही.",
            "fertilizer_timing": "शेत तयार करताना बेसल खत द्या. पुढील खत पीक अवस्था आणि माती परीक्षणानुसार द्या.",
            "fertilizer_dose": "रोगासाठी स्वतंत्र खताचा डोस नाही. माती परीक्षणानुसार खत वापरा.",
            "precautions": [
                "पडताळणी न केलेली प्रतिजैविके किंवा कीटकनाशके वापरू नका.",
                "रोगग्रस्त झाडे हाताळल्यानंतर साधने स्वच्छ करा.",
                "साधने स्वच्छ न करता रोगग्रस्त झाडांपासून निरोगी झाडांकडे जाऊ नका.",
                "मान्यताप्राप्त उत्पादनाचे लेबल पाळा."
            ],
            "prevention": [
                "रोगमुक्त बियाणे आणि रोपे वापरा.",
                "पानांवर वरून पाणी शिंपडणे टाळा.",
                "झाडांमध्ये योग्य अंतर ठेवा.",
                "रोगग्रस्त अवशेष काढून टाका.",
                "ओल्या झाडांमध्ये काम करणे टाळा."
            ],
            "source": "NIPHM टोमॅटो IPM मार्गदर्शक."
        }
    },

    # 2. EARLY BLIGHT
    "early blight": {
        "en": {
            "name": "Early Blight",
            "cause": "Fungal disease - Alternaria solani",
            "product": "Copper oxychloride 50% WP - reference option",
            "solution": "Use only if the current tomato product label permits it.",
            "active_ingredient": "Copper oxychloride 50% WP",
            "purpose": "Fungicide option for early blight disease management.",
            "target": "Early blight lesions on tomato leaves.",
            "application": [
                "Remove severely infected lower leaves.",
                "Use a calibrated sprayer.",
                "Cover leaf surfaces uniformly according to the product label.",
                "Avoid spraying during strong wind or immediately before rain.",
                "Follow the product label for repeat applications."
            ],
            "reference_dose": (
                "NIPHM reference: 1000 g in 300-400 L water per acre. "
                "The calculator uses 1000 g in 300 L as its calculation basis. "
                "Verify current product registration and label."
            ),
            "dose_per_acre": 1000,
            "water_per_acre": 300,
            "unit": "g",
            "fertilizer": "Balanced NPK based on soil testing. Avoid excessive nitrogen.",
            "fertilizer_timing": "Apply basal nutrients during field preparation. Split later nutrient applications according to crop stage and soil test.",
            "fertilizer_dose": "No disease-specific fertilizer dose. Follow soil-test recommendations.",
            "precautions": [
                "Wear gloves, protective clothing and eye protection.",
                "Follow the product label and pre-harvest interval.",
                "Do not exceed the approved dose.",
                "Do not mix products unless the label permits it.",
                "Keep children and animals away during spraying."
            ],
            "prevention": [
                "Remove infected lower leaves.",
                "Use mulch to reduce soil splashing.",
                "Water near the soil instead of wetting leaves.",
                "Maintain good airflow and plant spacing.",
                "Rotate crops where practical."
            ],
            "source": "NIPHM Tomato IPM package. Reference rate requires current label verification."
        },
        "mr": {
            "name": "अर्ली ब्लाइट",
            "cause": "बुरशीजन्य रोग - Alternaria solani",
            "product": "कॉपर ऑक्सिक्लोराइड 50% WP - संदर्भ पर्याय",
            "solution": "टोमॅटोवरील सध्याचे उत्पादन लेबल परवानगी देत असल्यासच वापरा.",
            "active_ingredient": "कॉपर ऑक्सिक्लोराइड 50% WP",
            "purpose": "अर्ली ब्लाइट व्यवस्थापनासाठी बुरशीनाशकाचा संदर्भ पर्याय.",
            "target": "टोमॅटोच्या पानांवरील अर्ली ब्लाइटची लक्षणे.",
            "application": [
                "तीव्र रोगग्रस्त खालची पाने काढून टाका.",
                "योग्य प्रकारे सेट केलेला फवारणी पंप वापरा.",
                "उत्पादनाच्या लेबलनुसार पानांवर समान फवारणी करा.",
                "जोरदार वाऱ्यात किंवा पावसाच्या अगोदर फवारणी करू नका.",
                "पुन्हा फवारणीसाठी उत्पादनाच्या लेबलवरील सूचना पाळा."
            ],
            "reference_dose": (
                "NIPHM संदर्भ: प्रति एकर 300-400 लिटर पाण्यात 1000 ग्रॅम. "
                "गणनेसाठी 300 लिटर पाण्याचा आधार घेतला आहे. "
                "सध्याचे उत्पादन लेबल तपासा."
            ),
            "dose_per_acre": 1000,
            "water_per_acre": 300,
            "unit": "g",
            "fertilizer": "माती परीक्षणानुसार संतुलित NPK खत वापरा. अतिरिक्त नत्र खत टाळा.",
            "fertilizer_timing": "शेत तयार करताना बेसल खत द्या. पुढील खत पीक अवस्था आणि माती परीक्षणानुसार विभागून द्या.",
            "fertilizer_dose": "रोगासाठी स्वतंत्र खताचा डोस नाही. माती परीक्षणानुसार खत वापरा.",
            "precautions": [
                "हातमोजे, संरक्षक कपडे आणि डोळ्यांचे संरक्षण वापरा.",
                "उत्पादनाचे लेबल आणि काढणीपूर्व प्रतीक्षा कालावधी पाळा.",
                "मान्य डोसपेक्षा जास्त वापरू नका.",
                "लेबल परवानगी देत नसेल तर इतर औषधांमध्ये मिसळू नका.",
                "फवारणीदरम्यान लहान मुले आणि जनावरांना दूर ठेवा."
            ],
            "prevention": [
                "रोगग्रस्त खालची पाने काढून टाका.",
                "मातीचे कण पानांवर उडू नयेत म्हणून आच्छादन वापरा.",
                "पानांवर पाणी न टाकता जमिनीजवळ पाणी द्या.",
                "हवेचा योग्य प्रवाह आणि झाडांमध्ये अंतर ठेवा.",
                "शक्य असल्यास पीक फेरपालट करा."
            ],
            "source": "NIPHM टोमॅटो IPM मार्गदर्शक. सध्याच्या उत्पादन लेबलची पडताळणी आवश्यक."
        }
    },

    # 3. LATE BLIGHT
    "late blight": {
        "en": {
            "name": "Late Blight",
            "cause": "Oomycete disease - Phytophthora infestans",
            "product": "Current registered late-blight product - expert verification required",
            "solution": "Use only a product currently registered for tomato late blight.",
            "active_ingredient": "Select from currently registered products.",
            "purpose": "Management of confirmed late blight.",
            "target": "Water-soaked and dark late-blight lesions.",
            "application": [
                "Remove severely infected plant parts.",
                "Seek prompt agricultural advice because late blight can spread rapidly.",
                "Use a calibrated sprayer if a registered product is recommended.",
                "Follow the exact label dose and application instructions."
            ],
            "reference_dose": "No product dose configured. Verify the current registered product label.",
            "dose_per_acre": None,
            "water_per_acre": None,
            "unit": "g",
            "fertilizer": "Maintain balanced nutrition. Fertilizer does not cure late blight.",
            "fertilizer_timing": "Apply basal and split nutrients according to soil testing and crop stage.",
            "fertilizer_dose": "No disease-specific fertilizer dose.",
            "precautions": [
                "Do not delay expert advice if symptoms spread rapidly.",
                "Wear appropriate protective equipment.",
                "Follow the product label and harvest waiting period.",
                "Do not use an unverified chemical mixture."
            ],
            "prevention": [
                "Avoid prolonged leaf wetness.",
                "Improve field drainage.",
                "Maintain suitable plant spacing.",
                "Remove infected plant debris.",
                "Monitor crops during cool and humid weather."
            ],
            "source": "NIPHM Tomato IPM package and ICAR late-blight advisory."
        },
        "mr": {
            "name": "लेट ब्लाइट",
            "cause": "बुरशीसदृश रोगकारक - Phytophthora infestans",
            "product": "लेट ब्लाइटसाठी सध्याचे मान्यताप्राप्त उत्पादन - तज्ज्ञांचा सल्ला आवश्यक",
            "solution": "टोमॅटोवरील लेट ब्लाइटसाठी सध्या मान्यताप्राप्त उत्पादनच वापरा.",
            "active_ingredient": "सध्याच्या मान्यताप्राप्त उत्पादनातून निवडा.",
            "purpose": "निश्चित झालेल्या लेट ब्लाइटचे व्यवस्थापन.",
            "target": "पाणचट आणि काळसर लेट ब्लाइटची लक्षणे.",
            "application": [
                "तीव्र रोगग्रस्त झाडाचे भाग काढून टाका.",
                "लेट ब्लाइट वेगाने पसरू शकतो; त्वरित कृषी तज्ज्ञांचा सल्ला घ्या.",
                "मान्यताप्राप्त उत्पादन सुचवल्यास योग्य फवारणी पंप वापरा.",
                "उत्पादनाच्या लेबलवरील डोस आणि सूचना पाळा."
            ],
            "reference_dose": "उत्पादनाचा डोस निश्चित केलेला नाही. सध्याचे मान्यताप्राप्त लेबल तपासा.",
            "dose_per_acre": None,
            "water_per_acre": None,
            "unit": "g",
            "fertilizer": "संतुलित पोषण ठेवा. खतामुळे लेट ब्लाइट बरा होत नाही.",
            "fertilizer_timing": "माती परीक्षण आणि पीक अवस्थेनुसार बेसल व विभागून खत द्या.",
            "fertilizer_dose": "रोगासाठी स्वतंत्र खताचा डोस नाही.",
            "precautions": [
                "लक्षणे वेगाने पसरल्यास तज्ज्ञांचा सल्ला घेण्यास उशीर करू नका.",
                "योग्य संरक्षक साधने वापरा.",
                "उत्पादनाचे लेबल आणि काढणीपूर्व प्रतीक्षा कालावधी पाळा.",
                "पडताळणी न केलेले रासायनिक मिश्रण वापरू नका."
            ],
            "prevention": [
                "पानांवर जास्त वेळ ओलावा राहू देऊ नका.",
                "शेतातील पाण्याचा निचरा सुधारा.",
                "झाडांमध्ये योग्य अंतर ठेवा.",
                "रोगग्रस्त अवशेष काढून टाका.",
                "थंड आणि दमट हवामानात पिकाची तपासणी करा."
            ],
            "source": "NIPHM टोमॅटो IPM मार्गदर्शक आणि ICAR लेट ब्लाइट सल्ला."
        }
    },

    # 4. LEAF MOLD
    "leaf mold": {
        "en": {
            "name": "Leaf Mold",
            "cause": "Fungal disease",
            "product": "No verified product dose configured",
            "solution": "Remove affected leaves and reduce humidity.",
            "active_ingredient": "Not specified",
            "purpose": "Reduce infected material and unfavourable humidity.",
            "target": "Leaf mold growth, especially under leaf surfaces.",
            "application": [
                "Remove badly affected leaves.",
                "Improve greenhouse ventilation.",
                "Avoid wetting leaves during irrigation.",
                "Confirm the disease before choosing a fungicide."
            ],
            "reference_dose": "No verified dose configured.",
            "dose_per_acre": None,
            "water_per_acre": None,
            "unit": "g",
            "fertilizer": "Use balanced nutrition according to soil testing.",
            "fertilizer_timing": "Apply basal nutrients before transplanting and later nutrients according to crop stage.",
            "fertilizer_dose": "No disease-specific fertilizer dose.",
            "precautions": [
                "Do not apply an unverified fungicide.",
                "Avoid unnecessary chemical spraying.",
                "Use protective equipment if a registered product is prescribed."
            ],
            "prevention": [
                "Maintain good airflow.",
                "Reduce excessive humidity.",
                "Maintain adequate spacing.",
                "Inspect leaf undersides regularly."
            ],
            "source": "General cultural management; product dose requires local agricultural verification."
        },
        "mr": {
            "name": "लीफ मोल्ड",
            "cause": "बुरशीजन्य रोग",
            "product": "पडताळलेला उत्पादन डोस उपलब्ध नाही",
            "solution": "रोगग्रस्त पाने काढा आणि आर्द्रता कमी करा.",
            "active_ingredient": "निश्चित केलेला नाही",
            "purpose": "रोगग्रस्त भाग आणि अनुकूल आर्द्रता कमी करणे.",
            "target": "विशेषतः पानांच्या खालच्या बाजूवरील बुरशीची वाढ.",
            "application": [
                "तीव्र रोगग्रस्त पाने काढून टाका.",
                "हरितगृहातील वायुवीजन सुधारा.",
                "पाणी देताना पानांवर पाणी पडू देऊ नका.",
                "बुरशीनाशक निवडण्यापूर्वी रोगाची खात्री करा."
            ],
            "reference_dose": "पडताळलेला डोस उपलब्ध नाही.",
            "dose_per_acre": None,
            "water_per_acre": None,
            "unit": "g",
            "fertilizer": "माती परीक्षणानुसार संतुलित खत वापरा.",
            "fertilizer_timing": "लागवडीपूर्वी बेसल खत आणि पुढील खत पीक अवस्थेनुसार द्या.",
            "fertilizer_dose": "रोगासाठी स्वतंत्र खताचा डोस नाही.",
            "precautions": [
                "पडताळणी न केलेले बुरशीनाशक वापरू नका.",
                "अनावश्यक रासायनिक फवारणी टाळा.",
                "मान्यताप्राप्त उत्पादन वापरताना संरक्षक साधने वापरा."
            ],
            "prevention": [
                "हवेचा योग्य प्रवाह ठेवा.",
                "अतिरिक्त आर्द्रता कमी करा.",
                "झाडांमध्ये पुरेसे अंतर ठेवा.",
                "पानांच्या खालच्या बाजूची नियमित तपासणी करा."
            ],
            "source": "सामान्य पीक व्यवस्थापन; रासायनिक डोसासाठी स्थानिक कृषी पडताळणी आवश्यक."
        }
    },

    # 5. SEPTORIA LEAF SPOT
    "septoria leaf spot": {
        "en": {
            "name": "Septoria Leaf Spot",
            "cause": "Fungal disease",
            "product": "Mancozeb 75% WP - reference option",
            "solution": "Use only if currently registered and labelled for tomato.",
            "active_ingredient": "Mancozeb 75% WP",
            "purpose": "Fungicide option listed for Septoria leaf spot management.",
            "target": "Septoria leaf spot lesions.",
            "application": [
                "Remove infected lower leaves.",
                "Dispose of infected material safely.",
                "Confirm the disease and check current registration.",
                "Apply uniformly according to the approved product label."
            ],
            "reference_dose": (
                "NIPHM reference: 600-800 g in 300 L water per acre. "
                "Calculator uses 600 g in 300 L as its calculation basis. "
                "Confirm current tomato label and registration."
            ),
            "dose_per_acre": 600,
            "water_per_acre": 300,
            "unit": "g",
            "fertilizer": "Balanced nutrition based on soil testing. No fertilizer cures Septoria.",
            "fertilizer_timing": "Apply basal nutrients during field preparation and split later nutrients according to crop stage and soil test.",
            "fertilizer_dose": "No disease-specific fertilizer dose.",
            "precautions": [
                "Check the exact formulation and tomato label.",
                "Wear protective equipment.",
                "Follow pre-harvest and re-entry instructions.",
                "Do not exceed the label dose."
            ],
            "prevention": [
                "Remove infected lower leaves.",
                "Use mulch to reduce soil splash.",
                "Avoid overhead watering.",
                "Rotate crops where practical."
            ],
            "source": "NIPHM Tomato IPM package. Reference rate; verify label."
        },
        "mr": {
            "name": "सेप्टोरिया लीफ स्पॉट",
            "cause": "बुरशीजन्य रोग",
            "product": "मॅन्कोझेब 75% WP - संदर्भ पर्याय",
            "solution": "टोमॅटोवरील सध्याच्या मान्यताप्राप्त लेबलनुसारच वापरा.",
            "active_ingredient": "मॅन्कोझेब 75% WP",
            "purpose": "सेप्टोरिया लीफ स्पॉट व्यवस्थापनासाठी संदर्भित बुरशीनाशक.",
            "target": "सेप्टोरिया लीफ स्पॉटची लक्षणे.",
            "application": [
                "रोगग्रस्त खालची पाने काढून टाका.",
                "रोगग्रस्त भाग सुरक्षितपणे नष्ट करा.",
                "रोगाची खात्री आणि सध्याची मान्यता तपासा.",
                "मान्यताप्राप्त उत्पादनाच्या लेबलनुसार समान फवारणी करा."
            ],
            "reference_dose": (
                "NIPHM संदर्भ: प्रति एकर 300 लिटर पाण्यात 600-800 ग्रॅम. "
                "गणनेसाठी 600 ग्रॅम डोस वापरला आहे. "
                "टोमॅटोवरील सध्याचे लेबल आणि मान्यता तपासा."
            ),
            "dose_per_acre": 600,
            "water_per_acre": 300,
            "unit": "g",
            "fertilizer": "माती परीक्षणानुसार संतुलित पोषण द्या. खतामुळे सेप्टोरिया बरा होत नाही.",
            "fertilizer_timing": "शेत तयार करताना बेसल खत द्या आणि पुढील खत पीक अवस्था व माती परीक्षणानुसार द्या.",
            "fertilizer_dose": "रोगासाठी स्वतंत्र खताचा डोस नाही.",
            "precautions": [
                "अचूक फॉर्म्युलेशन आणि टोमॅटोवरील लेबल तपासा.",
                "संरक्षक साधने वापरा.",
                "काढणीपूर्व आणि पुनःप्रवेश सूचना पाळा.",
                "लेबलवरील डोसपेक्षा जास्त वापरू नका."
            ],
            "prevention": [
                "रोगग्रस्त खालची पाने काढून टाका.",
                "मातीचे कण उडू नयेत म्हणून आच्छादन वापरा.",
                "वरून पाणी शिंपडणे टाळा.",
                "शक्य असल्यास पीक फेरपालट करा."
            ],
            "source": "NIPHM टोमॅटो IPM मार्गदर्शक. संदर्भातील कमी डोस; लेबल तपासणे आवश्यक."
        }
    },

    # 6. SPIDER MITES
    "spider mites": {
        "en": {
            "name": "Spider Mites",
            "cause": "Mite pest - Tetranychus species",
            "product": "Fenazaquin 10% EC - reference option",
            "solution": "Use only if currently registered for tomato and spider mites.",
            "active_ingredient": "Fenazaquin 10% EC",
            "purpose": "Management of confirmed red spider mite infestation.",
            "target": "Spider mites on the undersides of tomato leaves.",
            "application": [
                "Confirm mites or webbing on leaf undersides.",
                "Use only a product currently registered for tomato and mites.",
                "Ensure label-directed coverage of leaf undersides.",
                "Follow the approved label for repeat application."
            ],
            "reference_dose": (
                "NIPHM reference: 500 ml in 200 L water per acre. "
                "Verify current label and crop registration."
            ),
            "dose_per_acre": 500,
            "water_per_acre": 200,
            "unit": "ml",
            "fertilizer": "Maintain balanced plant nutrition. Fertilizer does not control mites.",
            "fertilizer_timing": "Apply nutrients according to soil test and crop stage, not as a mite treatment.",
            "fertilizer_dose": "No mite-specific fertilizer dose.",
            "precautions": [
                "Confirm the pest before applying a miticide.",
                "Protect beneficial predatory mites and insects.",
                "Wear protective equipment.",
                "Follow label restrictions and harvest interval."
            ],
            "prevention": [
                "Inspect leaf undersides regularly.",
                "Avoid unnecessary broad-spectrum insecticides.",
                "Reduce dust and plant water stress.",
                "Conserve natural mite predators."
            ],
            "source": "NIPHM Tomato IPM package. Reference rate; current label verification required."
        },
        "mr": {
            "name": "स्पायडर माइट्स",
            "cause": "माइट्सची कीड - Tetranychus प्रजाती",
            "product": "फेनाझाक्विन 10% EC - संदर्भ पर्याय",
            "solution": "टोमॅटो आणि स्पायडर माइट्ससाठी सध्याची मान्यता असल्यासच वापरा.",
            "active_ingredient": "फेनाझाक्विन 10% EC",
            "purpose": "निश्चित झालेल्या लाल स्पायडर माइट्सचा प्रादुर्भाव नियंत्रित करणे.",
            "target": "टोमॅटोच्या पानांच्या खालच्या बाजूवरील स्पायडर माइट्स.",
            "application": [
                "पानांच्या खालच्या बाजूला माइट्स किंवा जाळी आहे का ते तपासा.",
                "टोमॅटो आणि माइट्ससाठी सध्या मान्यताप्राप्त उत्पादनच वापरा.",
                "लेबलनुसार पानांच्या खालच्या बाजूला फवारणी करा.",
                "पुन्हा फवारणीसाठी मान्यताप्राप्त लेबल पाळा."
            ],
            "reference_dose": (
                "NIPHM संदर्भ: प्रति एकर 200 लिटर पाण्यात 500 मिली. "
                "सध्याचे लेबल आणि पिकावरील मान्यता तपासा."
            ),
            "dose_per_acre": 500,
            "water_per_acre": 200,
            "unit": "ml",
            "fertilizer": "झाडांना संतुलित पोषण द्या. खतामुळे माइट्स नियंत्रित होत नाहीत.",
            "fertilizer_timing": "माती परीक्षण आणि पीक अवस्थेनुसार खत द्या; माइट्सच्या उपचारासाठी खत वापरू नका.",
            "fertilizer_dose": "माइट्ससाठी स्वतंत्र खताचा डोस नाही.",
            "precautions": [
                "माइट्सची खात्री झाल्यानंतरच माइटनाशक वापरा.",
                "उपयुक्त परभक्षी माइट्स आणि कीटकांचे संरक्षण करा.",
                "संरक्षक साधने वापरा.",
                "लेबलवरील सूचना आणि काढणीपूर्व प्रतीक्षा कालावधी पाळा."
            ],
            "prevention": [
                "पानांच्या खालच्या बाजूची नियमित तपासणी करा.",
                "अनावश्यक व्यापक-प्रभावाची कीटकनाशके टाळा.",
                "धूळ आणि पाण्याचा ताण कमी करा.",
                "नैसर्गिक परभक्षी माइट्सचे संरक्षण करा."
            ],
            "source": "NIPHM टोमॅटो IPM मार्गदर्शक. संदर्भ डोस; सध्याच्या लेबलची पडताळणी आवश्यक."
        }
    },

    # 7. TARGET SPOT
    "target spot": {
        "en": {
            "name": "Target Spot",
            "cause": "Fungal disease",
            "product": "No verified disease-specific dose configured",
            "solution": "Remove infected leaves and manage leaf wetness.",
            "active_ingredient": "Not specified",
            "purpose": "Reduce disease spread and infected material.",
            "target": "Target spot lesions on tomato leaves.",
            "application": [
                "Remove badly affected leaves.",
                "Dispose of infected plant material safely.",
                "Confirm the diagnosis before choosing a fungicide.",
                "Use only a product labelled for tomato and the confirmed disease."
            ],
            "reference_dose": "No verified target-spot dose configured.",
            "dose_per_acre": None,
            "water_per_acre": None,
            "unit": "g",
            "fertilizer": [
    "NPK 19:19:19",
    "NPK 12:32:16",
    "NPK 10:10:10",
    "Potassium Sulphate (00:00:50)",
    "Calcium Nitrate"
],

"fertilizer_timing": (
    "Apply according to crop growth stage and soil test results."
),

"fertilizer_dose": (
    "Follow soil test recommendations and product label instructions. "
    "Avoid excessive nitrogen application."
),
            "precautions": [
                "Do not use a fungicide based only on an AI prediction.",
                "Check current product registration and label.",
                "Wear protective equipment if a product is prescribed."
            ],
            "prevention": [
                "Maintain good airflow.",
                "Avoid overhead irrigation.",
                "Remove crop debris.",
                "Inspect nearby plants."
            ],
            "source": "Disease-specific chemical rate not verified in the references used."
        },
        "mr": {
            "name": "टार्गेट स्पॉट",
            "cause": "बुरशीजन्य रोग",
            "product": "रोगासाठी विशिष्ट पडताळलेला डोस उपलब्ध नाही",
            "solution": "रोगग्रस्त पाने काढा आणि पानांवरील ओलावा कमी करा.",
            "active_ingredient": "निश्चित केलेला नाही",
            "purpose": "रोगाचा प्रसार आणि संक्रमित भाग कमी करणे.",
            "target": "टोमॅटोच्या पानांवरील टार्गेट स्पॉटची लक्षणे.",
            "application": [
                "तीव्र रोगग्रस्त पाने काढून टाका.",
                "संक्रमित वनस्पतींचे भाग सुरक्षितपणे नष्ट करा.",
                "बुरशीनाशक निवडण्यापूर्वी रोगाची खात्री करा.",
                "टोमॅटो आणि निश्चित रोगासाठी लेबल असलेले उत्पादनच वापरा."
            ],
            "reference_dose": "टार्गेट स्पॉटसाठी पडताळलेला डोस उपलब्ध नाही.",
            "dose_per_acre": None,
            "water_per_acre": None,
            "unit": "g",
            "fertilizer": "माती परीक्षणानुसार संतुलित पोषण द्या.",
            "fertilizer_timing": "पीक अवस्था आणि माती परीक्षणानुसार बेसल व विभागून खत द्या.",
            "fertilizer_dose": "रोगासाठी स्वतंत्र खताचा डोस नाही.",
            "precautions": [
                "केवळ AI अंदाजावर आधारित बुरशीनाशक वापरू नका.",
                "सध्याची उत्पादन मान्यता आणि लेबल तपासा.",
                "उत्पादन सुचवले असल्यास संरक्षक साधने वापरा."
            ],
            "prevention": [
                "हवेचा योग्य प्रवाह ठेवा.",
                "वरून पाणी शिंपडणे टाळा.",
                "पिकांचे अवशेष काढून टाका.",
                "जवळच्या झाडांची तपासणी करा."
            ],
            "source": "वापरलेल्या संदर्भांमध्ये रोगासाठी विशिष्ट रासायनिक डोस पडताळलेला नाही."
        }
    },

    # 8. TOMATO YELLOW LEAF CURL VIRUS
    "tomato yellow leaf curl virus": {
        "en": {
            "name": "Tomato Yellow Leaf Curl Virus",
            "cause": "Viral disease spread by whiteflies",
            "product": "No product cures the virus",
            "solution": "Whitefly monitoring and integrated vector management.",
            "active_ingredient": "No virus-curing active ingredient",
            "purpose": "Reduce whitefly spread; this does not cure infected plants.",
            "target": "Whitefly vectors and infected plants.",
            "application": [
                "Inspect plants for whiteflies.",
                "Use yellow sticky traps for monitoring.",
                "Remove severely infected plants when advised.",
                "Use an insecticide only if whitefly infestation is confirmed and the product is registered for tomato."
            ],
            "reference_dose": "No pesticide dose cures this virus.",
            "dose_per_acre": None,
            "water_per_acre": None,
            "unit": "ml",
            "fertilizer": "Maintain balanced nutrition. Fertilizer cannot cure viral infection.",
            "fertilizer_timing": "Apply nutrients according to soil test and crop growth stage.",
            "fertilizer_dose": "No virus-specific fertilizer dose.",
            "precautions": [
                "Do not claim that insecticide cures the virus.",
                "Do not apply insecticides without confirming whiteflies.",
                "Follow the label of any approved vector-control product."
            ],
            "prevention": [
                "Use healthy seedlings.",
                "Grow resistant varieties where available.",
                "Monitor whiteflies.",
                "Remove weed hosts around the crop.",
                "Remove infected plants when advised."
            ],
            "source": "NIPHM Tomato IPM package: leaf curl and whitefly management."
        },
        "mr": {
            "name": "टोमॅटो यलो लीफ कर्ल व्हायरस",
            "cause": "पांढऱ्या माशीमुळे पसरणारा विषाणूजन्य रोग",
            "product": "विषाणू बरा करणारे उत्पादन उपलब्ध नाही",
            "solution": "पांढऱ्या माशीचे निरीक्षण आणि एकात्मिक नियंत्रण.",
            "active_ingredient": "विषाणू बरा करणारा सक्रिय घटक उपलब्ध नाही",
            "purpose": "पांढऱ्या माशीचा प्रसार कमी करणे; यामुळे बाधित झाड बरे होत नाही.",
            "target": "पांढरी माशी आणि बाधित झाडे.",
            "application": [
                "झाडांवर पांढऱ्या माशीची तपासणी करा.",
                "निरीक्षणासाठी पिवळे चिकट सापळे वापरा.",
                "सल्ल्यानुसार तीव्र बाधित झाडे काढून टाका.",
                "पांढऱ्या माशीचा प्रादुर्भाव निश्चित झाल्यास आणि टोमॅटोसाठी मान्य असल्यासच कीटकनाशक वापरा."
            ],
            "reference_dose": "कोणताही कीटकनाशक डोस हा विषाणू बरा करत नाही.",
            "dose_per_acre": None,
            "water_per_acre": None,
            "unit": "ml",
            "fertilizer": "संतुलित पोषण ठेवा. खतामुळे विषाणूजन्य रोग बरा होत नाही.",
            "fertilizer_timing": "माती परीक्षण आणि पीक अवस्थेनुसार खत द्या.",
            "fertilizer_dose": "विषाणूसाठी स्वतंत्र खताचा डोस नाही.",
            "precautions": [
                "कीटकनाशकामुळे विषाणू बरा होतो असा दावा करू नका.",
                "पांढऱ्या माशीची खात्री न करता कीटकनाशक वापरू नका.",
                "मान्यताप्राप्त नियंत्रण उत्पादनाचे लेबल पाळा."
            ],
            "prevention": [
                "निरोगी रोपे वापरा.",
                "उपलब्ध असल्यास प्रतिकारक्षम जाती वापरा.",
                "पांढऱ्या माशीचे निरीक्षण करा.",
                "पिकाजवळील तण काढा.",
                "सल्ल्यानुसार बाधित झाडे काढून टाका."
            ],
            "source": "NIPHM टोमॅटो IPM मार्गदर्शक: लीफ कर्ल आणि पांढरी माशी व्यवस्थापन."
        }
    },

    # 9. TOMATO MOSAIC VIRUS
    "tomato mosaic virus": {
        "en": {
            "name": "Tomato Mosaic Virus",
            "cause": "Viral disease",
            "product": "No curative pesticide",
            "solution": "Sanitation, healthy seed and prevention of mechanical transmission.",
            "active_ingredient": "Not applicable",
            "purpose": "Reduce spread through infected sap, tools and plant contact.",
            "target": "Virus transmission pathways.",
            "application": [
                "Confirm the disease with an agricultural expert.",
                "Remove infected plants when advised.",
                "Clean hands and tools after handling suspect plants.",
                "Do not apply fungicide as a cure for a virus."
            ],
            "reference_dose": "No pesticide dose cures this virus.",
            "dose_per_acre": None,
            "water_per_acre": None,
            "unit": "g",
            "fertilizer": "Maintain balanced nutrition. Fertilizer does not cure mosaic virus.",
            "fertilizer_timing": "Apply nutrients according to soil testing and crop stage.",
            "fertilizer_dose": "No virus-specific fertilizer dose.",
            "precautions": [
                "Do not use products claiming to cure the virus.",
                "Disinfect tools between plants.",
                "Dispose of infected plants safely."
            ],
            "prevention": [
                "Use healthy seeds.",
                "Clean tools and hands.",
                "Avoid transferring plant sap between plants.",
                "Remove infected plant debris."
            ],
            "source": "NIPHM Tomato IPM package: tomato mosaic disease information."
        },
        "mr": {
            "name": "टोमॅटो मोझॅक व्हायरस",
            "cause": "विषाणूजन्य रोग",
            "product": "रोग बरा करणारे कीटकनाशक उपलब्ध नाही",
            "solution": "स्वच्छता, निरोगी बियाणे आणि यांत्रिक प्रसार रोखणे.",
            "active_ingredient": "लागू नाही",
            "purpose": "संक्रमित रस, साधने आणि झाडांच्या संपर्कातून होणारा प्रसार कमी करणे.",
            "target": "विषाणू प्रसाराचे मार्ग.",
            "application": [
                "कृषी तज्ज्ञांकडून रोगाची खात्री करा.",
                "सल्ल्यानुसार संक्रमित झाडे काढून टाका.",
                "संशयित झाडे हाताळल्यानंतर हात आणि साधने स्वच्छ करा.",
                "विषाणू बरा करण्यासाठी बुरशीनाशक वापरू नका."
            ],
            "reference_dose": "कोणताही कीटकनाशक डोस हा विषाणू बरा करत नाही.",
            "dose_per_acre": None,
            "water_per_acre": None,
            "unit": "g",
            "fertilizer": "संतुलित पोषण ठेवा. खतामुळे मोझॅक विषाणू बरा होत नाही.",
            "fertilizer_timing": "माती परीक्षण आणि पीक अवस्थेनुसार खत द्या.",
            "fertilizer_dose": "विषाणूसाठी स्वतंत्र खताचा डोस नाही.",
            "precautions": [
                "विषाणू बरा करण्याचा दावा करणारी उत्पादने वापरू नका.",
                "प्रत्येक झाडानंतर साधने स्वच्छ करा.",
                "संक्रमित झाडे सुरक्षितपणे नष्ट करा."
            ],
            "prevention": [
                "निरोगी बियाणे वापरा.",
                "हात आणि साधने स्वच्छ ठेवा.",
                "एका झाडाचा रस दुसऱ्या झाडाला लागू देऊ नका.",
                "संक्रमित अवशेष काढून टाका."
            ],
            "source": "NIPHM टोमॅटो IPM मार्गदर्शक: टोमॅटो मोझॅक रोग."
        }
    },

    # 10. HEALTHY LEAF
    "healthy": {
        "en": {
            "name": "Healthy Tomato Leaf",
            "cause": "No disease detected by the classifier",
            "product": "No pesticide required",
            "solution": "Routine crop care and balanced nutrition.",
            "active_ingredient": "Not applicable",
            "purpose": "Maintain healthy plant growth.",
            "target": "Overall tomato plant health.",
            "application": [
                "Continue regular crop monitoring.",
                "Apply fertilizer based on soil test results.",
                "Irrigate according to crop requirement.",
                "Do not spray pesticides without a confirmed need."
            ],
            "reference_dose": "No pesticide dose required.",
            "dose_per_acre": None,
            "water_per_acre": None,
            "unit": "g",
            "fertilizer": "Balanced NPK and organic manure based on soil testing.",
            "fertilizer_timing": "Apply well-decomposed FYM before transplanting. Apply later nutrients in splits according to crop stage and soil test.",
            "fertilizer_dose": "Use soil-test-based recommendations; no universal dose is provided.",
            "precautions": [
                "Avoid unnecessary pesticide use.",
                "Do not over-apply nitrogen fertilizer.",
                "Follow irrigation and nutrient recommendations."
            ],
            "prevention": [
                "Use healthy seedlings.",
                "Maintain proper irrigation.",
                "Provide adequate sunlight and spacing.",
                "Monitor leaves regularly.",
                "Keep the field clean."
            ],
            "source": "NIPHM Tomato IPM package: crop-stage nutrient management."
        },
        "mr": {
            "name": "निरोगी टोमॅटोचे पान",
            "cause": "AI वर्गीकरणानुसार रोग आढळलेला नाही",
            "product": "कीटकनाशकाची आवश्यकता नाही",
            "solution": "नियमित पीक निगा आणि संतुलित पोषण.",
            "active_ingredient": "लागू नाही",
            "purpose": "झाडाची निरोगी वाढ टिकवून ठेवणे.",
            "target": "टोमॅटो झाडाचे एकूण आरोग्य.",
            "application": [
                "पिकाची नियमित तपासणी सुरू ठेवा.",
                "माती परीक्षणानुसार खत वापरा.",
                "पिकाच्या गरजेनुसार पाणी द्या.",
                "रोग निश्चित नसताना कीटकनाशक फवारू नका."
            ],
            "reference_dose": "कीटकनाशकाचा डोस आवश्यक नाही.",
            "dose_per_acre": None,
            "water_per_acre": None,
            "unit": "g",
            "fertilizer": "माती परीक्षणानुसार संतुलित NPK आणि सेंद्रिय खत वापरा.",
            "fertilizer_timing": "लागवडीपूर्वी पूर्ण कुजलेले शेणखत द्या. पुढील खत पीक अवस्था आणि माती परीक्षणानुसार विभागून द्या.",
            "fertilizer_dose": "माती परीक्षणानुसार खत वापरा; एकच सार्वत्रिक डोस दिलेला नाही.",
            "precautions": [
                "अनावश्यक कीटकनाशके वापरू नका.",
                "नत्र खताचा अतिरेक करू नका.",
                "पाणी आणि खत व्यवस्थापनाच्या सूचनांचे पालन करा."
            ],
            "prevention": [
                "निरोगी रोपे वापरा.",
                "योग्य प्रमाणात पाणी द्या.",
                "पुरेसा सूर्यप्रकाश आणि अंतर ठेवा.",
                "पानांची नियमित तपासणी करा.",
                "शेत स्वच्छ ठेवा."
            ],
            "source": "NIPHM टोमॅटो IPM मार्गदर्शक: पीक अवस्थेनुसार पोषण व्यवस्थापन."
        }
    }
}


# ============================================================
# DISEASE NAME NORMALIZATION
# This function is intentionally kept together with its aliases.
# It accepts common Keras/PlantVillage class-name formats.
# ============================================================

DISEASE_ALIASES = {
    "bacterial spot": "bacterial spot",
    "bacterial_spot": "bacterial spot",
    "early blight": "early blight",
    "early_blight": "early blight",
    "late blight": "late blight",
    "late_blight": "late blight",
    "leaf mold": "leaf mold",
    "leaf_mold": "leaf mold",
    "septoria leaf spot": "septoria leaf spot",
    "septoria_leaf_spot": "septoria leaf spot",
    "spider mites": "spider mites",
    "spider_mites": "spider mites",
    "two spotted spider mite": "spider mites",
    "target spot": "target spot",
    "target_spot": "target spot",
    "tomato yellow leaf curl virus": "tomato yellow leaf curl virus",
    "tomato_yellow_leaf_curl_virus": "tomato yellow leaf curl virus",
    "tomato yellow leaf curl": "tomato yellow leaf curl virus",
    "tomato mosaic virus": "tomato mosaic virus",
    "tomato_mosaic_virus": "tomato mosaic virus",
    "healthy": "healthy",
    "healthy leaf": "healthy",
    "healthy tomato leaf": "healthy"
}


def normalize_disease(disease_name):
    """Convert model output into a disease database key."""

    name = str(disease_name or "").lower().strip()

    # Remove common dataset prefixes.
    name = name.replace("tomato___", "")
    name = name.replace("tomato__", "")
    name = name.replace("tomato_", "")

    # Normalize separators.
    name = name.replace("_", " ")
    name = name.replace("-", " ")
    name = " ".join(name.split())

    # Exact match first.
    if name in DISEASE_ALIASES:
        return DISEASE_ALIASES[name]

    # Match known names inside longer model labels.
    for alias in sorted(DISEASE_ALIASES, key=len, reverse=True):
        if alias in name:
            return DISEASE_ALIASES[alias]

    return None


# ============================================================
# GET DISEASE ADVICE
# ============================================================

def get_disease_advice(disease_name, language="en", growth_stage=None):
    """
    Returns disease-specific advice in English or Marathi.

    Example:
        get_disease_advice("Tomato___Early_blight", "en")
        get_disease_advice("Late Blight", "mr")
    """

    key = normalize_disease(disease_name)

    lang_value = str(language or "en").lower().strip()
    lang = "mr" if lang_value in ("mr", "marathi") else "en"

    if key is None:
        if lang == "mr":
            return {
                "name": "अज्ञात रोग",
                "cause": "रोग निश्चित झालेला नाही",
                "product": "माहिती उपलब्ध नाही",
                "solution": "कृषी तज्ज्ञांकडून रोगाची खात्री करा.",
                "active_ingredient": "निश्चित नाही",
                "purpose": "रोगाची खात्री करणे.",
                "target": "निश्चित नाही",
                "application": ["पडताळणी न केलेले रसायन वापरू नका."],
                "reference_dose": "उपलब्ध नाही",
                "fertilizer": "माती परीक्षणानुसार खत वापरा.",
                "fertilizer_timing": "पीक अवस्था आणि माती परीक्षणानुसार.",
                "fertilizer_dose": "उपलब्ध नाही",
                "precautions": ["कृषी तज्ज्ञांचा सल्ला घ्या."],
                "prevention": ["पिकाची नियमित तपासणी करा."],
                "dose_per_acre": None,
                "water_per_acre": None,
                "unit": "g",
                "dose_available": False,
                "source": "No disease-specific source configured.",
                "disease_key": None,
                "language": lang,
                "growth_stage": growth_stage or "माहिती उपलब्ध नाही"
            }

        return {
            "name": "Unknown Disease",
            "cause": "Disease not identified",
            "product": "Information unavailable",
            "solution": "Consult an agricultural expert to confirm the disease.",
            "active_ingredient": "Not specified",
            "purpose": "Confirm the diagnosis.",
            "target": "Not specified",
            "application": ["Do not use unverified chemicals."],
            "reference_dose": "Not available",
            "fertilizer": "Use fertilizer based on soil testing.",
            "fertilizer_timing": "Based on crop stage and soil testing.",
            "fertilizer_dose": "Not available",
            "precautions": ["Consult an agricultural expert."],
            "prevention": ["Monitor the crop regularly."],
            "dose_per_acre": None,
            "water_per_acre": None,
            "unit": "g",
            "dose_available": False,
            "source": "No disease-specific source configured.",
            "disease_key": None,
            "language": lang,
            "growth_stage": growth_stage or "Not specified"
        }

    # Return a copy so callers cannot modify the original database.
    advice = DISEASES[key][lang].copy()

    advice["disease_key"] = key
    advice["language"] = lang

    advice["dose_available"] = (
        advice.get("dose_per_acre") is not None
        and advice.get("water_per_acre") is not None
    )

    advice["growth_stage"] = growth_stage or (
        "माहिती उपलब्ध नाही" if lang == "mr" else "Not specified"
    )

    # Backward compatibility with templates that expect "treatment".
    advice["treatment"] = advice["application"]

    return advice


# ============================================================
# ACRE + 15 LITRE SPRAYER CALCULATOR
# ============================================================

def calculate_spray_quantity(
    disease_name,
    area_acres,
    water_litres_per_acre=None,
    tank_capacity=SPRAYER_CAPACITY,
    language="en"
):
    """
    Calculates product and water quantities from a configured
    reference dose per acre.

    This calculator does not invent missing doses.
    Verify the current product label before actual application.
    """

    advice = get_disease_advice(disease_name, language)

    if not advice["dose_available"]:
        raise ValueError(
            "No verified area-based product dose is configured "
            "for this disease. Do not calculate or invent a dose."
        )

    try:
        area = float(area_acres)
        tank = float(tank_capacity)
    except (TypeError, ValueError):
        raise ValueError("Enter valid numeric area and tank capacity.")

    if area <= 0:
        raise ValueError("Area must be greater than zero.")

    if tank <= 0:
        raise ValueError("Tank capacity must be greater than zero.")

    dose_per_acre = float(advice["dose_per_acre"])

    water_per_acre = (
        float(water_litres_per_acre)
        if water_litres_per_acre is not None
        else float(advice["water_per_acre"])
    )

    if water_per_acre <= 0:
        raise ValueError("Water per acre must be greater than zero.")

    total_water = area * water_per_acre
    total_product = area * dose_per_acre

    # Number of 15-litre tanks, rounding up.
    tank_count = int(np_ceil(total_water / tank)) if False else (
        int(total_water // tank) + (1 if total_water % tank > 0 else 0)
    )

    product_per_litre = dose_per_acre / water_per_acre
    product_per_full_tank = product_per_litre * tank

    last_tank_water = total_water % tank
    if last_tank_water == 0:
        last_tank_product = 0
    else:
        last_tank_product = product_per_litre * last_tank_water

    area_per_tank = tank / water_per_acre

    return {
        "disease": advice["name"],
        "area_acres": round(area, 3),
        "tank_capacity_litres": tank,
        "water_per_acre": round(water_per_acre, 2),
        "dose_per_acre": round(dose_per_acre, 2),
        "product_unit": advice["unit"],
        "total_water_litres": round(total_water, 2),
        "total_product": round(total_product, 2),
        "tank_count": tank_count,
        "product_per_litre": round(product_per_litre, 4),
        "product_per_full_tank": round(product_per_full_tank, 2),
        "last_tank_water_litres": round(last_tank_water, 2),
        "last_tank_product": round(last_tank_product, 2),
        "area_covered_by_full_tank_acres": round(area_per_tank, 4),
        "calculation_note": (
            "Calculated from the configured reference rate. "
            "Check current product registration and label before use."
        )
    }


# ============================================================
# BACKWARD COMPATIBILITY
# Existing app code can continue using get_advice().
# ============================================================

def get_advice(disease, language="en", growth_stage=None):
    return get_disease_advice(
        disease_name=disease,
        language=language,
        growth_stage=growth_stage
    )


# ============================================================
# TEST ALL 10 DISEASES
# Run: python disease_advice.py
# ============================================================

if __name__ == "__main__":

    print("\nLEAFVISION AI - DISEASE LOOKUP TEST\n")

    for disease_key in DISEASES:
        english = get_disease_advice(disease_key, "en")
        marathi = get_disease_advice(disease_key, "mr")

        print("-" * 55)
        print("Database key:", disease_key)
        print("English:", english["name"])
        print("English product:", english["product"])
        print("Marathi:", marathi["name"])
        print("Marathi product:", marathi["product"])
        print("Dose calculator available:", english["dose_available"])

    print("\nEARLY BLIGHT - 1 ACRE EXAMPLE")

    try:
        calculation = calculate_spray_quantity(
            disease_name="Tomato___Early_blight",
            area_acres=1,
            tank_capacity=15,
            language="en"
        )
        print(calculation)
    except ValueError as error:
        print("Calculator message:", error)
