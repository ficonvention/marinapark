# -*- coding: utf-8 -*-
"""Marina Park static site generator.
Run: python3 build.py  -> writes *.html into this folder.
Images are currently linked from the Wix CDN; replace with /images/ files later.
"""
import os, html

OUT = os.path.dirname(os.path.abspath(__file__))

def wix(media_id, w=1600, h=1067):
    return f"https://static.wixstatic.com/media/{media_id}/v1/fill/w_{w},h_{h},al_c,q_85/{media_id}"

# ---------- shared data ----------
SITE = "Marina Park"
ADDRESS = "서울 서초구 반포동 115-1"
TEL = "02-596-2440"
FAX = "02-537-2499"
EMAIL = "ficonvention@gmail.com"
INSTAGRAM = "https://www.instagram.com/marinaparkwedding"
FACEBOOK = "https://www.facebook.com/Floatingisland1"

NAV = [
    ("index.html", "Home", [("about.html", "About us")]),
    ("business-party.html", "Business Party", []),
    ("launching-party.html", "Launching Party", []),
    ("first-party.html", "1st Party", []),
    ("wedding.html", "Wedding", [("garden-wedding.html", "Garden Wedding")]),
    ("cafe.html", "Marina Cafe", [("cafe.html#menu", "Cafe Menu")]),
    ("contact.html", "Contact", []),
]

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

def page(current, title, body, hero=None, desc="마리나파크 — 한강 위에서 만나는 웨딩, 기업연회, MICE 이벤트, 돌잔치, 마리나 카페. 서울 서초구 반포 서래나루."):
    hero_cls = " has-hero" if hero else ""
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} | Marinapark</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:site_name" content="Marinapark">
<meta property="og:title" content="{html.escape(title)} | Marinapark">
<meta property="og:type" content="website">
<meta property="og:image" content="{wix('2649b2_f1c4946dee4f4dbcb7d5237ec2b0e743~mv2.jpeg', 1200, 630)}">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Noto+Sans+KR:wght@300;400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css?v=2">
</head>
<body class="page-{current.replace('.html','')}{hero_cls}">
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html"><span class="brand-main">MARINA PARK</span><span class="brand-sub">마리나파크</span></a>
    <button class="nav-toggle" aria-label="메뉴 열기" aria-expanded="false"><span></span><span></span><span></span></button>
    <nav class="site-nav"><ul>
{nav_html(current)}
    </ul></nav>
  </div>
</header>
{body}
<footer class="site-footer">
  <div class="wrap footer-grid">
    <div class="f-col">
      <div class="f-brand">MARINA PARK</div>
      <p>{ADDRESS}</p>
      <p>Tel: <a href="tel:025962440">{TEL}</a> &nbsp;|&nbsp; Fax: {FAX}</p>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
    <div class="f-col f-links">
      <a href="about.html">About us</a>
      <a href="business-party.html">Business Party</a>
      <a href="launching-party.html">Launching Party</a>
      <a href="first-party.html">1st Party</a>
      <a href="wedding.html">Wedding</a>
      <a href="garden-wedding.html">Garden Wedding</a>
      <a href="cafe.html">Marina Cafe</a>
      <a href="contact.html">Contact</a>
    </div>
    <div class="f-col f-social">
      <a href="{INSTAGRAM}" target="_blank" rel="noopener" aria-label="Instagram"><svg viewBox="0 0 24 24"><path d="M12 2.2c3.2 0 3.6 0 4.9.1 3.3.1 4.8 1.7 4.9 4.9.1 1.3.1 1.6.1 4.8s0 3.6-.1 4.8c-.1 3.2-1.7 4.8-4.9 4.9-1.3.1-1.6.1-4.9.1s-3.6 0-4.8-.1c-3.3-.1-4.8-1.7-4.9-4.9C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.8C2.4 3.9 4 2.4 7.2 2.3c1.2-.1 1.6-.1 4.8-.1zM12 0C8.7 0 8.3 0 7.1.1 2.7.3.3 2.7.1 7.1 0 8.3 0 8.7 0 12s0 3.7.1 4.9c.2 4.4 2.6 6.8 7 7 1.2.1 1.6.1 4.9.1s3.7 0 4.9-.1c4.4-.2 6.8-2.6 7-7 .1-1.2.1-1.6.1-4.9s0-3.7-.1-4.9c-.2-4.4-2.6-6.8-7-7C15.7 0 15.3 0 12 0zm0 5.8a6.2 6.2 0 1 0 0 12.4 6.2 6.2 0 0 0 0-12.4zM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm6.4-11.8a1.4 1.4 0 1 0 0 2.9 1.4 1.4 0 0 0 0-2.9z"/></svg></a>
      <a href="{FACEBOOK}" target="_blank" rel="noopener" aria-label="Facebook"><svg viewBox="0 0 24 24"><path d="M24 12a12 12 0 1 0-13.9 11.9v-8.4H7.1V12h3V9.4c0-3 1.8-4.7 4.5-4.7 1.3 0 2.7.2 2.7.2v3h-1.5c-1.5 0-2 .9-2 1.9V12h3.3l-.5 3.5h-2.8v8.4A12 12 0 0 0 24 12z"/></svg></a>
    </div>
  </div>
  <div class="wrap copyright">© 2026 Marina Park. All rights reserved.</div>
