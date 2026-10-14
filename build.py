# -*- coding: utf-8 -*-
"""Marina Park static site generator.
Run: python3 build.py  -> writes *.html, robots.txt, sitemap.xml, llms.txt into this folder.
2026-10-14: photo refresh, phone 02-537-2440, Instagram x3, SEO (per-page meta, alt, canonical, OG,
robots/sitemap) and GEO (JSON-LD EventVenue/LocalBusiness/FAQPage, facts blocks, llms.txt).
"""
import os, html, json, re, datetime

OUT = os.path.dirname(os.path.abspath(__file__))

def wix(media_id, w=1600, h=1067):
    """old Wix-era image ids -> local images/ file"""
    return "images/" + re.sub(r"_d_\d+_\d+_s_\d(_\d)?", "", media_id.replace("~mv2", ""))

def img(name):
    """new 2026 photos (images/mp-*.jpg) or any plain filename in images/"""
    return name if name.startswith("images/") else "images/" + name

# ---------- shared data ----------
SITE = "Marina Park"
SITE_KO = "마리나파크"
BASE_URL = "https://marinapark.co.kr"
ADDRESS = "서울 서초구 반포동 115-1"
ADDRESS_FULL = "서울특별시 서초구 반포동 115-1 (서래나루, 반포한강공원)"
TEL = "02-537-2440"
TEL_RAW = "025372440"
TEL_INTL = "+82-2-537-2440"
FAX = "02-537-2499"
EMAIL = "ficonvention@gmail.com"
GEO_LAT, GEO_LNG = 37.5093, 126.9960
CAFE_HOURS = "매일 10:00 – 22:00"
INSTAGRAM = {
    "cafe":    ("https://www.instagram.com/marinapark_banpo", "마리나파크 카페", "Cafe"),
    "event":   ("https://www.instagram.com/marinaparkevent", "마리나파크 이벤트", "Event"),
    "wedding": ("https://www.instagram.com/marinaparkwedding", "마리나파크 웨딩", "Wedding"),
}
FACEBOOK = "https://www.facebook.com/Floatingisland1"
TODAY = datetime.date.today().isoformat()

NAV = [
    ("index.html", "Home", [("about.html", "About us")]),
    ("business-party.html", "Business Party", []),
    ("launching-party.html", "Launching Party", []),
    ("first-party.html", "1st Party", []),
    ("wedding.html", "Wedding", [("garden-wedding.html", "Garden Wedding")]),
    ("cafe.html", "Marina Cafe", [("cafe.html#menu", "Cafe Menu")]),
    ("contact.html", "Contact", []),
]

# ---------- alt text for every image ----------
ALT = {
    # 2026 photos
    "mp-b09.jpg": "마리나파크 야경 — 한강 위 조명이 켜진 건물 외관",
    "mp-b10.jpg": "마리나파크 3층 루프탑 가든 선셋 리셉션, 한강 노을",
    "mp-b17.jpg": "마리나파크 2층 컨벤션홀 — 한강 통창의 빈 연회장",
    "mp-b18.jpg": "마리나파크 2층 홀 라운드 테이블 세팅과 샹들리에",
    "mp-b21.jpg": "마리나파크 가든 칵테일 테이블 세팅, 한강 노을",
    "mp-b24.jpg": "마리나파크 야간 외관, 한강에 비친 조명",
    "mp-b25.jpg": "마리나파크 루프탑 가든 선셋 네트워킹 파티",
    "mp-b26.jpg": "마리나파크 2층 홀 레드카펫 기업 행사 리셉션",
    "mp-b27.jpg": "마리나파크 야경 — 반포 한강변 서래나루 전경",
    "mp-b28.jpg": "마리나파크 2층 컨벤션 무대와 LED 스크린 런칭 행사",
    "mp-b29.jpg": "마리나파크 외관 노을 — 한강 요트 선착장 앞",
    "mp-b30.jpg": "마리나파크 루프탑 송년 파티 불꽃놀이",
    "mp-b31.jpg": "마리나파크 가든 야간 파티 — 조명과 한강 야경",
    "mp-b32.jpg": "마리나파크 가든 야간 행사, 한강 다리 야경",
    "mp-c01.jpg": "마리나파크 3층 가든 웨딩 세팅 — 한강과 화이트 가제보",
    "mp-c02.jpg": "마리나파크 가든 예식 플라워 아치와 하객석",
    "mp-c03.jpg": "마리나파크 2층 홀 웨딩 — 그린 플라워 버진로드",
    "mp-c04.jpg": "마리나파크 홀 웨딩 라운드 테이블과 플라워 데코",
    "mp-c05.jpg": "마리나파크 홀 웨딩 테이블 세팅, 한강 통창",
    "mp-c06.jpg": "마리나파크 루프탑 가든 소규모 예식 세팅",
    "mp-c07.jpg": "마리나파크 홀 예식 — 플라워 가든 버진로드",
    "mp-c08.jpg": "마리나파크 홀 웨딩 연회 테이블",
    "mp-c09.jpg": "마리나파크 홀 예식 단상 플라워 데코, 한강 뷰",
    "mp-c10.jpg": "마리나파크 2층 홀 웨딩 — 나무 아치 버진로드",
    "mp-c14.jpg": "마리나파크 신부대기실 — 한강이 보이는 라운지",
    "mp-c15.jpg": "마리나파크 가든 버진로드와 플라워 가제보",
    "mp-c21.jpg": "마리나파크 가든 선셋 예식 — 가제보 아래 신랑신부",
    "mp-c22.jpg": "마리나파크 3층 가든 잔디와 한강 전경",
    "mp-c33.jpg": "마리나파크 가든 예식 하객석 세팅, 한강 뷰",
    "mp-c34.jpg": "마리나파크 가든 웨딩 플라워 세팅",
    "mp-c35.jpg": "마리나파크 가든 예식 버진로드 플라워",
    "mp-c36.jpg": "마리나파크 가든 웨딩 — 서울 스카이라인 배경",
    "mp-c49.jpg": "마리나파크 가든 야간 예식 세팅과 조명",
    "mp-c50.jpg": "마리나파크 가든 야간 플라워 조명",
    "mp-c52.jpg": "마리나파크 2층 홀 웨딩 세팅 — 화이트 플라워 버진로드",
    "mp-c53.jpg": "마리나파크 돌잔치·가족연회 라운드 테이블 세팅",
    "mp-c54.jpg": "마리나파크 홀 버진로드 플라워 세팅",
    "mp-c55.jpg": "마리나파크 홀 소규모 예식 세팅",
    "mp-c56.jpg": "마리나파크 홀 예식 단상과 샹들리에",
    "mp-c58.jpg": "마리나파크 가든 텐트 아래 가족 연회 테이블",
    "mp-c59.jpg": "마리나파크 웨딩 데이 입구 플라워 세팅",
    "mp-c60.jpg": "마리나파크 홀에서 보는 한강 노을",
    "mp-e05.jpg": "마리나파크 갈라 디너 테이블 세팅 — 화이트 린넨과 센터피스",
    "mp-e06.jpg": "마리나파크 2층 홀 기업 갈라 디너 전경",
    # old wix images kept
    "2649b2_0eba81bbe25c4fb393a391de7f8e4517": "마리나파크 1층 마리나 카페 외관",
    "2649b2_256b3a1192ce4999b2c9cdaa52cba08f": "마리나파크 1층 카페와 레드 어닝",
    "2649b2_27aac57c162e474eb1debfcef01fee8c": "마리나파크 돌잔치 데코레이션 테이블",
    "2649b2_2550e0e1deda4df8a29c7eb8a3ae9d1e": "마리나파크 기업 행사 무대 조명",
    "2649b2_ffa6948050474d00a60c19183833a48e": "마리나파크에서 본 한강 야경과 분수",
    "2649b2_c8e0b565869f450eb0e3f2077065fe64": "마리나파크 기업 행사 배너",
    "2649b2_2e13c691e36f4f9f975aa6e7f7489290": "마리나파크 단체 행사 참가자 기념 촬영",
    "2649b2_1f4e534b009a455795154239a1f1f044": "마리나파크 컨퍼런스 무대 연출",
    "2649b2_c61315fdb1d8465daf24e08a05ebad93": "마리나파크 기업 행사 식사 세팅",
    "2649b2_349a109dd0544dc68648d9f7df86de79": "마리나파크 시상식 무대",
    "2649b2_f58fea24227f40d0ac2b928e00be2ac5": "마리나파크 런칭 행사 리셉션",
    "2649b2_72c455d453074068a52a1ee11fc9a2c1": "마리나파크 세미나 세팅",
    "2649b2_dad8a86f44a54addbec2938ead2ed497": "마리나파크 기업 행사 참석자",
    "2649b2_ab37a379303f483e8dbc62ae094457a0": "마리나파크 런칭 파티 무대",
    "2649b2_2aa49e3249b8467eb9ab97690b1a6849": "마리나파크 브랜드 런칭쇼 리셉션",
    "2649b2_f5a265e7d0a4424f84543524a97c1576": "마리나파크 런칭 파티 — 한강 통창 홀",
    "2649b2_1e7ed286fc8744979968ca852dc81221": "마리나파크 런칭 행사 포토월",
    "2649b2_c95dc8b4388643c6a46599f9b158c4b4": "마리나파크 런칭 파티 네트워킹",
    "2649b2_b90262263cde4c458a442c8e3c15e334": "마리나파크 런칭 행사 미디어 월",
    "2649b2_5357ded7cd6b472fa32e52d98ba38ea9": "마리나파크 런칭 파티 케이터링",
    "2649b2_4a9979fcb2a8482798bb6ca6b67a4d36": "마리나파크 프로모션 행사",
    "2649b2_375da41383a14dcf9352d6eadfc9d79a": "마리나파크 런칭쇼 참석자",
    "2649b2_0cacf8685e5f4c1b8e26dfeaf77fb801": "마리나파크 런칭 행사 무대 연출",
    "2649b2_8a79a494c04a452cabc6d16479ae6ed5": "마리나파크 런칭 파티 라운지",
    "2649b2_366cf79f6c2a44fdbcd60faf77bb2b05": "마리나파크 저녁 리셉션",
    "2649b2_862325761e3d4188a6ee89a5d94bbc60": "마리나파크 돌잔치 입구 배너",
    "2649b2_964b10c0a456478f915c818841fa41ef": "마리나파크 돌잔치 돌상 데코",
    "2649b2_878a67299d624f2f8126810caa5915e0": "마리나파크 돌잔치 홀 세팅",
    "2649b2_a8231255dc614b1b96e934212a2c7727": "마리나파크 돌잔치 테이블 네임카드",
    "2649b2_f8e846adf12640ecb1082724fdb0103d": "마리나파크 돌잔치 센터피스",
    "2649b2_ee6b0814763143daabed0fbd9d19a0e7": "마리나파크 돌잔치 식사 세팅",
    "2649b2_5e0ff44e223448338d9ef00b03bcf84c": "마리나파크 돌잔치 포토테이블",
    "2649b2_300b85e2fe7148889ac0ea5a72225ca9": "마리나파크 돌잔치 홀 전경",
    "2649b2_d915a9a8d8fb4330880447692450ba8f": "마리나파크 돌잔치 케이크 테이블",
    "2649b2_58b4fb5d2edc4079bc5a78fc5c1695ac": "마리나파크 돌잔치 데코",
    "2649b2_26654215ffe04ac08d029f33207d8b1a": "마리나파크 돌잔치 답례품 테이블",
    "2649b2_c537efda88cc4316bb161b99c910f3e1": "마리나파크 가족 연회 테이블",
    "2649b2_b0a27021a5e2480bb624dd050178f88a": "마리나파크 돌잔치 식전 세팅",
    "2649b2_9a69d241636f420f9f74f8c549c596ec": "마리나파크 돌잔치 홀 조명",
    "2649b2_d10aace456fc4cf5a6cc299301d883d9": "마리나파크 돌잔치 메인 테이블",
    "2649b2_d68896f967204194a87c7acbefe756ec": "마리나파크 웨딩 — 플라워 아치의 신부",
    "8bb438_ec9a72099f9648dfb08d9412804a464a": "마리나파크 웨딩 플라워 데코",
    "2649b2_5ce8952e336d431c8a9f170eb5929234": "마리나파크 가든 웨딩 한강 전경",
    "2649b2_c143d015d0454bed82088c76f228a8dc": "마리나파크 가든 웨딩 연회 테이블",
    "2649b2_b13801a7f8d04061a365a1e6a05f88e9": "마리나파크 가든 웨딩 하객석",
    "2649b2_f1c4946dee4f4dbcb7d5237ec2b0e743": "마리나파크 가든 웨딩 가제보와 버진로드",
    "2649b2_334aea7b16464fd78967881c4fb4bbf3": "마리나파크 가든 웨딩 파노라마",
    "2649b2_a170c69162b34c87af8cb43680b1d836f003": "마리나파크 가든 웨딩 전경",
    "2649b2_0bc81bf517e94690b2ee2cb2f02e0258": "마리나파크 가든 웨딩 플라워",
    "2649b2_e9885f9c949647e394df146dfae49c3d": "마리나파크 가든 예식 세팅",
    "2649b2_322b463071914e24b0db2a7303ba4ec4": "마리나파크 가든 웨딩 리셉션",
    "c19c76_5134149a64f04927a9597998ef802ceb": "마리나파크 한강 전경",
}
def alt_of(path):
    base = os.path.basename(path)
    if base in ALT: return ALT[base]
    key = re.sub(r"\.(jpe?g|png)$", "", base)
    return ALT.get(key, "마리나파크 — 반포 한강 연회장")

