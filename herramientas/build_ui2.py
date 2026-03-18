import os

# HTML MAIN to be substituted replacing the whole <main> block
html_main = """<main id="main-content" class="pt-20">
<section class="bg-background min-h-screen pt-8 pb-12"><div class="container mx-auto px-4 pt-2 pb-12 is-tool-content max-w-7xl">
      <!-- Breadcrumb -->
      <nav class="flex mb-6 text-xs font-medium text-gray-400 uppercase-none" aria-label="Breadcrumb">
        <ol class="inline-flex items-center space-x-2">
          <li><a href="../index.html" class="text-gray-600 hover:text-primary transition-colors">Inicio</a></li>
          <li><span class="mx-2">/</span></li>
          <li><a href="../herramientas.html" class="text-gray-600 hover:text-primary transition-colors">Herramientas</a></li>
          <li><span class="mx-2">/</span></li>
          <li class="text-gray-900 font-bold">Cálculo de Compresión Panhandle</li>
        </ol>
      </nav>

      <div class="title-box mb-8 relative z-10">
        <h1 class="text-3xl font-bold tracking-tight text-gray-900" id="title">Panhandle Hydraulics Calculator</h1>
        <p class="text-gray-500 mt-2 text-sm font-medium" id="subtitle">Estimación hidráulica y diseño de gasoductos (American Gas Association)</p>
      </div>

      <!-- Tabs Navigation -->
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

      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <!-- Left Column: Gas Comp & Grid -->
        <div class="lg:col-span-2">
            <div class="card">
                <div class="flex justify-between items-center mb-4">
                  <div>
                      <h2>Gas Composition</h2>
                      <p class="text-xs text-gray-500">Mole Fraction (Sum should be 1.0)</p>
                  </div>
                  <div class="flex flex-col items-end gap-1">
                    <div class="text-sm">
                        Sum: <span id="moleSum" class="font-mono">0.0000</span>
                    </div>
                    <div class="flex gap-2">
                      <button class="text-xs py-1.5 px-3 bg-blue-50 text-blue-700 hover:bg-blue-100 rounded-md border border-blue-200 font-medium transition-colors flex items-center gap-1" onclick="pasteFromExcel()" title="Paste column from Excel">
                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01"/></svg> Paste
                      </button>
                      <button class="text-xs py-1.5 px-3 bg-red-50 text-red-600 hover:bg-red-100 rounded-md border border-red-200 font-medium transition-colors" onclick="clearComposition()">Clear</button>
                    </div>
                  </div>
                </div>
                <!-- Grilla de compuestos -->
                <div class="composition-grid" id="compGrid"></div>
            </div>
        </div>

        <!-- Right Column: Operating Params -->
        <div>
            <div class="card sticky top-24">
              <h2>Operating Parameters</h2>
              <div class="space-y-4">
                
                <div class="grid grid-cols-2 gap-3">
                    <div class="input-group">
                        <label for="tb" class="font-bold text-gray-700 text-xs">T Base <span class="units font-normal">(&deg;R)</span></label>
                        <input type="number" id="tb" value="520" class="font-mono text-sm" />
                    </div>
                    <div class="input-group">
                        <label for="pb" class="font-bold text-gray-700 text-xs">P Base <span class="units font-normal">(psia)</span></label>
                        <input type="number" id="pb" value="14.73" step="0.01" class="font-mono text-sm" />
                    </div>
                </div>
                
                <div class="input-group">
                  <label for="tavg" class="required font-bold text-gray-700">Avg Temp. <span class="units font-normal">(&deg;R)</span></label>
                  <input type="number" id="tavg" placeholder="Tavg" required class="font-mono text-lg" />
                </div>
                
                <div class="input-group">
                  <label for="linel" class="required font-bold text-gray-700">Line Length L <span class="units font-normal">(km)</span></label>
                  <input type="number" id="linel" placeholder="Distancia" required class="font-mono text-lg" />
                </div>

                <div class="input-group tab1-input tab3-input">
                  <label for="p1" class="required font-bold text-gray-700">Inlet P1 <span class="units font-normal">(psig)</span></label>
                  <input type="number" id="p1" placeholder="P upstream" class="font-mono text-lg" />
                </div>

                <div class="input-group tab1-input tab2-input">
                  <label for="p2" class="required font-bold text-gray-700">Arrival P2 <span class="units font-normal">(psig)</span></label>
                  <input type="number" id="p2" placeholder="P downstream" class="font-mono text-lg" />
                </div>

                <div class="input-group tab1-input tab3-input">
                  <label for="flow" class="required font-bold text-gray-700">Flow Rate Q <span class="units font-normal">(MMSCFD)</span></label>
                  <input type="number" id="flow" placeholder="Q" class="font-mono text-lg" />
                </div>
                
                <div class="input-group tab1-input tab2-input tab3-input" id="pipeSectionWrapper">
                  <label class="required font-bold text-gray-700" id="pipeSectionLabel">Pipe Size <span class="text-xs text-gray-400 font-normal">(ASME B36.10)</span></label>
                  <select id="pipeSize" class="w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 font-mono text-sm py-2" onchange="updateWall()"></select>
                  
                  <div class="grid grid-cols-2 gap-4 mt-2">
                      <div class="input-group">
                          <label class="text-xs text-gray-600">Schedule</label>
                          <select id="schedule" class="w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 font-mono text-sm py-2" onchange="updateWall()"></select>
                      </div>
                      <div class="input-group">
                          <label class="text-xs text-gray-600" for="idDisplay">Internal Diameter(in)</label>
                          <input type="text" id="idDisplay" class="text-sm py-2 bg-gray-50 text-gray-500 font-mono cursor-not-allowed w-full border border-gray-300 rounded" readonly placeholder="-" />
                      </div>
                  </div>
                </div>

                <div class="pt-4 border-t border-gray-100 flex flex-col gap-3">
                  <button id="calculateBtn" class="w-full py-3 text-lg shadow-lg hover:shadow-xl transform transition-all active:scale-[0.98]" onclick="calculate()">
                    Run Calculation
                  </button>
                  <button class="w-full py-2 text-sm text-gray-500 hover:text-gray-700 bg-transparent hover:bg-gray-50 rounded" onclick="clearFields()">
                    Reset Form
                  </button>
                </div>
              </div>
            </div>
        </div>
      </div>

       <!-- RESULTS GRID PRO IDENTICO AL A08 -->
       <div id="resultsCard" class="card hidden animate-fade-in mt-6 border-t-4 border-blue-600 shadow-lg p-0 overflow-hidden bg-white">
            <div class="bg-gray-50 border-b border-gray-200 px-6 py-4 flex justify-between items-center">
                <h2 class="flex items-center gap-2 text-lg font-bold text-gray-800 m-0">
                    <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>
                    Simulation Results
                </h2>
                <button onclick="window.print()" class="text-xs font-medium text-blue-600 hover:text-blue-800 flex items-center gap-1">
                    <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"/></svg>
                    Imprimir Memoria de Cálculo
                </button>
            </div>
            
            <div id="tab1-results" class="hidden p-6">
                <!-- Top KPIs (4 cols) -->
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
                    <!-- KPI A -->
                    <div class="bg-gradient-to-br from-blue-600 to-blue-700 rounded-lg p-4 text-white shadow-md relative overflow-hidden flex flex-col justify-between h-32">
                         <div class="relative z-10">
                            <p class="text-blue-100 text-xs font-bold uppercase tracking-wider mb-1">D-Min (Pan. A)</p>
                            <div class="flex items-baseline gap-2">
                                 <span id="dminA" class="text-3xl font-bold tracking-tight text-white font-mono">-</span>
                                 <span class="text-lg text-blue-200 font-medium">in</span>
                            </div>
                         </div>
                    </div>
                    
                    <!-- KPI B -->
                    <div class="bg-white border border-gray-200 rounded-lg p-4 shadow-sm relative flex flex-col justify-between h-32 hover:border-blue-300 transition-colors">
                         <div>
                            <p class="text-gray-500 text-xs font-bold uppercase tracking-wider mb-1">D-Min (Pan. B)</p>
                            <div class="flex items-baseline gap-2">
                                <span id="dminB" class="text-3xl font-bold text-gray-800 font-mono">-</span>
                                <span class="text-lg text-gray-400 font-medium">in</span>
                            </div>
                         </div>
                    </div>

                    <!-- Reynolds -->
                    <div class="bg-purple-50 border border-purple-100 rounded-lg p-4 shadow-sm flex flex-col justify-between h-32 relative overflow-hidden">
                         <div>
                            <p class="text-purple-800 text-xs font-bold uppercase tracking-wider mb-1">Reynolds Number</p>
                            <div class="flex items-baseline gap-2">
                                <span id="reynolds1" class="text-2xl font-bold text-gray-800 font-mono">-</span>
                            </div>
                         </div>
                         <span class="text-xs text-purple-400 font-medium self-end capitalize" id="eq_tab1_sub">Evaluando Régimen</span>
                    </div>

                    <!-- Evaluation -->
                    <div class="bg-gray-50 border border-gray-200 rounded-lg p-4 shadow-inner flex flex-col justify-between h-32 items-center text-center">
                         <div class="flex flex-col h-full justify-center">
                            <p class="text-gray-500 text-xs font-bold uppercase tracking-wider mb-2">Dictamen Comercial</p>
                            <div class="flex items-baseline gap-2 justify-center">
                                <span id="evalD1" class="text-sm font-bold text-gray-700 font-mono">-</span>
                            </div>
                         </div>
                    </div>
                </div>

                <!-- Detailed Tables (3 Cols inside grid) -->
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 border-t border-gray-100 pt-6">
                    <div>
                        <h3 class="text-xs font-bold text-gray-400 uppercase tracking-widest mb-4 flex items-center gap-2">
                            <span class="w-2 h-2 bg-blue-500 rounded-full"></span> Termodinámica
                        </h3>
                        <div class="space-y-0">
                             <div class="flex justify-between items-center py-2 border-b border-gray-100">
                                <span class="text-sm text-gray-600 font-medium">Specific Gravity (G)</span>
                                <span class="text-base font-bold text-gray-800 font-mono" id="sg_tab1">-</span>
                             </div>
                             <div class="flex justify-between items-center py-2 border-b border-gray-100">
                                <span class="text-sm text-gray-600 font-medium">Avg Compressibility (Z)</span>
                                <span class="text-base font-bold text-blue-600 font-mono" id="z_tab1">-</span>
                             </div>
                             <div class="flex justify-between items-center py-2 border-b border-gray-100">
                                <span class="text-sm text-gray-600 font-medium">Recom. Equation</span>
                                <span class="text-base font-bold text-purple-600 font-mono" id="eq_tab1">-</span>
                             </div>
                        </div>
                    </div>
                    <div>
                        <h3 class="text-xs font-bold text-gray-400 uppercase tracking-widest mb-4 flex items-center gap-2">
                            <span class="w-2 h-2 bg-purple-500 rounded-full"></span> Assessment
                        </h3>
                        <div class="space-y-0">
                             <div class="flex justify-between items-center py-2 border-b border-gray-100">
                                <span class="text-sm text-gray-600 font-medium">Eff. Factor (A/B)</span>
                                <div class="text-right">
                                    <span class="text-base font-bold text-gray-800 block leading-none font-mono"><span id="faA_tab1">-</span> / <span id="faB_tab1">-</span></span>
                                </div>
                             </div>
                             <div class="flex justify-between items-center py-2 border-b border-gray-100">
                                <span class="text-sm text-gray-600 font-medium">Commercial Cap. (A)</span>
                                 <div class="text-right">
                                    <span class="text-base font-bold text-green-600 block leading-none font-mono flex items-end"><span id="qA_com1"></span><span class="text-[10px] ml-1">MMSCFD</span></span>
                                 </div>
                             </div>
                             <div class="flex justify-between items-center py-2 border-b border-gray-100">
                                <span class="text-sm text-gray-600 font-medium">Commercial Cap. (B)</span>
                                 <div class="text-right">
                                    <span class="text-base font-bold text-green-600 block leading-none font-mono flex items-end"><span id="qB_com1"></span><span class="text-[10px] ml-1">MMSCFD</span></span>
                                 </div>
                             </div>
                        </div>
                    </div>
                </div>
            </div>

            <div id="tab2-results" class="hidden p-6">
                <!-- Top KPIs -->
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
                    <div class="bg-gradient-to-br from-blue-600 to-blue-700 rounded-lg p-4 text-white shadow-md relative overflow-hidden flex flex-col justify-between h-32">
                         <div class="relative z-10">
                            <p class="text-blue-100 text-xs font-bold uppercase tracking-wider mb-1">Flow (Pan. A)</p>
                            <div class="flex items-baseline gap-2">
                                 <span id="qResA" class="text-3xl font-bold tracking-tight text-white font-mono">-</span>
                                 <span class="text-lg text-blue-200 font-medium">MMSCFD</span>
                            </div>
                         </div>
                    </div>
                    
                    <div class="bg-white border border-gray-200 rounded-lg p-4 shadow-sm relative flex flex-col justify-between h-32">
                         <div>
                            <p class="text-gray-500 text-xs font-bold uppercase tracking-wider mb-1">Flow (Pan. B)</p>
                            <div class="flex items-baseline gap-2">
                                <span id="qResB" class="text-3xl font-bold text-gray-800 font-mono">-</span>
                                <span class="text-lg text-gray-400 font-medium">MMSCFD</span>
                            </div>
                         </div>
                    </div>

                    <div class="bg-purple-50 border border-purple-100 rounded-lg p-4 shadow-sm flex flex-col justify-between h-32 relative overflow-hidden">
                         <div>
                            <p class="text-purple-800 text-xs font-bold uppercase tracking-wider mb-1">Erosional Vel (API)</p>
                            <div class="flex items-baseline gap-2">
                                <span id="veRes" class="text-3xl font-bold text-gray-800 font-mono">-</span>
                            </div>
                         </div>
                         <span class="text-xs text-purple-400 font-medium self-end">ft/s</span>
                    </div>

                    <div class="bg-gray-50 border border-gray-200 rounded-lg p-4 shadow-inner flex flex-col justify-between h-32">
                         <div>
                            <p class="text-gray-500 text-xs font-bold uppercase tracking-wider mb-1">50% Velocity Lmt</p>
                            <div class="flex items-baseline gap-2">
                                <span id="vrRes" class="text-3xl font-bold text-gray-700 font-mono">-</span>
                            </div>
                         </div>
                         <span class="text-xs text-gray-400 font-medium self-end">ft/s</span>
                    </div>
                </div>

                <!-- Tables -->
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 border-t border-gray-100 pt-6">
                    <div>
                        <h3 class="text-xs font-bold text-gray-400 uppercase tracking-widest mb-4 flex items-center gap-2">
                            <span class="w-2 h-2 bg-blue-500 rounded-full"></span> Operation
                        </h3>
                        <div class="space-y-0">
                             <div class="flex justify-between items-center py-2 border-b border-gray-100">
                                <span class="text-sm text-gray-600 font-medium">Actual Inlet Vel (P1)</span>
                                <div class="text-right flex items-end gap-1">
                                    <span class="text-base font-bold text-blue-600 block leading-none font-mono" id="vActRes">-</span>
                                    <span class="text-[10px] text-gray-400">ft/s</span>
                                </div>
                             </div>
                             <div class="flex justify-between items-center py-2 border-b border-gray-100">
                                <span class="text-sm text-gray-600 font-medium">Avg Compressibility (Z)</span>
                                <span class="text-base font-bold text-gray-800 font-mono" id="z_tab2">-</span>
                             </div>
                        </div>
                    </div>
                    <div>
                        <h3 class="text-xs font-bold text-gray-400 uppercase tracking-widest mb-4 flex items-center gap-2">
                            <span class="w-2 h-2 bg-purple-500 rounded-full"></span> Regime
                        </h3>
                        <div class="space-y-0">
                             <div class="flex justify-between items-center py-2 border-b border-gray-100">
                                <span class="text-sm text-gray-600 font-medium">Reynolds Num</span>
                                <span class="text-base font-bold text-gray-800 font-mono" id="reynolds2">-</span>
                             </div>
                             <div class="flex justify-between items-center py-2 border-b border-gray-100">
                                <span class="text-sm text-gray-600 font-medium">Recommended Eq.</span>
                                <span class="text-base font-bold text-purple-600 font-mono" id="eq_tab2">-</span>
                             </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- TAB 3 (Presión) -->
            <div id="tab3-results" class="hidden p-6">
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
                    <!-- KPI A -->
                    <div class="bg-gradient-to-br from-blue-600 to-blue-700 rounded-lg p-4 text-white shadow-md relative overflow-hidden flex flex-col justify-between h-32 md:col-span-2">
                         <div class="relative z-10 flex flex-col justify-between h-full">
                            <p class="text-blue-100 text-xs font-bold uppercase tracking-wider mb-1">Arrival P2 (Pan. A)</p>
                            <div class="flex items-baseline gap-2">
                                 <span id="p2ResA" class="text-4xl font-bold tracking-tight text-white font-mono">-</span>
                                 <span class="text-lg text-blue-200 font-medium">psig</span>
                            </div>
                            <p class="text-[10px] text-blue-200 font-mono text-right mt-1">Abs: <span id="p2ResAbsA"></span> psia</p>
                         </div>
                    </div>
                    
                    <!-- KPI B -->
                    <div class="bg-white border border-gray-200 rounded-lg p-4 shadow-sm relative flex flex-col justify-between h-32 md:col-span-2 hover:border-blue-300 transition-colors">
                         <div class="flex flex-col justify-between h-full">
                            <p class="text-gray-500 text-xs font-bold uppercase tracking-wider mb-1">Arrival P2 (Pan. B)</p>
                            <div class="flex items-baseline gap-2">
                                <span id="p2ResB" class="text-3xl font-bold text-gray-800 font-mono">-</span>
                                <span class="text-lg text-gray-400 font-medium">psig</span>
                            </div>
                            <p class="text-[10px] text-gray-400 font-mono text-right mt-1">Abs: <span id="p2ResAbsB"></span> psia</p>
                         </div>
                    </div>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 border-t border-gray-100 pt-6">
                    <div>
                        <div class="space-y-0">
                             <div class="flex justify-between items-center py-2 border-b border-gray-100">
                                <span class="text-sm text-gray-600 font-medium">Converged Z Factor</span>
                                <span class="text-base font-bold text-blue-600 font-mono" id="z_tab3">-</span>
                             </div>
                             <div class="flex justify-between items-center py-2 border-b border-gray-100">
                                <span class="text-sm text-gray-600 font-medium">Reynolds Num</span>
                                <span class="text-base font-bold text-gray-800 font-mono" id="reynolds3">-</span>
                             </div>
                        </div>
                    </div>
                    <div>
                        <div class="space-y-0">
                             <div class="flex justify-between items-center py-2 border-b border-gray-100">
                                <span class="text-sm text-gray-600 font-medium">&Delta;P (Pan. A)</span>
                                 <div class="text-right flex items-end gap-1">
                                    <span class="text-base font-bold text-red-600 block leading-none font-mono" id="dpA_tab3">-</span>
                                    <span class="text-[10px] text-gray-400">psi</span>
                                 </div>
                             </div>
                             <div class="flex justify-between items-center py-2 border-b border-gray-100">
                                <span class="text-sm text-gray-600 font-medium">&Delta;P (Pan. B)</span>
                                 <div class="text-right flex items-end gap-1">
                                    <span class="text-base font-bold text-red-600 block leading-none font-mono" id="dpB_tab3">-</span>
                                    <span class="text-[10px] text-gray-400">psi</span>
                                 </div>
                             </div>
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

start_main = text.find('<main')
end_main = text.find('</main>') + len('</main>')

if start_main != -1 and end_main != -1:
    new_text = text[:start_main] + html_main + text[end_main:]
    with open('13_panhandle_calculator.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("UI fixed successfully!")
else:
    print("Could not find <main> tags")