</footer>
<div class="lightbox" id="lightbox" hidden><button class="lb-close" aria-label="닫기">&times;</button><button class="lb-prev" aria-label="이전">&#8249;</button><img alt=""><button class="lb-next" aria-label="다음">&#8250;</button></div>
<script src="js/main.js"></script>
</body>
</html>
"""

def gallery(ids, cls="gallery"):
    """ids: list of (media_id, w, h) tuples -> masonry-ish grid, each opens lightbox"""
    out = [f'<div class="{cls}">']
    for mid, w, h in ids:
        thumb = wix(mid, 900, 600 if w >= h else 1200)
        full = wix(mid, 1800, 1200 if w >= h else 2400)
        orient = "landscape" if w >= h else "portrait"
        out.append(f'<a class="g-item {orient}" href="{full}" data-lightbox><img src="{thumb}" loading="lazy" alt="Marina Park"></a>')
    out.append('</div>')
    return "\n".join(out)

# ---------- HOME ----------
HERO = "2649b2_60058f1b65d549229010f461f06b7d2b~mv2_d_4146_2764_s_4_2.jpg"
home = f"""
<section class="hero" style="background-image:url('{wix(HERO, 1920, 1280)}')">
  <div class="hero-inner">
    <p class="eyebrow">Marina Park</p>
    <h1>Creating Unforgettable<br>Memories</h1>
    <p class="lead">한강 위에서 만나는 특별한 하루 — 웨딩, 파티, MICE 이벤트</p>
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
        <img src="{wix('2649b2_f58fea24227f40d0ac2b928e00be2ac5~mv2_d_4811_3202_s_4_2.jpg', 900, 640)}" loading="lazy" alt="Business Party">
        <h3>Business Party</h3><p>기업연회 · 가족연회 · 모임</p>
      </a>
      <a class="service" href="business-party.html">
        <img src="{wix('2649b2_2e0824818c1549558216f89a30024150~mv2_d_4032_1960_s_2.jpg', 900, 640)}" loading="lazy" alt="MICE Events">
        <h3>MICE Events</h3><p>컨퍼런스 · 세미나 · 단체행사</p>
      </a>
      <a class="service" href="launching-party.html">
        <img src="{wix('2649b2_c95dc8b4388643c6a46599f9b158c4b4~mv2_d_4769_3174_s_4_2.jpg', 900, 640)}" loading="lazy" alt="Launching">
        <h3>Launching</h3><p>런칭쇼 · 프로모션 · 미디어 행사</p>
      </a>
      <a class="service" href="wedding.html">
        <img src="{wix('2649b2_f1c4946dee4f4dbcb7d5237ec2b0e743~mv2.jpeg', 900, 640)}" loading="lazy" alt="Wedding">
        <h3>Wedding</h3><p>컨벤션 웨딩 · 가든 웨딩</p>
      </a>
    </div>
  </div>
</section>

<section class="section intro-split">
  <div class="wrap split">
    <div class="split-img"><img src="{wix('2649b2_84591f625adb41e695567464f8fa76f0~mv2_d_5760_3840_s_4_2.jpg', 1100, 733)}" loading="lazy" alt="Marina Park 전경"></div>
    <div class="split-text">
      <p class="eyebrow">Han River · Seoraenaru</p>
      <h2>한강과 서리풀 공원이<br>어우러진 공간</h2>
      <p>마리나 파크는 반포 서래나루에 위치한 복합 연회 공간입니다. 1층 마리나 카페, 2층 350석 규모의 컨벤션, 3층 화이트 가제보 가든까지 — 한강의 정취를 그대로 담은 세 개의 공간에서 비즈니스 행사부터 웨딩까지 모든 순간을 준비합니다.</p>
      <a class="btn" href="about.html">About Marina Park</a>
      <p class="contact-line"><a href="tel:025962440">Tel {TEL}</a></p>
    </div>
  </div>
</section>

<section class="section gallery-teaser">
  <div class="wrap">
    <p class="eyebrow center">Event Gallery</p>
    <h2 class="center">Unforgettable Memories</h2>
    {gallery([
        ("2649b2_b13801a7f8d04061a365a1e6a05f88e9~mv2.jpg", 3, 2),
        ("2649b2_37fdd5efdaa3408dabf8f72164a53c04~mv2.jpg", 4, 3),
        ("2649b2_3246882a53704939a0e96ecdf9d94e5b~mv2_d_5760_3840_s_4_2.jpg", 3, 2),
        ("2649b2_256b3a1192ce4999b2c9cdaa52cba08f~mv2_d_5760_1657_s_2.jpg", 3, 1),
        ("2649b2_322b463071914e24b0db2a7303ba4ec4~mv2.jpeg", 4, 3),
        ("2649b2_366cf79f6c2a44fdbcd60faf77bb2b05~mv2_d_4176_2784_s_4_2.jpg", 3, 2),
    ], "gallery cols-3")}
    <p class="center"><a class="btn" href="business-party.html">Discover Party</a></p>
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>Contact us to turn your dream into a reality</h2>
    <p>행사 일정과 인원을 알려주시면 맞춤 제안을 드립니다.</p>
    <a class="btn btn-light" href="contact.html">Contact</a>
    <a class="btn btn-outline" href="mailto:{EMAIL}">E-mail</a>
  </div>