# ---------- JSON-LD ----------
SAME_AS = [v[0] for v in INSTAGRAM.values()] + [FACEBOOK]
VENUE_LD = {
    "@context": "https://schema.org",
    "@type": ["EventVenue", "LocalBusiness"],
    "@id": BASE_URL + "/#venue",
    "name": "마리나파크 (Marina Park)",
    "alternateName": ["Marina Park Seoul", "마리나파크 반포", "마리나파크 세빛섬"],
    "description": "서울 반포 한강 서래나루에 있는 연회·웨딩·MICE 베뉴. 1층 마리나 카페, 2층 컨벤션홀(100~300명), 3층 루프탑 가든. 송년회·기업연회·소규모 예식·가든웨딩·돌잔치 전문.",
    "url": BASE_URL + "/",
    "telephone": TEL_INTL,
    "faxNumber": "+82-2-537-2499",
    "email": EMAIL,
    "image": [BASE_URL + "/images/og-marinapark.jpg", BASE_URL + "/images/mp-b27.jpg", BASE_URL + "/images/mp-c01.jpg"],
    "logo": BASE_URL + "/favicon.svg",
    "priceRange": "₩₩₩",
    "currenciesAccepted": "KRW",
    "address": {"@type": "PostalAddress", "streetAddress": "반포동 115-1 (서래나루)", "addressLocality": "서초구", "addressRegion": "서울특별시", "postalCode": "06501", "addressCountry": "KR"},
    "geo": {"@type": "GeoCoordinates", "latitude": GEO_LAT, "longitude": GEO_LNG},
    "hasMap": "https://www.google.com/maps?q=%EC%84%9C%EC%9A%B8+%EC%84%9C%EC%B4%88%EA%B5%AC+%EB%B0%98%ED%8F%AC%EB%8F%99+115-1",
    "areaServed": ["서울", "서초구", "반포", "강남", "Seoul"],
    "maximumAttendeeCapacity": 300,
    "amenityFeature": [
        {"@type": "LocationFeatureSpecification", "name": "한강 전망 (Han River view)", "value": True},
        {"@type": "LocationFeatureSpecification", "name": "3층 루프탑 가든 (야외 예식·리셉션)", "value": True},
        {"@type": "LocationFeatureSpecification", "name": "무대·음향·LED 영상 장비", "value": True},
        {"@type": "LocationFeatureSpecification", "name": "신부대기실", "value": True},
        {"@type": "LocationFeatureSpecification", "name": "주차 (한강공원 주차장 약 200대, 참석자 3시간 무료)", "value": True},
        {"@type": "LocationFeatureSpecification", "name": "우천 시 실내 전환", "value": True},
    ],
    "containsPlace": [
        {"@type": "Restaurant", "name": "마리나 카페 (Marina Cafe, 1F)", "servesCuisine": ["Coffee", "Italian", "Dessert"], "openingHours": "Mo-Su 10:00-22:00"},
        {"@type": "EventVenue", "name": "2층 컨벤션홀 (2F Convention)", "maximumAttendeeCapacity": 300, "description": "100~300명 규모 기업연회·송년회·웨딩·돌잔치. 무대·LED·음향 완비, 사면 한강 통창."},
        {"@type": "EventVenue", "name": "3층 루프탑 가든 (3F Garden)", "description": "화이트 대리석 가제보와 잔디 가든. 가든 예식, 칵테일 리셉션, 선셋 파티."},
    ],
    "makesOffer": [
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "송년회·연말 모임·기업연회 (50~300명, 100~200명 최다)", "serviceType": "Year-end party / corporate banquet"}, "availability": "https://schema.org/InStock"},
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "소규모 예식·스몰웨딩·가든웨딩 (50~300명)", "serviceType": "Small wedding / garden wedding"}, "availability": "https://schema.org/InStock"},
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "돌잔치·가족 연회 (50명 룸~200명)", "serviceType": "First birthday party"}, "availability": "https://schema.org/InStock", "priceSpecification": {"@type": "PriceSpecification", "name": "돌상·포토테이블 세팅 패키지", "price": 1500000, "priceCurrency": "KRW"}},
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "런칭쇼·MICE·컨퍼런스", "serviceType": "Launching party / MICE"}, "availability": "https://schema.org/InStock"},
    ],
    "sameAs": SAME_AS,
    "parentOrganization": {"@type": "Organization", "name": "세빛섬 플로팅아일랜드 컨벤션 (Floating Island Convention)", "email": EMAIL},
}
WEBSITE_LD = {"@context": "https://schema.org", "@type": "WebSite", "@id": BASE_URL + "/#website", "url": BASE_URL + "/", "name": "마리나파크 Marina Park", "inLanguage": "ko", "publisher": {"@id": BASE_URL + "/#venue"}}

def ld(obj): return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + '</script>'

def breadcrumb(fname, title):
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": BASE_URL + "/"}]
    if fname != "index.html":
        items.append({"@type": "ListItem", "position": 2, "name": title, "item": BASE_URL + "/" + fname})
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}

# ---------- per-page SEO ----------
META = {
    "index.html": dict(
        title="마리나파크 | 반포 한강 연회장 — 송년회·소규모 예식·돌잔치·기업행사",
        desc="서울 반포 한강 서래나루 마리나파크. 2층 컨벤션홀 100~300명, 3층 루프탑 가든, 1층 카페. 송년회·연말 모임, 소규모 예식·가든웨딩, 돌잔치, 기업연회·런칭쇼. 문의 02-537-2440",
        og="og-marinapark.jpg", kw="마리나파크, 반포 연회장, 한강 연회장, 송년회 장소, 소규모 예식, 가든웨딩, 돌잔치 장소, 기업연회, 서초 MICE"),
    "about.html": dict(
        title="공간 안내 — 1층 카페 · 2층 컨벤션홀(100~300명) · 3층 가든 | 마리나파크",
        desc="마리나파크 공간 소개. 1층 마리나 카페(10:00~22:00), 2층 사면 한강 통창 컨벤션홀 100~300명, 3층 화이트 가제보 루프탑 가든. 서울 서초구 반포동 115-1 서래나루.",
        og="og-marinapark-night.jpg", kw="마리나파크 공간, 반포 컨벤션홀, 한강 루프탑 가든, 서래나루"),
    "business-party.html": dict(
        title="반포 송년회 장소 · 기업연회 · MICE 행사장 100~300명 | 마리나파크",
        desc="송년회·연말 모임·기업 갈라디너·컨퍼런스를 한강이 보이는 마리나파크에서. 50명 모임부터 300명 전사 송년회(2층 컨벤션홀 100~300명)까지. 무대·LED·음향 완비, 루프탑 리셉션, 코스·뷔페·프리드링크. 서초 반포.",
        og="og-marinapark-night.jpg", kw="송년회 장소, 반포 송년회, 강남 송년회 장소, 한강 기업연회, 갈라디너, 서초 컨퍼런스 장소, 연말 모임 장소"),
    "launching-party.html": dict(
        title="런칭쇼 · 브랜드 프로모션 · 미디어 행사장 한강뷰 | 마리나파크",
        desc="신제품 런칭쇼, 브랜드 프로모션, 미디어 데이를 한강 전망의 마리나파크에서. 2층 컨벤션 무대·LED 스크린·음향, 3층 루프탑 애프터파티, 야간 외관 조명 연출.",
        og="og-marinapark-night.jpg", kw="런칭쇼 장소, 브랜드 런칭 파티, 미디어 행사장, 한강 이벤트홀"),
    "first-party.html": dict(
        title="반포 돌잔치 장소 · 한강뷰 가족 연회 50~200명 | 마리나파크",
        desc="서초·반포 돌잔치는 한강이 보이는 마리나파크에서. 50명 룸 가족 돌잔치부터 100~200명 돌잔치까지, 돌상·포토테이블 패키지·현수막·코스 식사·사회자. 5세 이하 식사 무료, 주차 3시간 무료. 문의 02-537-2440",
        og="og-marinapark.jpg", kw="돌잔치 장소, 반포 돌잔치, 서초 돌잔치, 강남 돌잔치 장소, 한강뷰 돌잔치, 가족 연회"),
    "wedding.html": dict(
        title="한강 소규모 예식 · 스몰웨딩 · 컨벤션 웨딩 | 마리나파크 반포",
        desc="최소 50명 가족 예식부터 100~300명 컨벤션 웨딩까지. 한강 통창 2층 홀 예식과 3층 가든 예식, 주말 12시·18시 두 타임 하루 두 커플. 코스 1인 10만원부터, 우천 시 실내 전환, 주차 200대.",
        og="og-marinapark.jpg", kw="소규모 예식, 스몰웨딩 서울, 한강 웨딩홀, 반포 웨딩, 가족 예식 장소, 주례 없는 결혼식"),
    "garden-wedding.html": dict(
        title="한강 가든웨딩 · 야외 결혼식 — 화이트 가제보 루프탑 | 마리나파크",
        desc="반포 한강과 서리풀 공원을 배경으로 한 마리나파크 3층 가든웨딩. 화이트 대리석 가제보, 잔디 버진로드, 선셋 예식. 3월 말~6월·9~11월 가능, 우천 시 2층 홀 전환, 최소 50명.",
        og="og-marinapark.jpg", kw="가든웨딩, 한강 야외결혼식, 서울 가든 웨딩홀, 루프탑 웨딩, 야외 예식장 서울"),
    "cafe.html": dict(
        title="마리나 카페 — 한강뷰 카페 · 피자 파스타 와인 · 10:00~22:00 | 마리나파크 1층",
        desc="반포 한강공원 서래나루 마리나파크 1층 카페. 커피·티·디저트·피자·파스타·와인. 매일 10:00~22:00. 카페 가든 소규모 파티·모임 예약 가능.",
        og="og-marinapark.jpg", kw="반포 한강 카페, 서래나루 카페, 한강뷰 카페, 반포한강공원 카페"),
    "contact.html": dict(
        title="문의 · 오시는 길 — 02-537-2440 | 마리나파크 반포 서래나루",
        desc="마리나파크 행사 문의 02-537-2440, ficonvention@gmail.com. 서울 서초구 반포동 115-1 서래나루(반포한강공원). 송년회·예식·돌잔치·기업행사 견적 문의.",
        og="og-marinapark-night.jpg", kw="마리나파크 문의, 마리나파크 전화번호, 마리나파크 오시는 길"),
}

def nav_html(current):
    items = []
    for href, label, subs in NAV:
        active = " active" if href == current or any(s[0].split('#')[0] == current for s in subs) else ""
        if subs:
            sub = "".join(f'<li><a href="{s[0]}">{s[1]}</a></li>' for s in subs)
            items.append(f'<li class="has-sub{active}"><a href="{href}">{label}</a><ul class="sub">{sub}</ul></li>')
        else:
            items.append(f'<li class="{active.strip()}"><a href="{href}">{label}</a></li>')
    return "\n".join(items)

