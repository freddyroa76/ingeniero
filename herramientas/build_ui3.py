import json

with open('pipe_data.json', 'r', encoding='utf-8') as f:
    pipe_data_str = f.read()

html = f"""<!doctype html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="theme-color" content="#0F172A" />
    <meta name="robots" content="index, follow" />
    <meta name="author" content="Freddy Roa Monsalvo" />
    <title>Panhandle Hydraulics Calculator - Engineering Edition</title>
    <link rel="icon" type="image/x-icon" href="../images/logos/favicon.ico">
    <!-- Professional Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;500;600&family=Outfit:wght@400;500;600;700;800&display=swap" />
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;500;600&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet" media="print" onload="this.media='all'" />
    <noscript><link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;500;600&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet" /></noscript>
    <!-- Tailwind CDN -->
    <script>
      tailwind.config = {{
        theme: {{
          extend: {{
            colors: {{
              primary: "#0F172A",
              secondary: "#008F4C",
              accent: "#D4E157",
              background: "#F8FAFC",
              surface: "#ffffff",
              "text-primary": "#334155",
              "text-secondary": "#1E293B",
            }},
            fontFamily: {{
              heading: ["Outfit", "sans-serif"],
              sans: ["DM Sans", "sans-serif"],
            }},
          }},
        }},
      }};
    </script>
    <link rel="stylesheet" href="../tailwind_compiled.css" />
    <link rel="stylesheet" href="../custom_styles.css">
    <script src="js/common.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjs/11.8.0/math.js"></script>
  </head>
  <body class="bg-background text-text-primary">
    <a href="#main-content" class="sr-only focus:not-sr-only focus:absolute focus:top-2 focus:left-2 focus:z-[100] focus:bg-white focus:px-4 focus:py-2 focus:text-primary focus:rounded-md focus:shadow-lg focus:font-bold">Ir al contenido principal</a>
    <!-- Header -->
    <header class="fixed top-0 left-0 right-0 z-50 transition-all duration-300 shadow-md bg-surface">
      <div class="bg-[#0f172a] text-gray-300 text-xs py-2 border-b border-gray-800 hidden sm:block">
         <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex justify-between items-center gap-6">
            <span class="font-medium text-gray-300 tracking-wide">Ing. Mec Freddy Roa</span>
            <div class="flex items-center gap-6">
               <a href="mailto:freddy.roa76@gmail.com" class="hover:text-[#D4E157] transition-colors flex items-center gap-1">
                  <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
                  freddy.roa76@gmail.com
               </a>
            </div>
         </div>
      </div>
      <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 bg-white/95 backdrop-blur-md">
        <div class="flex items-center justify-end h-20">
          <div class="hidden sm:flex items-center space-x-4">
            <a href="../index.html" class="group-link">Inicio</a>
            <a href="../index.html#expertise" class="group-link">Expertise</a>
            <a href="../index.html#projects" class="group-link">Proyectos</a>
            <a href="../index.html#experience" class="group-link">Experiencia</a>
            <a href="../herramientas.html" class="group-link text-[#0F172A] font-bold">Herramientas</a>
            <a href="../index.html#contact" class="btn-contact-custom ml-4">CONTACTAR</a>
          </div>
          <div class="flex items-center sm:hidden">
            <button id="mobile-menu-button" type="button" class="inline-flex items-center justify-center p-2 rounded-md text-[#334155] hover:bg-gray-100 focus:outline-none transition-colors" aria-controls="mobile-menu" aria-expanded="false">
              <svg id="menu-icon" class="block h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
              </svg>
              <svg id="close-icon" class="hidden h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
              </svg>
            </button>
          </div>
        </div>
      </nav>
      <div id="mobile-menu" class="hidden sm:hidden bg-white border-t border-gray-100 overflow-y-auto max-h-[calc(100vh-80px)] shadow-xl">
        <div class="px-4 pt-4 pb-6 space-y-1">
          <a href="../index.html" class="text-[#0F172A] block px-3 py-3 rounded-md text-base font-bold">Inicio</a>
          <a href="../herramientas.html" class="text-[#0F172A] block px-3 py-3 rounded-md text-base font-bold bg-[#F1F5F9]">Herramientas</a>
        </div>
      </div>
    </header>

<main id="main-content" class="pt-32">
<section class="bg-background min-h-screen pt-4 pb-12"><div class="container mx-auto px-4 max-w-[1400px]">

      <!-- Breadcrumb -->
      <nav class="flex mb-6 text-xs font-medium text-gray-400" aria-label="Breadcrumb">
        <ol class="inline-flex items-center space-x-2">
          <li><a href="../index.html" class="text-gray-600 hover:text-primary transition-colors">Inicio</a></li>
          <li><span class="mx-2">/</span></li>
          <li><a href="../herramientas.html" class="text-gray-600 hover:text-primary transition-colors">Herramientas</a></li>
          <li><span class="mx-2">/</span></li>
          <li class="text-gray-900 font-bold">Cálculo hidráulico Panhandle</li>
        </ol>
      </nav>

      <div class="title-box mb-8">
        <h1 class="text-3xl font-bold tracking-tight text-gray-900" id="title">Panhandle Hydraulics Calculator</h1>
        <p class="text-gray-500 mt-2 text-sm font-medium" id="subtitle">Estimación hidráulica según AGA (Ecuación Panhandle A & B)</p>
      </div>

      <!-- Tabs Navigation -->
      <div class="mb-6 flex space-x-2 border-b border-gray-200 overflow-x-auto" id="tabs-container">
        <button class="py-2.5 px-5 font-bold border-b-2 text-sm tracking-wide transition-colors border-blue-600 text-blue-700 bg-blue-50/50 tab-btn whitespace-nowrap" onclick="switchTab(1)" id="tab-btn-1">
          1. Calcular Diámetro Mín.
        </button>
        <button class="py-2.5 px-5 font-bold border-b-2 text-sm tracking-wide transition-colors border-transparent text-gray-500 hover:text-blue-600 hover:bg-gray-50 tab-btn whitespace-nowrap" onclick="switchTab(2)" id="tab-btn-2">
          2. Calcular Presión de Llegada
        </button>
        <button class="py-2.5 px-5 font-bold border-b-2 text-sm tracking-wide transition-colors border-transparent text-gray-500 hover:text-blue-600 hover:bg-gray-50 tab-btn whitespace-nowrap" onclick="switchTab(3)" id="tab-btn-3">
          3. Diám. por Caída Tolerable
        </button>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <!-- Left Column: Gas Composition identical to 08_gas_compression -->
        <div class="lg:col-span-2 space-y-6">
            <div class="card">
                <div class="flex justify-between items-center mb-4">
                  <div>
                      <h2>Gas Composition</h2>
                      <p class="text-xs text-gray-500">Mole Fraction (Sum should be 1.0)</p>
                  </div>
                  <div class="flex flex-col items-end gap-1">
                    <div class="text-sm">
                        Sum: <span id="moleSum" class="font-mono font-bold text-orange-500">0.000000</span>
                    </div>
                    <div class="flex gap-2">
                      <button class="text-xs py-1.5 px-3 bg-blue-50 text-blue-700 hover:bg-blue-100 rounded-md border border-blue-200 font-medium transition-colors flex items-center gap-1" onclick="pasteFromExcel()" title="Paste column from Excel">
                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01"/></svg> Paste
                      </button>
                      <button class="text-xs py-1.5 px-3 bg-red-50 text-red-600 hover:bg-red-100 rounded-md border border-red-200 font-medium transition-colors" onclick="clearComposition()">Clear</button>
                    </div>
                  </div>
                </div>
                
                <div class="composition-grid" id="compGrid"></div>
            </div>
            
            <!-- RESULT CARD MOVED TO LEFT COLUMN BOTTOM -->
            <div id="resultsCard" class="card hidden animate-fade-in border-t-4 border-blue-600 p-0 overflow-hidden">
                <div class="bg-gray-50 border-b border-gray-200 px-6 py-4 flex justify-between items-center">
                    <h2 class="flex items-center gap-2 text-lg font-bold text-gray-800 m-0">
                        <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>
                        Resultados de Simulación
                    </h2>
                    <button onclick="window.print()" class="text-xs font-medium text-blue-600 hover:text-blue-800 flex items-center gap-1 print:hidden">
                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"/></svg>
                        Imprimir Memoria de Cálculo
                    </button>
                </div>
                
                <div id="tab1-results" class="hidden p-6">
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
                        <div class="bg-blue-50 border border-blue-100 rounded-lg p-5 relative overflow-hidden shadow-sm">
                             <p class="text-blue-800 text-xs font-bold uppercase tracking-wider mb-2">Diámetro Interno (Pan A)</p>
                             <p class="text-4xl font-extrabold text-blue-900 font-mono"><span id="dminA">-</span> <span class="text-lg text-blue-500 font-medium">in</span></p>
                        </div>
                        <div class="bg-indigo-50 border border-indigo-100 rounded-lg p-5 relative overflow-hidden shadow-sm">
                             <p class="text-indigo-800 text-xs font-bold uppercase tracking-wider mb-2">Diámetro Interno (Pan B)</p>
                             <p class="text-4xl font-extrabold text-indigo-900 font-mono"><span id="dminB">-</span> <span class="text-lg text-indigo-500 font-medium">in</span></p>
                        </div>
                    </div>
                </div>

                <div id="tab2-results" class="hidden p-6">
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
                        <div class="bg-blue-50 border border-blue-100 rounded-lg p-5 relative overflow-hidden shadow-sm">
                             <p class="text-blue-800 text-xs font-bold uppercase tracking-wider mb-2">P. Llegada (Pan A)</p>
                             <p class="text-4xl font-extrabold text-blue-900 font-mono"><span id="p2ResA">-</span> <span class="text-lg text-blue-500 font-medium">psig</span></p>
                             <p class="text-[10px] text-blue-600 mt-2 font-mono font-bold uppercase border-t border-blue-200/50 pt-2">Abs: <span id="p2ResAbsA">-</span> psia</p>
                        </div>
                        <div class="bg-indigo-50 border border-indigo-100 rounded-lg p-5 relative overflow-hidden shadow-sm">
                             <p class="text-indigo-800 text-xs font-bold uppercase tracking-wider mb-2">P. Llegada (Pan B)</p>
                             <p class="text-4xl font-extrabold text-indigo-900 font-mono"><span id="p2ResB">-</span> <span class="text-lg text-indigo-500 font-medium">psig</span></p>
                             <p class="text-[10px] text-indigo-600 mt-2 font-mono font-bold uppercase border-t border-indigo-200/50 pt-2">Abs: <span id="p2ResAbsB">-</span> psia</p>
                        </div>
                    </div>
                </div>

                <div id="tab3-results" class="hidden p-6">
                     <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
                        <div class="bg-blue-50 border border-blue-100 rounded-lg p-5 relative overflow-hidden shadow-sm">
                             <p class="text-blue-800 text-xs font-bold uppercase tracking-wider mb-2">Diámetro Interno (Pan A)</p>
                             <p class="text-4xl font-extrabold text-blue-900 font-mono"><span id="dminA_t3">-</span> <span class="text-lg text-blue-500 font-medium">in</span></p>
                        </div>
                        <div class="bg-indigo-50 border border-indigo-100 rounded-lg p-5 relative overflow-hidden shadow-sm">
                             <p class="text-indigo-800 text-xs font-bold uppercase tracking-wider mb-2">Diámetro Interno (Pan B)</p>
                             <p class="text-4xl font-extrabold text-indigo-900 font-mono"><span id="dminB_t3">-</span> <span class="text-lg text-indigo-500 font-medium">in</span></p>
                        </div>
                    </div>
                    
                    <div class="bg-gray-50 rounded-lg p-4 border border-gray-100">
                        <p class="text-sm text-gray-700 font-medium"><span class="font-bold">Target Arrival Pressure (P2):</span> <span id="targetP2_t3" class="font-mono font-bold text-green-600 ml-2 text-xl">-</span> psig</p>
                    </div>
                </div>

                <div class="p-6 border-t border-gray-100 bg-white grid grid-cols-1 md:grid-cols-3 gap-6">
                     <div>
                          <p class="text-[10px] tracking-widest text-gray-400 font-bold uppercase mb-1">Reynolds / Reg.</p>
                          <p class="text-lg font-bold text-gray-800 font-mono" id="res_reynolds">-</p>
                     </div>
                     <div>
                          <p class="text-[10px] tracking-widest text-gray-400 font-bold uppercase mb-1">Z Promedio</p>
                          <p class="text-lg font-bold text-gray-800 font-mono" id="res_z">-</p>
                     </div>
                     <div>
                          <p class="text-[10px] tracking-widest text-gray-400 font-bold uppercase mb-1">G (Gravedad Esp)</p>
                          <p class="text-lg font-bold text-gray-800 font-mono" id="res_sg">-</p>
                     </div>
                </div>
            </div>
        </div>

        <!-- Right Column: Operating Params -->
        <div>
            <div class="card sticky top-24 shadow-md border border-gray-100">
              <h2 class="mb-4">Operating Parameters</h2>
              <div class="space-y-4">
                <div class="grid grid-cols-2 gap-3 pb-3 border-b border-gray-100">
                    <div>
                        <label for="tb" class="block text-xs font-bold text-gray-700 mb-1">T Base <span class="text-gray-400 font-normal">(&deg;R)</span></label>
                        <input type="number" id="tb" value="520" class="w-full rounded border-gray-300 font-mono text-sm py-1.5 px-2 bg-gray-50" />
                    </div>
                    <div>
                        <label for="pb" class="block text-xs font-bold text-gray-700 mb-1">P Base <span class="text-gray-400 font-normal\">(psia)</span></label>
                        <input type="number" id="pb" value="14.73" step="0.01" class="w-full rounded border-gray-300 font-mono text-sm py-1.5 px-2 bg-gray-50" />
                    </div>
                </div>

                <div>
                  <label for="flow" class="block text-sm font-semibold text-gray-700 mb-1">Flow Rate (Q) <span class="text-red-500">*</span> <span class="text-blue-600 font-normal text-xs ml-1">(MMSCFD)</span></label>
                  <input type="number" id="flow" placeholder="Ej. 100" required class="w-full rounded-lg border-2 border-slate-300 focus:border-blue-600 focus:ring-blue-600 transition-all py-2.5 px-3 font-mono text-lg text-gray-900" />
                </div>
                
                <div>
                  <label for="linel" class="block text-sm font-semibold text-gray-700 mb-1">Line Length (L) <span class="text-red-500">*</span> <span class="text-blue-600 font-normal text-xs ml-1">(millas)</span></label>
                  <input type="number" id="linel" placeholder="Ej. 25" required class="w-full rounded-lg border-2 border-slate-300 focus:border-blue-600 focus:ring-blue-600 transition-all py-2.5 px-3 font-mono text-lg text-gray-900" />
                </div>

                <div>
                  <label for="tavg" class="block text-sm font-semibold text-gray-700 mb-1">Avg Flow Temp (T<sub>avg</sub>) <span class="text-red-500">*</span> <span class="text-blue-600 font-normal text-xs ml-1">(&deg;R)</span></label>
                  <input type="number" id="tavg" value="520" required class="w-full rounded-lg border-2 border-slate-300 focus:border-blue-600 focus:ring-blue-600 transition-all py-2.5 px-3 font-mono text-lg text-gray-900" />
                </div>

                <div class="grid grid-cols-3 gap-3 pb-3 border-b border-gray-100 mt-2">
                    <div>
                        <label for="zfactor" class="block text-[10px] font-bold text-gray-700 mb-1" title="Si deja en blanco, usa 0.9">Z Factor</label>
                        <input type="number" id="zfactor" placeholder="0.9" step="0.001" class="w-full rounded border-gray-300 font-mono text-xs py-1.5 px-2 bg-gray-50 text-gray-700" />
                    </div>
                    <div>
                        <label for="effA" class="block text-[10px] font-bold text-gray-700 mb-1">Eff (E) Pan A</label>
                        <input type="number" id="effA" value="0.92" step="0.01" class="w-full rounded border-gray-300 font-mono text-xs py-1.5 px-2 bg-gray-50 text-gray-700" />
                    </div>
                    <div>
                        <label for="effB" class="block text-[10px] font-bold text-gray-700 mb-1">Eff (E) Pan B</label>
                        <input type="number" id="effB" value="0.88" step="0.01" class="w-full rounded border-gray-300 font-mono text-xs py-1.5 px-2 bg-gray-50 text-gray-700" />
                    </div>
                </div>

                <div class="pt-2 border-t border-gray-100"></div>

                <div>
                  <label for="p1" class="block text-sm font-semibold text-gray-700 mb-1">Presión de Salida P1 (Upstream) <span class="text-red-500">*</span> <span class="text-blue-600 font-normal text-xs ml-1">(psig)</span></label>
                  <input type="number" id="p1" placeholder="Ej. 1200" required class="w-full rounded-lg border-2 border-slate-300 focus:border-green-600 focus:ring-green-600 transition-all py-2.5 px-3 font-mono text-lg text-gray-900" />
                </div>

                <div class="tab1-input">
                  <label for="p2" class="block text-sm font-semibold text-gray-700 mb-1">Presión de Llegada P2 <span class="text-red-500">*</span> <span class="text-blue-600 font-normal text-xs ml-1">(psig)</span></label>
                  <input type="number" id="p2" placeholder="Ej. 800" class="w-full rounded-lg border-2 border-slate-300 focus:border-green-600 focus:ring-green-600 transition-all py-2.5 px-3 font-mono text-lg text-gray-900" />
                </div>

                <div class="tab3-input hidden">
                  <label for="dropRate" class="block text-sm font-semibold text-gray-700 mb-1">Caída Tolerable (&Delta;P/L) <span class="text-red-500">*</span> <span class="text-blue-600 font-normal text-xs ml-1">(psig/milla)</span></label>
                  <input type="number" id="dropRate" value="5" class="w-full rounded-lg border-2 border-slate-300 focus:border-green-600 focus:ring-green-600 transition-all py-2.5 px-3 font-mono text-lg text-gray-900" />
                </div>

                <div class="tab2-input hidden space-y-4">
                    <h3 class="text-xs font-bold text-gray-400 uppercase tracking-wider mb-2 flex items-center gap-2 mt-4">
                        <span class="w-2 h-2 rounded-full bg-blue-500"></span> Selección de Tubería
                    </h3>
                    <div>
                        <label for="pipeSize" class="block text-sm font-semibold text-gray-700 mb-1">
                            Nominal Pipe Size (NPS) <span class="text-red-500">*</span>
                        </label>
                        <select id="pipeSize" onchange="updatePipeDimensions()" class="w-full rounded-lg border-2 border-slate-300 focus:border-blue-600 focus:ring-blue-600 py-2.5 px-3 bg-white text-gray-900">
                            <option value="">Select size</option>
                        </select>
                    </div>

                    <div>
                        <label for="schedule" class="block text-sm font-semibold text-gray-700 mb-1">
                            Schedule Reference <span class="text-red-500">*</span>
                        </label>
                        <select id="schedule" onchange="updateWallThickness()" disabled class="w-full rounded-lg border-2 border-slate-300 focus:border-blue-600 focus:ring-blue-600 py-2.5 px-3 bg-white disabled:bg-gray-100 text-gray-900">
                             <option value="">Select size first</option>
                        </select>
                    </div>

                    <div class="mt-2 flex items-center justify-between text-xs text-gray-600 bg-gray-50 rounded px-3 py-2 border border-blue-100">
                        <span>Internal Diameter (ID):</span>
                        <span class="font-bold text-blue-700 font-mono text-base"><span id="idDisplay">-</span> in</span>
                    </div>
                </div>

                <div class="pt-4 border-t border-gray-100 flex flex-col sm:flex-row gap-3 mt-4">
                  <button class="flex-1 w-full bg-primary text-accent hover:bg-slate-800 text-base font-bold py-3.5 px-6 rounded-xl shadow-md hover:shadow-lg transition-all duration-200 flex items-center justify-center gap-2" onclick="calculate()">
                    <svg class="w-5 h-5 cursor-pointer" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z"/></svg>
                    Calcular
                  </button>
                  <button class="flex-none bg-white text-slate-500 border border-slate-200 hover:bg-slate-50 hover:text-slate-700 font-semibold py-3.5 px-6 rounded-xl transition-all duration-200 flex items-center justify-center" onclick="clearFields()">
                    Limpiar
                  </button>
                </div>
              </div>
            </div>
        </div>
      </div>
    </div>
</section>
</main>
<footer id="contact" class="bg-gray-900 text-white border-t-4 border-[#008F4C]">
   <div class="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:px-8">
      <div class="flex flex-col flex-wrap justify-between items-center text-sm text-gray-500">
         <p class="mt-8 text-center text-sm text-gray-400">&copy; <span class="copyright-year">2026</span> Freddy Roa Monsalvo. Todos los derechos reservados.</p>
      </div>
   </div>
</footer>
<script>
    const pipeDimensions = {pipe_data_str};
    let currentTab = 1;
    let actualInternalDia = null;

    // Component grid definitions exact matching 08
    const components = [
      {{ id: "C1", formula: "CH₄", name: "Methane", mw: 16.043 }},
      {{ id: "N2", formula: "N₂", name: "Nitrogen", mw: 28.013 }},
      {{ id: "CO2", formula: "CO₂", name: "Carbon Dioxide", mw: 44.01 }},
      {{ id: "C2", formula: "C₂H₆", name: "Ethane", mw: 30.07 }},
      {{ id: "C3", formula: "C₃H₈", name: "Propane", mw: 44.097 }},
      {{ id: "H2O", formula: "H₂O", name: "Water", mw: 18.015 }},
      {{ id: "H2S", formula: "H₂S", name: "Hydrogen Sulfide", mw: 34.082 }},
      {{ id: "H2", formula: "H₂", name: "Hydrogen", mw: 2.016 }},
      {{ id: "CO", formula: "CO", name: "Carbon Monoxide", mw: 28.01 }},
      {{ id: "O2", formula: "O₂", name: "Oxygen", mw: 31.999 }},
      {{ id: "iC4", formula: "iC₄H₁₀", name: "i-Butane", mw: 58.123 }},
      {{ id: "nC4", formula: "nC₄H₁₀", name: "n-Butane", mw: 58.123 }},
      {{ id: "iC5", formula: "iC₅H₁₂", name: "i-Pentane", mw: 72.15 }},
      {{ id: "nC5", formula: "nC₅H₁₂", name: "n-Pentane", mw: 72.15 }},
      {{ id: "nC6", formula: "nC₆H₁₄", name: "n-Hexane", mw: 86.177 }},
      {{ id: "nC7", formula: "nC₇H₁₆", name: "n-Heptane", mw: 100.204 }},
      {{ id: "nC8", formula: "nC₈H₁₈", name: "n-Octane", mw: 114.231 }},
      {{ id: "nC9", formula: "nC₉H₂₀", name: "n-Nonane", mw: 128.258 }},
      {{ id: "nC10", formula: "nC₁₀H₂₂", name: "n-Decane", mw: 142.285 }},
      {{ id: "He", formula: "He", name: "Helium", mw: 4.003 }},
      {{ id: "Ar", formula: "Ar", name: "Argon", mw: 39.948 }}
    ];

    function initGasGrid() {{
        const grid = document.getElementById("compGrid");
        grid.innerHTML = `<div class=\"grid grid-cols-12 gap-2 text-[10px] font-bold text-gray-400 tracking-wider mb-2 px-2 uppercase\">
            <div class=\"col-span-2\">Formula</div><div class=\"col-span-4\">Name</div><div class=\"col-span-3 text-right pr-2\">Mole Fr.</div><div class=\"col-span-3 text-right\">MW</div>
        </div>`;
        components.forEach((comp) => {{
          const row = document.createElement("div");
          row.className = "grid grid-cols-12 gap-2 py-2.5 items-center border-t border-gray-100 hover:bg-gray-50 transition-colors px-2";
          row.innerHTML = `
            <div class="col-span-2 font-mono text-xs font-bold text-gray-700">${{comp.formula}}</div>
            <div class="col-span-4 text-sm text-gray-600">${{comp.name}}</div>
            <div class="col-span-3 text-right pr-2">
              <input type="number" id="mf_${{comp.id}}" step="0.000001" placeholder="0.000000" class="w-full text-right font-mono text-xs border border-gray-200 rounded py-1 px-1 focus:ring-blue-500 focus:border-blue-500 bg-white" oninput="updateTotal()" />
            </div>
            <div class="col-span-3 text-right font-mono text-xs text-gray-400">${{comp.mw.toFixed(1)}}</div>
          `;
          grid.appendChild(row);
        }});
    }}

    function initPipeSizes() {{
        const select = document.getElementById('pipeSize');
        for (const [size, data] of Object.entries(pipeDimensions)) {{
            let label = `NPS ${{size}}" (OD: ${{data.OD}}")`;
            select.add(new Option(label, size));
        }}
    }}

    function updatePipeDimensions() {{
        const sizeInput = document.getElementById('pipeSize').value;
        const scheduleSelect = document.getElementById('schedule');
        const idDisplay = document.getElementById('idDisplay');
        
        scheduleSelect.innerHTML = '<option value="">Select schedule</option>';
        idDisplay.textContent = '-';
        actualInternalDia = null;

        if (sizeInput && pipeDimensions[sizeInput]) {{
            scheduleSelect.disabled = false;
            for (const sched of Object.keys(pipeDimensions[sizeInput].schedules)) {{
                scheduleSelect.add(new Option(sched, sched));
            }}
        }} else {{
            scheduleSelect.disabled = true;
        }}
    }}

    function updateWallThickness() {{
        const sizeInput = document.getElementById('pipeSize').value;
        const schedInput = document.getElementById('schedule').value;
        const idDisplay = document.getElementById('idDisplay');

        if (sizeInput && schedInput && pipeDimensions[sizeInput].schedules[schedInput]) {{
            const od = pipeDimensions[sizeInput].OD;
            const wt = pipeDimensions[sizeInput].schedules[schedInput];
            actualInternalDia = od - (2 * wt);
            idDisplay.textContent = actualInternalDia.toFixed(3);
        }}
    }}

    function switchTab(t) {{
        currentTab = t;
        [1,2,3].forEach(i => {{
             document.getElementById('tab-btn-' + i).classList.remove('border-blue-600', 'text-blue-700', 'bg-blue-50/50');
             document.getElementById('tab-btn-' + i).classList.add('border-transparent', 'text-gray-500');
             document.querySelectorAll('.tab' + i + '-input').forEach(el => el.classList.add('hidden'));
             document.getElementById('tab' + i + '-results').classList.add('hidden');
        }});
        document.getElementById('tab-btn-' + t).classList.add('border-blue-600', 'text-blue-700', 'bg-blue-50/50');
        document.getElementById('tab-btn-' + t).classList.remove('border-transparent', 'text-gray-500');
        document.querySelectorAll('.tab' + t + '-input').forEach(el => el.classList.remove('hidden'));
        document.getElementById('resultsCard').classList.add('hidden');
    }}

    function updateTotal() {{
        let total = 0;
        components.forEach(c => {{
            const val = parseFloat(document.getElementById('mf_' + c.id).value);
            if (!isNaN(val)) {{ total += val; }}
        }});
        const span = document.getElementById('moleSum');
        span.textContent = total.toFixed(6);
        span.className = isValidComp() ? "font-mono font-bold text-green-600" : "font-mono font-bold text-red-500";
    }}

    function isValidComp() {{
        let total = 0;
        components.forEach(c => {{
            const val = parseFloat(document.getElementById('mf_' + c.id).value) || 0;
            total += val;
        }});
        return Math.abs(total - 1.0) < 0.0001;
    }}

    function pasteFromExcel() {{
        navigator.clipboard.readText().then(text => {{
            const values = text.split(/[\\r\\n\\t]+/).filter(v => v !== "");
            let idx = 0;
            components.forEach(c => {{
                if (idx < values.length) {{
                    const val = parseFloat(values[idx++].replace(',', '.'));
                    if (!isNaN(val)) document.getElementById('mf_' + c.id).value = val;
                }}
            }});
            updateTotal();
        }});
    }}

    function clearComposition() {{
        components.forEach(c => document.getElementById('mf_' + c.id).value = "");
        updateTotal();
    }}

    function clearFields() {{
        document.getElementById('p1').value = "";
        document.getElementById('p2').value = "";
        document.getElementById('flow').value = "";
        document.getElementById('linel').value = "";
        document.getElementById('pipeSize').value = "";
        updatePipeDimensions();
        document.getElementById('resultsCard').classList.add('hidden');
    }}

    // Hydraulic Logic via Panhandle
    function calculate() {{
        if (!isValidComp()) {{
            alert("La fracción molar debe sumar exactamente 1.0.");
            return;
        }}

        // Specific Gravity
        let mwMix = 0;
        components.forEach(c => {{
             let mf = parseFloat(document.getElementById('mf_' + c.id).value) || 0;
             mwMix += mf * c.mw;
        }});
        let sg = mwMix / 28.9625;
        
        let p1g = parseFloat(document.getElementById('p1').value);
        let tb = parseFloat(document.getElementById('tb').value);
        let pb = parseFloat(document.getElementById('pb').value);
        let tavg = parseFloat(document.getElementById('tavg').value);
        let flow = parseFloat(document.getElementById('flow').value);
        let l = parseFloat(document.getElementById('linel').value); // MILES!
        
        if (isNaN(p1g) || isNaN(tb) || isNaN(pb) || isNaN(tavg) || isNaN(l) || isNaN(flow)) {{
             alert("Complete todos los campos obligatorios.");
             return;
        }}

        let zStr = document.getElementById('zfactor').value;
        let z = zStr ? parseFloat(zStr) : 0.9;
        let faA = parseFloat(document.getElementById('effA').value) || 0.92;
        let faB = parseFloat(document.getElementById('effB').value) || 0.88; 
        
        document.getElementById('res_sg').textContent = sg.toFixed(4);
        document.getElementById('res_z').textContent = z.toFixed(3);

        if (currentTab === 1) {{
             let p2g = parseFloat(document.getElementById('p2').value);
             if (isNaN(p2g)) {{ alert("Ingrese Presión de Llegada P2"); return; }}
             let p1_abs = p1g + pb;
             let p2_abs = p2g + pb;
             if (p1_abs <= p2_abs) {{ alert("P1 debe ser mayor a P2"); return; }}

             let termA = ( Math.pow(p1_abs, 2) - Math.pow(p2_abs, 2) ) / ( Math.pow(sg, 0.8539) * tavg * l * z );
             let q_std = flow * 1e6; // scfd
             let resA = 435.87 * faA * (tb/pb);
             let dA_in = Math.pow( (q_std / resA) / Math.pow(termA, 0.5394) , 1/2.618 );

             let termB = ( Math.pow(p1_abs, 2) - Math.pow(p2_abs, 2) ) / ( Math.pow(sg, 0.961) * tavg * l * z );
             let resB = 737 * faB * (tb/pb);
             let dB_in = Math.pow( (q_std / resB) / Math.pow(termB, 0.510) , 1/2.53 );

             document.getElementById('dminA').textContent = dA_in.toFixed(3);
             document.getElementById('dminB').textContent = dB_in.toFixed(3);
             document.getElementById('res_reynolds').textContent = '-';
             document.getElementById('tab1-results').classList.remove('hidden');

        }} else if (currentTab === 2) {{
             if (!actualInternalDia) {{ alert("Seleccione tamaño de tubería nominal y cédula."); return; }}
             
             let p1_abs = p1g + pb;
             let id_in = actualInternalDia;
             let q_std = flow * 1e6;

             // Solve P2 Panhandle A
             let ca = 435.87 * faA * (tb/pb) * Math.pow(id_in, 2.618);
             let deltaA = Math.pow( q_std / ca , 1/0.5394 ) * ( Math.pow(sg, 0.8539) * tavg * l * z );
             let p2_sqA = Math.pow(p1_abs, 2) - deltaA;
             
             if (p2_sqA <= 0) {{
                 document.getElementById('p2ResA').textContent = "NO FLUYE";
                 document.getElementById('p2ResAbsA').textContent = "-";
             }} else {{
                 let p2A_abs = Math.sqrt(p2_sqA);
                 document.getElementById('p2ResA').textContent = (p2A_abs - pb).toFixed(1);
                 document.getElementById('p2ResAbsA').textContent = p2A_abs.toFixed(1);
             }}

             // Solve P2 Panhandle B
             let cb = 737 * faB * (tb/pb) * Math.pow(id_in, 2.53);
             let deltaB = Math.pow( q_std / cb , 1/0.510 ) * ( Math.pow(sg, 0.961) * tavg * l * z );
             let p2_sqB = Math.pow(p1_abs, 2) - deltaB;
             
             if (p2_sqB <= 0) {{
                 document.getElementById('p2ResB').textContent = "NO FLUYE";
                 document.getElementById('p2ResAbsB').textContent = "-";
             }} else {{
                 let p2B_abs = Math.sqrt(p2_sqB);
                 document.getElementById('p2ResB').textContent = (p2B_abs - pb).toFixed(1);
                 document.getElementById('p2ResAbsB').textContent = p2B_abs.toFixed(1);
             }}
             
             let Re = (20000 * flow * 1000 * sg) / id_in; 
             document.getElementById('res_reynolds').textContent = Re.toExponential(2);
             document.getElementById('tab2-results').classList.remove('hidden');

        }} else if (currentTab === 3) {{
             let dropRate = parseFloat(document.getElementById('dropRate').value);
             if (isNaN(dropRate)) {{ alert("Ingrese Caída Tolerable."); return; }}
             
             let p1_abs = p1g + pb;
             let p2g = p1g - (dropRate * l);
             if (p2g < 0) {{ alert("La caída tolerable genera una presión menor a 0. Reduzca la longitud o caída."); return; }}
             
             let p2_abs = p2g + pb;

             let termA = ( Math.pow(p1_abs, 2) - Math.pow(p2_abs, 2) ) / ( Math.pow(sg, 0.8539) * tavg * l * z );
             let q_std = flow * 1e6;
             let resA = 435.87 * faA * (tb/pb);
             let dA_in = Math.pow( (q_std / resA) / Math.pow(termA, 0.5394) , 1/2.618 );

             let termB = ( Math.pow(p1_abs, 2) - Math.pow(p2_abs, 2) ) / ( Math.pow(sg, 0.961) * tavg * l * z );
             let resB = 737 * faB * (tb/pb);
             let dB_in = Math.pow( (q_std / resB) / Math.pow(termB, 0.510) , 1/2.53 );

             document.getElementById('targetP2_t3').textContent = p2g.toFixed(1);
             document.getElementById('dminA_t3').textContent = dA_in.toFixed(3);
             document.getElementById('dminB_t3').textContent = dB_in.toFixed(3);
             document.getElementById('res_reynolds').textContent = '-';
             document.getElementById('tab3-results').classList.remove('hidden');
        }}

        document.getElementById('resultsCard').classList.remove('hidden');
        document.getElementById('resultsCard').scrollIntoView({{ behavior: 'smooth', block: 'start' }});
    }}

    initGasGrid();
    initPipeSizes();
    updateTotal();
</script>
</body>
</html>
"""

with open('13_panhandle_calculator.html', 'w', encoding='utf-8') as f:
    f.write(html)