</section>
"""

# ---------- ABOUT ----------
about = f"""
<section class="page-hero" style="background-image:url('{wix('2649b2_c87b628eab2a43f792de898f5d610861~mv2.jpg', 1920, 1000)}')">
  <div class="wrap"><p class="eyebrow">Marina Park</p><h1>About us</h1></div>
</section>

<section class="section">
  <div class="wrap floors">
    <article class="floor">
      <div class="floor-img"><img src="{wix('2649b2_0eba81bbe25c4fb393a391de7f8e4517~mv2.jpg', 1000, 667)}" loading="lazy" alt="1F Marina Cafe"></div>
      <div class="floor-text">
        <p class="eyebrow">1F</p><h2>Marina Cafe</h2>
        <p>마리나 파크는 반포 서래나루에 위치하고 있으며 1층은 카페로, 이국적인 분위기에서 간단하게 차와 커피, 피자와 파스타, 와인 등을 즐길 수 있는 공간으로 구성되어 있습니다. 마리나 파크 1층 가든에서는 작은 파티나 모임을 즐길 수 있는 여유 있는 공간입니다.</p>
        <a class="btn" href="cafe.html">Cafe Menu</a>
      </div>
    </article>
    <article class="floor reverse">
      <div class="floor-img"><img src="{wix('2649b2_dc09fa2843df4bdf9c67640d80228780~mv2_d_3264_2448_s_4_2.jpg', 1000, 750)}" loading="lazy" alt="2F Convention"></div>
      <div class="floor-text">
        <p class="eyebrow">2F</p><h2>Convention</h2>
        <p>2층은 기업연회, 런칭쇼, 마이스 단체행사, 가족연회, 지인들과의 모임 등을 하실 수 있는 공간으로 350석 세팅이 가능합니다. 무대, 영상장비, 음향장치를 모두 갖추고 있으며, 사면이 통유리로 되어 있어 한강의 아름다운 정취를 마음껏 즐기실 수 있습니다.</p>
        <a class="btn" href="business-party.html">Business Party</a>
      </div>
    </article>
    <article class="floor">
      <div class="floor-img"><img src="{wix('2649b2_967bd6b1f14c4a08a7b51daad0fb962f~mv2.jpeg', 1000, 834)}" loading="lazy" alt="3F Garden"></div>
      <div class="floor-text">
        <p class="eyebrow">3F</p><h2>Garden</h2>
        <p>대리석 단상 위로 화이트 대리석 가제보가 있는 마리나 파크의 가든은 한강이 그대로 내려다보이며, 서리풀 공원과 가든의 조경이 함께 어우러진 환상적인 공간입니다. 칵테일 파티, 연회 전 식전 리셉션, 가든 예식을 하기에도 좋은 공간입니다.</p>
        <a class="btn" href="garden-wedding.html">Garden Wedding</a>
      </div>
    </article>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <h2 class="center">Turning a Vision into Reality</h2>
    <p class="center sub">Anniversary Flower · Romantic Garden Wedding · A Perfectionist on Every Detail</p>
    {gallery([
        ("2649b2_1daa0bb1284345b7b91e1ef9d47f9f71~mv2.jpeg", 6, 5),
        ("2649b2_4d4ad3ea74e14ec3ae098e80aa1cb928~mv2.jpg", 3, 4),
        ("2649b2_322b463071914e24b0db2a7303ba4ec4~mv2.jpeg", 4, 3),
    ], "gallery cols-3")}
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>This is a great place for your special day</h2>
    <a class="btn btn-light" href="mailto:{EMAIL}">Book a place</a>
  </div>
</section>
"""

# ---------- BUSINESS PARTY / MICE ----------
business = f"""
<section class="page-hero" style="background-image:url('{wix('2649b2_2e0824818c1549558216f89a30024150~mv2_d_4032_1960_s_2.jpg', 1920, 933)}')">
  <div class="wrap"><p class="eyebrow">Marina Park</p><h1>Business Party / MICE Event</h1></div>
