#!/usr/bin/env python3
"""Generates the static site (index, services/, sitemap, robots).
Run:  python3 build.py   (edit content below, then re-run)"""
import json, os, html, datetime

SITE = "https://sensesphysiotherapy.com"
BOOK = "https://kumar.janeapp.com/"
BOOK_BASE = BOOK + "locations/baseline-senses-physiotherapy-clinic/book"
BOOK_CH = BOOK + "locations/craig-henry-plaza-senses-physiotherapy-clinic/book"
PHONE, PHONE_I = "613-829-7367", "+16138297367"
EMAIL = "sensesphysiotherapy@gmail.com"
IG = "https://www.instagram.com/sensesphysiotherapy/"
FB = "https://www.facebook.com/profile.php?id=61566591580494"
OUT = os.path.dirname(os.path.abspath(__file__))
TODAY = datetime.date.today().isoformat()

I = {  # inline icons (stroke)
 "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
 "check": '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
 "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a2 2 0 01-2 2A16 16 0 013 6a2 2 0 012-2z"/>',
 "pin": '<path d="M12 21s7-6.2 7-11.5A7 7 0 005 9.5C5 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
 "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
 "cal": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
 "clip": '<path d="M9 4h6a1 1 0 011 1v2H8V5a1 1 0 011-1z"/><rect x="5" y="6" width="14" height="15" rx="2"/><path d="M9 13l2 2 4-4"/>',
 "spark": '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/>',
 "heart": '<path d="M12 20s-7-4.4-7-10a4 4 0 017-2.6A4 4 0 0119 10c0 5.6-7 10-7 10z"/>',
 "target": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
 "leaf": '<path d="M5 19c0-9 5-14 15-14 0 10-5 15-14 15"/><path d="M5 19c3-5 6-7 10-9"/>',
 "shield": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
 "star": '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/>',
 "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0113 0M16 4.6a3.5 3.5 0 010 6.8M18 14a6 6 0 013.5 6"/>',
 "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
 "moon": '<path d="M20 14.5A8 8 0 019.5 4 8 8 0 1020 14.5z"/>',
 "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
 "x": '<path d="M6 6l12 12M18 6L6 18"/>',
 "up": '<path d="M12 19V5M6 11l6-6 6 6"/>',
 "ig": '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".8" fill="currentColor"/>',
 "fb": '<path d="M14 8h3V4h-3a4 4 0 00-4 4v3H7v4h3v6h4v-6h3l1-4h-4V8z"/>',
 # service icons
 "bone": '<path d="M7 7a2.5 2.5 0 10-3 3.5 2.5 2.5 0 103.5 3L14 7.5A2.5 2.5 0 1017 4a2.5 2.5 0 103.5 3 2.5 2.5 0 10-3 3.5L10.5 17A2.5 2.5 0 107 20a2.5 2.5 0 10-3-3.5"/>',
 "needle": '<path d="M20 4l-9 9M14 7l3 3M11 13l-6 6-1 2 2-1 6-6"/>',
 "bolt": '<path d="M13 2L5 14h6l-1 8 8-12h-6z"/>',
 "dumb": '<path d="M6 8v8M3 10v4M18 8v8M21 10v4M6 12h12"/>',
 "spiral": '<path d="M12 12m-1 0a1 1 0 102 0 1 1 0 10-2 0M12 8a4 4 0 11-4 4M12 4a8 8 0 11-8 8"/>',
 "jaw": '<path d="M5 8c0-3 3-5 7-5s7 2 7 5c0 5-3 9-7 9s-7-4-7-9z"/><path d="M9 14c1 1 5 1 6 0"/>',
 "cup": '<path d="M5 9h14l-1.5 9a3 3 0 01-3 2.5h-5a3 3 0 01-3-2.5z"/><path d="M8 9V6a4 4 0 018 0v3"/>',
 "spine": '<rect x="9" y="3" width="6" height="3.5" rx="1.2"/><rect x="9" y="8.5" width="6" height="3.5" rx="1.2"/><rect x="9" y="14" width="6" height="3.5" rx="1.2"/><path d="M12 19.5V21"/>',
 "link": '<path d="M10 14a4 4 0 005.6 0l3-3a4 4 0 00-5.6-5.6l-1 1M14 10a4 4 0 00-5.6 0l-3 3A4 4 0 0011 18.6l1-1"/>',
 "hand": '<path d="M8 12V5a1.5 1.5 0 013 0v5M11 10V4a1.5 1.5 0 013 0v6M14 10V5.5a1.5 1.5 0 013 0V13M8 12l-1.5-1.8a1.5 1.5 0 00-2.4 1.8L7 17.5A5 5 0 0011.5 21H14a5 5 0 005-5v-3"/>',
}
def ic(n, cls=""):
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{I[n]}</svg>'