def insta_links(cls="f-social"):
    out = []
    for key, (url, ko, en) in INSTAGRAM.items():
        out.append(f'<a href="{url}" target="_blank" rel="noopener" aria-label="인스타그램 {ko}" title="{ko} @{url.rsplit("/",1)[1]}">'
                   f'<svg viewBox="0 0 24 24"><path d="M12 2.2c3.2 0 3.6 0 4.9.1 3.3.1 4.8 1.7 4.9 4.9.1 1.3.1 1.6.1 4.8s0 3.6-.1 4.8c-.1 3.2-1.7 4.8-4.9 4.9-1.3.1-1.6.1-4.9.1s-3.6 0-4.8-.1c-3.3-.1-4.8-1.7-4.9-4.9C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.8C2.4 3.9 4 2.4 7.2 2.3c1.2-.1 1.6-.1 4.8-.1zM12 0C8.7 0 8.3 0 7.1.1 2.7.3.3 2.7.1 7.1 0 8.3 0 8.7 0 12s0 3.7.1 4.9c.2 4.4 2.6 6.8 7 7 1.2.1 1.6.1 4.9.1s3.7 0 4.9-.1c4.4-.2 6.8-2.6 7-7 .1-1.2.1-1.6.1-4.9s0-3.7-.1-4.9c-.2-4.4-2.6-6.8-7-7C15.7 0 15.3 0 12 0zm0 5.8a6.2 6.2 0 1 0 0 12.4 6.2 6.2 0 0 0 0-12.4zM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm6.4-11.8a1.4 1.4 0 1 0 0 2.9 1.4 1.4 0 0 0 0-2.9z"/></svg>'
                   f'<span class="s-label">{en}</span></a>')
    out.append(f'<a href="{FACEBOOK}" target="_blank" rel="noopener" aria-label="Facebook" title="Facebook"><svg viewBox="0 0 24 24"><path d="M24 12a12 12 0 1 0-13.9 11.9v-8.4H7.1V12h3V9.4c0-3 1.8-4.7 4.5-4.7 1.3 0 2.7.2 2.7.2v3h-1.5c-1.5 0-2 .9-2 1.9V12h3.3l-.5 3.5h-2.8v8.4A12 12 0 0 0 24 12z"/></svg><span class="s-label">Facebook</span></a>')
    return f'<div class="{cls}">' + "".join(out) + '</div>'

def page(current, title, body, extra_ld=None):
    m = META[current]
    url = BASE_URL + "/" + ("" if current == "index.html" else current)
    og_img = BASE_URL + "/images/" + m["og"]
    lds = [ld(VENUE_LD), ld(WEBSITE_LD), ld(breadcrumb(current, title))] + [ld(x) for x in (extra_ld or [])]
    hero_cls = " has-hero"
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(m["title"])}</title>
<meta name="description" content="{html.escape(m["desc"])}">
<meta name="keywords" content="{html.escape(m["kw"])}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<link rel="canonical" href="{url}">
<meta name="author" content="Marina Park · Floating Island Convention">
<meta name="geo.region" content="KR-11">
<meta name="geo.placename" content="서울 서초구 반포동 서래나루">
<meta name="geo.position" content="{GEO_LAT};{GEO_LNG}">
<meta property="og:site_name" content="마리나파크 Marina Park">
<meta property="og:locale" content="ko_KR">
<meta property="og:locale:alternate" content="en_US">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{html.escape(m["title"])}">
<meta property="og:description" content="{html.escape(m["desc"])}">
<meta property="og:image" content="{og_img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{html.escape(alt_of(m["og"]) if m["og"] in ALT else "마리나파크 — 반포 한강 연회장")}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(m["title"])}">
<meta name="twitter:description" content="{html.escape(m["desc"])}">
<meta name="twitter:image" content="{og_img}">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=Josefin+Sans:wght@300;400&family=Noto+Sans+KR:wght@300;400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css?v=3">
{chr(10).join(lds)}
</head>
<body class="page-{current.replace('.html','')}{hero_cls}">
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="마리나파크 홈"><span class="brand-main">MARINA PARK</span><span class="brand-sub">마리나파크</span></a>
    <button class="nav-toggle" aria-label="메뉴 열기" aria-expanded="false"><span></span><span></span><span></span></button>
    <nav class="site-nav" aria-label="주 메뉴"><ul>
{nav_html(current)}
    </ul></nav>
  </div>
</header>
<main>
{body}
</main>
<footer class="site-footer">
  <div class="wrap footer-grid">
    <div class="f-col">
      <div class="f-brand">MARINA PARK <span class="f-brand-ko">마리나파크</span></div>
      <p>{ADDRESS_FULL}</p>
      <p>Tel: <a href="tel:{TEL_RAW}">{TEL}</a> &nbsp;|&nbsp; Fax: {FAX}</p>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <p class="f-hours">마리나 카페 {CAFE_HOURS} · 행사 문의 평일 10:00 – 18:00</p>
    </div>
    <div class="f-col f-links">
      <a href="about.html">About us</a>
      <a href="business-party.html">Business Party · 송년회</a>
      <a href="launching-party.html">Launching Party</a>
      <a href="first-party.html">1st Party · 돌잔치</a>
      <a href="wedding.html">Wedding · 소규모 예식</a>
      <a href="garden-wedding.html">Garden Wedding</a>
      <a href="cafe.html">Marina Cafe</a>
      <a href="contact.html">Contact</a>
    </div>
    <div class="f-col">
      <p class="f-social-title">Instagram</p>
      {insta_links()}
    </div>
  </div>
  <div class="wrap copyright">© 2026 Marina Park · Floating Island Convention. All rights reserved. &nbsp;·&nbsp; <a href="llms.txt">AI summary</a></div>
</footer>
<div class="lightbox" id="lightbox" hidden><button class="lb-close" aria-label="닫기">&times;</button><button class="lb-prev" aria-label="이전">&#8249;</button><img alt=""><button class="lb-next" aria-label="다음">&#8250;</button></div>
<script src="js/main.js"></script>
</body>
</html>
"""

def gallery(items, cls="gallery"):
    """items: (image, w, h) -> image is 'mp-xxx.jpg' (new) or wix id (old). Each opens lightbox."""
    out = [f'<div class="{cls}">']
    for mid, w, h in items:
        src = img(mid) if mid.startswith("mp-") else wix(mid)
        orient = "landscape" if w >= h else "portrait"
        out.append(f'<a class="g-item {orient}" href="{src}" data-lightbox><img src="{src}" loading="lazy" alt="{html.escape(alt_of(src))}"></a>')
    out.append('</div>')
    return "\n".join(out)

def hero(image, eyebrow, h1, lead=None, tall=False):
    src = img(image) if image.startswith("mp-") else wix(image)
    lead_html = f'<p class="lead">{lead}</p>' if lead else ""
    return f"""<section class="page-hero{' tall' if tall else ''}" style="background-image:url('{src}')" role="img" aria-label="{html.escape(alt_of(src))}">
  <div class="wrap"><p class="eyebrow">{eyebrow}</p><h1>{h1}</h1>{lead_html}</div>
</section>"""

def facts(eyebrow, heading, lead, rows, en=None):
    """GEO: fact block with definition list (machine-readable key facts)."""
    dl = "".join(f'<div class="fact"><dt>{k}</dt><dd>{v}</dd></div>' for k, v in rows)
    en_html = f'<p class="facts-en" lang="en">{en}</p>' if en else ""
    return f"""<section class="section facts">
  <div class="wrap">
    <p class="eyebrow">{eyebrow}</p>
    <h2>{heading}</h2>
    <p class="facts-lead">{lead}</p>
    <dl class="facts-grid">{dl}</dl>
    {en_html}
  </div>
</section>"""

def faq(heading, qa, intro=None):
    """GEO: visible FAQ (<details>) + FAQPage JSON-LD. Returns (html, ld_obj)."""
    items = "".join(f'<details class="faq-item"><summary>{q}</summary><div class="faq-a"><p>{a}</p></div></details>' for q, a in qa)
    intro_html = f'<p class="sub">{intro}</p>' if intro else ""
    h = f"""<section class="section faq-section">
  <div class="wrap narrow">
    <p class="eyebrow center">FAQ</p>
    <h2 class="center">{heading}</h2>
    {intro_html}
    <div class="faq">{items}</div>
  </div>
</section>"""
    obj = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": re.sub("<[^>]+>", "", q), "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}} for q, a in qa]}
    return h, obj

def service_ld(name, stype, desc, url, audience=None, cap=None):
    o = {"@context": "https://schema.org", "@type": "Service", "name": name, "serviceType": stype, "description": desc, "url": url,
         "provider": {"@id": BASE_URL + "/#venue"}, "areaServed": ["서울", "서초구", "반포", "강남"],
         "availableChannel": {"@type": "ServiceChannel", "servicePhone": {"@type": "ContactPoint", "telephone": TEL_INTL, "contactType": "reservations", "availableLanguage": ["Korean", "English"]}}}
    if audience: o["audience"] = {"@type": "Audience", "audienceType": audience}
    return o

CTA_TEL = f'<a class="btn" href="tel:{TEL_RAW}">전화 문의 {TEL}</a> <a class="btn btn-outline-dark" href="contact.html">온라인 문의</a>'

# ======================================================================
# HOME
# ======================================================================
home = f"""
<section class="hero" style="background-image:url('{img('mp-b27.jpg')}')" role="img" aria-label="{alt_of('mp-b27.jpg')}">
  <div class="hero-inner">
    <h1 class="hero-title">Marina Park</h1>
    <p class="hero-sub">Creating Unforgettable<br>Memories</p>
    <p class="lead">반포 한강 서래나루 — 송년회 · 소규모 예식 · 돌잔치 · 기업 행사</p>
    <div class="hero-cta">
      <a class="btn btn-light" href="wedding.html">Discover Wedding</a>
      <a class="btn btn-outline" href="business-party.html">Discover Party</a>
    </div>
  </div>
</section>

<section class="section services">
  <div class="wrap">
    <p class="eyebrow center">Services</p>
    <h2 class="center">Design your Wedding and Party</h2>
    <div class="service-grid">
      <a class="service" href="business-party.html">
        <img src="{img('mp-e06.jpg')}" loading="lazy" alt="{alt_of('mp-e06.jpg')}">
        <h3>송년회 · 기업연회</h3><p>연말 모임 · 갈라디너 · 100~300명</p>
      </a>
      <a class="service" href="business-party.html">
        <img src="{img('mp-b28.jpg')}" loading="lazy" alt="{alt_of('mp-b28.jpg')}">
        <h3>MICE Events</h3><p>컨퍼런스 · 세미나 · 단체행사</p>
      </a>
      <a class="service" href="first-party.html">
        <img src="{img('mp-c53.jpg')}" loading="lazy" alt="{alt_of('mp-c53.jpg')}">
        <h3>돌잔치 · 가족연회</h3><p>50명 룸 가족 돌잔치부터 200명까지</p>
      </a>
      <a class="service" href="wedding.html">
        <img src="{img('mp-c01.jpg')}" loading="lazy" alt="{alt_of('mp-c01.jpg')}">
        <h3>소규모 예식 · 가든웨딩</h3><p>50명대 가족 예식 · 한강 가든</p>
      </a>
    </div>
  </div>
</section>

<section class="section intro-split">
  <div class="wrap split">
    <div class="split-img"><img src="{img('mp-b10.jpg')}" loading="lazy" alt="{alt_of('mp-b10.jpg')}"></div>
    <div class="split-text">
      <p class="eyebrow">Han River · Seoraenaru</p>
      <h2>한강과 서리풀 공원이<br>어우러진 공간</h2>
      <p>마리나파크는 서울 서초구 반포 서래나루(반포한강공원)에 위치한 복합 연회 공간입니다. 1층 마리나 카페, 2층 100~300명 규모의 컨벤션홀, 3층 화이트 가제보 루프탑 가든까지 — 한강의 정취를 그대로 담은 세 개의 공간에서 송년회·기업행사부터 소규모 예식, 돌잔치까지 모든 순간을 준비합니다.</p>
      <a class="btn" href="about.html">About Marina Park</a>
      <p class="contact-line"><a href="tel:{TEL_RAW}">Tel {TEL}</a></p>
    </div>
  </div>
</section>

