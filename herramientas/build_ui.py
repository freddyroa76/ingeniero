import re
import os

html_main = """<main id="main-content" class="pt-20">
  <section class="bg-background min-h-screen pt-8 pb-12">
    <div class="container mx-auto px-4 pt-2 pb-12 is-tool-content max-w-7xl">
      <!-- Breadcrumb -->
      <nav class="flex mb-6 text-xs font-medium text-gray-400 uppercase-none" aria-label="Breadcrumb">
        <ol class="inline-flex items-center space-x-2">
          <li><a href="../index.html" class="text-gray-600 hover:text-primary transition-colors">Inicio</a></li>
          <li><span class="mx-2">/</span></li>
          <li><a href="../herramientas.html" class="text-gray-600 hover:text-primary transition-colors">Herramientas</a></li>
          <li><span class="mx-2">/</span></li>
          <li class="text-gray-900 font-bold">Cálculo hidráulico Panhandle</li>
        </ol>
      </nav>

      <!-- Title Area -->
      <div class="title-box mb-8 relative z-10">
        <div class="flex justify-between items-start">
          <div>
            <h1 class="text-3xl font-bold tracking-tight text-gray-900" id="title">Panhandle Hydraulics Calculator</h1>
            <p class="text-gray-500 mt-2 text-sm font-medium" id="subtitle">Estimación hidráulica y diseño de gasoductos (Amercian Gas Association - Panhandle A & B)</p>
          </div>
        </div>
      </div>

      <!-- Tabs Navigation (Premium Style) -->
      <div class="mb-6 flex space-x-2 border-b border-gray-200 overflow-x-auto" id="tabs-container">
        <button class="py-2.5 px-5 font-bold border-b-2 text-sm uppercase tracking-wide transition-colors border-blue-600 text-blue-700 bg-blue-50/50 tab-btn whitespace-nowrap" onclick="switchTab(1)" id="tab-btn-1">
          1. Diámetro Mínimo
        </button>
        <button class="py-2.5 px-5 font-bold border-b-2 text-sm uppercase tracking-wide transition-colors border-transparent text-gray-500 hover:text-blue-600 hover:bg-gray-50 tab-btn whitespace-nowrap" onclick="switchTab(2)" id="tab-btn-2">
          2. Caudal & ErosionalVel
        </button>
        <button class="py-2.5 px-5 font-bold border-b-2 text-sm uppercase tracking-wide transition-colors border-transparent text-gray-500 hover:text-blue-600 hover:bg-gray-50 tab-btn whitespace-nowrap" onclick="switchTab(3)" id="tab-btn-3">
          3. Presión Llegada
        </button>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 lg:gap-8">
        <!-- Left Area (Gas Comp & Results) -->
        <div class="lg:col-span-8 flex flex-col gap-6">
            
            <!-- Gas Composition Card -->
            <div class="card shadow-sm border border-gray-100 rounded-xl overflow-hidden bg-white">
                <div class="px-5 py-4 border-b border-gray-100 flex justify-between items-center bg-gray-50/50">
                  <div>
                      <h2 class="m-0 text-base font-bold text-gray-800 flex items-center gap-2">
                        <svg class="w-4 h-4 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"/></svg>
                        Gas Composition
                      </h2>
                      <p class="text-xs text-gray-500 m-0 mt-0.5">Mole Fraction (Target Sum: 1.0)</p>
                  </div>
                  <div class="flex flex-col items-end gap-1.5">
                    <div class="text-[11px] font-bold text-gray-400 uppercase tracking-widest bg-gray-100 px-2 py-0.5 rounded">Total Sum: <span id="moleSum" class="font-mono text-orange-500 ml-1">0.0000</span></div>
                    <div class="flex gap-2 mt-1">
                      <button class="text-xs py-1 px-2.5 bg-blue-50 text-blue-700 hover:bg-blue-100 rounded border border-blue-200 font-medium transition-colors flex items-center gap-1 shadow-sm" onclick="pasteFromExcel()" title="Paste specific column from Excel (Ctrl+V)">
                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01"/></svg> Paste Moles
                      </button>
                      <button class="text-xs py-1 px-2.5 text-gray-500 hover:text-red-600 hover:bg-red-50 rounded border border-gray-200 hover:border-red-200 font-medium transition-colors" onclick="clearComposition()">Clear</button>
                    </div>
                  </div>
                </div>
                
                <div class="grid grid-cols-[60px_1fr_90px_50px] gap-2 text-[10px] font-bold text-gray-400 uppercase tracking-wider px-5 py-2 border-b border-gray-100 items-center bg-gray-50">
                    <div class="text-left">Symbol</div>
                    <div class="text-left pl-2">Component Name</div>
                    <div class="text-right pr-2">y (Frac)</div>
                    <div class="text-center">MW</div>
                </div>
                <div class="composition-grid space-y-0 text-sm max-h-[250px] overflow-y-auto w-full px-5 py-2 custom-scrollbar" id="compGrid"></div>
            </div>
            
            <!-- RESULTS CARD PRO (Matched to 08 styling) -->
            <div id="resultsCard" class="card shadow-xl border-t-4 border-blue-600 hidden bg-white rounded-xl overflow-hidden p-0 animate-fade-in relative z-10 transition-all duration-500">
                <div class="bg-gradient-to-r from-gray-50 to-white px-6 py-4 border-b border-gray-100 flex justify-between items-center relative isolation-auto">
                    <!-- Subtle background decoration -->
                    <div class="absolute right-0 top-0 opacity-5 pointer-events-none">
                        <svg width="150" height="100" viewBox="0 0 100 100"><circle cx="50" cy="50" r="40" fill="currentColor"/></svg>
                    </div>

                    <h2 class="text-lg font-bold text-gray-800 m-0 flex items-center gap-2">
                        <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                        Memoria de Cálculo Técnico
                    </h2>
                    <button onclick="window.print()" class="text-[11px] font-bold text-blue-600 hover:bg-blue-50 px-3 py-1.5 rounded-full border border-blue-200 transition-colors uppercase tracking-wider flex items-center gap-1.5 print:hidden">
                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"/></svg> Imprimir
                    </button>
                </div>
                
                <!-- CONTENT TAB 1: MÁX/MIN DIÁMETRO -->
                <div id="tab1-results" class="hidden p-6">
                    <div class="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
                        <!-- KPI A -->
                        <div class="bg-gradient-to-br from-blue-600 to-blue-700 p-4 rounded-xl text-white shadow-md relative overflow-hidden flex flex-col justify-between h-28 transform transition hover:scale-[1.02]">
                            <div class="absolute -right-6 -bottom-6 w-24 h-24 bg-white opacity-10 rounded-full blur-xl"></div>
                            <div>
                                <p class="text-[10px] text-blue-200 font-bold uppercase tracking-wider mb-1 drop-shadow-sm">Ø Mínimo Pan. A</p>
                                <div class="flex items-baseline gap-1">
                                    <span class="text-3xl font-bold font-mono text-white tracking-tight" id="dminA">-</span>
                                    <span class="text-sm font-medium text-blue-200 uppercase">pulg</span>
                                </div>
                            </div>
                        </div>

                        <!-- KPI B -->
                        <div class="bg-gradient-to-br from-indigo-500 to-indigo-600 p-4 rounded-xl text-white shadow-md relative overflow-hidden flex flex-col justify-between h-28 transform transition hover:scale-[1.02]">
                            <div class="absolute -right-6 -bottom-6 w-24 h-24 bg-white opacity-10 rounded-full blur-xl"></div>
                            <div>
                                <p class="text-[10px] text-indigo-200 font-bold uppercase tracking-wider mb-1 drop-shadow-sm">Ø Mínimo Pan. B</p>
                                <div class="flex items-baseline gap-1">
                                    <span class="text-3xl font-bold font-mono text-white tracking-tight" id="dminB">-</span>
                                    <span class="text-sm font-medium text-indigo-200 uppercase">pulg</span>
                                </div>
                            </div>
                        </div>

                        <!-- REYNOLDS -->
                        <div class="bg-gray-50 border border-gray-200 p-4 rounded-xl shadow-inner flex flex-col justify-between h-28">
                            <p class="text-[10px] text-gray-500 font-bold uppercase tracking-wider mb-1">Nº Reynolds</p>
                            <span class="text-xl font-bold font-mono text-gray-800" id="reynolds1">-</span>
                            <span class="text-[10px] text-gray-400 font-medium" id="eq_tab1_sub">Evaluando Régimen</span>
                        </div>

                        <!-- EVALUATION -->
                        <div class="bg-gray-50 border border-gray-200 p-4 rounded-xl shadow-inner flex flex-col justify-center h-28 items-center text-center">
                            <p class="text-[10px] text-gray-500 font-bold uppercase tracking-wider mb-1">Dictamen Tubería</p>
                            <span class="text-sm font-bold font-mono text-gray-700" id="evalD1">-</span>
                        </div>
                    </div>

                    <!-- Breakdown Table -->
                    <div class="border border-gray-100 rounded-lg overflow-hidden">
                        <div class="bg-gray-50 px-4 py-2 border-b border-gray-100">
                            <h3 class="text-xs font-bold text-gray-500 uppercase tracking-widest flex items-center gap-2">
                                <span class="w-1.5 h-1.5 bg-blue-500 rounded-full"></span> Parámetros de Diseño y Factores Críticos (AGA)
                            </h3>
                        </div>
                        <div class="grid grid-cols-1 lg:grid-cols-2 divide-y lg:divide-y-0 lg:divide-x divide-gray-100 text-sm text-gray-600 bg-white">
                            <div class="p-4 space-y-2.5">
                                <div class="flex justify-between items-center"><span class="font-medium">Gravedad Esp. (G):</span><span class="font-mono text-gray-900 font-bold" id="sg_tab1">-</span></div>
                                <div class="flex justify-between items-center"><span class="font-medium">Factor Z (Prom.):</span><span class="font-mono text-gray-900 font-bold" id="z_tab1">-</span></div>
                                <div class="flex justify-between items-center"><span class="font-medium">Ecuación Dictaminada:</span><span class="font-mono text-blue-700 font-bold bg-blue-50 px-2 py-0.5 rounded text-xs" id="eq_tab1">-</span></div>
                            </div>
                            <div class="p-4 space-y-2.5">
                                <div class="flex justify-between items-center border-t border-dashed border-gray-200 pt-2"><span class="font-medium">Q<sub>max</sub> Tubería Com. (A):</span><span class="font-mono text-green-700 font-bold"><span id="qA_com1">-</span> MMSCFD</span></div>
                                <div class="flex justify-between items-center"><span class="font-medium">Q<sub>max</sub> Tubería Com. (B):</span><span class="font-mono text-green-700 font-bold"><span id="qB_com1">-</span> MMSCFD</span></div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- CONTENT TAB 2: CAUDAL -->
                <div id="tab2-results" class="hidden p-6">
                    <div class="grid grid-cols-2 lg:grid-cols-4 gap-4 mb-6 text-center">
                        <div class="bg-gradient-to-b from-green-50 to-white border border-green-200 rounded-xl p-4 flex flex-col justify-center relative overflow-hidden">
                            <div class="text-[10px] text-green-600 font-bold uppercase mb-2 tracking-widest z-10">Caudal Panhandle A</div>
                            <div class="text-3xl font-bold font-mono text-green-700 leading-none z-10"><span id="qResA">-</span></div>
                            <div class="text-[10px] text-green-500 mt-1 uppercase tracking-wide font-bold z-10">MMSCFD</div>
                        </div>
                        <div class="bg-gradient-to-b from-emerald-50 to-white border border-emerald-200 rounded-xl p-4 flex flex-col justify-center relative overflow-hidden">
                            <div class="text-[10px] text-emerald-600 font-bold uppercase mb-2 tracking-widest z-10">Caudal Panhandle B</div>
                            <div class="text-3xl font-bold font-mono text-emerald-700 leading-none z-10"><span id="qResB">-</span></div>
                            <div class="text-[10px] text-emerald-500 mt-1 uppercase tracking-wide font-bold z-10">MMSCFD</div>
                        </div>
                        <div class="bg-red-50 border border-red-100 rounded-xl p-4 flex flex-col justify-center">
                            <div class="text-[10px] text-red-500 font-bold uppercase tracking-widest mb-1">Velocidad Erosional (API 14E)</div>
                            <div class="text-xl font-bold font-mono text-red-700 mt-1"><span id="veRes">-</span> <span class="text-sm">ft/s</span></div>
                        </div>
                        <div class="bg-gray-50 border border-gray-200 rounded-xl p-4 flex flex-col justify-center">
                            <div class="text-[10px] text-gray-500 font-bold uppercase tracking-widest mb-1">Límite Contrac. (50% Ve)</div>
                            <div class="text-xl font-bold font-mono text-gray-700 mt-1"><span id="vrRes">-</span> <span class="text-sm">ft/s</span></div>
                        </div>
                    </div>

                    <div class="bg-gray-900 border border-gray-700 rounded-lg p-4 mb-6 flex justify-between items-center shadow-inner">
                        <div class="flex items-center gap-3">
                            <div class="w-2 h-2 rounded-full bg-blue-400 animate-pulse"></div>
                            <span class="text-sm font-bold text-gray-300 uppercase tracking-widest">Est. Velocidad Real Operativa (P1)</span>
                        </div>
                        <span class="text-2xl font-mono font-bold text-blue-400" id="vActRes">- ft/s</span>
                    </div>

                    <div class="border border-gray-100 rounded-lg overflow-hidden">
                        <div class="bg-gray-50 px-4 py-2 border-b border-gray-100">
                            <h3 class="text-xs font-bold text-gray-500 uppercase tracking-widest flex items-center gap-2">
                                <span class="w-1.5 h-1.5 bg-green-500 rounded-full"></span> Evaluación Termodinámica & Régimen
                            </h3>
                        </div>
                        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 divide-y lg:divide-y-0 lg:divide-x divide-gray-100 text-sm text-gray-600 bg-white">
                            <div class="p-3 flex justify-between"><span class="font-medium text-xs text-gray-500 uppercase">Factor Z:</span><span class="font-mono font-bold text-gray-800" id="z_tab2">-</span></div>
                            <div class="p-3 flex justify-between"><span class="font-medium text-xs text-gray-500 uppercase">Reynolds:</span><span class="font-mono font-bold text-gray-800" id="reynolds2">-</span></div>
                            <div class="p-3 flex justify-between bg-blue-50/30"><span class="font-medium text-xs text-gray-500 uppercase">Se Sugiere:</span><span class="font-mono font-bold text-blue-700 text-xs" id="eq_tab2">-</span></div>
                        </div>
                    </div>
                </div>
                
                <!-- CONTENT TAB 3: PRESIÓN DE LLEGADA -->
                <div id="tab3-results" class="hidden p-6">
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
                        <div class="bg-white border-2 border-purple-100 rounded-2xl p-6 relative overflow-hidden shadow-sm hover:shadow-md transition-shadow">
                            <div class="absolute right-0 bottom-0 opacity-10">
                                <svg width="100" height="100" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 8v8"/><path d="M8 12h8"/></svg>
                            </div>
                            <div class="flex justify-between items-start mb-4">
                                <div class="text-[11px] text-purple-600 font-bold uppercase tracking-widest bg-purple-50 px-2 py-1 rounded inline-block border border-purple-100">Solución 1: Panhandle A</div>
                            </div>
                            <div class="flex items-end gap-2 text-purple-900 z-10 relative">
                                <span class="text-5xl font-black font-mono tracking-tighter" id="p2ResA">-</span>
                                <span class="text-sm font-bold uppercase mb-1">psig</span>
                            </div>
                            <div class="text-xs text-purple-500 mt-2 font-mono flex justify-between border-t border-purple-50 pt-2"><span class="uppercase font-bold tracking-wider">Presión Absoluta:</span> <span><span id="p2ResAbsA">-</span> psia</span></div>
                        </div>

                        <div class="bg-white border-2 border-indigo-100 rounded-2xl p-6 relative overflow-hidden shadow-sm hover:shadow-md transition-shadow">
                            <div class="absolute right-0 bottom-0 opacity-10">
                                <svg width="100" height="100" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
                            </div>
                            <div class="flex justify-between items-start mb-4">
                                <div class="text-[11px] text-indigo-600 font-bold uppercase tracking-widest bg-indigo-50 px-2 py-1 rounded inline-block border border-indigo-100">Solución 2: Panhandle B</div>
                            </div>
                            <div class="flex items-end gap-2 text-indigo-900 z-10 relative">
                                <span class="text-5xl font-black font-mono tracking-tighter" id="p2ResB">-</span>
                                <span class="text-sm font-bold uppercase mb-1">psig</span>
                            </div>
                            <div class="text-xs text-indigo-500 mt-2 font-mono flex justify-between border-t border-indigo-50 pt-2"><span class="uppercase font-bold tracking-wider">Presión Absoluta:</span> <span><span id="p2ResAbsB">-</span> psia</span></div>
                        </div>
                    </div>
                    
                    <div class="border border-gray-200 rounded-lg overflow-hidden bg-white shadow-sm">
                        <div class="grid grid-cols-1 md:grid-cols-2 text-sm text-gray-700">
                            <!-- Column 1 metrics -->
                            <div class="p-4 border-b md:border-b-0 md:border-r border-gray-200 space-y-3">
                                <div class="flex items-center justify-between"><span class="text-xs font-bold text-gray-500 uppercase tracking-wide">Factor Z Convergido:</span> <span class="font-mono text-blue-700 font-bold bg-blue-50 px-2 py-0.5 rounded" id="z_tab3">-</span></div>
                                <div class="flex items-center justify-between"><span class="text-xs font-bold text-gray-500 uppercase tracking-wide">Número Reynolds:</span> <span class="font-mono font-bold text-gray-800" id="reynolds3">-</span></div>
                            </div>
                            <!-- Column 2 metrics -->
                            <div class="p-4 bg-red-50/30 space-y-3">
                                <div class="flex items-center justify-between"><span class="text-[11px] font-bold text-red-500 uppercase tracking-wider">Diferencial (ΔP) Pan. A:</span> <span class="font-mono font-bold text-red-700" id="dpA_tab3">-</span></div>
                                <div class="flex items-center justify-between"><span class="text-[11px] font-bold text-red-500 uppercase tracking-wider">Diferencial (ΔP) Pan. B:</span> <span class="font-mono font-bold text-red-700" id="dpB_tab3">-</span></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Right Sidebar (Inputs) -->
        <div class="lg:col-span-4">
            <div class="card shadow-md border border-gray-200 rounded-xl bg-white sticky top-24">
              <h2 class="mb-4 pb-3 border-b border-gray-100 text-lg font-bold text-gray-800 flex items-center gap-2">
                 <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"/></svg>
                 Condiciones de Operación
              </h2>
              
              <div class="space-y-4">
                <!-- Base Conditions Section -->
                <div class="bg-gray-50 p-3 rounded-lg border border-gray-100 flex gap-3">
                    <div class="flex-1">
                        <label for="tb" class="block text-[10px] font-bold text-gray-500 uppercase tracking-wider mb-1">T Base (&deg;R)</label>
                        <input type="number" id="tb" value="520" class="w-full font-mono text-sm text-gray-600 bg-white border border-gray-200 rounded px-2 py-1.5 focus:border-blue-500 focus:ring-0" />
                    </div>
                    <div class="flex-1">
                        <label for="pb" class="block text-[10px] font-bold text-gray-500 uppercase tracking-wider mb-1">P Base (psia)</label>
                        <input type="number" id="pb" value="14.73" step="0.01" class="w-full font-mono text-sm text-gray-600 bg-white border border-gray-200 rounded px-2 py-1.5 focus:border-blue-500 focus:ring-0" />
                    </div>
                </div>
                
                <div class="grid gap-4 pt-1">
                    <div class="relative">
                      <label for="tavg" class="absolute -top-2 left-3 bg-white px-1 text-[10px] font-bold text-gray-500 uppercase tracking-wider z-10 required">Temperatura Prom. T<sub>avg</sub></label>
                      <div class="relative flex items-center">
                          <input type="number" id="tavg" placeholder="Ej. 520" required class="w-full font-mono font-bold text-lg border-2 border-gray-200 rounded-lg p-3 pt-3 pb-3 focus:border-blue-500 transition-colors" />
                          <span class="absolute right-4 font-bold text-gray-400 pointer-events-none">&deg;R</span>
                      </div>
                    </div>
                    
                    <div class="relative">
                      <label for="linel" class="absolute -top-2 left-3 bg-white px-1 text-[10px] font-bold text-gray-500 uppercase tracking-wider z-10 required">Longitud de Línea L</label>
                      <div class="relative flex items-center">
                          <input type="number" id="linel" placeholder="Distancia Total" required class="w-full font-mono font-bold text-lg border-2 border-gray-200 rounded-lg p-3 pt-3 pb-3 focus:border-blue-500 transition-colors" />
                          <span class="absolute right-4 font-bold text-gray-400 pointer-events-none">km</span>
                      </div>
                    </div>

                    <div class="relative tab1-input tab3-input">
                      <label for="p1" class="absolute -top-2 left-3 bg-white px-1 text-[10px] font-bold text-blue-600 uppercase tracking-wider z-10 required">Presión Entrada P1</label>
                      <div class="relative flex items-center">
                          <input type="number" id="p1" placeholder="P upstream" class="w-full font-mono font-bold text-lg border-2 border-blue-200 rounded-lg p-3 outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500 bg-blue-50/20" />
                          <span class="absolute right-4 font-bold text-blue-400 pointer-events-none">psig</span>
                      </div>
                    </div>

                    <div class="relative tab1-input tab2-input">
                      <label for="p2" class="absolute -top-2 left-3 bg-white px-1 text-[10px] font-bold text-blue-600 uppercase tracking-wider z-10 required">Presión Llegada P2</label>
                      <div class="relative flex items-center">
                          <input type="number" id="p2" placeholder="P downstream" class="w-full font-mono font-bold text-lg border-2 border-blue-200 rounded-lg p-3 outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500 bg-blue-50/20" />
                          <span class="absolute right-4 font-bold text-blue-400 pointer-events-none">psig</span>
                      </div>
                    </div>

                    <div class="relative tab1-input tab3-input">
                      <label for="flow" class="absolute -top-2 left-3 bg-white px-1 text-[10px] font-bold text-emerald-600 uppercase tracking-wider z-10 required">Caudal Q</label>
                      <div class="relative flex items-center">
                          <input type="number" id="flow" placeholder="Caudal deseado" class="w-full font-mono font-bold text-lg border-2 border-emerald-200 rounded-lg p-3 outline-none focus:border-emerald-500 focus:ring-1 focus:ring-emerald-500 bg-emerald-50/20" />
                          <span class="absolute right-4 font-bold text-emerald-400 pointer-events-none text-xs">MMSCFD</span>
                      </div>
                    </div>
                    
                    <!-- PIPE SECTION -->
                    <div class="border border-gray-200 rounded-lg p-3 bg-gray-50/50 mt-2 tab1-input tab2-input tab3-input" id="pipeSectionWrapper">
                        <label class="block text-xs font-bold text-gray-700 uppercase tracking-wider mb-2" id="pipeSectionLabel">Tubería de Evaluación <span class="text-[10px] font-normal text-gray-400 normal-case ml-1 relative -top-0.5">(ASME B36.10)</span></label>
                        <div class="flex flex-col gap-2">
                            <select id="pipeSize" class="w-full font-mono text-sm py-2.5 px-3 border border-gray-300 rounded focus:ring-blue-500 focus:border-blue-500 shadow-sm bg-white font-medium" onchange="updateWall()"></select>
                            <div class="flex gap-2 isolate">
                                <select id="schedule" class="font-mono text-sm py-2 px-3 border border-gray-300 rounded focus:ring-blue-500 focus:border-blue-500 flex-1 shadow-sm bg-white" onchange="updateWall()"></select>
                                <div class="bg-gray-800 text-white font-mono text-xs flex flex-col px-3 py-1 rounded w-24 border border-gray-700 text-center justify-center whitespace-nowrap shadow-inner">
                                    <span class="text-[9px] text-gray-400 uppercase tracking-wider mb-0.5 leading-none">Internal Ø</span>
                                    <span id="idDisplay" class="font-bold text-sm leading-none">-</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="pt-6 border-t border-gray-100 flex flex-col gap-3">
                  <button class="w-full py-4 text-base tracking-widest shadow-lg hover:shadow-xl transform transition-all hover:-translate-y-0.5 active:translate-y-0 bg-[#0F172A] hover:bg-[#1e293b] text-[#D4E157] rounded-lg font-black uppercase overflow-hidden relative group" onclick="calculate()">
                    <span class="absolute inset-0 w-full h-full bg-gradient-to-r from-transparent via-[#D4E157]/20 to-transparent -translate-x-[150%] skew-x-[-15deg] group-hover:transition-transform group-hover:duration-700 group-hover:translate-x-[150%]"></span>
                    <div class="flex items-center justify-center gap-2 relative z-10">
                        <svg class="w-5 h-5 text-current" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                        Ejecutar Simulación
                    </div>
                  </button>
                  <button class="w-full py-2.5 text-sm text-gray-500 hover:text-red-600 bg-white hover:bg-red-50 border border-gray-200 hover:border-red-200 rounded-lg font-bold transition-all" onclick="clearFields()">
                    Limpiar Entradas
                  </button>
                </div>
              </div>
            </div>
        </div>
      </div>
    </div>
  </section>
</main>"""

with open('13_panhandle_calculator.html', 'r', encoding='utf-8') as f:
    text = f.read()

# I will replace the <main>...</main> section explicitly avoiding messing up the header and footer scripts.
start_main = text.find('<main')
end_main = text.find('</main>') + len('</main>')

new_text = text[:start_main] + html_main + text[end_main:]

with open('13_panhandle_calculator.html', 'w', encoding='utf-8') as f:
    f.write(new_text)
