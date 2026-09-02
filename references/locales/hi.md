# Hindi locale pack

This file is the fixed हिन्दी UI and intent contract for dj-crate-digger. The JSON block is consumed by the Skill; prose outside it is documentation.

```json
{
  "locale": "hi",
  "language_name": "Hindi",
  "native_name": "हिन्दी",
  "direction": "ltr",
  "market_policy": {
    "language_independent": true,
    "blank_region": "क्षेत्र खाली हो तो इस सत्र के लिए केवल व्यापक हिंदी-भाषी बाज़ार का उपयोग करें।",
    "explicit_region": "स्पष्ट रूप से दिया गया देश या क्षेत्र भाषा-अनुमान पर प्राथमिकता रखता है, संचार भाषा नहीं बदलता।",
    "persistence": "लक्षित बाज़ार को दीर्घकालिक पसंद के रूप में न सहेजें।"
  },
  "quick_start": {
    "intro": "DJ चयन सहायक में आपका स्वागत है। यह Agent Skill आपको DJ सेट बनाने में मदद करता है। आप दो चरणों में अपनी ज़रूरत की पुष्टि करेंगे और ट्रैक सुझाव पाएँगे। भरने के नियम:",
    "tutorial_label": "एक-क्लिक Set आयात मार्गदर्शिका",
    "tutorial_url": "https://github.com/komakizhu/dj-crate-digger/blob/main/docs/w4dj/README.en.md"
  },
  "intake": {
    "round_1": {
      "title": "[पहला चरण: आवश्यक जानकारी]",
      "rules": [
        "1. आप उदाहरण कॉपी कर सकते हैं, अपनी तरह भर सकते हैं या खाली छोड़ सकते हैं",
        "2. खाली छोड़ने का अर्थ है कि AI संकेतों के आधार पर उत्तर का बुद्धिमानी से निर्णय करेगा"
      ],
      "fields": [
        {
          "key": "scene",
          "label": "परिस्थिति",
          "example": "प्रदर्शन का संदर्भ। उदाहरण: `bar` / `club` / `wedding` / `art exhibition`"
        },
        {
          "key": "target_market",
          "label": "लक्षित देश / क्षेत्र",
          "example": "उदाहरण: `Mainland China` / `Taiwan` / `Hong Kong` / `Japan` / `international English market`"
        },
        {
          "key": "core_sound",
          "label": "मुख्य ध्वनि दिशा",
          "example": "संदर्भ कलाकार, ट्रैक और शैली। उदाहरण: `Skrillex` का `Tears`, आधुनिक `UK Bass`"
        },
        {
          "key": "track_count_or_duration",
          "label": "ट्रैक संख्या या सेट अवधि",
          "example": "उदाहरण: `20 tracks` / `60 minutes`"
        },
        {
          "key": "output_mode",
          "label": "आउटपुट संस्करण",
          "example": "Fast / Brief / Rich विकल्प"
        },
        {
          "key": "other",
          "label": "अन्य सीमाएँ",
          "example": "उदाहरण: `बहुत बज चुके ट्रैक नहीं`, `वोकल नहीं`, `केवल Remix`; वैकल्पिक"
        }
      ],
      "prompt": "DJ चयन सहायक में आपका स्वागत है। यह Agent Skill आपको DJ सेट बनाने में मदद करता है। आप दो चरणों में अपनी ज़रूरत की पुष्टि करेंगे और ट्रैक सुझाव पाएँगे। भरने के नियम:\n\n1. आप उदाहरण कॉपी कर सकते हैं, अपनी तरह भर सकते हैं या खाली छोड़ सकते हैं\n2. खाली छोड़ने का अर्थ है कि AI संकेतों के आधार पर उत्तर का बुद्धिमानी से निर्णय करेगा\n\n[पहला चरण: आवश्यक जानकारी]\n\nपरिस्थिति:\n“प्रदर्शन का संदर्भ। उदाहरण: `bar` / `club` / `wedding` / `art exhibition`”\nलक्षित देश / क्षेत्र:\n“उदाहरण: `Mainland China` / `Taiwan` / `Hong Kong` / `Japan` / `international English market`”\nमुख्य ध्वनि दिशा:\n“संदर्भ कलाकार, ट्रैक और शैली। उदाहरण: `Skrillex` का `Tears`, आधुनिक `UK Bass`”\nट्रैक संख्या या सेट अवधि:\n“उदाहरण: `20 tracks` / `60 minutes`”\nआउटपुट संस्करण:\n“`Fast`: तेज़ playlist आउटपुट; गुणवत्ता कम हो सकती है”\n“`Brief`: केवल एक संयुक्त playlist”\n“`Rich`: शैली, परिस्थिति और खोज के अलग दृष्टिकोण, फिर अंतिम संयुक्त playlist”\nअन्य सीमाएँ:\n“उदाहरण: `बहुत बज चुके ट्रैक नहीं`, `वोकल नहीं`, `केवल Remix`; वैकल्पिक”\n\n\u0060\u0060\u0060markdown\nपरिस्थिति:\nलक्षित देश / क्षेत्र:\nमुख्य ध्वनि दिशा:\nट्रैक संख्या या सेट अवधि:\nआउटपुट संस्करण:\nअन्य सीमाएँ:\n\u0060\u0060\u0060"
    },
    "round_2": {
      "title": "[दूसरा चरण: अनुरोध को स्पष्ट करना]",
      "rules": [
        "1. आप उदाहरण कॉपी कर सकते हैं, अपनी तरह भर सकते हैं या खाली छोड़ सकते हैं"
      ],
      "fields": [
        {
          "key": "style",
          "label": "विशिष्ट शैली",
          "example": "उदाहरण: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`"
        },
        {
          "key": "bpm",
          "label": "गति / BPM",
          "example": "उदाहरण: `105` / `128` / `140` / `150` / `170`"
        },
        {
          "key": "familiarity_era",
          "label": "परिचितता और खोज",
          "example": "`परिचित` / `संतुलित` / `खोज`"
        },
        {
          "key": "era_classic",
          "label": "युग और क्लासिक्स",
          "example": "`समकालीन` / `कुछ क्लासिक एंकर` / `नए-पुराने का पुल` / `क्लासिक्स पहले`"
        },
        {
          "key": "mood",
          "label": "मूड",
          "example": "उदाहरण: `नॉस्टैल्जिक` / `ठंडा` / `रोमांटिक`"
        },
        {
          "key": "energy",
          "label": "SET ऊर्जा स्तर या ऊर्जा वक्र",
          "example": "उदाहरण: `कम` / `ज़्यादा`; `स्थिर` / `रोलर कोस्टर`"
        },
        {
          "key": "platform",
          "label": "प्लेटफ़ॉर्म और लिंक आवश्यकताएँ",
          "example": "उदाहरण: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`; एक प्लेटफ़ॉर्म हो तो केवल वही, कई हों तो दिए क्रम की प्राथमिकता"
        },
        {
          "key": "other",
          "label": "अन्य",
          "example": ""
        }
      ],
      "prompt": "[दूसरा चरण: अनुरोध को स्पष्ट करना]\n\nविशिष्ट शैली:\n“उदाहरण: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`”\nगति / BPM:\n“उदाहरण: `105` / `128` / `140` / `150` / `170`”\nपरिचितता और खोज:\n“`परिचित` / `संतुलित` / `खोज`”\nयुग और क्लासिक्स:\n“`समकालीन` / `कुछ क्लासिक एंकर` / `नए-पुराने का पुल` / `क्लासिक्स पहले`”\nमूड:\n“उदाहरण: `नॉस्टैल्जिक` / `ठंडा` / `रोमांटिक`”\nSET ऊर्जा स्तर या ऊर्जा वक्र:\n“उदाहरण: `कम` / `ज़्यादा`; `स्थिर` / `रोलर कोस्टर`”\nप्लेटफ़ॉर्म और लिंक आवश्यकताएँ:\n“उदाहरण: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`; एक प्लेटफ़ॉर्म हो तो केवल वही, कई हों तो दिए क्रम की प्राथमिकता”\nअन्य:\n\n\u0060\u0060\u0060markdown\nविशिष्ट शैली:\nगति / BPM:\nपरिचितता और खोज:\nयुग और क्लासिक्स:\nमूड:\nSET ऊर्जा स्तर या ऊर्जा वक्र:\nप्लेटफ़ॉर्म और लिंक आवश्यकताएँ:\nअन्य:\n\u0060\u0060\u0060"
    }
  },
  "report": {
    "fast": {
      "title": "# Fast मोड",
      "first_batch_title": "# Fast पहली खेप",
      "final_title": "# Fast मोड",
      "columns": [
        "ट्रैक",
        "कलाकार",
        "लिंक"
      ],
      "next_steps": [
        {
          "label": "पहला | चयन प्रतिक्रिया साझा करें",
          "body": "यदि चाहें तो प्राकृतिक भाषा में बताएँ कि चयन कैसा रहा। इससे आपकी निजी पसंद और आगे के सुझाव बेहतर होंगे।"
        },
        {
          "label": "दूसरा | playlist निर्यात या हस्तांतरण",
          "body": "आप टेक्स्ट playlist निकाल सकते हैं या W4DJ को दे सकते हैं। `output text playlist` या `export to w4dj` लिखें।"
        }
      ],
      "digging_notes": "Digging नोट्स",
      "mix_suggestion": "Mix सुझाव",
      "unknown": "अज्ञात",
      "verified": "सत्यापित",
      "target_platform_missing": "लक्षित प्लेटफ़ॉर्म उपलब्ध नहीं"
    },
    "brief": {
      "title": "# Brief मोड",
      "first_batch_title": "# Brief मोड",
      "final_title": "# Brief मोड",
      "columns": [
        "ट्रैक",
        "कलाकार",
        "एल्बम / EP",
        "शैली",
        "BPM",
        "की",
        "अवधि",
        "ऊर्जा",
        "रिलीज़ तारीख",
        "नोट्स",
        "चयन कारण",
        "लिंक"
      ],
      "next_steps": [
        {
          "label": "पहला | चयन प्रतिक्रिया साझा करें",
          "body": "यदि चाहें तो प्राकृतिक भाषा में बताएँ कि चयन कैसा रहा। इससे आपकी निजी पसंद और आगे के सुझाव बेहतर होंगे।"
        },
        {
          "label": "दूसरा | playlist निर्यात या हस्तांतरण",
          "body": "आप टेक्स्ट playlist निकाल सकते हैं या W4DJ को दे सकते हैं। `output text playlist` या `export to w4dj` लिखें।"
        },
        {
          "label": "तीसरा | हार्मोनिक सेट क्रम",
          "body": "क्या मैं Camelot wheel का उपयोग करके सेट को क्रमबद्ध करूँ?"
        }
      ],
      "digging_notes": "Digging नोट्स",
      "mix_suggestion": "Mix सुझाव",
      "unknown": "अज्ञात",
      "verified": "सत्यापित",
      "target_platform_missing": "लक्षित प्लेटफ़ॉर्म उपलब्ध नहीं"
    },
    "rich": {
      "title": "# Rich मोड",
      "first_batch_title": "# Rich मोड",
      "final_title": "# Rich मोड",
      "columns": [
        "ट्रैक",
        "कलाकार",
        "एल्बम / EP",
        "शैली",
        "BPM",
        "की",
        "अवधि",
        "ऊर्जा",
        "रिलीज़ तारीख",
        "नोट्स",
        "चयन कारण",
        "लिंक"
      ],
      "next_steps": [
        {
          "label": "पहला | चयन प्रतिक्रिया साझा करें",
          "body": "यदि चाहें तो प्राकृतिक भाषा में बताएँ कि चयन कैसा रहा। इससे आपकी निजी पसंद और आगे के सुझाव बेहतर होंगे।"
        },
        {
          "label": "दूसरा | playlist निर्यात या हस्तांतरण",
          "body": "आप टेक्स्ट playlist निकाल सकते हैं या W4DJ को दे सकते हैं। `output text playlist` या `export to w4dj` लिखें।"
        },
        {
          "label": "तीसरा | हार्मोनिक सेट क्रम",
          "body": "क्या मैं Camelot wheel का उपयोग करके सेट को क्रमबद्ध करूँ?"
        }
      ],
      "digging_notes": "Digging नोट्स",
      "mix_suggestion": "Mix सुझाव",
      "unknown": "अज्ञात",
      "verified": "सत्यापित",
      "target_platform_missing": "लक्षित प्लेटफ़ॉर्म उपलब्ध नहीं",
      "view_titles": [
        "शैली दृष्टिकोण",
        "परिस्थिति दृष्टिकोण",
        "परिचितता / खोज दृष्टिकोण",
        "गतिशील संयुक्त दृष्टिकोण"
      ]
    }
  },
  "actions": {
    "share_feedback": {
      "label": "चयन प्रतिक्रिया",
      "positive": [
        "मुझे यह ट्रैक पसंद है"
      ],
      "negative": [
        "मुझे यह ट्रैक पसंद नहीं है"
      ],
      "ambiguous": [
        "मैं इस ट्रैक को लेकर निश्चित नहीं हूँ"
      ]
    },
    "export_w4dj": {
      "label": "W4DJ में निर्यात",
      "positive": [
        "W4DJ में निर्यात करें"
      ],
      "negative": [
        "W4DJ में निर्यात न करें"
      ],
      "ambiguous": [
        "शायद W4DJ में निर्यात करें"
      ]
    },
    "output_text_playlist": {
      "label": "टेक्स्ट playlist निकालें",
      "positive": [
        "टेक्स्ट playlist निकालें"
      ],
      "negative": [
        "टेक्स्ट playlist न निकालें"
      ],
      "ambiguous": [
        "शायद टेक्स्ट playlist निकालें"
      ]
    },
    "harmonic_reorder": {
      "label": "हार्मोनिक पुनर्क्रम",
      "positive": [
        "Camelot wheel के अनुसार क्रम दें"
      ],
      "negative": [
        "पुनर्क्रम न करें"
      ],
      "ambiguous": [
        "शायद Camelot wheel के अनुसार क्रम दें"
      ]
    },
    "confirm_long_term_memory": {
      "label": "दीर्घकालिक स्मृति की पुष्टि",
      "positive": [
        "इस पसंद को याद रखें"
      ],
      "negative": [
        "इस पसंद को सहेजें नहीं"
      ],
      "ambiguous": [
        "शायद इस पसंद को याद रखें"
      ]
    }
  },
  "platform_policy": {
    "aliases": {
      "spotify": "Spotify",
      "apple_music": "Apple Music",
      "soundcloud": "SoundCloud",
      "netease_cloud_music": "NetEase Cloud Music",
      "bandcamp": "Bandcamp",
      "beatport": "Beatport",
      "beatsource": "Beatsource"
    },
    "exclusive_markers": [
      "केवल",
      "सिर्फ",
      "केवल उपयोग"
    ],
    "preferred_markers": [
      "प्राथमिकता",
      "पसंद",
      "अग्रता"
    ],
    "fallback_markers": [
      "वैकल्पिक",
      "बैकअप",
      "उपलब्ध न हो तो"
    ],
    "forbidden_markers": [
      "उपयोग न करें",
      "बहिष्कृत",
      "नहीं"
    ]
  },
  "status": {
    "unknown": "अज्ञात",
    "verified": "सत्यापित",
    "target_platform_missing": "लक्षित प्लेटफ़ॉर्म उपलब्ध नहीं"
  },
  "export": {
    "text": "वर्तमान क्रम में कॉपी करने योग्य टेक्स्ट playlist निकालें।",
    "w4dj": "W4DJ के लिए UTF-8 `.w4dj` हस्तांतरण फ़ाइल बनाएँ।",
    "harmonic": "ज्ञात keys के साथ Camelot wheel क्रम का अनुरोध करें।",
    "feedback": "प्राकृतिक भाषा प्रतिक्रिया केवल वर्तमान सत्र अपडेट करती है; दीर्घकालिक संग्रह के लिए पुष्टि चाहिए।",
    "memory_confirmation": "मैंने इसे पसंद में बदलाव के संक्षिप्त सार के रूप में समझा। क्या इसे निजी दीर्घकालिक प्रोफ़ाइल में सहेजें?"
  },
  "trigger_capsule": [
    "DJ सेट",
    "प्लेलिस्ट",
    "संगीत खोजना",
    "ट्रैक ढूँढना",
    "सेट बनाना",
    "तेज़ मोड",
    "संयुक्त मोड",
    "पूर्ण मोड",
    "DJ सेट बनाना",
    "DJ",
    "house",
    "techno",
    "drum & bass",
    "jungle"
  ],
  "trigger_contract": {
    "path": "references/trigger-signals.json",
    "version": 1
  },
  "trigger_signal_families": [
    "mode",
    "dj_action",
    "dj_object",
    "dj_context",
    "reference",
    "set_detail",
    "genre_context",
    "generic_music_term",
    "negative_context",
    "explanatory_context",
    "genre_families"
  ]
}
```