SERVICES = [
 dict(slug="physiotherapy", name="Physiotherapy", icon="bone", img="photo1", alt="Athlete holding ankle in pain, a common physiotherapy case",
  short="Hands-on care for pain, injury and mobility.",
  title="Physiotherapy in Ottawa", kw="physiotherapy Ottawa",
  tag="Ease your movement, enrich your life.",
  intro="Registered physiotherapists assess what's driving your pain, then build a plan to move you from hurting to healing. Evidence-based, hands-on and tailored to your goals.",
  body=["Whether it's a sports injury, a stiff back or recovery after surgery, we focus on the cause, not just the symptom. Treatment blends manual therapy, targeted exercise and education so results last.",
        "Our clinicians bring experience across orthopedic, neurological, geriatric and pediatric care, and combine physiotherapy with tools such as laser, acupuncture and spinal decompression when they help."],
  helps=["Back, neck & shoulder pain","Sports & overuse injuries","Post-surgical rehab (e.g. joint replacement)","Sciatica & frozen shoulder","Arthritis & tendinopathies","Carpal tunnel & nerve pain"],
  faq=[("Do I need a referral to see a physiotherapist?","No. In Ontario you can book directly with a physiotherapist without a doctor's referral. Check your insurance plan for its own requirements."),
       ("What happens at the first visit?","A thorough assessment of your history, movement and pain, then a clear plan and the first treatment, usually in the same session.")]),
 dict(slug="acupuncture-under-physiotherapy-practice", name="Acupuncture", icon="needle", img="photo3", alt="Calm green leaves representing balance and healing",
  short="Acupuncture & dry needling for pain relief.",
  title="Acupuncture Under Physiotherapy Practice", kw="acupuncture Ottawa",
  tag="Targeted relief with fine needles.",
  intro="Acupuncture delivered within physiotherapy practice. Fine needles are used to calm pain, release tight muscle and support recovery alongside your treatment plan.",
  body=["Our clinicians hold Canadian certifications in acupuncture and functional dry needling. Needling is combined with movement, manual therapy and exercise to treat the root of the problem.",
        "Sessions are gentle, hygienic (single-use sterile needles) and adjusted to your comfort."],
  helps=["Muscle tightness & trigger points","Chronic and recurring pain","Neck, back & shoulder pain","Tension headaches","Sports injury recovery"],
  faq=[("Does acupuncture hurt?","Most people feel little more than a light tap or a mild ache. We adjust the technique to your comfort."),
       ("Is it covered by insurance?","Many extended health plans cover acupuncture within physiotherapy. Check with your provider.")]),
 dict(slug="laser-therapy", name="Laser Therapy", icon="bolt", img="photo4", alt="Two people jogging outdoors, active recovery after injury",
  short="Painless light therapy for faster healing.",
  title="Laser Therapy", kw="laser therapy Ottawa",
  tag="Light that helps tissue heal.",
  intro="Therapeutic laser is a painless, non-invasive treatment that supports your body's natural healing, helping reduce pain and inflammation.",
  body=["Low-level laser delivers focused light to injured tissue. It's quick, comfortable and works well alongside manual therapy and exercise.",
        "Many clients use it for stubborn tendon, joint and soft-tissue problems that haven't settled with rest alone."],
  helps=["Tendon & ligament injuries","Joint pain & arthritis","Muscle strains","Inflammation & swelling","Slow-healing soft tissue"],
  faq=[("Is laser therapy safe?","Yes. It is non-invasive and painless. You may feel mild warmth. Your therapist will check suitability first."),
       ("How many sessions will I need?","It depends on the condition. Your therapist will outline a plan after your assessment.")]),
 dict(slug="exercise-rehabilitation", name="Exercise Rehab", icon="dumb", img="photo2", alt="Person using a foam roller on an exercise mat",
  short="Rebuild strength, balance and confidence.",
  title="Exercise Rehabilitation", kw="exercise rehabilitation Ottawa",
  tag="Stronger, steadier, back in action.",
  intro="Personalized exercise programs that restore strength, mobility and function so you can return to the activities you love and stay there.",
  body=["Your program is built from your assessment: the right exercises, at the right level, progressed as you improve. We coach technique so you feel confident on your own.",
        "It's the part of care that keeps pain from coming back."],
  helps=["Return to sport or work","Post-surgery strengthening","Posture & core stability","Injury prevention","Fall-risk and mobility programs"],
  faq=[("Do I need gym equipment?","No. We design programs that work at home, with simple equipment or none at all."),
       ("Is it suitable for older adults?","Absolutely. Programs are scaled to your ability and goals.")]),
 dict(slug="vestibular-and-balance-physiotherapy", name="Vestibular & Balance", icon="spiral", img="photo6", alt="Two people doing balanced lunges outdoors",
  short="Relief from dizziness and unsteadiness.",
  title="Vestibular and Balance Physiotherapy", kw="vestibular physiotherapy Ottawa",
  tag="Steady ground beneath you.",
  intro="Specialized rehab for dizziness, vertigo and balance problems. Targeted exercises retrain your balance system so everyday movement feels safe again.",
  body=["After a thorough assessment, we use positioning techniques and tailored exercises to reduce dizziness and improve stability.",
        "Care is gentle, progressive and paced to your symptoms."],
  helps=["Dizziness & vertigo","Balance problems & falls","Post-concussion dizziness","Inner-ear conditions","Unsteadiness with age"],
  faq=[("What causes dizziness?","Many things, including inner-ear issues, neck problems and concussion. An assessment helps identify the source."),
       ("Is treatment uncomfortable?","Some exercises can briefly bring on symptoms. We keep them controlled and manageable.")]),
 dict(slug="tmj-therapy-temporomandibular-jaw-joint", name="TMJ Therapy", icon="jaw", img="photo5", alt="Smiling man relaxed after jaw and neck treatment",
  short="Jaw pain, clicking and tension relief.",
  title="TMJ Therapy (Temporomandibular / Jaw Joint)", kw="TMJ therapy Ottawa",
  tag="Open wide without the pain.",
  intro="Treatment for jaw pain, clicking, locking and the headaches and neck tension that often go with them.",
  body=["The jaw is closely linked to the neck and posture. We combine gentle manual therapy, exercises and self-care strategies to ease the joint and surrounding muscles.",
        "Our clinicians have experience treating TMJ disorders as part of a whole-body approach."],
  helps=["Jaw pain & clicking","Difficulty chewing or opening wide","Tension headaches","Teeth grinding strain","Neck & facial tension"],
  faq=[("Can physiotherapy help TMJ pain?","Yes. Manual therapy, exercises and posture work can reduce jaw and neck strain for many people."),
       ("Do I need to see my dentist too?","Often a team approach works best. We're happy to coordinate with your dentist.")]),
 dict(slug="cupping-therapy", name="Cupping Therapy", icon="cup", img="photo7", alt="Therapist applying kinesiology tape to a knee",
  short="Release tight muscles, boost circulation.",
  title="Cupping Therapy", kw="cupping therapy Ottawa",
  tag="Lift tension, restore flow.",
  intro="Traditional cupping uses gentle suction to release tight muscle and fascia and improve circulation, a great partner to hands-on physiotherapy.",
  body=["Cups are placed on the skin for a few minutes. Many clients notice looser muscles and easier movement afterwards.",
        "Light, temporary circular marks are normal and fade in days."],
  helps=["Tight, knotted muscles","Neck & upper back stiffness","Muscle soreness","Sports recovery","Reduced range of motion"],
  faq=[("Will it leave marks?","Cupping can leave light circular marks that typically fade within a few days."),
       ("Is it painful?","It feels like a firm pulling sensation. We keep suction comfortable.")]),
 dict(slug="spinal-decompression-physiotherapy", name="Spinal Decompression", icon="spine", img="photo1", alt="Person gripping a painful leg, back and leg pain relief",
  short="Ease pressure on the back and neck.",
  title="Spinal Decompression Physiotherapy", kw="spinal decompression Ottawa",
  tag="Take the pressure off your spine.",
  intro="Gentle, non-surgical spinal decompression that relieves pressure on discs and nerves, supporting relief from back and neck pain.",
  body=["Controlled traction creates space between spinal segments. It's combined with exercise and manual therapy to help the benefits last.",
        "A suitable option for many people who want to avoid or delay more invasive care."],
  helps=["Disc-related back & neck pain","Sciatica","Nerve compression","Spondylosis","Chronic stiffness"],
  faq=[("Is spinal decompression safe?","It is suitable for many people but not all. Your therapist screens you first."),
       ("Is it surgery?","No. It is a non-surgical, non-invasive treatment.")]),
 dict(slug="connecttherapy-concept-physiotherapy", name="ConnectTherapy", icon="link", img="photo6", alt="Two people performing lunges, whole-body movement",
  short="Whole-body approach to movement.",
  title="ConnectTherapy Concept Physiotherapy", kw="ConnectTherapy Ottawa",
  tag="Everything in your body is connected.",
  intro="ConnecTherapy looks at the body as one connected system, treating the true source of restriction rather than just the sore spot.",
  body=["Through assessment of movement chains and fascia, your therapist finds the link driving your symptoms and treats it with precise manual techniques and exercise.",
        "Ideal if pain keeps returning or doesn't match where the problem seems to be."],
  helps=["Recurring pain","Movement restrictions","Postural imbalance","Sports performance","Stubborn aches"],
  faq=[("How is this different from regular physiotherapy?","It places extra emphasis on how regions connect, so treatment often targets areas away from where you feel pain."),
       ("Who is it for?","Anyone with pain that lingers or keeps coming back.")]),
 dict(slug="osteopathy", name="Osteopathy", icon="hand", img="photo3", alt="Soft green leaves symbolising gentle holistic care",
  short="Gentle, whole-body manual treatment.",
  title="Osteopathy", kw="osteopathy Ottawa",
  tag="Experience gentle osteopathic care today.",
  intro="Manual, drug-free, gentle and non-invasive hands-on treatment that treats the whole body to improve mobility and bring you back to balance.",
  body=["Our trained therapists have extensive anatomical knowledge and combine the benefits of a massage therapist, chiropractor and physiotherapist in one.",
        "The goal: improve your mobility, reduce pain and stiffness, and restore balance throughout the body."],
  helps=["Pain & stiffness","Restricted mobility","Postural strain","Tension & stress","Whole-body imbalances"],
  faq=[("Is osteopathy painful?","No. Techniques are gentle and non-invasive."),
       ("Can all ages be treated?","Yes. Care is adapted to each person.")]),
]
BY = {s["slug"]: s for s in SERVICES}