</section>
<section class="section">
  <div class="wrap">
    <p class="center sub">기업연회, 컨퍼런스, 세미나, 시상식, 단체행사 — 한강이 보이는 2층 컨벤션에서 350석 규모까지 진행하실 수 있습니다.</p>
    {gallery([
        ("2649b2_2550e0e1deda4df8a29c7eb8a3ae9d1e~mv2.png", 7, 4),
        ("2649b2_636984f857884ec5862938336596d24b~mv2.png", 3, 2),
        ("2649b2_ffa6948050474d00a60c19183833a48e~mv2.jpg", 2, 1),
        ("2649b2_c8e0b565869f450eb0e3f2077065fe64~mv2.jpg", 1, 2),
        ("2649b2_72c455d453074068a52a1ee11fc9a2c1~mv2.jpg", 4, 3),
        ("2649b2_dad8a86f44a54addbec2938ead2ed497~mv2.jpg", 4, 3),
        ("2649b2_cfd0ac9a9e7847968b4decf60ab855a1~mv2_d_4032_1960_s_2.jpg", 2, 1),
        ("2649b2_2e13c691e36f4f9f975aa6e7f7489290~mv2_d_6768_3936_s_4_2.jpg", 5, 3),
        ("2649b2_d926ed3ab4c84454974a1f0588fb6d5a~mv2.jpg", 4, 3),
        ("2649b2_1f4e534b009a455795154239a1f1f044~mv2.png", 5, 3),
        ("2649b2_87fc26bd77764513b5782db4fd3e94bd~mv2_d_1220_1519_s_2.jpg", 4, 5),
        ("2649b2_ccfffc11c15e4e73b6c97e18c1b5dcb2~mv2.png", 5, 3),
        ("2649b2_e40fee1083d24a0d9f6f830c052fe4a3~mv2.png", 3, 2),
        ("2649b2_2e0824818c1549558216f89a30024150~mv2_d_4032_1960_s_2.jpg", 2, 1),
        ("2649b2_6bb045be39ae450a9744388421bb42ac~mv2.jpg", 2, 1),
        ("2649b2_c20265e04ec5477c9fbe2f145cf747e3~mv2_d_4176_2784_s_4_2.jpg", 3, 2),
        ("2649b2_9f39b5e2f8ce494f86810921c4241890~mv2.png", 4, 3),
        ("2649b2_c61315fdb1d8465daf24e08a05ebad93~mv2.jpeg", 3, 2),
        ("2649b2_60c1bdb7648c466fa92327361f19d98c~mv2.jpg", 1, 2),
        ("2649b2_4ad430a3c6584cfda09f00569257fcfe~mv2.png", 3, 2),
        ("2649b2_c15a83d4f31b48769862324403dcd04b~mv2.png", 4, 3),
        ("2649b2_f374c3c359a34cebbeb7f2ca94d1b021~mv2.png", 5, 3),
        ("2649b2_349a109dd0544dc68648d9f7df86de79~mv2.jpg", 4, 3),
        ("2649b2_f58fea24227f40d0ac2b928e00be2ac5~mv2_d_4811_3202_s_4_2.jpg", 3, 2),
        ("2649b2_fc09e9d6e3b84d0b8ed413a4df1115dd~mv2_d_4176_2784_s_4_2.jpg", 3, 2),
        ("2649b2_37a4bf3b822742a89b42fac6e8663687~mv2_d_4117_2745_s_4_2.jpg", 3, 2),
    ])}
  </div>
</section>
<section class="section cta-band"><div class="wrap center"><h2>Turning a Vision into Reality</h2><a class="btn btn-light" href="contact.html">행사 문의</a></div></section>
"""

# ---------- LAUNCHING PARTY ----------
launching = f"""
<section class="page-hero" style="background-image:url('{wix('2649b2_c95dc8b4388643c6a46599f9b158c4b4~mv2_d_4769_3174_s_4_2.jpg', 1920, 1100)}')">
  <div class="wrap"><p class="eyebrow">Marina Park</p><h1>Launching Party</h1></div>
</section>
<section class="section">
  <div class="wrap">
    <p class="center sub">신제품 런칭쇼, 브랜드 프로모션, 미디어 행사 — 무대·영상·음향 장비를 갖춘 공간에서 브랜드의 첫 순간을 연출합니다.</p>
    {gallery([
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
        ("2649b2_0c4cca6b5557431a9ccbcb9b3e5eafb9~mv2_d_4044_2696_s_4_2.jpg", 3, 2),
        ("2649b2_d682cebc68084792af51e925ca719ce5~mv2_d_4176_2784_s_4_2.jpg", 3, 2),
        ("2649b2_738fa7efc11f4f30923c6a83a75d2fd5~mv2_d_4176_2784_s_4_2.jpg", 3, 2),
        ("2649b2_366cf79f6c2a44fdbcd60faf77bb2b05~mv2_d_4176_2784_s_4_2.jpg", 3, 2),
        ("2649b2_f139744468aa4bfda560aaf595d14b08~mv2_d_2784_4176_s_4_2.jpg", 2, 3),
        ("2649b2_0cacda5967ae4e07b3c05898e41c6c26~mv2_d_4176_2784_s_4_2.jpg", 3, 2),
        ("2649b2_3daed4a68502430e93e942a2f421ca8d~mv2_d_4928_3280_s_4_2.jpg", 3, 2),
        ("2649b2_4d0354b1fa314448a52abed77c7f96ec~mv2_d_4176_2784_s_4_2.jpg", 3, 2),
        ("2649b2_4237e242dd12477fa8b06c294e008ace~mv2_d_2048_2048_s_2.jpg", 1, 1),
        ("2649b2_c1deb13d3e2a45c5a53315a9b29d8cb5~mv2_d_4032_3024_s_4_2.jpg", 4, 3),
        ("2649b2_94fc19e636f747f395465359d70ab42c~mv2_d_4032_3024_s_4_2.jpg", 4, 3),
        ("2649b2_ba92704de5c44e9c8f7cf9b21b9223cc~mv2.jpg", 3, 4),
        ("2649b2_0ef3c070b53d42ae9ebd6dc2f497b143~mv2.jpg", 3, 4),
    ])}
  </div>