{facts("At a glance", "마리나파크 핵심 정보",
  "AI 비서나 검색에서 바로 확인할 수 있도록 핵심 사실을 정리했습니다.",
  [("위치", "서울 서초구 반포동 115-1 서래나루 · 반포한강공원 내, 한강 바로 앞"),
   ("공간", "1층 마리나 카페 · 2층 컨벤션홀 · 3층 루프탑 가든 (화이트 가제보)"),
   ("수용 인원", "2층 홀 100~300명 (연회·예식), 3층 가든 리셉션·소규모 예식, 돌잔치 50명 룸~200명"),
   ("주요 용도", "송년회·연말 모임 · 기업연회·갈라디너 · 소규모 예식·가든웨딩 · 돌잔치 · 런칭쇼·MICE"),
   ("장비", "무대 · 음향 · LED 영상 · 조명 완비, 사면 한강 통창"),
   ("식사", "코스 · 뷔페 · 핑거푸드 · 프리드링크 패키지 (국제 행사용 할랄·채식 대응)"),
   ("우천 시", "야외 가든 행사는 2층 실내 홀로 전환 가능"),
   ("주차", "한강공원 주차장 약 200대, 행사 참석자 3시간 무료"),
   ("식사 기준가", "코스 1인 10만원부터 (상세 견적 문의)"),
   ("카페 영업", CAFE_HOURS),
   ("문의", f"{TEL} · {EMAIL} · 영어 상담 가능")],
  en="Marina Park is a riverside event venue at Seoraenaru, Banpo Han River Park, Seoul: a ground-floor cafe, a 2nd-floor convention hall for 100–300 guests, and a 3rd-floor rooftop garden with a white marble gazebo. Year-end parties, corporate galas, intimate weddings, garden weddings, first-birthday celebrations and product launches. English inquiries welcome: +82-2-537-2440.")}

<section class="section gallery-teaser">
  <div class="wrap">
    <p class="eyebrow center">Event Gallery</p>
    <h2 class="center">Unforgettable Memories</h2>
    {gallery([
        ("mp-b25.jpg", 3, 2), ("mp-c03.jpg", 3, 2), ("mp-b31.jpg", 3, 2),
        ("mp-c34.jpg", 3, 2), ("mp-b30.jpg", 3, 2), ("mp-c60.jpg", 3, 2),
    ], "gallery cols-3 even")}
    <p class="center"><a class="btn" href="business-party.html">Discover Party</a></p>
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>Contact us to turn your dream into a reality</h2>
    <p>행사 일정과 인원을 알려주시면 맞춤 제안을 드립니다. · {TEL}</p>
    <a class="btn btn-light" href="contact.html">Contact</a>
    <a class="btn btn-outline" href="mailto:{EMAIL}">E-mail</a>
  </div>
</section>
"""
home_faq, home_faq_ld = faq("자주 묻는 질문", [
    ("마리나파크는 어디에 있나요?", "서울 서초구 반포동 115-1, 반포한강공원 서래나루에 있습니다. 한강 바로 앞 건물로 지하철 9호선 신반포역·고속터미널역에서 가깝고, 한강공원 주차장을 이용할 수 있습니다."),
    ("어떤 행사를 할 수 있나요?", "송년회·연말 모임, 기업연회·갈라디너, 컨퍼런스·세미나, 신제품 런칭쇼, 소규모 예식·가든웨딩·컨벤션 웨딩, 돌잔치·가족 연회, 카페 가든 소모임까지 가능합니다."),
    ("수용 인원은 몇 명인가요?", "2층 컨벤션홀은 100명부터 최대 300명까지 식사 세팅이 가능합니다. 3층 루프탑 가든은 리셉션·소규모 예식용이며, 돌잔치는 50명 규모의 룸부터 200명까지 진행합니다."),
    ("견적은 어떻게 받나요?", f"행사 종류·희망 날짜·예상 인원을 전화({TEL}) 또는 이메일({EMAIL})로 알려주시면 맞춤 견적을 보내드립니다. 영어 상담도 가능합니다."),
])
home = home.replace('<section class="section cta-band">', home_faq + '\n<section class="section cta-band">', 1)

# ======================================================================
# ABOUT
# ======================================================================
about = f"""
{hero("mp-b24.jpg", "Marina Park", "About us", "반포 한강 서래나루의 세 가지 공간")}

<section class="section">
  <div class="wrap floors">
    <article class="floor">
      <div class="floor-img"><img src="{wix('2649b2_0eba81bbe25c4fb393a391de7f8e4517~mv2.jpg')}" loading="lazy" alt="{alt_of('2649b2_0eba81bbe25c4fb393a391de7f8e4517')}"></div>
      <div class="floor-text">
        <p class="eyebrow">1F</p><h2>Marina Cafe</h2>
        <p>마리나파크 1층은 한강이 보이는 카페입니다. 이국적인 분위기에서 커피와 티, 디저트, 피자와 파스타, 와인을 즐길 수 있으며, 카페 가든에서는 생일 모임·동호회·소규모 파티를 열 수 있습니다. 영업시간 {CAFE_HOURS}.</p>
        <a class="btn" href="cafe.html">Cafe Menu</a> <a class="btn btn-outline-dark" href="https://marinapark.cafe" target="_blank" rel="noopener">카페 홈페이지</a>
      </div>
    </article>
    <article class="floor reverse">
      <div class="floor-img"><img src="{img('mp-b17.jpg')}" loading="lazy" alt="{alt_of('mp-b17.jpg')}"></div>
      <div class="floor-text">
        <p class="eyebrow">2F</p><h2>Convention Hall</h2>
        <p>2층 컨벤션홀은 송년회·기업연회·런칭쇼·MICE 단체행사·가족연회·예식을 위한 공간으로, 100명부터 최대 300명까지 식사 세팅이 가능합니다. 무대·LED 영상·음향 장비를 모두 갖추고 있으며, 사면이 통유리로 되어 있어 한강의 정취를 그대로 즐길 수 있습니다.</p>
        <a class="btn" href="business-party.html">Business Party</a>
      </div>
    </article>
    <article class="floor">
      <div class="floor-img"><img src="{img('mp-c22.jpg')}" loading="lazy" alt="{alt_of('mp-c22.jpg')}"></div>
      <div class="floor-text">
        <p class="eyebrow">3F</p><h2>Rooftop Garden</h2>
        <p>대리석 단상 위로 화이트 대리석 가제보가 있는 3층 루프탑 가든은 한강이 그대로 내려다보이며 서리풀 공원의 조경과 어우러집니다. 가든 예식, 칵테일 리셉션, 선셋 파티, 송년회 애프터파티에 쓰이며 우천 시에는 2층 홀로 전환합니다.</p>
        <a class="btn" href="garden-wedding.html">Garden Wedding</a>
      </div>
    </article>
  </div>
</section>

{facts("Venue facts", "공간별 상세 정보",
  "층별 용도와 규모를 한눈에 정리했습니다.",
  [("1층 마리나 카페", f"카페 · 가든 소모임 · {CAFE_HOURS}"),
   ("2층 컨벤션홀", "100~300명 · 라운드/극장식/클래스룸 세팅 · 무대·LED·음향 · 사면 한강 통창"),
   ("3층 루프탑 가든", "화이트 가제보 · 잔디 버진로드 · 리셉션·소규모 예식 · 선셋 뷰"),
   ("부대 시설", "신부대기실 · 포토존 · 현수막 설치 · 케이터링 주방"),
   ("접근", "지하철 9호선 신반포역 · 고속터미널역, 반포한강공원 서래나루 입구"),
   ("주차", "한강공원 주차장 약 200대, 행사 참석자 3시간 무료")],
  en="Floors: 1F Marina Cafe (daily 10:00–22:00) · 2F Convention Hall for 100–300 guests with stage, LED and sound, floor-to-ceiling river views · 3F Rooftop Garden with a white marble gazebo for ceremonies and receptions. Rain backup: the 2F hall.")}

<section class="section alt">
  <div class="wrap">
    <h2 class="center">Turning a Vision into Reality</h2>
    <p class="center sub">Anniversary Flower · Romantic Garden Wedding · A Perfectionist on Every Detail</p>
    {gallery([("mp-c05.jpg", 3, 2), ("mp-c21.jpg", 3, 2), ("mp-b21.jpg", 4, 3)], "gallery cols-3 even")}
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>This is a great place for your special day</h2>
    <a class="btn btn-light" href="contact.html">Book a place</a>
  </div>
</section>
"""

# ======================================================================
# BUSINESS PARTY / 송년회 / MICE
# ======================================================================
biz_faq, biz_faq_ld = faq("송년회 · 기업행사 FAQ", [
    ("송년회는 몇 명부터 가능한가요?", "50명 소규모 모임부터 300명 전사 송년회까지 가능합니다. 가장 많은 규모는 100~200명이며 2층 컨벤션홀에서 진행하고, 50명 내외 모임은 작은 룸이나 3층 루프탑 가든·1층 카페 가든을 이용합니다."),
    ("송년회 예약은 언제까지 해야 하나요?", "12월은 가장 예약이 빠른 시기입니다. 금요일 저녁 기준 10~11월 중 예약을 권장하며, 평일 저녁은 상대적으로 여유가 있습니다. 날짜와 인원만 먼저 알려주시면 가예약으로 잡아드립니다."),
    ("식사는 코스와 뷔페 중 선택할 수 있나요?", "네. 착석 코스 디너, 뷔페, 스탠딩 핑거푸드 리셉션 중 선택할 수 있고, 맥주·와인·소프트드링크 프리드링크 패키지를 추가할 수 있습니다. 국제 행사를 위한 할랄·채식 메뉴도 준비합니다."),
    ("무대·마이크·스크린이 포함되나요? 경품 추첨·공연도 되나요?", "2층 홀에는 무대, 음향, 무선 마이크, LED 영상 스크린, 조명이 갖춰져 있어 시상식·경품 추첨·공연·영상 상영을 바로 진행할 수 있습니다. 별도 연출이 필요하면 협력 업체를 연결해 드립니다."),
    ("송년회 1차 후 2차 장소도 있나요?", "같은 건물 3층 루프탑 가든에서 애프터파티를 이어갈 수 있고, 1층 마리나 카페(22:00까지)도 이용 가능합니다. 이동 없이 한 곳에서 마무리할 수 있는 점이 장점입니다."),
    ("주차와 단체 버스 이용은 어떻게 하나요?", "반포한강공원 주차장(약 200대)을 이용하며 행사 참석자는 3시간 무료입니다. 단체 버스는 반포한강공원 주차장에서 하차하며, 사전에 알려주시면 동선을 안내해 드립니다."),
    ("현수막·포토월·기업 로고 노출이 가능한가요?", "홀 내부 현수막과 포토월 설치가 가능하고, 외부 도교·외벽 현수막은 별도 협의로 설치할 수 있습니다. 시안은 행사 1주 전까지 전달해 주시면 됩니다."),
])
business = f"""
{hero("mp-b28.jpg", "Marina Park", "Business Party / MICE Event", "송년회 · 연말 모임 · 기업연회 · 컨퍼런스 — 100~300명")}
<section class="section">
  <div class="wrap">
    <p class="center sub">송년회·연말 모임, 기업연회·갈라디너, 컨퍼런스·세미나·시상식 — 한강이 보이는 2층 컨벤션홀에서 100명부터 300명까지 진행하실 수 있습니다. 식사 후에는 3층 루프탑 가든에서 애프터파티를 이어갑니다.</p>
    {gallery([
        ("mp-e06.jpg", 4, 3), ("mp-e05.jpg", 3, 4), ("mp-b26.jpg", 3, 2), ("mp-b28.jpg", 3, 2),
        ("mp-b18.jpg", 3, 2), ("mp-b25.jpg", 2, 1), ("mp-b31.jpg", 3, 2), ("mp-b30.jpg", 3, 2),
        ("mp-b17.jpg", 3, 2), ("mp-b32.jpg", 2, 1), ("mp-b10.jpg", 3, 2), ("mp-b09.jpg", 3, 2),
        ("2649b2_2550e0e1deda4df8a29c7eb8a3ae9d1e~mv2.png", 7, 4),
        ("2649b2_ffa6948050474d00a60c19183833a48e~mv2.jpg", 2, 1),
        ("2649b2_2e13c691e36f4f9f975aa6e7f7489290~mv2_d_6768_3936_s_4_2.jpg", 5, 3),
        ("2649b2_1f4e534b009a455795154239a1f1f044~mv2.png", 5, 3),
        ("2649b2_c61315fdb1d8465daf24e08a05ebad93~mv2.jpeg", 3, 2),
        ("2649b2_349a109dd0544dc68648d9f7df86de79~mv2.jpg", 4, 3),
        ("2649b2_72c455d453074068a52a1ee11fc9a2c1~mv2.jpg", 4, 3),
        ("2649b2_dad8a86f44a54addbec2938ead2ed497~mv2.jpg", 4, 3),
    ])}
  </div>