TEAM = [
 dict(id="honey", name="Honey Bodara", role="Physiotherapy", where="Baseline · Craig Henry", img="honey",
  tags=["Physiotherapy","Fitness & Health Promotion"],
  bio=["Holds a bachelor's degree in Physiotherapy and a Diploma in Fitness and Health Promotion. Dedicated to continually building skills and helping people carry out daily activities within their functional capacity, and supporting healthy individuals in reaching their performance goals."]),
 dict(id="kumar", name="Kalpeshkumar Harkhani", role="Registered Physiotherapist", where="Baseline · Craig Henry", img="kalpesh",
  tags=["Orthopedics","Neurological","Geriatrics","Pediatrics","Acupuncture","Dry Needling","Cupping","Kinesiology Taping","Mulligan & McKenzie"],
  bio=["Kumar is a Registered Physiotherapist with extensive clinical experience in Canada, committed to evidence-based, personalized treatment plans that help patients reach their rehabilitation goals.",
       "He has treated arthritis, joint-replacement recovery, sciatica, frozen shoulder, tendinopathies, carpal tunnel, stroke, spinal cord injuries, spondylosis, TMJ and more, always treating the body as one connected system.",
       "Bachelor of Physiotherapy (India, 2006) with advanced Canadian certifications in Acupuncture, Functional Dry Needling, Traditional Cupping, Kinesiology Taping, and Mulligan and McKenzie techniques."]),
 dict(id="ritu", name="Ritu Patel", role="Physiotherapy", where="Baseline", img="ritu",
  tags=["Manual Therapy","Exercise Prescription","Orthotics & Bracing","Compression Fitting","Cupping","Acupuncture","Dry Needling","Vestibular Rehab"],
  bio=["Graduated with a Bachelor of Physiotherapy in 2016. Expertise in manual therapy, exercise prescription and comprehensive orthotics assessments, including compression stocking fittings, cupping and taping.",
       "Her client-centred approach helps reduce pain and improve daily function, empowering clients to take an active part in their own self-management."]),
 dict(id="sweta", name="Sweta Vaghasiya", role="Resident Physiotherapist & Manual Osteopathy Therapist", where="Baseline", img="sweta",
  tags=["Osteopathy","Physiotherapy","Neuro rehab","Post-surgical rehab","Pediatric"],
  bio=["Over six years of clinical experience in multi-specialty hospitals and rehabilitation settings. Experienced in orthopedic and neurological conditions, post-surgical rehab, chronic pain and neurorehabilitation.",
       "Strong background in manual therapy, therapeutic exercise, postural correction and pediatric neurodevelopmental therapy. Her approach is patient-centred and evidence-based, with hands-on technique, movement therapy and education."]),
 dict(id="tonya", name="Tonya Gartshore", role="RMT · Massage Therapy", where="Baseline", img="tonya",
  tags=["Stress & tension","Relaxation","Sports","Myofascial","Prenatal","All ages"],
  bio=["Experienced Registered Massage Therapist with over 20 years in practice, working in Ottawa West for the past ten years. Graduate of Algonquin College's Massage Therapy Intensive program and Toronto's Shiatsu School of Canada diploma program.",
       "Alongside Senses Physio, she also has her own practice, TG Massage Therapy, on Greenbank Rd."]),
]