</section>
<section class="section cta-band"><div class="wrap center"><h2>Launch your brand on the Han River</h2><a class="btn btn-light" href="contact.html">행사 문의</a></div></section>
"""

# ---------- 1st PARTY ----------
first = f"""
<section class="page-hero" style="background-image:url('{wix('2649b2_27aac57c162e474eb1debfcef01fee8c~mv2.jpg', 1920, 1300)}')">
  <div class="wrap"><p class="eyebrow">Marina Park</p><h1>1st Party</h1></div>
</section>
<section class="section">
  <div class="wrap">
    <p class="center sub">아이의 첫 번째 생일, 한강이 보이는 공간에서 가족과 함께하는 돌잔치 — 데코레이션부터 식사까지 맞춤으로 준비합니다.</p>
    {gallery([
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
        ("2649b2_37fdd5efdaa3408dabf8f72164a53c04~mv2.jpg", 4, 3),
        ("2649b2_26654215ffe04ac08d029f33207d8b1a~mv2.jpg", 3, 4),
        ("2649b2_c537efda88cc4316bb161b99c910f3e1~mv2.jpg", 4, 3),
        ("2649b2_b0a27021a5e2480bb624dd050178f88a~mv2.jpg", 4, 3),
        ("2649b2_9a69d241636f420f9f74f8c549c596ec~mv2.jpg", 4, 3),
        ("2649b2_d10aace456fc4cf5a6cc299301d883d9~mv2.jpg", 4, 3),
    ])}
  </div>
</section>
<section class="section cta-band"><div class="wrap center"><h2>A day to remember for the whole family</h2><a class="btn btn-light" href="contact.html">돌잔치 문의</a></div></section>
"""

# ---------- WEDDING ----------
wedding = f"""
<section class="page-hero tall" style="background-image:url('{wix('2649b2_9066f5fd9a0c412aab686c19d06b9327~mv2.jpg', 1920, 1270)}')">
  <div class="wrap"><p class="eyebrow">Marina Park</p><h1>Marina Park Wedding</h1></div>
</section>
<section class="section">
  <div class="wrap narrow prose">
    <p>마리나 파크는 컨벤션 동시 웨딩과 야외 가든웨딩을 진행합니다.</p>
    <p>플로리스트와의 컨셉 미팅을 통해 준비되는 웨딩 플라워 데코레이션과 웨딩 연출, 하루에 두 커플만 진행하는 여유로운 시간 간격과 서리풀 공원을 배경으로 한강 위에서 진행되는 격조 있는 예식은 새로운 출발을 앞둔 커플에게 소중하고 특별한 추억으로 남을 것입니다.</p>
    <p>국제연회를 진행해 온 감각 있는 스타일리스트가 함께하는 마리나 파크 웨딩은 최고의 셰프가 준비하는 디너와 함께 더욱 빛을 발할 것입니다.</p>
    <p class="center cta-inline"><a class="btn" href="tel:025962440">문의: {TEL}</a> <a class="btn btn-outline-dark" href="mailto:{EMAIL}">메일 문의 (E-mail inquiry)</a></p>
  </div>
