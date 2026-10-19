import streamlit as st
import streamlit.components.v1 as components

# 1. Page Configuration
st.set_page_config(
    page_title="Patil Infra | Dharashiv - 2D/3D Planning & Estimation",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Hide Streamlit's default header, footer, and padding for a pure website look
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

# 3. Complete Patil Infra Website (HTML + Tailwind + React) embedded inside Streamlit
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
          <p id="nav-sub" class="text-[11px] text-slate-400">Architectural 2D/3D Planning, BIM & Cost Estimation</p>
        </div>
      </div>

      <!-- RIGHT CONTROLS: SMALL MARATHI TOGGLE & OWNER LOCK -->
      <div class="flex items-center gap-2">
        <div class="bg-slate-800 p-0.5 rounded-lg border border-slate-700 flex text-xs font-bold">
          <button onclick="setLang('en')" id="btn-en" class="px-2.5 py-1 rounded-md bg-amber-500 text-slate-950 transition">EN</button>
          <button onclick="setLang('mr')" id="btn-mr" class="px-2.5 py-1 rounded-md text-slate-300 hover:text-white transition">मराठी</button>
        </div>
        <button onclick="toggleOwnerModal()" title="Owner Login (PIN: 2026)" class="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 text-xs">
          🔒
        </button>
      </div>
    </div>
  </nav>

  <!-- HERO SECTION -->
  <section class="bg-[#0f172a] text-white py-14 px-4 border-b border-slate-800">
    <div class="max-w-7xl mx-auto grid md:grid-cols-2 gap-10 items-center">
      <div>
        <span class="inline-block text-xs font-bold uppercase tracking-widest bg-amber-500/10 text-amber-400 border border-amber-500/30 px-3 py-1 rounded-full mb-4" id="hero-badge">
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
          <a href="#portfolio" class="bg-slate-800 hover:bg-slate-700 text-white font-semibold px-5 py-3 rounded-xl text-sm border border-slate-700">
            📐 View Our Uploaded Plans
          </a>
        </div>
      </div>

      <!-- QUICK SERVICE CARDS -->
      <div class="grid grid-cols-2 gap-4">
        <div class="bg-slate-800/90 border border-slate-700 p-4 rounded-2xl">
          <div class="text-amber-400 text-xl mb-1">📐</div>
          <h3 class="font-bold text-sm mb-1" id="srv1-t">2D AutoCAD Planning</h3>
          <p class="text-xs text-slate-400" id="srv1-d">Vastu-compliant floor plans, column layout & municipal blueprints.</p>
        </div>
        <div class="bg-slate-800/90 border border-slate-700 p-4 rounded-2xl">
          <div class="text-sky-400 text-xl mb-1">🏠</div>
          <h3 class="font-bold text-sm mb-1" id="srv2-t">3D Elevation & Revit BIM</h3>
          <p class="text-xs text-slate-400" id="srv2-d">Realistic 3D exterior views, wall schedules & walkthrough models.</p>
        </div>
        <div class="bg-slate-800/90 border border-slate-700 p-4 rounded-2xl">
          <div class="text-emerald-400 text-xl mb-1">📊</div>
          <h3 class="font-bold text-sm mb-1" id="srv3-t">Detailed Cost Estimation</h3>
          <p class="text-xs text-slate-400" id="srv3-d">Exact RCC & Brickwork Rate Analysis, Material BOQ & Abstract sheets.</p>
        </div>
        <div class="bg-slate-800/90 border border-slate-700 p-4 rounded-2xl">
          <div class="text-purple-400 text-xl mb-1">🏦</div>
          <h3 class="font-bold text-sm mb-1" id="srv4-t">Bank Loan Valuation</h3>
          <p class="text-xs text-slate-400" id="srv4-d">Standardized engineer estimate sheets ready for home loan approval.</p>
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
          Auto-calculates BOQ + Consultancy Fee
        </span>
      </div>

      <div class="grid lg:grid-cols-12 gap-8 mt-6">
        <!-- INPUTS -->
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
                <option value="1">Ground Floor Only (G)</option>
                <option value="2">G + 1 (Duplex / 2 Floors)</option>
                <option value="3">G + 2 (3 Floors)</option>
              </select>
            </div>
            <div>
              <label class="block text-xs font-bold text-slate-600 uppercase mb-1">Required Package</label>
              <select id="pkg" onchange="runCalc()" class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 font-semibold text-sm">
                <option value="2d">Only 2D Floor Plan (₹4/sq.ft)</option>
                <option value="est">Only Cost Estimate & BOQ (₹3/sq.ft)</option>
                <option value="combo" selected>2D Plan + 3D + Full Estimate (₹9/sq.ft)</option>
                <option value="bim">Complete Revit BIM + BOQ Package (₹12/sq.ft)</option>
              </select>
            </div>
          </div>

          <div class="grid grid-cols-2 gap-4 pt-2">
            <input type="text" id="clientName" placeholder="Your Full Name" class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 text-sm"/>
            <input type="text" id="clientPhone" placeholder="WhatsApp Number" class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 text-sm"/>
          </div>

          <button onclick="sendWhatsAppQuote()" class="w-full gold-gradient text-slate-950 font-extrabold py-3 rounded-xl text-sm shadow-md hover:opacity-95 transition">
            📲 Get Official Quotation & Send to WhatsApp
          </button>
        </div>

        <!-- OUTPUT SLIP -->
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
            <span>📍 Patil Infra Consultancy, Dharashiv</span>
            <button onclick="window.print()" class="text-amber-400 hover:underline font-semibold">🖨️ Print Slip</button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- OWNER PRIVATE UPLOAD STUDIO (HIDDEN BY DEFAULT, UNLOCKS WITH PIN 2026) -->
  <section id="ownerPanel" class="hidden py-6 px-4 max-w-7xl mx-auto">
    <div class="bg-amber-50 border-2 border-amber-400 rounded-2xl p-6">
      <div class="flex items-center justify-between mb-4">
        <div>
          <span class="text-xs font-extrabold uppercase bg-amber-500 text-slate-950 px-2.5 py-0.5 rounded">🔓 Owner Admin Mode Active</span>
          <h3 class="text-lg font-extrabold text-slate-900 mt-1">Upload Your 2D/3D Plans & Estimates (Only Visible to You)</h3>
        </div>
        <button onclick="lockOwner()" class="text-xs bg-slate-900 text-white px-3 py-1.5 rounded-lg font-bold">Lock Panel 🔒</button>
      </div>
      <div class="grid sm:grid-cols-4 gap-3">
        <input id="upTitle" type="text" placeholder="Project Title (e.g. 30x40 G+1 Plan)" class="px-3 py-2 rounded-xl border border-slate-300 text-sm bg-white"/>
        <select id="upType" class="px-3 py-2 rounded-xl border border-slate-300 text-sm bg-white font-semibold">
          <option value="2D AutoCAD Plan">2D AutoCAD Plan</option>
          <option value="3D Revit / SketchUp">3D Revit / SketchUp</option>
          <option value="BOQ & Cost Estimate">BOQ & Cost Estimate</option>
        </select>
        <input id="upSpecs" type="text" placeholder="Details (e.g. East Facing, ₹22L BOQ)" class="px-3 py-2 rounded-xl border border-slate-300 text-sm bg-white"/>
        <input id="upFile" type="file" accept="image/*" class="text-xs bg-white p-1.5 rounded-xl border border-slate-300"/>
      </div>
      <button onclick="addOwnerProject()" class="mt-3 bg-slate-900 text-amber-400 font-bold px-5 py-2 rounded-xl text-xs">
        ➕ Publish Plan to Portfolio
      </button>
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

  <!-- OWNER PIN MODAL -->
  <div id="pinModal" class="hidden fixed inset-0 bg-slate-950/75 z-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl max-w-xs w-full p-6 text-center shadow-2xl">
      <h4 class="font-extrabold text-slate-900 text-base mb-1">Owner Studio Login</h4>
      <p class="text-xs text-slate-500 mb-4">Enter Owner PIN to upload new plans (Default PIN: <b>2026</b>)</p>
      <input id="pinInput" type="password" placeholder="Enter PIN" class="w-full px-3 py-2 border border-slate-300 rounded-xl text-center font-bold mb-3"/>
      <div class="flex gap-2">
        <button onclick="toggleOwnerModal()" class="w-1/2 py-2 rounded-xl bg-slate-100 text-xs font-bold">Cancel</button>
        <button onclick="verifyPin()" class="w-1/2 py-2 rounded-xl gold-gradient text-slate-950 text-xs font-extrabold">Unlock</button>
      </div>
    </div>
  </div>

  <!-- FOOTER -->
  <footer class="bg-[#0b1324] text-slate-400 py-8 px-4 text-center text-xs border-t border-slate-800 mt-10">
    <p class="font-bold text-white text-sm mb-1">PATIL INFRA — DHARASHIV (OSMANABAD)</p>
    <p>Architectural 2D/3D Planning • Autodesk Revit BIM • Detailed Civil Cost Estimation & Rate Analysis</p>
  </footer>

  <script>
    let projects = [
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

    function renderPortfolio() {
      const grid = document.getElementById('portfolioGrid');
      grid.innerHTML = projects.map(p => `
        <div class="bg-white rounded-2xl overflow-hidden shadow-md border border-slate-200 flex flex-col justify-between">
          <div>
            <img src="${p.img}" class="w-full h-44 object-cover" alt="${p.title}"/>
            <div class="p-4">
              <span class="text-[10px] font-bold uppercase bg-amber-100 text-amber-800 px-2.5 py-0.5 rounded-full">${p.type}</span>
              <h3 class="font-extrabold text-slate-900 text-base mt-2">${p.title}</h3>
              <p class="text-xs text-slate-500 mt-1">${p.specs}</p>
            </div>
          </div>
        </div>
      `).join('');
    }

    function runCalc() {
      const w = parseFloat(document.getElementById('plotW').value) || 0;
      const l = parseFloat(document.getElementById('plotL').value) || 0;
      const f = parseInt(document.getElementById('floors').value) || 1;
      const pkg = document.getElementById('pkg').value;

      const builtUp = Math.round(w * l * 0.8 * f);
      const rateMap = { '2d': 4, 'est': 3, 'combo': 9, 'bim': 12 };
      const fee = builtUp * (rateMap[pkg] || 9);
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
      const name = document.getElementById('clientName').value || 'Client';
      const area = document.getElementById('areaBadge').innerText;
      const fee = document.getElementById('outFee').innerText;
      const msg = encodeURIComponent(`Hello Patil Infra Dharashiv! I am ${name}. I need a Plan/Estimate (${area}). Automated Consultancy Fee Quote: ${fee}.`);
      window.open(`https://wa.me/919000000000?text=${msg}`, '_blank');
    }

    function toggleOwnerModal() {
      document.getElementById('pinModal').classList.toggle('hidden');
    }

    function verifyPin() {
      const pin = document.getElementById('pinInput').value;
      if (pin === '2026') {
        document.getElementById('ownerPanel').classList.remove('hidden');
        document.getElementById('pinModal').classList.add('hidden');
      } else {
        alert('Incorrect Owner PIN!');
      }
    }

    function lockOwner() {
      document.getElementById('ownerPanel').classList.add('hidden');
    }

    function addOwnerProject() {
      const title = document.getElementById('upTitle').value;
      const type = document.getElementById('upType').value;
      const specs = document.getElementById('upSpecs').value;
      const fileInput = document.getElementById('upFile');
      if (!title) return alert('Please enter project title!');

      if (fileInput.files && fileInput.files[0]) {
        const reader = new FileReader();
        reader.onload = function(e) {
          projects.unshift({ title, type, specs, img: e.target.result });
          renderPortfolio();
        };
        reader.readAsDataURL(fileInput.files[0]);
      } else {
        projects.unshift({
          title, type, specs,
          img: "https://images.unsplash.com/photo-1503387762-592deb58ef4e?auto=format&fit=crop&w=800&q=80"
        });
        renderPortfolio();
      }
      document.getElementById('upTitle').value = '';
      document.getElementById('upSpecs').value = '';
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

# Render the full website smoothly inside Streamlit
components.html(website_html, height=1950, scrolling=True)