FAQ = [
 ("Do I need a referral for physiotherapy in Ottawa?","No. You can book directly online with a registered physiotherapist, no doctor's referral required. Some insurance plans have their own rules, so check yours."),
 ("How do I book an appointment?","Tap Book Now, choose your clinic and clinician, then pick a time. Booking is available online 24/7 through our secure booking system."),
 ("Where are your clinics?","Two Ottawa locations: Baseline (2944 Baseline Rd) and Craig Henry Plaza (3 Chartwell Ave)."),
 ("What should I bring to my first visit?","Comfortable clothing, your health card, any imaging or reports, and your insurance details if you plan to claim."),
 ("What treatments do you offer?","Physiotherapy, acupuncture, laser therapy, exercise rehab, vestibular & balance therapy, TMJ therapy, cupping, spinal decompression, ConnecTherapy and osteopathy, plus massage therapy."),
]

def e(s): return html.escape(s, quote=True)

def head(r, title, desc, path, extra="", og_img="img/og.jpg"):
    url = SITE + path
    return f'''<!doctype html>
<html lang="en-CA" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="index,follow,max-image-preview:large">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#0b7fd4">
<meta name="geo.region" content="CA-ON"><meta name="geo.placename" content="Ottawa">
<meta property="og:type" content="website"><meta property="og:site_name" content="Senses Physiotherapy Clinic">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/{og_img}">
<meta property="og:locale" content="en_CA">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{e(title)}"><meta name="twitter:description" content="{e(desc)}"><meta name="twitter:image" content="{SITE}/{og_img}">
<link rel="icon" type="image/png" href="{r}img/favicon.png"><link rel="apple-touch-icon" href="{r}img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap">
<script>try{{var t=localStorage.getItem('theme')||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');document.documentElement.setAttribute('data-theme',t)}}catch(e){{}}</script>
<link rel="stylesheet" href="{r}css/style.css">
{extra}
</head>
<body>
<a class="skip" href="#main">Skip to content</a><div id="progress"></div>
'''