</section>

{facts("Year-end party", "송년회 · 연말 모임 안내",
  "마리나파크는 서울 반포 한강 서래나루에 있는 송년회·연말 모임 장소입니다. 50명 소규모 모임부터 300명 전사 송년회까지, 2층 컨벤션홀에서 식사와 시상식·경품 추첨·공연을 진행하고, 3층 루프탑 가든에서 한강 야경을 보며 애프터파티를 이어갈 수 있습니다.",
  [("적합 규모", "50명 소규모 모임 ~ 300명 전사 송년회 (100~200명이 가장 많음)"),
   ("추천 구성", "웰컴 드링크(가든) → 코스/뷔페 디너 + 시상·경품·공연(2층 홀) → 루프탑 애프터파티"),
   ("식사", "코스 디너 · 뷔페 · 핑거푸드 리셉션 · 프리드링크(맥주·와인·소프트) 패키지"),
   ("장비", "무대 · 음향 · 무선 마이크 · LED 스크린 · 조명 — 영상 상영·시상식 바로 가능"),
   ("연출", "현수막 · 포토월 · 테이블 센터피스 · 외벽 현수막(협의)"),
   ("시즌", "11~12월 금요일 저녁은 조기 마감 — 10~11월 예약 권장"),
   ("주차·교통", "한강공원 주차장 약 200대, 참석자 3시간 무료 · 9호선 신반포역 · 단체 버스는 한강공원 주차장 하차")],
  en="Year-end parties and corporate galas for 50–300 guests in the river-view 2F hall, with a rooftop garden after-party on the 3rd floor. Course dinner, buffet or canapé reception with free-flow drinks; stage, LED screen and sound included. Halal and vegetarian menus available for international groups.")}

{facts("MICE", "컨퍼런스 · 세미나 · 런칭 · 시상식",
  "국제 행사 경험이 많은 팀이 등록 데스크부터 식사, 영상, 통역 부스 동선까지 함께 설계합니다.",
  [("세팅", "극장식 · 클래스룸 · 라운드 · 스탠딩 리셉션"),
   ("영상·음향", "LED 메인 스크린 · 프로젝터 · 음향 · 무선 마이크 · 동시통역 부스 설치 가능(협의)"),
   ("부대 공간", "등록 데스크 · VIP 대기실 · 포토존 · 전시 부스 라인"),
   ("식사", "국제 행사 기준 할랄·채식·논알코올 대응, 커피 브레이크"),
   ("언어", "영어 상담 및 영문 견적서 제공")])}

{biz_faq}
<section class="section cta-band"><div class="wrap center"><h2>Turning a Vision into Reality</h2><p>송년회 · 기업행사 문의 {TEL}</p><a class="btn btn-light" href="contact.html">행사 문의</a></div></section>
"""

# ======================================================================
# LAUNCHING PARTY
# ======================================================================
launch_faq, launch_faq_ld = faq("런칭 행사 FAQ", [
    ("런칭쇼에 필요한 무대와 영상 장비가 있나요?", "2층 컨벤션홀에 무대, LED 메인 스크린, 음향, 조명이 갖춰져 있어 제품 공개 영상과 프레젠테이션을 바로 진행할 수 있습니다. 특수 연출·추가 LED는 협력 업체와 연결해 드립니다."),
    ("미디어·인플루언서 초청 행사에 적합한가요?", "한강 전망의 통창 홀과 야간 외관 조명, 3층 루프탑 포토존이 있어 사진과 영상 콘텐츠가 잘 나오는 공간입니다. 포토월과 미디어 월 설치가 가능합니다."),
    ("행사 후 네트워킹 공간이 있나요?", "3층 루프탑 가든에서 칵테일 애프터파티를 이어갈 수 있습니다. 한강 야경을 배경으로 한 스탠딩 리셉션이 가능합니다."),
    ("전시 부스나 제품 디스플레이가 가능한가요?", "홀 내부와 로비에 제품 디스플레이·부스 설치가 가능하며 전력·동선을 사전에 함께 점검합니다."),
])
launching = f"""
{hero("mp-b26.jpg", "Marina Park", "Launching Party", "런칭쇼 · 브랜드 프로모션 · 미디어 데이")}
<section class="section">
  <div class="wrap">
    <p class="center sub">신제품 런칭쇼, 브랜드 프로모션, 미디어 행사 — 무대·LED·음향 장비를 갖춘 한강 전망 홀과 루프탑 포토존에서 브랜드의 첫 순간을 연출합니다.</p>
    {gallery([
        ("mp-b28.jpg", 3, 2), ("mp-b26.jpg", 3, 2), ("mp-b29.jpg", 2, 1), ("mp-b27.jpg", 3, 2), ("mp-b32.jpg", 2, 1), ("mp-b24.jpg", 3, 2),
        ("2649b2_ab37a379303f483e8dbc62ae094457a0~mv2_d_4032_3024_s_4_2.jpg", 4, 3),
        ("2649b2_2aa49e3249b8467eb9ab97690b1a6849~mv2_d_4928_3280_s_4_2.jpg", 3, 2),
        ("2649b2_f58fea24227f40d0ac2b928e00be2ac5~mv2_d_4811_3202_s_4_2.jpg", 3, 2),
        ("2649b2_f5a265e7d0a4424f84543524a97c1576~mv2_d_4146_2764_s_4_2.jpg", 3, 2),
        ("2649b2_1e7ed286fc8744979968ca852dc81221~mv2_d_4176_2784_s_4_2.jpg", 3, 2),
        ("2649b2_c95dc8b4388643c6a46599f9b158c4b4~mv2_d_4769_3174_s_4_2.jpg", 3, 2),
        ("2649b2_b90262263cde4c458a442c8e3c15e334~mv2_d_4176_2784_s_4_2.jpg", 3, 2),
        ("2649b2_5357ded7cd6b472fa32e52d98ba38ea9~mv2_d_4093_2729_s_4_2.jpg", 3, 2),
        ("2649b2_4a9979fcb2a8482798bb6ca6b67a4d36~mv2_d_4176_2784_s_4_2.jpg", 3, 2),
        ("2649b2_375da41383a14dcf9352d6eadfc9d79a~mv2_d_4176_2784_s_4_2.jpg", 3, 2),
        ("2649b2_0cacf8685e5f4c1b8e26dfeaf77fb801~mv2_d_4122_2748_s_4_2.jpg", 3, 2),
        ("2649b2_8a79a494c04a452cabc6d16479ae6ed5~mv2_d_4176_2784_s_4_2.jpg", 3, 2),
        ("2649b2_366cf79f6c2a44fdbcd60faf77bb2b05~mv2_d_4176_2784_s_4_2.jpg", 3, 2),
    ])}
  </div>
</section>
{facts("Launching", "런칭 행사 안내",
  "마리나파크는 반포 한강변의 런칭쇼·브랜드 프로모션 행사장입니다.",
  [("규모", "100~300명 착석 또는 스탠딩 리셉션"),
   ("장비", "무대 · LED 메인 스크린 · 음향 · 조명 · 무선 마이크"),
   ("연출 공간", "통창 홀 · 야간 외관 조명 · 3층 루프탑 포토존 · 포토월/미디어 월"),
   ("식사", "핑거푸드 리셉션 · 코스 · 프리드링크"),
   ("애프터파티", "3층 루프탑 가든 칵테일 리셉션")],
  en="Product launches, brand promotions and media days for 100–300 guests: stage, LED screen, sound and lighting in a glass-walled river-view hall, plus a rooftop garden for photo moments and after-parties.")}
{launch_faq}
<section class="section cta-band"><div class="wrap center"><h2>Launch your brand on the Han River</h2><p>런칭 행사 문의 {TEL}</p><a class="btn btn-light" href="contact.html">행사 문의</a></div></section>
"""

# ======================================================================
# 1st PARTY / 돌잔치
# ======================================================================
first_faq, first_faq_ld = faq("돌잔치 FAQ", [
    ("돌잔치는 몇 명부터 가능한가요?", "최소 50명부터 진행합니다. 50명 규모는 작은 룸에서 가족 돌잔치로, 100명 이상~200명 돌잔치는 2층 컨벤션홀에서 인원에 맞춰 구성해 드립니다."),
    ("돌상과 포토테이블이 포함되나요?", "돌상·포토테이블 세팅 패키지는 150만원이며 현수막 설치가 가능합니다. 돌잡이 등 행사 진행을 맡는 전문 사회자는 20만원에 추가할 수 있습니다."),
    ("식사는 어떻게 제공되나요?", "착석 코스 또는 뷔페 중 선택할 수 있습니다. 5세 이하 아이 식사는 무료이고 유아 의자가 준비되어 있으며, 어르신 참석이 많은 가족 연회에 맞춘 메뉴 조정도 가능합니다."),
    ("답례품이나 케이크를 가져와도 되나요?", "답례품 반입과 전용 테이블 세팅이 가능합니다. 케이크·떡 등 일부 식품 반입은 사전에 알려주시면 안내해 드립니다."),
    ("주차와 유모차 이동은 편한가요?", "반포한강공원 주차장(약 200대)을 이용하며 참석자는 3시간 무료입니다. 엘리베이터로 유모차 이동이 가능하고, 한강공원 산책로가 바로 앞이라 식사 후 가족 사진 촬영에도 좋습니다."),
    ("주말 돌잔치 예약은 언제 해야 하나요?", "주말 점심 시간대는 2~3개월 전 예약을 권장합니다. 평일과 저녁 시간대는 비교적 여유가 있습니다."),
])
first = f"""
{hero("2649b2_27aac57c162e474eb1debfcef01fee8c~mv2.jpg", "Marina Park", "1st Party", "반포 한강뷰 돌잔치 · 가족 연회")}
<section class="section">
  <div class="wrap">
    <p class="center sub">아이의 첫 번째 생일, 한강이 보이는 공간에서 가족과 함께하는 돌잔치 — 50명 규모 룸 돌잔치부터 100명 이상·200명 돌잔치까지, 돌상 데코레이션부터 식사·사회자까지 맞춤으로 준비합니다.</p>
    {gallery([
        ("mp-c53.jpg", 4, 3), ("mp-c52.jpg", 4, 3), ("mp-c58.jpg", 3, 2), ("mp-c56.jpg", 4, 3),
        ("2649b2_862325761e3d4188a6ee89a5d94bbc60~mv2.jpg", 3, 4),
        ("2649b2_964b10c0a456478f915c818841fa41ef~mv2.jpg", 4, 3),
        ("2649b2_878a67299d624f2f8126810caa5915e0~mv2.jpg", 4, 3),
        ("2649b2_a8231255dc614b1b96e934212a2c7727~mv2.jpg", 3, 4),
        ("2649b2_f8e846adf12640ecb1082724fdb0103d~mv2.jpg", 3, 4),
        ("2649b2_27aac57c162e474eb1debfcef01fee8c~mv2.jpg", 4, 3),
        ("2649b2_ee6b0814763143daabed0fbd9d19a0e7~mv2.jpg", 4, 3),
        ("2649b2_5e0ff44e223448338d9ef00b03bcf84c~mv2.jpg", 4, 3),
        ("2649b2_300b85e2fe7148889ac0ea5a72225ca9~mv2.jpg", 4, 3),
        ("2649b2_d915a9a8d8fb4330880447692450ba8f~mv2.jpg", 4, 3),
        ("2649b2_58b4fb5d2edc4079bc5a78fc5c1695ac~mv2.jpg", 3, 4),
        ("2649b2_26654215ffe04ac08d029f33207d8b1a~mv2.jpg", 3, 4),
        ("2649b2_c537efda88cc4316bb161b99c910f3e1~mv2.jpg", 4, 3),
        ("2649b2_b0a27021a5e2480bb624dd050178f88a~mv2.jpg", 4, 3),
        ("2649b2_9a69d241636f420f9f74f8c549c596ec~mv2.jpg", 4, 3),
        ("2649b2_d10aace456fc4cf5a6cc299301d883d9~mv2.jpg", 4, 3),
    ])}
  </div>