</section>
<section class="section alt">
  <div class="wrap">
    {gallery([
        ("2649b2_522621181b864e16bb74300bc6955941~mv2.jpg", 3, 4),
        ("2649b2_300b9e0590eb4821bfec14efc6ae2166~mv2_d_3633_5615_s_4_2.jpg", 2, 3),
        ("2649b2_eba15c8dce214569a62990393a60b952~mv2_d_3744_5616_s_4_2.jpg", 2, 3),
        ("2649b2_832edd7144b84532b22a0636b783acc6~mv2_d_3597_5395_s_4_2.jpg", 2, 3),
        ("2649b2_3d8136d2c0d84f348d46063170aaf143~mv2_d_5616_3744_s_4_2.jpg", 3, 2),
        ("2649b2_9066f5fd9a0c412aab686c19d06b9327~mv2.jpg", 3, 2),
        ("2649b2_d68896f967204194a87c7acbefe756ec~mv2_d_3553_5236_s_4_2.jpg", 2, 3),
        ("2649b2_2f177478a1e045618322a26a1be7732c~mv2.jpg", 3, 2),
        ("2649b2_27d67eda4d144f21a335e39c40b8f2d8~mv2.jpg", 3, 2),
        ("8bb438_ec9a72099f9648dfb08d9412804a464a~mv2_d_3000_2000_s_2.jpg", 3, 2),
        ("2649b2_261c82e221a94598bee29cdb27617856~mv2_d_3611_5320_s_4_2.jpg", 2, 3),
        ("2649b2_561ae3e3301944bb996a87a90e21d09c~mv2_d_3660_5362_s_4_2.jpg", 2, 3),
        ("2649b2_8a611ea075824cbdaaed9983343a7865~mv2_d_3588_5382_s_4_2.jpg", 2, 3),
    ])}
    <p class="center"><a class="btn" href="garden-wedding.html">Garden Wedding 보기</a></p>
  </div>
</section>
"""

# ---------- GARDEN WEDDING ----------
garden = f"""
<section class="page-hero tall" style="background-image:url('{wix('2649b2_f1c4946dee4f4dbcb7d5237ec2b0e743~mv2.jpeg', 1920, 1280)}')">
  <div class="wrap"><p class="eyebrow">Marina Park</p><h1>Garden Wedding</h1><p class="lead">Making Dreams Come True</p></div>
</section>
<section class="section">
  <div class="wrap">
    <p class="center sub">한강과 서리풀 공원을 배경으로, 화이트 대리석 가제보 아래에서 진행되는 로맨틱 가든 웨딩.</p>
    {gallery([
        ("2649b2_5ce8952e336d431c8a9f170eb5929234~mv2.png", 4, 3),
        ("2649b2_2443090602d440b7b48d46a629396a7c~mv2_d_2539_1683_s_2.jpg", 3, 2),
        ("2649b2_c143d015d0454bed82088c76f228a8dc~mv2.jpg", 5, 3),
        ("2649b2_b13801a7f8d04061a365a1e6a05f88e9~mv2.jpg", 3, 2),
        ("2649b2_5472b3b50c3b4aac9663aa8ae54ba1b9~mv2.jpg", 3, 2),
        ("2649b2_f1c4946dee4f4dbcb7d5237ec2b0e743~mv2.jpeg", 3, 2),
        ("2649b2_d5db0a3018b14303b99c0b6d64b102f9~mv2.jpg", 3, 2),
        ("2649b2_df61750e0ad14373b4578897599542c4~mv2.jpg", 2, 3),
        ("2649b2_334aea7b16464fd78967881c4fb4bbf3~mv2.jpg", 2, 1),
        ("2649b2_2071f7b5e2af4218a81d5b4bf788f7ce~mv2.jpg", 3, 2),
        ("2649b2_3d8b3f8289414b92bb090bd13e2a3cc7~mv2.jpg", 3, 2),
        ("2649b2_392ec9148cb14e06a61de81645e5d781~mv2.jpg", 3, 2),
        ("2649b2_5154bb08d3494242b92727bca3ce57b0~mv2.jpg", 2, 3),
        ("2649b2_0b6846f19ba34bd09f5434d57fa4ea15~mv2.jpg", 3, 2),
        ("2649b2_29df86c4408041e9a880f1a3ced79127~mv2.jpg", 2, 3),
        ("2649b2_fbc38110626f47f1920a4e30574c75c6~mv2.jpg", 3, 2),
        ("2649b2_27ea47742fe7483b8fb4b03de0c4f0fe~mv2.jpg", 3, 2),
        ("2649b2_05448bba1a6a412a86261e4f8ac3fa3c~mv2.jpeg", 1, 1),
        ("2649b2_d3d703bbf514444fbb81a52c6a153da8~mv2.jpg", 1, 1),
        ("2649b2_a170c69162b34c87af8cb43680b1d836f003.jpg", 16, 9),
        ("2649b2_0bc81bf517e94690b2ee2cb2f02e0258~mv2.jpeg", 3, 2),
        ("2649b2_322b463071914e24b0db2a7303ba4ec4~mv2.jpeg", 4, 3),
        ("2649b2_e9885f9c949647e394df146dfae49c3d~mv2.jpeg", 3, 2),
        ("2649b2_ff12730b16034114b9b8561eea9db8bb~mv2.jpeg", 2, 3),
        ("2649b2_4d4ad3ea74e14ec3ae098e80aa1cb928~mv2.jpg", 3, 4),
    ])}
  </div>