def nav(r):
    items = "".join(f'<a href="{r}services/{s["slug"]}/">{e(s["name"])}</a>' for s in SERVICES)
    home = r if r else "./"
    return f'''<header class="nav" id="top"><div class="wrap nav-in">
<a href="{home}" class="logo" aria-label="Senses Physiotherapy home"><img src="{r}img/logo-mark.webp" width="32" height="42" alt=""><span class="lt"><i>SENSES</i><b>PHYSIOTHERAPY</b><small>The Caring Hands You Deserve</small></span></a>
<nav class="menu" id="menu" aria-label="Main">
<a href="{home}#about">About</a>
<div class="dd"><button aria-haspopup="true">Services ▾</button><div class="dd-panel"><a href="{r}services/">All services</a>{items}</div></div>
<a href="{home}#team">Team</a><a href="{home}#locations">Locations</a><a href="{home}#faq">FAQ</a><a href="{home}#contact">Contact</a>
</nav>
<div class="nav-actions">
<button class="icon-btn" id="theme" aria-label="Toggle dark mode">{ic("moon","moon")}{ic("sun","sun")}</button>
<a class="btn btn-primary" href="{BOOK}">Book Now</a>
<button class="icon-btn burger" id="burger" aria-label="Open menu" aria-expanded="false">{ic("menu")}</button>
</div></div></header>
'''

def footer(r):
    home = r if r else "./"
    sl = "".join(f'<li><a href="{r}services/{s["slug"]}/">{e(s["name"])}</a></li>' for s in SERVICES[:6])
    return f'''<footer id="contact"><div class="wrap foot">
<div><a href="{home}" class="logo"><img src="{r}img/logo-mark.webp" width="32" height="42" alt="" loading="lazy"><span class="lt"><i>SENSES</i><b>PHYSIOTHERAPY</b><small>The Caring Hands You Deserve</small></span></a>
<p style="margin-top:14px;max-width:290px">Personalized physiotherapy &amp; massage in Ottawa. Trusted care since 2019.</p>
<div class="socials"><a href="{IG}" aria-label="Instagram" rel="noopener">{ic("ig")}</a><a href="{FB}" aria-label="Facebook" rel="noopener">{ic("fb")}</a></div></div>
<div><h4>Services</h4><ul>{sl}<li><a href="{r}services/">View all</a></li></ul></div>
<div><h4>Clinics</h4><ul><li>Baseline<br>2944 Baseline Rd, Ottawa, ON K2H 7T3</li><li style="margin-top:12px">Craig Henry Plaza<br>3 Chartwell Ave, Ottawa, ON K2G 4K3</li></ul></div>
<div><h4>Contact</h4><ul><li><a href="tel:{PHONE_I}">{PHONE}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li>Fax 613-515-0452</li><li><a href="{BOOK}">Book online</a></li><li><a href="{BOOK}login">Client login</a></li></ul></div>
</div><p class="copy">© <span class="yr">2026</span> Senses Physiotherapy Clinic. All rights reserved.</p></footer>
<a class="btn btn-primary btn-lg float-book" href="{BOOK}">Book Now {ic("arrow")}</a>
<a class="icon-btn to-top" href="#top" aria-label="Back to top">{ic("up")}</a>
<script src="{r}js/main.js" defer></script>
</body></html>'''

def org_schema():
    def clinic(name, street, pc, geo, url):
        return {"@type": ["Physiotherapy", "MedicalBusiness", "LocalBusiness"], "@id": f"{SITE}/#{url}", "name": name,
          "url": SITE, "telephone": PHONE_I, "email": EMAIL, "image": f"{SITE}/img/og.jpg", "logo": f"{SITE}/img/icon-512.png",
          "priceRange": "$$", "medicalSpecialty": "Physiotherapy",
          "address": {"@type": "PostalAddress", "streetAddress": street, "addressLocality": "Ottawa", "addressRegion": "ON", "postalCode": pc, "addressCountry": "CA"},
          "geo": {"@type": "GeoCoordinates", "latitude": geo[0], "longitude": geo[1]},
          "areaServed": ["Ottawa", "Nepean", "Barrhaven", "Kanata"],
          "sameAs": [IG, FB], "potentialAction": {"@type": "ReserveAction", "target": BOOK, "name": "Book an appointment"}}
    return [clinic("Senses Physiotherapy Clinic - Baseline", "2944 Baseline Rd", "K2H 7T3", (45.3323947, -75.770038), "baseline"),
            clinic("Senses Physiotherapy Clinic - Craig Henry Plaza", "3 Chartwell Ave", "K2G 4K3", (45.3357385, -75.7992949), "craig-henry")]

def ld(obj): return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + "</script>"

def svc_cards(r, items=SERVICES):
    out = []
    for i, s in enumerate(items):
        out.append(f'''<article class="s-card rv" style="--d:{(i%4)*.08:.2f}s"><div class="s-img"><img src="{r}img/{s["img"]}.webp" alt="{e(s["alt"])}" width="700" height="450" loading="lazy"></div>
<div class="s-body"><span class="s-ic">{ic(s["icon"])}</span><h3><a href="{r}services/{s["slug"]}/">{e(s["name"])}</a></h3><p>{e(s["short"])}</p><span class="more">Learn more {ic("arrow")}</span></div></article>''')
    return "\n".join(out)

def faq_html(items):
    return "".join(f"<details class='rv'><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in items)

def faq_schema(items):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}

def cta_band(h="Ready to feel better?", p="Book your visit online in under a minute."):
    return f'''<section class="final"><div class="wrap rv"><h2>{h}</h2><p>{p}</p><div class="cta-row"><a class="btn btn-light btn-lg" href="{BOOK}">Book Now {ic("arrow")}</a><a class="btn btn-outline-light btn-lg" href="tel:{PHONE_I}">{ic("phone")} {PHONE}</a></div></div></section>'''

def write(path, content):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(content)