</section>
{facts("First birthday", "돌잔치 안내",
  "마리나파크는 서울 서초구 반포 한강변의 돌잔치·가족 연회 장소입니다. 50명 규모의 작은 룸 가족 돌잔치부터 100명 이상~200명 돌잔치까지 인원에 맞춰 홀을 구성하고, 돌상·포토테이블·현수막·식사·사회자를 한 번에 준비합니다.",
  [("규모", "최소 50명 (작은 룸) ~ 100명 이상·200명 (2층 홀)"),
   ("돌상·포토테이블", "세팅 패키지 150만원 · 현수막 설치"),
   ("사회자", "돌잡이·행사 진행 전문 사회자 20만원 (선택)"),
   ("식사", "착석 코스 또는 뷔페 · 5세 이하 식사 무료 · 유아 의자 · 어르신 맞춤 메뉴"),
   ("반입", "답례품 반입 및 전용 테이블 가능 (식품 반입은 사전 안내)"),
   ("편의", "엘리베이터 · 유모차 이동 · 한강공원 산책로 가족 촬영"),
   ("주차", "한강공원 주차장(약 200대) 참석자 3시간 무료"),
   ("예약", "주말 점심 2~3개월 전 권장")],
  en="First-birthday (doljanchi) celebrations for 50 to 200 guests with river views: dol table and photo table package, banner, course or buffet meal, free meals for children under 5, high chairs, optional professional MC. Free parking for 3 hours at Banpo Han River Park.")}
{first_faq}
<section class="section cta-band"><div class="wrap center"><h2>A day to remember for the whole family</h2><p>돌잔치 문의 {TEL}</p><a class="btn btn-light" href="contact.html">돌잔치 문의</a></div></section>
"""

# ======================================================================
# WEDDING / 소규모 예식
# ======================================================================
wed_faq, wed_faq_ld = faq("소규모 예식 · 웨딩 FAQ", [
    ("소규모 예식은 몇 명부터 가능한가요?", "최소 보증 인원 50명부터 진행합니다. 가족·지인 중심 50~100명 소규모 예식에 특히 적합하고, 2층 실내 홀 예식은 100명 이상 최대 300명, 3층 가든 예식 후 피로연은 2층 홀에서 이어집니다."),
    ("하루에 몇 커플이 예식을 하나요?", "하루 두 커플만 진행합니다. 예식 사이 시간 간격이 넉넉해 준비와 촬영, 피로연을 여유 있게 진행할 수 있습니다."),
    ("주례 없는 예식이나 가족 식사형 예식도 가능한가요?", "네. 주례 없는 예식, 양가 가족 식사 중심의 스몰웨딩, 야외 가든 서약식 후 홀 피로연 등 형식에 맞춰 진행을 설계해 드립니다."),
    ("우천 시에는 어떻게 되나요?", "가든 예식이 예정된 날 비가 오면 2층 컨벤션홀로 이동해 실내 예식으로 진행합니다. 답사 때 우천 대비 홀 세팅을 미리 확정해 두어 당일 혼선이 없습니다."),
    ("신부대기실과 폐백실이 있나요?", "한강이 보이는 신부대기실이 있으며, 폐백·가족 사진 촬영 공간을 함께 준비해 드립니다."),
    ("외부 플로리스트·스냅·메이크업 반입이 가능한가요?", "가능합니다. 플라워 데코는 저희 플로리스트와의 컨셉 미팅으로 준비해 드리며, 외부 업체 반입도 사전 협의로 진행합니다."),
    ("식사 메뉴는 어떻게 구성되나요?", "셰프가 준비하는 코스 디너(1인 10만원부터) 또는 뷔페 중 선택할 수 있으며, 하객 구성(어르신·아이·외국인 하객)에 따라 메뉴를 조정합니다. 할랄·채식 메뉴도 가능합니다."),
    ("예식 가능한 시간대와 예약 시기는?", "주말 예식은 12:00와 18:00 두 타임으로 하루 두 커플만 진행합니다. 실내 예식은 1~12월 연중 가능하고, 가든 예식은 3월 말~6월·9~11월입니다. 봄·가을 주말은 6개월 이상 전 예약을 권장합니다."),
])
wedding = f"""
{hero("mp-c10.jpg", "Marina Park", "Marina Park Wedding", "한강 소규모 예식 · 컨벤션 웨딩 · 가든 웨딩", tall=True)}
<section class="section">
  <div class="wrap narrow prose">
    <p>마리나파크는 2층 홀에서 진행하는 컨벤션 웨딩과 3층 루프탑에서 진행하는 야외 가든웨딩을 모두 갖춘 한강 웨딩 공간입니다. 최소 보증 인원 50명의 가족·지인 중심 소규모 예식부터 100명 이상 최대 300명 규모의 실내 홀 예식까지, 형식에 맞춰 진행을 설계합니다. 주말 예식은 12:00·18:00 두 타임입니다.</p>
    <p>플로리스트와의 컨셉 미팅을 통해 준비되는 웨딩 플라워 데코레이션과 웨딩 연출, 하루에 두 커플만 진행하는 여유로운 시간 간격, 서리풀 공원을 배경으로 한강 위에서 진행되는 격조 있는 예식은 새로운 출발을 앞둔 커플에게 소중하고 특별한 추억으로 남을 것입니다.</p>
    <p>국제연회를 진행해 온 감각 있는 스타일리스트가 함께하는 마리나파크 웨딩은 셰프가 준비하는 디너와 함께 더욱 빛을 발할 것입니다.</p>
    <p class="center cta-inline">{CTA_TEL}</p>
  </div>
</section>
<section class="section alt">
  <div class="wrap">
    {gallery([
        ("mp-c03.jpg", 3, 2), ("mp-c04.jpg", 3, 2), ("mp-c52.jpg", 4, 3), ("mp-c54.jpg", 3, 4),
        ("mp-c07.jpg", 3, 2), ("mp-c08.jpg", 3, 2), ("mp-c09.jpg", 3, 2), ("mp-c15.jpg", 2, 3),
        ("mp-c14.jpg", 3, 2), ("mp-c55.jpg", 4, 3), ("mp-c59.jpg", 3, 2), ("mp-c60.jpg", 3, 2),
        ("mp-c05.jpg", 3, 2), ("mp-c56.jpg", 4, 3),
        ("2649b2_d68896f967204194a87c7acbefe756ec~mv2_d_3553_5236_s_4_2.jpg", 2, 3),
        ("8bb438_ec9a72099f9648dfb08d9412804a464a~mv2_d_3000_2000_s_2.jpg", 3, 2),
    ])}
    <p class="center"><a class="btn" href="garden-wedding.html">Garden Wedding 보기</a></p>
  </div>
</section>
{facts("Intimate wedding", "소규모 예식 · 스몰웨딩 안내",
  "마리나파크는 서울 반포 한강 서래나루의 소규모 예식·스몰웨딩 장소입니다. 하객 50명대 가족 예식부터 300명 컨벤션 웨딩까지, 2층 한강 통창 홀과 3층 가든 두 공간을 날씨와 인원에 맞춰 씁니다.",
  [("규모", "최소 보증 50명 · 소규모 예식 50~100명 · 실내 홀 예식 100~300명"),
   ("공간", "2층 홀 예식(실내, 한강 통창, 1~12월) · 3층 가든 예식(야외, 화이트 가제보, 3월 말~6월·9~11월) · 피로연은 2층 홀"),
   ("시간대", "주말 12:00 · 18:00 두 타임, 하루 두 커플만"),
   ("진행", "주례 없는 예식 · 가족 식사형 스몰웨딩 · 서약식+피로연"),
   ("우천 시", "2층 컨벤션홀로 이동해 실내 예식 (답사 시 사전 확정)"),
   ("부대 시설", "한강뷰 신부대기실 · 폐백/가족 촬영 공간 · 포토존"),
   ("식사", "셰프 코스 디너 1인 10만원부터 · 뷔페 · 어르신/아이/외국인 하객 맞춤 · 할랄·채식 가능"),
   ("데코", "전속 플로리스트 컨셉 미팅 · 외부 업체 반입 협의 가능"),
   ("주차", "한강공원 주차장 약 200대 · 참석자 3시간 무료"),
   ("예약", "봄·가을 주말은 6개월 이상 전 권장")],
  en="Intimate weddings from a 50-guest minimum up to 300 (weekend ceremonies at 12:00 and 18:00, two couples a day): an indoor hall with floor-to-ceiling Han River views on the 2nd floor and an outdoor rooftop garden ceremony space with a white marble gazebo on the 3rd floor. Only two couples per day; rain backup indoors; bridal room with river view; chef's course dinner or buffet.")}
{wed_faq}
"""

# ======================================================================
# GARDEN WEDDING
# ======================================================================
garden_faq, garden_faq_ld = faq("가든웨딩 FAQ", [
    ("가든 예식은 언제가 가장 좋은가요?", "3월 말~6월과 9~11월에 가능하며, 5~6월·10월 선셋 시간대를 가장 추천합니다. 선셋 시간대 예식은 한강 노을을 배경으로 진행되어 사진이 특히 아름답습니다. 한여름·한겨울은 2층 홀 예식을 권합니다."),
    ("비가 오면 어떻게 하나요?", "2층 컨벤션홀로 이동해 실내 예식으로 진행합니다. 답사 때 우천 대비 세팅을 미리 확정해 두므로 당일 아침 날씨에 따라 바로 결정할 수 있습니다."),
    ("가든 예식 후 식사는 어디서 하나요?", "예식은 3층 가든, 피로연 식사는 2층 홀에서 이어집니다. 가든에서 칵테일 리셉션을 먼저 하고 홀로 이동하는 구성도 많이 선택합니다."),
    ("가든 예식에 적합한 인원은?", "소규모 예식에 가장 적합하며, 하객이 많은 경우 가든 서약식 후 2층 홀 피로연으로 구성합니다. 정확한 세팅은 답사 때 현장에서 함께 확정합니다."),
    ("야간 가든 예식도 가능한가요?", "조명과 스트링 라이트를 활용한 야간 가든 예식·리셉션이 가능합니다. 한강 다리 야경이 배경이 됩니다."),
])
garden = f"""
{hero("mp-c01.jpg", "Marina Park", "Garden Wedding", "Making Dreams Come True — 한강 가든웨딩 · 야외 결혼식", tall=True)}
<section class="section">
  <div class="wrap">
    <p class="center sub">한강과 서리풀 공원을 배경으로, 화이트 대리석 가제보 아래에서 진행되는 로맨틱 가든 웨딩. 3월 말~6월·9~11월 선셋 예식을 추천하며, 우천 시에는 2층 컨벤션홀로 이동합니다.</p>
    {gallery([
        ("mp-c02.jpg", 3, 2), ("mp-c06.jpg", 3, 2), ("mp-c21.jpg", 3, 2), ("mp-c33.jpg", 3, 2),
        ("mp-c34.jpg", 3, 2), ("mp-c35.jpg", 3, 2), ("mp-c36.jpg", 4, 3), ("mp-c22.jpg", 3, 2),
        ("mp-c49.jpg", 3, 2), ("mp-c50.jpg", 2, 3), ("mp-b21.jpg", 4, 3), ("mp-c01.jpg", 2, 1),
        ("2649b2_5ce8952e336d431c8a9f170eb5929234~mv2.png", 4, 3),
        ("2649b2_c143d015d0454bed82088c76f228a8dc~mv2.jpg", 5, 3),
        ("2649b2_b13801a7f8d04061a365a1e6a05f88e9~mv2.jpg", 3, 2),
        ("2649b2_f1c4946dee4f4dbcb7d5237ec2b0e743~mv2.jpeg", 3, 2),
        ("2649b2_334aea7b16464fd78967881c4fb4bbf3~mv2.jpg", 2, 1),
        ("2649b2_a170c69162b34c87af8cb43680b1d836f003.jpg", 16, 9),
        ("2649b2_0bc81bf517e94690b2ee2cb2f02e0258~mv2.jpeg", 3, 2),
        ("2649b2_e9885f9c949647e394df146dfae49c3d~mv2.jpeg", 3, 2),
    ])}
  </div>
