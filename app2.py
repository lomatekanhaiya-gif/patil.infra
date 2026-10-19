import streamlit as st
import streamlit.components.v1 as components

# 1. Page Configuration
st.set_page_config(
    page_title="Patil Infra | Dharashiv - 2D/3D Planning & Estimation",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Hide Streamlit's default UI for a pure full-screen website
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
        iframe {
            width: 100%;
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

# 3. Complete Patil Infra Website with Full Detailed WhatsApp Requirement Integration
website_html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Patil Infra Dharashiv</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    body { font-family: 'Inter', sans-serif; margin: 0; padding: 0; background-color: #f8fafc; color: #0f172a; }
    .gold-gradient { background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); }
  </style>
</head>
<body>

  <!-- TOP NAVBAR -->
  <nav class="sticky top-0 z-50 bg-[#0b1324] text-white border-b border-slate-800 shadow-lg">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
      <div class="flex items-center gap-3">
        <!-- FIXED 38x38 LOGO -->
        <div style="width: 38px; height: 38px; min-width: 38px; max-width: 38px; overflow: hidden;" class="flex items-center justify-center">
          <svg width="38" height="38" viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect x="6" y="6" width="108" height="108" rx="26" fill="#0f172a" stroke="#f59e0b" stroke-width="6"/>
            <path d="M28 58C28 40 42 28 60 28C78 28 92 40 92 58H28Z" fill="#f59e0b"/>
            <rect x="55" y="25" width="10" height="33" rx="3" fill="#fde68a"/>
            <rect x="22" y="56" width="76" height="8" rx="4" fill="#d97706"/>
            <rect x="33" y="74" width="14" height="18" rx="2" fill="#38bdf8"/>
            <rect x="52" y="68" width="16" height="24" rx="2" fill="#0284c7"/>
            <rect x="73" y="77" width="14" height="15" rx="2" fill="#38bdf8"/>
            <rect x="28" y="94" width="64" height="5" rx="2.5" fill="#f59e0b"/>
          </svg>
        </div>
        <div>
          <div class="flex items-center gap-2">
            <span class="font-extrabold text-lg tracking-wider text-white">PATIL <span class="text-amber-400">INFRA</span></span>
            <span class="text-[10px] bg-sky-900/80 text-sky-300 border border-sky-700 px-2 py-0.5 rounded font-semibold">DHARASHIV</span>
          </div>
          <p class="text-[11px] text-slate-400">Architectural 2D/3D Planning, BIM & Cost Estimation</p>
        </div>
      </div>

      <!-- RIGHT CONTROLS -->
      <div class="flex items-center gap-2">
        <div class="bg-slate-800 p-0.5 rounded-lg border border-slate-700 flex text-xs font-bold">
          <button type="button" onclick="setLang('en')" id="btn-en" class="px-2.5 py-1 rounded-md bg-amber-500 text-slate-950 transition">EN</button>
          <button type="button" onclick="setLang('mr')" id="btn-mr" class="px-2.5 py-1 rounded-md text-slate-300 hover:text-white transition">मराठी</button>
        </div>
        <button type="button" onclick="togglePinBar()" id="lockBtn" title="Admin Access" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-amber-400 border border-slate-700 text-xs font-bold transition flex items-center gap-1 cursor-pointer">
          🔒
        </button>
      </div>
    </div>

    <!-- INLINE OWNER AUTH BAR -->
    <div id="pinBar" style="display: none;" class="bg-slate-900 border-t border-slate-800 px-4 py-3">
      <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3">
        <div class="flex items-center gap-2 text-xs text-slate-300 font-semibold">
          <span>🔐 Authorized Admin Login</span>
        </div>
        <div class="flex items-center gap-2">
          <input id="pinInput" type="password" autocomplete="off" placeholder="Enter Access Key" onkeydown="if(event.key==='Enter') verifyPin()" class="px-3 py-1.5 rounded-lg bg-slate-800 border border-slate-600 text-white text-xs font-bold w-44 focus:outline-none focus:border-amber-400"/>
          <button type="button" onclick="verifyPin()" class="gold-gradient text-slate-950 font-extrabold px-4 py-1.5 rounded-lg text-xs cursor-pointer">
            Login
          </button>
          <button type="button" onclick="togglePinBar()" class="bg-slate-800 text-slate-300 px-2.5 py-1.5 rounded-lg text-xs">
            ✕
          </button>
        </div>
      </div>
      <p id="pinError" style="display: none;" class="text-red-400 text-xs font-bold mt-1 text-right max-w-7xl mx-auto">❌ Access Denied! Invalid Key.</p>
    </div>
  </nav>

  <!-- OWNER PRIVATE UPLOAD STUDIO -->
  <section id="ownerPanel" style="display: none;" class="bg-amber-50/90 border-b-2 border-amber-400 py-6 px-4 shadow-inner">
    <div class="max-w-7xl mx-auto">
      <div class="flex flex-wrap items-center justify-between gap-2 mb-4">
        <div>
          <span class="text-xs font-extrabold uppercase bg-amber-500 text-slate-950 px-2.5 py-1 rounded">🔓 Owner Studio Active</span>
          <h3 class="text-lg font-extrabold text-slate-900 mt-1">Upload Your New 2D/3D Plans & Estimates</h3>
          <p class="text-xs text-slate-600">इथून अपलोड केलेले प्लॅन्स खाली Portfolio मध्ये दिसतील.</p>
        </div>
        <button type="button" onclick="lockOwner()" class="text-xs bg-slate-900 hover:bg-slate-800 text-white px-4 py-2 rounded-xl font-bold cursor-pointer">
          Logout 🔒
        </button>
      </div>

      <div class="grid sm:grid-cols-4 gap-3 bg-white p-4 rounded-2xl border border-amber-300 shadow-sm">
        <div>
          <label class="block text-[11px] font-bold text-slate-600 uppercase mb-1">Project Title *</label>
          <input id="upTitle" type="text" placeholder="e.g. 30x40 East Facing 2BHK" class="w-full px-3 py-2 rounded-xl border border-slate-300 text-sm"/>
        </div>
        <div>
          <label class="block text-[11px] font-bold text-slate-600 uppercase mb-1">Category</label>
          <select id="upType" class="w-full px-3 py-2 rounded-xl border border-slate-300 text-sm font-semibold">
            <option value="2D AutoCAD Plan">2D AutoCAD Plan</option>
            <option value="3D Revit / SketchUp">3D Revit / SketchUp</option>
            <option value="BOQ & Cost Estimate">BOQ & Cost Estimate</option>
          </select>
        </div>
        <div>
          <label class="block text-[11px] font-bold text-slate-600 uppercase mb-1">Plan Details & Estimate</label>
          <input id="upSpecs" type="text" placeholder="e.g. 1200 Sq.Ft • ₹19.5L BOQ" class="w-full px-3 py-2 rounded-xl border border-slate-300 text-sm"/>
        </div>
        <div>
          <label class="block text-[11px] font-bold text-slate-600 uppercase mb-1">Select Plan Photo/Image</label>
          <input id="upFile" type="file" accept="image/*" class="w-full text-xs bg-slate-50 p-1.5 rounded-xl border border-slate-300"/>
        </div>
      </div>

      <div class="mt-3 flex items-center gap-3">
        <button type="button" onclick="addOwnerProject()" class="bg-slate-900 hover:bg-slate-800 text-amber-400 font-extrabold px-6 py-2.5 rounded-xl text-xs shadow cursor-pointer">
          ➕ Upload & Publish to Website
        </button>
        <span id="uploadSuccess" style="display: none;" class="text-xs font-bold text-emerald-700 bg-emerald-100 px-3 py-1.5 rounded-lg">
          ✅ तुझा प्लॅन पोर्टफोलिओमध्ये यशस्वीरित्या जोडला गेला आहे!
        </span>
      </div>
    </div>
  </section>

  <!-- HERO SECTION -->
  <section class="bg-[#0f172a] text-white py-14 px-4 border-b border-slate-800">
    <div class="max-w-7xl mx-auto grid md:grid-cols-2 gap-10 items-center">
      <div>
        <span class="inline-block text-xs font-bold uppercase tracking-widest bg-amber-500/10 text-amber-400 border border-amber-500/30 px-3 py-1 rounded-full mb-4">
          Pure Design & Estimation Studio • Dharashiv
        </span>
        <h1 id="hero-title" class="text-3xl sm:text-5xl font-extrabold leading-tight mb-4">
          Smart 2D/3D Building Plans & <span class="text-amber-400">Accurate Cost Estimates</span>
        </h1>
        <p id="hero-desc" class="text-slate-300 text-sm sm:text-base mb-6 leading-relaxed">
          We specialize exclusively in Architectural 2D AutoCAD Drafting, 3D SketchUp & Revit BIM Modeling, and Bank/Construction Cost Estimation (BOQ & Rate Analysis) in Dharashiv. No contracting hassle—100% transparent technical consultancy.
        </p>
        <div class="flex flex-wrap gap-3">
          <a href="#calculator" class="gold-gradient text-slate-950 font-bold px-5 py-3 rounded-xl text-sm shadow-lg">
            ⚡ Instant Plan & Estimate Calculator
          </a>
          <a href="https://wa.me/919607721250" target="_blank" class="bg-emerald-600 hover:bg-emerald-500 text-white font-bold px-5 py-3 rounded-xl text-sm shadow-lg">
            💬 WhatsApp: 9607721250
          </a>
        </div>
      </div>

      <!-- QUICK SERVICE CARDS -->
      <div class="grid grid-cols-2 gap-4">
        <div class="bg-slate-800/90 border border-slate-700 p-4 rounded-2xl">
          <div class="text-amber-400 text-xl mb-1">📐</div>
          <h3 class="font-bold text-sm mb-1">2D AutoCAD Planning</h3>
          <p class="text-xs text-slate-400">Vastu-compliant floor plans, column layout & municipal blueprints.</p>
        </div>
        <div class="bg-slate-800/90 border border-slate-700 p-4 rounded-2xl">
          <div class="text-sky-400 text-xl mb-1">🏠</div>
          <h3 class="font-bold text-sm mb-1">3D Elevation & Revit BIM</h3>
          <p class="text-xs text-slate-400">Realistic 3D exterior views, wall schedules & walkthrough models.</p>
        </div>
        <div class="bg-slate-800/90 border border-slate-700 p-4 rounded-2xl">
          <div class="text-emerald-400 text-xl mb-1">📊</div>
          <h3 class="font-bold text-sm mb-1">Detailed Cost Estimation</h3>
          <p class="text-xs text-slate-400">Exact RCC & Brickwork Rate Analysis, Material BOQ & Abstract sheets.</p>
        </div>
        <div class="bg-slate-800/90 border border-slate-700 p-4 rounded-2xl">
          <div class="text-purple-400 text-xl mb-1">🏦</div>
          <h3 class="font-bold text-sm mb-1">Bank Loan Valuation</h3>
          <p class="text-xs text-slate-400">Standardized engineer estimate sheets ready for home loan approval.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- AUTOMATED FEE & MATERIAL ESTIMATE CALCULATOR -->
  <section id="calculator" class="py-12 px-4 max-w-7xl mx-auto">
    <div class="bg-white rounded-3xl shadow-xl border border-slate-200 p-6 sm:p-8">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-6 border-b border-slate-100">
        <div>
          <span class="text-xs font-bold uppercase text-amber-600 tracking-wider">100% Automated Engine</span>
          <h2 id="calc-title" class="text-2xl font-extrabold text-slate-900">Instant Planning Fee & Construction Estimate</h2>
        </div>
        <span class="text-xs bg-emerald-50 text-emerald-700 border border-emerald-200 px-3 py-1 rounded-full font-semibold">
          Direct WhatsApp Quote • +91 9607721250
        </span>
      </div>

      <div class="grid lg:grid-cols-12 gap-8 mt-6">
        <div class="lg:col-span-6 space-y-4">
          <div class="grid grid-cols-2 gap-4">
            <div>
              <label class="block text-xs font-bold text-slate-600 uppercase mb-1">Plot Width (Ft)</label>
              <input type="number" id="plotW" value="30" oninput="runCalc()" class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 font-semibold text-sm"/>
            </div>
            <div>
              <label class="block text-xs font-bold text-slate-600 uppercase mb-1">Plot Length (Ft)</label>
              <input type="number" id="plotL" value="50" oninput="runCalc()" class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 font-semibold text-sm"/>
            </div>
          </div>

          <div class="grid grid-cols-2 gap-4">
            <div>
              <label class="block text-xs font-bold text-slate-600 uppercase mb-1">Number of Floors</label>
              <select id="floors" onchange="runCalc()" class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 font-semibold text-sm">
                <option value="Ground Floor Only (G)">Ground Floor Only (G)</option>
                <option value="G + 1 (Duplex / 2 Floors)" selected>G + 1 (Duplex / 2 Floors)</option>
                <option value="G + 2 (3 Floors)">G + 2 (3 Floors)</option>
              </select>
            </div>
            <div>
              <label class="block text-xs font-bold text-slate-600 uppercase mb-1">Required Package</label>
              <select id="pkg" onchange="runCalc()" class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 font-semibold text-sm">
                <option value="Only 2D Floor Plan (₹4/sq.ft)">Only 2D Floor Plan (₹4/sq.ft)</option>
                <option value="Only Cost Estimate & BOQ (₹3/sq.ft)">Only Cost Estimate & BOQ (₹3/sq.ft)</option>
                <option value="2D Plan + 3D + Full Estimate (₹9/sq.ft)" selected>2D Plan + 3D + Full Estimate (₹9/sq.ft)</option>
                <option value="Complete Revit BIM + BOQ Package (₹12/sq.ft)">Complete Revit BIM + BOQ Package (₹12/sq.ft)</option>
              </select>
            </div>
          </div>

          <div class="grid grid-cols-2 gap-4 pt-2">
            <input type="text" id="clientName" placeholder="Your Full Name" class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 text-sm"/>
            <input type="text" id="clientPhone" placeholder="Your Mobile Number" class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 text-sm"/>
          </div>

          <button type="button" onclick="sendWhatsAppQuote()" class="w-full gold-gradient text-slate-950 font-extrabold py-3 rounded-xl text-sm shadow-md hover:opacity-95 transition cursor-pointer">
            📲 Send Requirement to Patil Infra WhatsApp
          </button>
        </div>

        <div class="lg:col-span-6 bg-slate-900 text-white rounded-2xl p-6 flex flex-col justify-between border border-slate-800">
          <div>
            <div class="flex justify-between items-center border-b border-slate-800 pb-3 mb-4">
              <span class="text-xs uppercase tracking-wider text-slate-400 font-bold">Automated Estimate Summary</span>
              <span id="areaBadge" class="text-xs bg-amber-500/20 text-amber-300 px-2.5 py-1 rounded font-bold">Built-up: 1200 Sq.Ft</span>
            </div>

            <div class="grid grid-cols-2 gap-4 mb-5">
              <div class="bg-slate-800/80 p-3.5 rounded-xl border border-slate-700">
                <p class="text-[11px] text-slate-400">Patil Infra Consultancy Fee</p>
                <p id="outFee" class="text-2xl font-extrabold text-amber-400">₹10,800</p>
                <p class="text-[10px] text-slate-400 mt-0.5">For Planning & Estimation</p>
              </div>
              <div class="bg-slate-800/80 p-3.5 rounded-xl border border-slate-700">
                <p class="text-[11px] text-slate-400">Est. Site Construction Cost</p>
                <p id="outConstCost" class="text-2xl font-extrabold text-sky-400">₹19.80 Lakhs</p>
                <p class="text-[10px] text-slate-400 mt-0.5">Approx. Material + Labour BOQ</p>
              </div>
            </div>

            <p class="text-xs font-bold text-slate-300 mb-2 uppercase tracking-wider">Estimated Key Material Quantities (BOQ Preview):</p>
            <div class="grid grid-cols-4 gap-2 text-center">
              <div class="bg-slate-800 p-2 rounded-lg">
                <div id="mCement" class="font-bold text-sm text-white">480</div>
                <div class="text-[10px] text-slate-400">Cement Bags</div>
              </div>
              <div class="bg-slate-800 p-2 rounded-lg">
                <div id="mSteel" class="font-bold text-sm text-white">4.2 T</div>
                <div class="text-[10px] text-slate-400">TMT Steel</div>
              </div>
              <div class="bg-slate-800 p-2 rounded-lg">
                <div id="mBricks" class="font-bold text-sm text-white">21,600</div>
                <div class="text-[10px] text-slate-400">Bricks (Nos)</div>
              </div>
              <div class="bg-slate-800 p-2 rounded-lg">
                <div id="mSand" class="font-bold text-sm text-white">18 Brass</div>
                <div class="text-[10px] text-slate-400">River/Crush Sand</div>
              </div>
            </div>
          </div>

          <div class="mt-5 pt-3 border-t border-slate-800 flex items-center justify-between text-[11px] text-slate-400">
            <span>📍 Patil Infra • 📞 +91 9607721250</span>
            <button type="button" onclick="window.print()" class="text-amber-400 hover:underline font-semibold">🖨️ Print Slip</button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- PORTFOLIO SECTION -->
  <section id="portfolio" class="py-10 px-4 max-w-7xl mx-auto">
    <div class="mb-6">
      <span class="text-xs font-bold uppercase text-sky-600">Our Work Samples</span>
      <h2 id="port-title" class="text-2xl font-extrabold text-slate-900">Completed 2D Plans, 3D Models & BOQ Sheets</h2>
    </div>
    <div id="portfolioGrid" class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6"></div>
  </section>

  <!-- FOOTER -->
  <footer class="bg-[#0b1324] text-slate-400 py-8 px-4 text-center text-xs border-t border-slate-800 mt-10">
    <p class="font-bold text-white text-sm mb-1">PATIL INFRA — DHARASHIV (OSMANABAD)</p>
    <p class="mb-2">Architectural 2D/3D Planning • Autodesk Revit BIM • Detailed Civil Cost Estimation & Rate Analysis</p>
    <p class="text-amber-400 font-semibold">📞 Contact / WhatsApp: +91 9607721250</p>
  </footer>

  <script>
    const defaultProjects = [
      {
        title: "30×50 East-Facing 2BHK Blueprint",
        type: "2D AutoCAD Plan",
        specs: "1500 Sq.Ft • Vastu Compliant + Column Centerline",
        img: "https://images.unsplash.com/photo-1503387762-592deb58ef4e?auto=format&fit=crop&w=800&q=80"
      },
      {
        title: "G+1 Modern Bungalow 3D & BIM Schedule",
        type: "3D Revit / SketchUp",
        specs: "2100 Sq.Ft • Dharashiv • Plinth & Wall Schedule",
        img: "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=800&q=80"
      },
      {
        title: "RCC & Brickwork Rate Analysis + Bank BOQ",
        type: "BOQ & Cost Estimate",
        specs: "M20 Concrete + Brickwork Abstract • ₹24.5 Lakhs",
        img: "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=800&q=80"
      }
    ];

    let isOwnerUnlocked = false;
    let projects = [];

    try {
      const saved = localStorage.getItem('patil_infra_projects');
      projects = saved ? JSON.parse(saved) : defaultProjects;
    } catch (e) {
      projects = defaultProjects;
    }

    function saveProjects() {
      try {
        localStorage.setItem('patil_infra_projects', JSON.stringify(projects));
      } catch (e) {}
    }

    function renderPortfolio() {
      const grid = document.getElementById('portfolioGrid');
      grid.innerHTML = projects.map((p, idx) => `
        <div class="bg-white rounded-2xl overflow-hidden shadow-md border border-slate-200 flex flex-col justify-between">
          <div>
            <img src="${p.img}" class="w-full h-48 object-cover" alt="${p.title}"/>
            <div class="p-4">
              <div class="flex items-center justify-between">
                <span class="text-[10px] font-bold uppercase bg-amber-100 text-amber-800 px-2.5 py-0.5 rounded-full">${p.type}</span>
                ${isOwnerUnlocked ? `<button onclick="deleteProject(${idx})" class="text-[11px] text-red-600 font-bold hover:underline">🗑️ Delete</button>` : ''}
              </div>
              <h3 class="font-extrabold text-slate-900 text-base mt-2">${p.title}</h3>
              <p class="text-xs text-slate-500 mt-1">${p.specs}</p>
            </div>
          </div>
        </div>
      `).join('');
    }

    function deleteProject(index) {
      projects.splice(index, 1);
      saveProjects();
      renderPortfolio();
    }

    function togglePinBar() {
      if (isOwnerUnlocked) {
        lockOwner();
        return;
      }
      const bar = document.getElementById('pinBar');
      const err = document.getElementById('pinError');
      err.style.display = 'none';
      if (bar.style.display === 'none') {
        bar.style.display = 'block';
        document.getElementById('pinInput').focus();
      } else {
        bar.style.display = 'none';
      }
    }

    function verifyPin() {
      const pin = document.getElementById('pinInput').value.trim();
      const err = document.getElementById('pinError');
      if (pin === '\x40\x44\x65\x6c\x6c\x67\x31\x35') {
        isOwnerUnlocked = true;
        document.getElementById('pinBar').style.display = 'none';
        document.getElementById('ownerPanel').style.display = 'block';
        document.getElementById('lockBtn').innerHTML = '🔓';
        document.getElementById('pinInput').value = '';
        err.style.display = 'none';
        renderPortfolio();
      } else {
        err.style.display = 'block';
      }
    }

    function lockOwner() {
      isOwnerUnlocked = false;
      document.getElementById('ownerPanel').style.display = 'none';
      document.getElementById('pinBar').style.display = 'none';
      document.getElementById('lockBtn').innerHTML = '🔒';
      renderPortfolio();
    }

    function addOwnerProject() {
      const title = document.getElementById('upTitle').value.trim();
      const type = document.getElementById('upType').value;
      const specs = document.getElementById('upSpecs').value.trim() || 'Dharashiv Consultancy Project';
      const fileInput = document.getElementById('upFile');
      const msg = document.getElementById('uploadSuccess');

      if (!title) {
        alert('भावा, आधी Project Title टाक!');
        return;
      }

      const finalizeAdd = (imgUrl) => {
        projects.unshift({ title, type, specs, img: imgUrl });
        saveProjects();
        renderPortfolio();
        document.getElementById('upTitle').value = '';
        document.getElementById('upSpecs').value = '';
        fileInput.value = '';
        msg.style.display = 'inline-block';
        setTimeout(() => { msg.style.display = 'none'; }, 4000);
      };

      if (fileInput.files && fileInput.files[0]) {
        const reader = new FileReader();
        reader.onload = function(e) {
          finalizeAdd(e.target.result);
        };
        reader.readAsDataURL(fileInput.files[0]);
      } else {
        finalizeAdd("https://images.unsplash.com/photo-1503387762-592deb58ef4e?auto=format&fit=crop&w=800&q=80");
      }
    }

    function runCalc() {
      const w = parseFloat(document.getElementById('plotW').value) || 0;
      const l = parseFloat(document.getElementById('plotL').value) || 0;
      const floorsEl = document.getElementById('floors');
      let floorCount = 1;
      if (floorsEl.value.includes('G + 1')) floorCount = 2;
      else if (floorsEl.value.includes('G + 2')) floorCount = 3;

      const builtUp = Math.round(w * l * 0.8 * floorCount);
      
      const pkgVal = document.getElementById('pkg').value;
      let rate = 9;
      if (pkgVal.includes('₹4')) rate = 4;
      else if (pkgVal.includes('₹3')) rate = 3;
      else if (pkgVal.includes('₹9')) rate = 9;
      else if (pkgVal.includes('₹12')) rate = 12;

      const fee = builtUp * rate;
      const constCostLakhs = ((builtUp * 1650) / 100000).toFixed(2);

      document.getElementById('areaBadge').innerText = `Built-up: ${builtUp} Sq.Ft`;
      document.getElementById('outFee').innerText = `₹${fee.toLocaleString('en-IN')}`;
      document.getElementById('outConstCost').innerText = `₹${constCostLakhs} Lakhs`;

      document.getElementById('mCement').innerText = Math.round(builtUp * 0.4);
      document.getElementById('mSteel').innerText = ((builtUp * 3.5) / 1000).toFixed(1) + ' T';
      document.getElementById('mBricks').innerText = Math.round(builtUp * 18).toLocaleString('en-IN');
      document.getElementById('mSand').innerText = Math.round(builtUp * 0.015) + ' Brass';
    }

    function sendWhatsAppQuote() {
      const name = document.getElementById('clientName').value.trim() || 'Valued Client';
      const clientMob = document.getElementById('clientPhone').value.trim() || 'Not Provided';
      const w = document.getElementById('plotW').value;
      const l = document.getElementById('plotL').value;
      const floors = document.getElementById('floors').value;
      const pkg = document.getElementById('pkg').value;
      const area = document.getElementById('areaBadge').innerText;
      const fee = document.getElementById('outFee').innerText;
      const constCost = document.getElementById('outConstCost').innerText;

      const text = `Hello *Patil Infra (Dharashiv)*!%0A%0A` +
                   `*New Client Requirement:*%0A` +
                   `👤 Name: ${name}%0A` +
                   `📞 Mobile: ${clientMob}%0A` +
                   `📐 Plot Size: ${w} x ${l} Ft%0A` +
                   `🏢 Floors: ${floors}%0A` +
                   `📦 Package: ${pkg}%0A` +
                   `📐 Total Area: ${area}%0A` +
                   `💰 Consultancy Fee: ${fee}%0A` +
                   `🏗️ Est. Construction Cost: ${constCost}`;

      window.open(`https://wa.me/919607721250?text=${text}`, '_blank');
    }

    function setLang(lang) {
      const isMr = lang === 'mr';
      document.getElementById('btn-en').className = !isMr ? 'px-2.5 py-1 rounded-md bg-amber-500 text-slate-950 transition' : 'px-2.5 py-1 rounded-md text-slate-300';
      document.getElementById('btn-mr').className = isMr ? 'px-2.5 py-1 rounded-md bg-amber-500 text-slate-950 transition' : 'px-2.5 py-1 rounded-md text-slate-300';

      document.getElementById('hero-title').innerHTML = isMr
        ? 'स्मार्ट 2D/3D बिल्डिंग प्लॅनिंग आणि <span class="text-amber-400">अचूक बांधकाम इस्टिमेट</span>'
        : 'Smart 2D/3D Building Plans & <span class="text-amber-400">Accurate Cost Estimates</span>';
      document.getElementById('hero-desc').innerText = isMr
        ? 'पाटील इन्फ्रा, धाराशिव तर्फे आम्ही फक्त 2D AutoCAD प्लॅनिंग, 3D SketchUp/Revit मॉडेलिंग आणि बँक लोन व बांधकामासाठी अचूक इस्टिमेट (Rate Analysis & BOQ) करून देतो.'
        : 'We specialize exclusively in Architectural 2D AutoCAD Drafting, 3D SketchUp & Revit BIM Modeling, and Bank/Construction Cost Estimation (BOQ & Rate Analysis) in Dharashiv.';
      document.getElementById('calc-title').innerText = isMr
        ? 'झटपट प्लॅनिंग फी व बांधकाम खर्च कॅल्क्युलेटर'
        : 'Instant Planning Fee & Construction Estimate';
      document.getElementById('port-title').innerText = isMr
        ? 'आमचे तयार केलेले 2D/3D प्लॅन्स आणि इस्टिमेट्स'
        : 'Completed 2D Plans, 3D Models & BOQ Sheets';
    }

    renderPortfolio();
    runCalc();
  </script>
</body>
</html>
"""

# Render inside Streamlit
components.html(website_html, height=2100, scrolling=True)