# ---------- HOME ----------
def home():
    r = ""
    team = ""
    tpl = ""
    for i, t in enumerate(TEAM):
        team += f'''<article class="person rv" style="--d:{i*.08:.2f}s"><div class="p-img"><img src="img/{t["img"]}.webp" alt="{e(t["name"])}, {e(t["role"])} at Senses Physiotherapy Ottawa" width="320" height="416" loading="lazy"></div>
<div class="p-body"><h3>{e(t["name"])}</h3><div class="role">{e(t["role"])}</div><button data-bio="tpl-{t["id"]}">View profile</button></div></article>'''
        bio = "".join(f"<p>{e(p)}</p>" for p in t["bio"])
        tags = "".join(f"<span>{e(x)}</span>" for x in t["tags"])
        tpl += f'''<template id="tpl-{t["id"]}"><div class="dlg"><img src="img/{t["img"]}.webp" alt="{e(t["name"])}" width="320" height="416"><div class="dlg-b"><h3>{e(t["name"])}</h3><div class="role">{e(t["role"])}</div><div class="tags">{tags}</div>{bio}<p><b>Clinic:</b> {e(t["where"])}</p><a class="btn btn-primary" href="{BOOK}">Book with us {ic("arrow")}</a></div></div></template>'''
    marq = ["Back pain","Neck pain","Sports injuries","Sciatica","Frozen shoulder","Post-surgery rehab","Dizziness & balance","Jaw pain (TMJ)","Arthritis","Tendinopathy","Posture","Stress & tension"]
    mq = "".join(f"<span>{m}</span>" for m in marq) * 2
    ig_tiles = "".join(f'<a href="{IG}" rel="noopener" aria-label="Instagram post"><img src="img/{p}.webp" alt="" width="200" height="200" loading="lazy"></a>' for p in ["photo4","photo6","photo2"])
    stats = ""
    for n, suf, lab in [(55000, "+", "patients served"), (13, "+", "years of experience"), (10, "", "specialized treatments"), (2, "", "Ottawa clinics")]:
        stats += f'<div class="rv"><b data-to="{n}" data-suf="{suf}">{n:,}{suf}</b><span>{lab}</span></div>'
    desc = "Senses Physiotherapy Clinic in Ottawa: physiotherapy, acupuncture, laser therapy, spinal decompression, osteopathy & massage at Baseline and Craig Henry Plaza. Book online 24/7."
    schema = ld({"@context": "https://schema.org", "@graph": org_schema() + [
        {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE, "name": "Senses Physiotherapy Clinic", "inLanguage": "en-CA"}]}) + ld(faq_schema(FAQ))
    s = head(r, "Senses Physiotherapy Clinic | Physio, Massage & Rehab in Ottawa", desc, "/", schema)
    s += nav(r) + f'''<main id="main">
<section class="hero"><div class="wrap hero-in">
<div><p class="pill rv"><span class="dot"></span> Now booking · Baseline &amp; Craig Henry, Ottawa</p>
<h1 class="rv" style="--d:.08s">Move better.<br><span class="grad">Feel better.</span></h1>
<p class="lead rv" style="--d:.16s">Personalized physiotherapy that gets you out of pain and back to the life you love.</p>
<div class="cta-row rv" style="--d:.24s"><a class="btn btn-primary btn-lg" href="{BOOK}">Book Appointment {ic("arrow")}</a><a class="btn btn-ghost btn-lg" href="#services">Explore treatments</a></div>
<ul class="trust rv" style="--d:.32s"><li>{ic("check")} No referral needed</li><li>{ic("check")} Book online 24/7</li><li>{ic("check")} Two Ottawa clinics</li></ul></div>
<div class="collage rv" style="--d:.15s"><div class="blob"><img src="img/photo4.webp" alt="Active adults exercising outdoors after physiotherapy" width="700" height="467" fetchpriority="high"></div>
<div class="mini"><img src="img/photo5.webp" alt="Smiling patient" width="130" height="130"></div>
<div class="chip c1"><span class="ic">{ic("shield")}</span><div><b>Since 2019</b><span>Trusted Ottawa care</span></div></div>
<div class="chip c2"><span class="ic">{ic("users")}</span><div><b>5 clinicians</b><span>Physio · Osteo · RMT</span></div></div>
<div class="chip c3"><span class="ic">{ic("star")}</span><div><b>Hands-on</b><span>+ advanced tech</span></div></div></div>
</div></section>
<div class="marquee" aria-label="Conditions we treat"><div class="track">{mq}</div></div>

<section class="section" id="services"><div class="wrap">
<div class="head rv"><span class="eyebrow">Treatments</span><h2>Care for every <span class="grad">body</span></h2><p>Ten specialized treatments under one roof. Tap any card to learn more.</p></div>
<div class="grid svc">{svc_cards(r)}</div></div></section>

<section class="section alt" id="about"><div class="wrap about">
<div class="about-img rv"><img src="img/photo7.webp" alt="Physiotherapist applying kinesiology tape to a patient's knee" width="700" height="467" loading="lazy"></div>
<div class="rv" style="--d:.1s"><span class="eyebrow">Our story</span><h2>Born from a shared passion for <span class="grad">holistic care</span></h2>
<p style="color:var(--mut);margin:16px 0">Senses started as a dream among friends: a place focused on your wellness. Your comfort and needs guide every step. We pair care and compassion with evidence-based treatment so you feel heard, understood and supported.</p>
<div class="points">
<div class="pt"><span class="ic">{ic("target")}</span><div><h3>Personalized plans</h3><p>Built around your goals, never a template.</p></div></div>
<div class="pt"><span class="ic">{ic("leaf")}</span><div><h3>Holistic approach</h3><p>We treat the cause, not just the pain.</p></div></div>
<div class="pt"><span class="ic">{ic("pin")}</span><div><h3>Convenient locations</h3><p>Baseline and Craig Henry Plaza, Ottawa.</p></div></div></div></div>
</div></section>

<section class="stats"><div class="wrap stat-grid">{stats}</div></section>

<section class="section"><div class="wrap">
<div class="head center rv"><span class="eyebrow">How it works</span><h2>Three simple steps</h2></div>
<div class="steps">
<div class="step rv"><span class="ic">{ic("cal")}</span><h3>Schedule your visit</h3><p>Pick your clinic, clinician and time online in under a minute.</p></div>
<div class="step rv" style="--d:.1s"><span class="ic">{ic("clip")}</span><h3>Get your plan</h3><p>A thorough assessment, then a clear plan built around you.</p></div>
<div class="step rv" style="--d:.2s"><span class="ic">{ic("spark")}</span><h3>Begin your journey</h3><p>Treatment, exercise and guidance to recover and stay strong.</p></div>
</div></div></section>

<section class="section alt" id="team"><div class="wrap">
<div class="head rv"><span class="eyebrow">Our team</span><h2>Meet your <span class="grad">clinicians</span></h2><p>Experienced, caring and always learning.</p></div>
<div class="grid team">{team}</div></div></section>
<dialog id="bio" aria-label="Clinician profile"><button class="icon-btn dlg-x" aria-label="Close">{ic("x")}</button><div id="bio-body"></div></dialog>{tpl}

<section class="section" id="community"><div class="wrap insta">
<div class="rv"><span class="eyebrow">Follow along</span><h2>Wellness tips &amp; clinic life on <span class="grad">Instagram</span></h2>
<p style="color:var(--mut);margin:16px 0 24px;font-size:1.05rem">Physio · Massage · Rehab. See what's new at Senses, from movement ideas to clinic updates.</p>
<ul class="checks"><li>{ic("check")}Trusted care since 2019</li><li>{ic("check")}13+ years of clinical experience</li><li>{ic("check")}55,000+ patients served</li></ul></div>
<div class="ig-card rv" style="--d:.12s"><div class="ig-top"><div class="ig-av"><img src="img/logo-mark.webp" alt="Senses Physiotherapy logo" width="70" height="70" loading="lazy"></div><div><b>sensesphysiotherapy</b><span>Senses Physiotherapy Clinic · Ottawa, ON</span></div></div>
<div class="ig-nums"><div><b>Physio</b><span>treatment</span></div><div><b>Massage</b><span>therapy</span></div><div><b>Rehab</b><span>programs</span></div></div>
<div class="ig-tiles">{ig_tiles}</div>
<a class="btn btn-ig btn-lg" href="{IG}" rel="noopener">{ic("ig")} Follow @sensesphysiotherapy</a></div>
</div></section>

<section class="section alt" id="faq"><div class="wrap"><div class="head center rv"><span class="eyebrow">FAQ</span><h2>Quick answers</h2></div>
<div class="faq">{faq_html(FAQ)}</div></div></section>

<section class="section" id="locations"><div class="wrap"><div class="head center rv"><span class="eyebrow">Find us</span><h2>Two clinics, <span class="grad">one team</span></h2></div>
<div class="grid locs">
<article class="loc rv"><iframe loading="lazy" title="Map: Senses Physiotherapy Baseline" src="https://maps.google.com/maps?q=2944+Baseline+Rd+Ottawa+ON&amp;output=embed" referrerpolicy="no-referrer-when-downgrade"></iframe>
<div class="loc-b"><h3>Baseline</h3><ul><li>{ic("pin")}2944 Baseline Rd, Ottawa, ON K2H 7T3</li><li>{ic("phone")}<a href="tel:{PHONE_I}">{PHONE}</a></li><li>{ic("users")}Honey · Kumar · Ritu · Sweta · Tonya</li></ul>
<div class="cta-row"><a class="btn btn-primary" href="{BOOK_BASE}">Book here</a><a class="btn btn-ghost" href="https://www.google.com/maps/place/Senses+Physiotherapy+Clinic/@45.3323947,-75.7726129,17z" rel="noopener">Directions</a></div></div></article>
<article class="loc rv" style="--d:.1s"><iframe loading="lazy" title="Map: Senses Physiotherapy Craig Henry Plaza" src="https://maps.google.com/maps?q=3+Chartwell+Ave+Ottawa+ON&amp;output=embed" referrerpolicy="no-referrer-when-downgrade"></iframe>
<div class="loc-b"><h3>Craig Henry Plaza</h3><ul><li>{ic("pin")}3 Chartwell Ave, Ottawa, ON K2G 4K3</li><li>{ic("phone")}<a href="tel:{PHONE_I}">{PHONE}</a></li><li>{ic("users")}Honey · Kumar</li></ul>
<div class="cta-row"><a class="btn btn-primary" href="{BOOK_CH}">Book here</a><a class="btn btn-ghost" href="https://www.google.com/maps/place/Senses+Physiotherapy+Clinic/@45.3357385,-75.8018698,17z" rel="noopener">Directions</a></div></div></article>
</div></div></section>
{cta_band()}</main>''' + footer(r)
    write("index.html", s)