</section>
<section class="section cta-band"><div class="wrap center"><h2>Turning a Vision into Reality</h2><p>Anniversary Flower · Romantic Garden Wedding · A Perfectionist on Every Detail</p><a class="btn btn-light" href="contact.html">웨딩 상담 문의</a></div></section>
"""

# ---------- CAFE ----------
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

cafe = f"""
<section class="page-hero" style="background-image:url('{wix('2649b2_256b3a1192ce4999b2c9cdaa52cba08f~mv2_d_5760_1657_s_2.jpg', 1920, 552)}')">
  <div class="wrap"><p class="eyebrow">1F</p><h1>Marina Park Cafe</h1></div>
</section>
<section class="section" id="menu">
  <div class="wrap">
    <p class="center sub">한강이 보이는 1층 카페에서 커피와 티, 디저트, 피자와 파스타, 와인을 즐기실 수 있습니다. 가격 단위: 천 원 (예: 4.5 = 4,500원)</p>
    <div class="menu-grid">
    {menu("Coffee", "Hot / Iced", [
        ("에스프레소","Espresso","3.5"),
        ("에스프레소 마끼아또","Espresso Macchiato","3.8"),
        ("아메리카노","Americano","4.0 / 4.5"),
        ("카푸치노","Cappuccino","4.5 / 5.0"),
        ("카페라떼","Cafe Latte","4.5 / 5.0"),
        ("바닐라 라떼","Vanilla Latte","5.0 / 5.5"),
        ("카라멜 라떼","Caramel Latte","5.0 / 5.5"),
        ("돌체라떼","Dolce Latte","5.0 / 5.5"),
        ("카페모카","Cafe Mocha","5.0 / 5.5"),
        ("카라멜 마끼아또","Caramel Macchiato","5.0 / 5.5"),
        ("민트 모카","Mint Mocha","5.0 / 5.5"),
        ("Dutch Coffee",),
        ("콜드브루","Cold Brew","4.5 / 5.0"),
        ("브루라떼","Brew Latte","5.0 / 5.5"),
        ("에스프레소 샷 추가","Extra shot","+0.5"),
    ])}
    {menu("Tea", "Hot / Iced", [
        ("얼그레이 / 다즐링 / 잉글리쉬 블랙퍼스트","Earl Grey / Darjeeling / English Breakfast","5.0"),
        ("허브차 (페퍼민트 / 카모마일 / 레몬스카이 / 루이보스 바닐라 / 레드베리)","Herbal Tea","5.0"),
        ("그린티","Green Tea","5.0"),
        ("깔라만시 티","Kalamansi Tea","5.0"),
        ("유자 티","Citron Tea","5.0"),
        ("자몽 티","Grapefruit Tea","5.0"),
        ("밀크 티","Milk Tea","5.5"),
        ("그린티 라떼","Green Tea Latte","5.5"),
    ])}
    {menu("Beverage", "Hot / Iced", [
        ("초콜릿","Hot Chocolate / Iced Chocolate","4.5 / 5.0"),
        ("민트초코","Mint Choco","5.0 / 5.5"),
        ("아이스 티 (레몬 / 복숭아)","Iced Tea (Lemon / Peach)","5.0"),
        ("에이드 (레몬 / 자몽 / 청포도)","Ade (Lemon / Grapefruit / Green Grape)","5.0"),
        ("이탈리안 소다 (라즈베리 / 블루베리 / 스트로베리 / 패션후르츠)","Italian Soda","5.0"),
        ("Blended",),
        ("스무디 (스트로베리 / 망고 / 믹스베리)","Smoothie","6.0"),
        ("요거트 스무디 (플레인 / 스트로베리 / 망고 / 베리믹스)","Yogurt Smoothie","6.0"),
        ("프라페 (리얼쿠키 / 그린티 / 자바칩 / 민트초코)","Frappe","7.0"),
        ("Fruit",),
        ("생과일 주스 (키위 / 키위바나나 / 토마토)","Fresh Juice","7.0"),
    ])}
    {menu("Bakery & Dessert", "", [
        ("베이글 (플레인)","Bagel (Plain)","3.0"),
        ("베이글 (블루베리 / 어니언 / 갈릭)","Bagel","4.0"),
        ("베이글 (치즈) · 크림치즈 추가 +0.7","Bagel (Cheese)","5.0"),
        ("스콘","Scone","4.0"),
        ("크로크 무슈","Croque Monsieur","5.0"),
        ("허니 버터 브레드","Honey Butter Bread","6.0"),
        ("조각케이크 (바나나 플람베 / 블랙 포레스트 / 더블 치즈 스트로베리 / 이탈리아노 티라미수 / 뉴욕치즈)","Piece of Cake","6.0"),
        ("Summer Dessert",),
        ("오리지널 팥빙수","Original Red Bean Bingsu","8.0"),
        ("망고빙수","Mango Bingsu","10.0"),
    ])}
    {menu("Food", "", [
        ("Pizza",),
        ("고르곤졸라","Gorgonzola Pizza","16.0"),
        ("마르게리따","Margherita Pizza","16.0"),
        ("페페로니","Pepperoni Pizza","16.0"),
        ("베이컨 포테이토","Bacon Potato Pizza","16.0"),
        ("Cutlet & Plates",),
        ("등심돈까스","Sirloin Cutlet","14.0"),
        ("치즈돈까스","Cheese Cutlet","15.0"),
        ("찹스테이크","Chop Steak","29.0"),
        ("볶음밥 (김치 / 새우)","Fried Rice (Kimchi / Shrimp)","14.0"),
        ("감자튀김 + 새우춘권","French Fries + Shrimp Spring Rolls","8.0"),
        ("버팔로 윙 & 칩스","Buffalo Wings & Chips","16.0"),
        ("쉬림프 앤 칩스","Shrimp & Chips","16.0"),
        ("연어샐러드","Salmon Salad","16.0"),
    ])}
    {menu("Drinks / Liquor", "Glass / Bottle", [
        ("White Wine",),
        ("깔리쟈 CVV","Caliza CVV","7.0 / 45.0"),
        ("켄달-잭슨 빈트너스 리저브 샤도네이","Kendall-Jackson Vintner's Reserve Chardonnay","90.0"),
        ("Red Wine",),
        ("깔리쟈 MST","Caliza MST","7.0 / 45.0"),
        ("토레스 마스 라 플라냐 카베르네 소비뇽 블랙 라벨","Torres Mas La Plana Cabernet Sauvignon","120.0"),
        ("Champagne",),
        ("세테카시네 프로세코 브륏","Sette Casine Prosecco Brut","50.0"),
        ("모엣 샹동","Moët & Chandon","120.0"),
        ("Draft Beer",),
        ("호가든 (250ml)","Hoegaarden","8.0"),
        ("스텔라 (330ml)","Stella Artois","8.0"),
        ("Bottle Beer",),
        ("코로나 (1병 / 바스켓 세트)","Corona","7.0 / 40.0"),
        ("스텔라","Stella Artois","8.0"),
        ("호가든","Hoegaarden","8.0"),
    ])}
    </div>
    <p class="center note">메뉴와 가격은 사정에 따라 변경될 수 있습니다. 단체 예약 및 카페 가든 파티 문의: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
  </div>