</section>
{facts("Garden wedding", "가든웨딩 안내",
  "마리나파크 3층 루프탑 가든은 반포 한강과 서리풀 공원이 보이는 야외 예식 공간입니다. 화이트 대리석 가제보와 잔디 버진로드에서 예식을 올리고, 2층 홀에서 피로연을 이어갑니다.",
  [("공간", "3층 루프탑 가든 · 화이트 대리석 가제보 · 잔디 버진로드 · 한강·서리풀 공원 뷰"),
   ("가능 시기", "3월 말~6월 · 9~11월 (선셋 시간대 추천) · 실내 홀 예식은 연중"),
   ("구성", "가든 예식 → 2층 홀 피로연 / 가든 칵테일 리셉션 → 홀 예식·식사"),
   ("우천 시", "2층 컨벤션홀로 이동 (답사 시 사전 확정)"),
   ("야간", "스트링 라이트·조명 야간 예식 및 리셉션 가능"),
   ("데코", "전속 플로리스트 플라워 아치·가제보 데코")],
  en="Outdoor garden weddings on the 3rd-floor rooftop with a white marble gazebo and lawn aisle overlooking the Han River; possible late March–June and September–November, sunset ceremonies recommended, indoor hall as rain backup, reception in the 2F hall.")}
{garden_faq}
<section class="section cta-band"><div class="wrap center"><h2>Turning a Vision into Reality</h2><p>Anniversary Flower · Romantic Garden Wedding · A Perfectionist on Every Detail</p><a class="btn btn-light" href="contact.html">웨딩 상담 문의</a></div></section>
"""

# ======================================================================
# CAFE
# ======================================================================
def menu(title, note, rows):
    out = [f'<div class="menu-card"><h3>{title}</h3>']
    if note: out.append(f'<p class="menu-note">{note}</p>')
    out.append('<table>')
    for r in rows:
        if len(r) == 1:
            out.append(f'<tr class="menu-group"><th colspan="3">{r[0]}</th></tr>')
        else:
            name, en, price = r
            out.append(f'<tr><td class="m-name">{name}<span class="m-en">{en}</span></td><td class="m-price">{price}</td></tr>')
    out.append('</table></div>')
    return "\n".join(out)

cafe_faq, cafe_faq_ld = faq("마리나 카페 FAQ", [
    ("카페 영업시간은 어떻게 되나요?", f"{CAFE_HOURS} 영업합니다. 행사 대관이 있는 날은 일부 공간 이용이 제한될 수 있습니다."),
    ("카페에서 소규모 모임이나 생일 파티를 할 수 있나요?", "1층 카페 가든에서 10~30명 규모의 생일 모임·동호회·브라이덜 샤워·소규모 송년 모임을 예약할 수 있습니다. 케이크 반입과 간단한 데코도 가능합니다."),
    ("주차는 어떻게 하나요?", "반포한강공원 주차장을 이용합니다. 한강공원 산책 후 들르기 좋은 위치입니다."),
])
cafe = f"""
{hero("2649b2_256b3a1192ce4999b2c9cdaa52cba08f~mv2_d_5760_1657_s_2.jpg", "1F · " + CAFE_HOURS, "Marina Park Cafe", "반포 한강공원 서래나루 한강뷰 카페")}
<section class="section" id="menu">
  <div class="wrap">
    <p class="center sub">반포한강공원 서래나루, 한강이 보이는 1층 카페에서 커피와 티, 디저트, 피자와 파스타, 와인을 즐기실 수 있습니다. 영업시간 {CAFE_HOURS}. 가격 단위: 천 원 (예: 4.5 = 4,500원)</p>
    <div class="menu-grid">
    {menu("Food", "", [
        ("Pizza",),
        ("고르곤졸라 / 마르게리따 피자","Gorgonzola Cheese Pizza / Margherita Pizza","22.0"),
        ("페퍼로니 / 쉬림프 피자","Pepperoni Pizza / Shrimp Pizza","24.0"),
        ("Plates",),
        ("돈까스 / 치즈돈까스","Pork Cutlet / Cheese Pork Cutlet","18.0 / 20.0"),
        ("함박스테이크","Hamburg Steak","26.0"),
        ("볶음밥 (김치 / 새우)","Fried Rice (Kimchi / Shrimp)","18.0"),
        ("까르보나라 / 쉬림프 오일 파스타","Carbonara / Shrimp Oil Pasta","22.0"),
        ("감자튀김 / 나초 & 멕시칸 살사","French Fries / Nachos & Salsa","10.0 / 12.0"),
        ("버팔로윙 & 칩스 / 쉬림프 & 칩스","Wings & Chips / Shrimp & Chips","20.0"),
        ("샐러드 (연어 / 치킨 / 부라타 치즈)","Salad (Salmon / Chicken / Burrata)","22.0"),
        ("떡볶이 / 닭강정","Tteokbokki / Sweet & Sour Chicken","20.0"),
        ("먹태 / 먹태 세트 (먹태 + 스텔라 2잔 330ml)","Pollack / Pollack Set","19.0 / 27.0"),
        ("찹스테이크 / 바베큐 폭립","Chop Steak / BBQ Pork Ribs","32.0 / 30.0"),
        ("Brunch Set (16:00까지)",),
        ("브런치 + 커피 (호밀빵+버터 · 베이컨&소시지 · 계란후라이 · 샐러드)","Brunch + Coffee","20.0"),
    ])}
    {menu("Coffee", "Hot / Iced", [
        ("에스프레소","Espresso","4.0"),
        ("에스프레소 콘파냐","Espresso Con Panna","4.5"),
        ("아메리카노 (디카페인 +0.5)","Americano","5.0 / 5.5"),
        ("원조 냉커피","Original Iced Coffee","6.0"),
        ("카푸치노","Cappuccino","5.5 / 6.0"),
        ("카페라떼","Cafe Latte","5.5 / 6.0"),
        ("바닐라라떼","Vanilla Latte","6.0 / 6.5"),
        ("카라멜라떼","Caramel Latte","6.0 / 6.5"),
        ("돌체라떼","Dolce Latte","6.0 / 6.5"),
        ("카라멜 마끼아또","Caramel Macchiato","6.0 / 6.5"),
        ("카페모카 (생크림 +0.5)","Cafe Mocha","6.0 / 6.5"),
        ("콜드브루","Cold Brew","5.5 / 6.0"),
        ("브루라떼","Brew Latte","6.0 / 6.5"),
        ("아포가토","Affogato","6.5"),
    ])}
    {menu("Tea", "Hot / Iced", [
        ("얼그레이 / 히비스커스 / 페퍼민트 / 카모마일 / 레몬스카이 / 루이보스 바닐라 / 녹차","Earl Grey · Hibiscus · Peppermint · Chamomile · Lemon Sky · Rooibos Vanilla · Green Tea","5.5 / 6.0"),
        ("유자차 / 자몽차 / 레몬차 (청)","Citron / Grapefruit / Lemon Tea","6.5 / 7.0"),
        ("로얄 밀크티","Royal Milk Tea","6.5 / 7.0"),
        ("말차라떼","Matcha Latte","6.5 / 7.0"),
    ])}
    {menu("Beverage", "Hot / Iced", [
        ("핫초코","Hot Choco","5.5 / 6.0"),
        ("민트초코라떼","Mint Chocolate Latte","6.0 / 6.5"),
        ("고구마라떼","Sweet Potato Latte","6.5 / 7.0"),
        ("딸기라떼","Strawberry Latte","7.0"),
        ("아이스티 (레몬 / 복숭아)","Ice Tea (Lemon / Peach)","6.0"),
        ("에이드 (레몬 / 자몽 / 청포도 / 체리)","Ade","6.5"),
        ("오렌지주스","Orange Juice","5.0"),
        ("생토마토주스","Fresh Tomato Juice","7.0"),
        ("스무디 (딸기 / 망고 / 키위)","Smoothie","7.5"),
        ("요거트 스무디 (플레인 / 딸기 / 망고 / 키위)","Yogurt Smoothie","7.5"),
        ("파인애플 샤베트","Pineapple Sherbet","8.0"),
    ])}
    {menu("Bakery", "", [
        ("플레인 베이글 + 크림치즈","Plain Bagel + Cream Cheese","4.5"),
        ("크로크무슈","Croque Monsieur","5.5"),
        ("아이스크림 크로플","Ice Cream Croffle","7.5"),
        ("허니버터브레드","Honey Butter Bread","6.5"),
        ("조각케이크","Piece of Cake","7.0"),
    ])}
    {menu("Wine · Beer · Soju", "Glass / Bottle", [
        ("Wine",),
        ("장발몽 샤르도네 (화이트) / 까베르네 소비뇽 (레드)","Jean Balmont Chardonnay / Cabernet Sauvignon","8.0 / 60.0"),
        ("켄달-잭슨 빈트너스 리저브 샤르도네 / 까베르네 소비뇽","Kendall-Jackson Vintner's Reserve","90.0"),
        ("Champagne",),
        ("장발몽 브륏","Jean Balmont Brut","60.0"),
        ("모엣 샹동","Moët & Chandon","120.0"),
        ("Highball",),
        ("짐빔 하이볼 (Glass)","Jim Beam Highball","8.0"),
        ("짐빔 버번 위스키 1병 + 토닉워터 6병","Jim Beam Bourbon + Tonic Water ×6","120.0"),
        ("Beer",),
        ("병맥주 코로나 / 스텔라 / 호가든 / 버드와이저 (330ml)","Bottle Beer","8.0"),
        ("코로나 / 버드와이저 5+1 세트","Corona / Budweiser 5+1 Set","40.0"),
        ("생맥주 스텔라 · 호가든 (330ml / 600ml)","Draft Stella Artois · Hoegaarden","8.0 / 14.0"),
        ("생맥주 한맥 (420ml / 2000ml)","Draft Hanmac","8.0 / 35.0"),
        ("Soju",),
        ("화요 (25°, 375ml)","Hwayo","35.0"),
    ])}
    </div>
    <p class="center note">메뉴와 가격은 사정에 따라 변경될 수 있습니다. 단체 예약 및 카페 가든 파티 문의: <a href="tel:{TEL_RAW}">{TEL}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="{INSTAGRAM['cafe'][0]}" target="_blank" rel="noopener">Instagram @marinapark_banpo</a> · <a href="https://marinapark.cafe" target="_blank" rel="noopener">카페 홈페이지 marinapark.cafe</a></p>
  </div>