# ---------- SERVICES INDEX ----------
def services_index():
    r = "../"
    crumbs = ld({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": "Services", "item": SITE + "/services/"}]})
    s = head(r, "Physiotherapy Services in Ottawa | Senses Physiotherapy", "Physiotherapy, acupuncture, laser therapy, spinal decompression, osteopathy, cupping, TMJ and vestibular therapy in Ottawa. Explore all treatments and book online.", "/services/", crumbs)
    s += nav(r) + f'''<main id="main"><section class="page-hero"><div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="{r}">Home</a> / <span>Services</span></nav>
<span class="eyebrow">Treatments</span><h1>Our <span class="grad">services</span></h1><p class="lead">Ten specialized treatments, one caring team in Ottawa.</p></div></section>
<section class="section"><div class="wrap"><div class="grid svc">{svc_cards(r)}</div></div></section>{cta_band()}</main>''' + footer(r)
    write("services/index.html", s)

# ---------- SERVICE PAGES ----------
def service_page(sv):
    r = "../../"
    url = f"/services/{sv['slug']}/"
    desc = f"{sv['name']} in Ottawa at Senses Physiotherapy Clinic. {sv['intro']}"[:300]
    schema = ld({"@context": "https://schema.org", "@type": "MedicalWebPage", "name": sv["title"], "url": SITE + url, "description": sv["intro"],
        "about": {"@type": "MedicalTherapy", "name": sv["name"]}, "provider": {"@id": f"{SITE}/#baseline"}, "image": f"{SITE}/img/{sv['img']}.webp"}) \
        + ld({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": "Services", "item": SITE + "/services/"},
        {"@type": "ListItem", "position": 3, "name": sv["name"], "item": SITE + url}]}) + ld(faq_schema(sv["faq"]))
    others = "".join(f'<a href="{r}services/{o["slug"]}/">{e(o["name"])}</a>' for o in SERVICES if o["slug"] != sv["slug"])
    helps = "".join(f"<li>{ic('check')}{e(h)}</li>" for h in sv["helps"])
    body = "".join(f"<p>{e(p)}</p>" for p in sv["body"])
    s = head(r, f"{sv['name']} in Ottawa | Senses Physiotherapy", desc, url, schema, og_img=f"img/og.jpg")
    s += nav(r) + f'''<main id="main"><section class="page-hero"><div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="{r}">Home</a> / <a href="{r}services/">Services</a> / <span>{e(sv["name"])}</span></nav>
<div class="ph-in"><div><span class="eyebrow">{e(sv["tag"])}</span><h1>{e(sv["title"])}</h1><p class="lead">{e(sv["intro"])}</p>
<div class="cta-row"><a class="btn btn-primary btn-lg" href="{BOOK}">Book Now {ic("arrow")}</a><a class="btn btn-ghost btn-lg" href="tel:{PHONE_I}">{ic("phone")} Call</a></div></div>
<div class="ph-img"><img src="{r}img/{sv["img"]}.webp" alt="{e(sv["alt"])}" width="700" height="500" fetchpriority="high"></div></div></div></section>
<section class="section"><div class="wrap two"><div class="prose rv"><span class="eyebrow">About this treatment</span><h2 style="margin-bottom:18px">What to expect</h2>{body}
<h3 style="margin-top:28px">Commonly helps with</h3><ul class="checks">{helps}</ul></div>
<aside class="side rv" style="--d:.1s"><h3>Book your visit</h3><p>Choose your clinic and clinician online.</p>
<a class="btn btn-primary" href="{BOOK_BASE}">Baseline clinic</a><a class="btn btn-ghost" href="{BOOK_CH}">Craig Henry Plaza</a>
<p style="margin:14px 0 0;text-align:center">Or call <a href="tel:{PHONE_I}" style="color:var(--p);font-weight:700">{PHONE}</a></p></aside></div></section>
<section class="section alt"><div class="wrap"><div class="head center rv"><span class="eyebrow">FAQ</span><h2>{e(sv["name"])} questions</h2></div><div class="faq">{faq_html(sv["faq"])}</div></div></section>
<section class="section"><div class="wrap"><div class="head rv"><span class="eyebrow">Explore more</span><h2>Other treatments</h2></div><div class="others rv">{others}</div></div></section>
{cta_band()}</main>''' + footer(r)
    write(f"services/{sv['slug']}/index.html", s)

home(); services_index()
for sv in SERVICES: service_page(sv)

urls = ["/", "/services/"] + [f"/services/{s['slug']}/" for s in SERVICES]
write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
      "".join(f"<url><loc>{SITE}{u}</loc><lastmod>{TODAY}</lastmod><priority>{'1.0' if u=='/' else '0.8'}</priority></url>\n" for u in urls) + "</urlset>\n")
write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
write("_redirects", "/about /#about 301\n/pages/contact /#contact 301\n/services /services/ 301\n")
write("site.webmanifest", json.dumps({"name": "Senses Physiotherapy Clinic", "short_name": "Senses Physio", "start_url": "/", "display": "standalone", "theme_color": "#0b7fd4", "background_color": "#ffffff", "icons": [{"src": "/img/icon-512.png", "sizes": "512x512", "type": "image/png"}]}))
print("built", len(urls), "pages")