</section>
<section class="section cta-band"><div class="wrap center"><h2>Private parties at the cafe garden</h2><p>1층 카페 가든에서 소규모 파티와 모임을 열어 보세요.</p><a class="btn btn-light" href="mailto:{EMAIL}">예약하기</a></div></section>
"""

# ---------- CONTACT ----------
contact = f"""
<section class="page-hero" style="background-image:url('{wix('c19c76_5134149a64f04927a9597998ef802ceb~mv2_d_5661_3774_s_4_2.jpg', 1920, 1280)}')">
  <div class="wrap"><p class="eyebrow">Marina Park</p><h1>Contact</h1></div>
</section>
<section class="section">
  <div class="wrap split contact-split">
    <div class="split-text">
      <h2>Contact us to turn your dream into a reality.</h2>
      <p>Please fill out this form and we will get back to you shortly.<br>행사 종류, 희망 날짜, 예상 인원을 함께 적어 주시면 더 빠르게 안내드릴 수 있습니다.</p>
      <div class="contact-card">
        <h3>MARINA PARK</h3>
        <p>{ADDRESS}</p>
        <p>Tel: <a href="tel:025962440">{TEL}</a><br>Fax: {FAX}</p>
        <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
        <p class="social-row"><a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a> · <a href="{FACEBOOK}" target="_blank" rel="noopener">Facebook</a></p>
      </div>
    </div>
    <form class="contact-form" id="contactForm" action="mailto:{EMAIL}" method="post" enctype="text/plain">
      <label>이름 / Name<input type="text" name="name" required></label>
      <label>이메일 / E-mail<input type="email" name="email" required></label>
      <label>연락처 / Phone<input type="tel" name="phone"></label>
      <label>행사 종류 / Event type
        <select name="event">
          <option>Wedding / Garden Wedding</option>
          <option>Business Party / MICE</option>
          <option>Launching Party</option>
          <option>1st Party (돌잔치)</option>
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
<section class="map-section">
  <iframe title="Marina Park 위치" src="https://www.google.com/maps?q=%EC%84%9C%EC%9A%B8+%EC%84%9C%EC%B4%88%EA%B5%AC+%EB%B0%98%ED%8F%AC%EB%8F%99+115-1&output=embed" loading="lazy" allowfullscreen referrerpolicy="no-referrer-when-downgrade"></iframe>
</section>
"""

PAGES = {
    "index.html": ("Home", home),
    "about.html": ("About us", about),
    "business-party.html": ("Business Party", business),
    "launching-party.html": ("Launching Party", launching),
    "first-party.html": ("1st Party", first),
    "wedding.html": ("Wedding", wedding),
    "garden-wedding.html": ("Garden Wedding", garden),
    "cafe.html": ("Marina Cafe", cafe),
    "contact.html": ("Contact", contact),
}

if __name__ == "__main__":
    for fname, (title, body) in PAGES.items():
        with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
            f.write(page(fname, title, body))
        print("wrote", fname)