</section>
{cafe_faq}
<section class="section cta-band"><div class="wrap center"><h2>Private parties at the cafe garden</h2><p>1층 카페 가든에서 10~30명 소규모 파티와 모임을 열어 보세요. · {CAFE_HOURS}</p><a class="btn btn-light" href="mailto:ficonvention@gmail.com?subject=%5B%EB%A7%88%EB%A6%AC%EB%82%98%ED%8C%8C%ED%81%AC%20%EC%B9%B4%ED%8E%98%5D%20%EC%98%88%EC%95%BD%20%EB%AC%B8%EC%9D%98&body=%EC%95%88%EB%85%95%ED%95%98%EC%84%B8%EC%9A%94%2C%20%EC%98%88%EC%95%BD%20%EB%AC%B8%EC%9D%98%EB%93%9C%EB%A6%BD%EB%8B%88%EB%8B%A4.%0A%0A%E2%96%A0%20%EC%9D%B4%EB%A6%84%20/%20%EC%97%B0%EB%9D%BD%EC%B2%98%3A%20%0A%E2%96%A0%20%ED%9D%AC%EB%A7%9D%20%EB%82%A0%EC%A7%9C%C2%B7%EC%8B%9C%EA%B0%84%3A%20%0A%E2%96%A0%20%EC%9D%B8%EC%9B%90%3A%20%0A%E2%96%A0%20%EB%AA%A8%EC%9E%84%20%EC%A2%85%EB%A5%98%28%EC%83%9D%EC%9D%BC%C2%B7%EB%8F%99%ED%98%B8%ED%9A%8C%C2%B7%EB%B8%8C%EB%9D%BC%EC%9D%B4%EB%8D%9C%EC%83%A4%EC%9B%8C%C2%B7%EC%86%8C%EB%AA%A8%EC%9E%84%20%EB%93%B1%29%3A%20%0A%E2%96%A0%20%EC%9A%94%EC%B2%AD%EC%82%AC%ED%95%AD%28%EC%BC%80%EC%9D%B4%ED%81%AC%20%EB%B0%98%EC%9E%85%2C%20%EB%8D%B0%EC%BD%94%20%EB%93%B1%29%3A%20%0A%0A%EA%B0%90%EC%82%AC%ED%95%A9%EB%8B%88%EB%8B%A4.">예약하기</a></div></section>
"""

# ======================================================================
# CONTACT
# ======================================================================
contact = f"""
{hero("mp-b29.jpg", "Marina Park", "Contact", "02-537-2440 · 서울 서초구 반포동 115-1 서래나루")}
<section class="section">
  <div class="wrap split contact-split">
    <div class="split-text">
      <h2>Contact us to turn your dream into a reality.</h2>
      <p>행사 종류, 희망 날짜, 예상 인원을 함께 적어 주시면 더 빠르게 안내드릴 수 있습니다.<br><span lang="en">Please send the event type, preferred date and number of guests — English inquiries welcome.</span></p>
      <div class="contact-card">
        <h3>MARINA PARK · 마리나파크</h3>
        <p>{ADDRESS_FULL}</p>
        <p>Tel: <a href="tel:{TEL_RAW}">{TEL}</a> &nbsp;(<span lang="en">{TEL_INTL}</span>)<br>Fax: {FAX}</p>
        <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
        <p>행사 문의 평일 10:00 – 18:00 · 마리나 카페 {CAFE_HOURS}</p>
        <p class="social-row">Instagram: <a href="{INSTAGRAM['cafe'][0]}" target="_blank" rel="noopener">카페 @marinapark_banpo</a> · <a href="{INSTAGRAM['event'][0]}" target="_blank" rel="noopener">이벤트 @marinaparkevent</a> · <a href="{INSTAGRAM['wedding'][0]}" target="_blank" rel="noopener">웨딩 @marinaparkwedding</a> · <a href="{FACEBOOK}" target="_blank" rel="noopener">Facebook</a></p>
      </div>
    </div>
    <form class="contact-form" id="contactForm" action="mailto:{EMAIL}" method="post" enctype="text/plain">
      <label>이름 / Name<input type="text" name="name" required></label>
      <label>이메일 / E-mail<input type="email" name="email" required></label>
      <label>연락처 / Phone<input type="tel" name="phone"></label>
      <label>행사 종류 / Event type
        <select name="event">
          <option>송년회 · 연말 모임 (Year-end party)</option>
          <option>Business Party / MICE</option>
          <option>Launching Party</option>
          <option>소규모 예식 · Wedding / Garden Wedding</option>
          <option>돌잔치 · 1st Party</option>
          <option>Cafe / Private Party</option>
          <option>기타 / Other</option>
        </select></label>
      <label>희망 날짜 / Date<input type="date" name="date"></label>
      <label>예상 인원 / Guests<input type="number" name="guests" min="1"></label>
      <label class="full">문의 내용 / Message<textarea name="message" rows="5" required></textarea></label>
      <button type="submit" class="btn full">Send</button>
      <p class="form-hint full">전송 버튼을 누르면 메일 앱이 열립니다. 메일 앱이 없으시면 <a href="mailto:{EMAIL}">{EMAIL}</a>로 직접 보내 주세요.</p>
    </form>
  </div>
</section>
{facts("Directions", "오시는 길",
  "마리나파크는 반포한강공원 서래나루 안에 있습니다.",
  [("주소", ADDRESS_FULL),
   ("지하철", "9호선 신반포역 · 3·7·9호선 고속터미널역 → 반포한강공원 서래나루 방면"),
   ("자가용", "반포한강공원 주차장 약 200대 · 행사 참석자 3시간 무료"),
   ("단체 버스", "반포한강공원 주차장 하차 (사전 안내)"),
   ("전화", f"{TEL} ({TEL_INTL})"),
   ("이메일", EMAIL)])}
<section class="map-section">
  <iframe title="마리나파크 위치 지도 — 서울 서초구 반포동 115-1" src="https://www.google.com/maps?q=%EC%84%9C%EC%9A%B8+%EC%84%9C%EC%B4%88%EA%B5%AC+%EB%B0%98%ED%8F%AC%EB%8F%99+115-1&output=embed" loading="lazy" allowfullscreen referrerpolicy="no-referrer-when-downgrade"></iframe>
</section>
"""

# ======================================================================
PAGES = {
    "index.html": ("Home", home, [home_faq_ld]),
    "about.html": ("About us", about, []),
    "business-party.html": ("Business Party · 송년회", business, [biz_faq_ld,
        service_ld("송년회·연말 모임·기업연회", "Year-end party / Corporate banquet", "서울 반포 한강 마리나파크 2층 컨벤션홀 100~300명 송년회·기업연회·갈라디너. 무대·LED·음향, 루프탑 애프터파티.", BASE_URL + "/business-party.html", "기업·단체", 300)]),
    "launching-party.html": ("Launching Party", launching, [launch_faq_ld,
        service_ld("런칭쇼·브랜드 프로모션", "Product launch event", "한강 전망 홀과 루프탑 포토존에서 진행하는 런칭쇼·미디어 행사.", BASE_URL + "/launching-party.html", "브랜드·기업")]),
    "first-party.html": ("1st Party · 돌잔치", first, [first_faq_ld,
        service_ld("돌잔치·가족 연회", "First birthday party", "반포 한강뷰 돌잔치 30명~100명 이상. 돌상·포토테이블·현수막·코스 식사.", BASE_URL + "/first-party.html", "가족")]),
    "wedding.html": ("Wedding · 소규모 예식", wedding, [wed_faq_ld,
        service_ld("소규모 예식·스몰웨딩·컨벤션 웨딩", "Wedding venue", "하객 50명대 가족 예식부터 300명 컨벤션 웨딩까지. 한강 통창 홀 + 가든, 하루 두 커플.", BASE_URL + "/wedding.html", "예비 신랑신부")]),
    "garden-wedding.html": ("Garden Wedding", garden, [garden_faq_ld,
        service_ld("가든웨딩·야외 결혼식", "Garden wedding", "3층 루프탑 화이트 가제보 가든 예식, 한강·서리풀 공원 뷰, 우천 시 실내 전환.", BASE_URL + "/garden-wedding.html", "예비 신랑신부")]),
    "cafe.html": ("Marina Cafe", cafe, [cafe_faq_ld]),
    "contact.html": ("Contact", contact, []),
}

ROBOTS = f"""User-agent: *
Allow: /

# AI / LLM crawlers — explicitly allowed
User-agent: GPTBot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: anthropic-ai
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Google-Extended
Allow: /
User-agent: Bingbot
Allow: /
User-agent: Yeti
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
"""

def sitemap():
    prio = {"index.html": "1.0", "business-party.html": "0.9", "wedding.html": "0.9", "first-party.html": "0.9", "garden-wedding.html": "0.8"}
    urls = []
    for f in PAGES:
        loc = BASE_URL + "/" + ("" if f == "index.html" else f)
        urls.append(f"  <url><loc>{loc}</loc><lastmod>{TODAY}</lastmod><changefreq>monthly</changefreq><priority>{prio.get(f, '0.7')}</priority></url>")
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n"

LLMS = f"""# 마리나파크 (Marina Park) — 반포 한강 연회장

> 서울 서초구 반포동 115-1, 반포한강공원 서래나루에 있는 연회·웨딩·MICE 베뉴.
> 송년회·연말 모임, 소규모 예식·가든웨딩, 돌잔치·가족 연회, 기업연회·런칭쇼·컨퍼런스 전문.
> 전화 {TEL} ({TEL_INTL}) · 이메일 {EMAIL} · 영어 상담 가능.

## 핵심 사실
- 위치: 서울 서초구 반포동 115-1 서래나루 (반포한강공원 내, 한강 바로 앞). 9호선 신반포역·고속터미널역 인근.
- 공간: 1층 마리나 카페({CAFE_HOURS}) · 2층 컨벤션홀(100~300명, 무대·LED·음향, 사면 한강 통창) · 3층 루프탑 가든(화이트 대리석 가제보, 잔디 버진로드).
- 수용 인원: 2층 홀 100명부터 최대 300명. 3층 가든은 리셉션·소규모 예식. 소규모 예식 최소 보증 50명. 돌잔치는 50명 룸부터 200명까지.
- 식사: 코스 디너 · 뷔페 · 핑거푸드 리셉션 · 프리드링크 패키지. 할랄·채식·논알코올 대응(국제 행사).
- 우천 시: 야외 가든 행사는 2층 실내 홀로 전환.
- 주차: 반포한강공원 주차장 약 200대, 행사 참석자 3시간 무료. 단체 버스 하차 가능.
- 식사 기준가: 코스 1인 10만원부터 (상세 견적 문의).
- 운영: 세빛섬 플로팅아일랜드 컨벤션(Floating Island Convention).

## 용도별 안내
### 송년회 · 연말 모임 ({BASE_URL}/business-party.html)
50명 소규모 모임부터 300명 전사 송년회까지(100~200명 최다). 2층 홀에서 식사+시상·경품 추첨·공연, 3층 루프탑 애프터파티. 11~12월 금요일 저녁은 조기 마감, 10~11월 예약 권장.
### 소규모 예식 · 스몰웨딩 ({BASE_URL}/wedding.html)
최소 보증 50명 가족 예식부터 100~300명 실내 홀 예식. 주말 12:00·18:00 두 타임, 하루 두 커플. 실내 예식 연중, 가든 예식 3월 말~6월·9~11월. 코스 1인 10만원부터. 주례 없는 예식·가족 식사형 스몰웨딩 가능. 한강뷰 신부대기실. 우천 시 2층 컨벤션홀로 이동.
### 가든웨딩 ({BASE_URL}/garden-wedding.html)
3층 루프탑 가든 야외 예식, 3월 말~6월·9~11월 (선셋 예식 추천), 피로연은 2층 홀.
### 돌잔치 ({BASE_URL}/first-party.html)
최소 50명(작은 룸) ~ 100명 이상·200명. 돌상·포토테이블 패키지 150만원, 현수막, 전문 사회자 20만원(선택), 5세 이하 식사 무료·유아 의자, 답례품 반입 가능. 주말 점심 2~3개월 전 예약 권장.
### 런칭쇼 · MICE ({BASE_URL}/launching-party.html)
무대·LED·음향, 포토월, 루프탑 애프터파티. 컨퍼런스·세미나는 극장식/클래스룸 세팅, 동시통역 부스 협의.
### 마리나 카페 ({BASE_URL}/cafe.html)
한강뷰 카페, 커피·티·디저트·피자·파스타·와인. 카페 가든 10~30명 소모임 예약.

## 페이지
- 홈: {BASE_URL}/
- 공간 안내: {BASE_URL}/about.html
- 문의·오시는 길: {BASE_URL}/contact.html

## 소셜
- Instagram 카페: {INSTAGRAM['cafe'][0]}
- Instagram 이벤트: {INSTAGRAM['event'][0]}
- Instagram 웨딩: {INSTAGRAM['wedding'][0]}
- Facebook: {FACEBOOK}

## English summary
Marina Park is a riverside event venue at Seoraenaru, Banpo Han River Park, Seoul (115-1 Banpo-dong, Seocho-gu). Ground-floor cafe (daily 10:00–22:00), 2nd-floor convention hall for 100–300 guests with stage, LED and sound, and a 3rd-floor rooftop garden with a white marble gazebo. Year-end parties, corporate galas and conferences, intimate weddings and garden weddings (two couples per day, indoor rain backup), first-birthday celebrations (50–200 guests), product launches. Course menus from KRW 100,000 per person; halal and vegetarian menus available. Parking for about 200 cars, free for 3 hours. Tel +82-2-537-2440, {EMAIL}.
"""

if __name__ == "__main__":
    for fname, (title, body, extra) in PAGES.items():
        with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
            f.write(page(fname, title, body, extra))
        print("wrote", fname)
    open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8").write(ROBOTS)
    open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8").write(sitemap())
    open(os.path.join(OUT, "llms.txt"), "w", encoding="utf-8").write(LLMS)
    print("wrote robots.txt sitemap.xml llms.txt")
