// Navigation logic and Shared Behaviors for Tool Pages
document.addEventListener("DOMContentLoaded", () => {
  // 1. Highlight Active Menu Item (if any)
  const currentPath = window.location.pathname;
  const menuLinks = document.querySelectorAll("nav a");
  
  menuLinks.forEach(link => {
      // Check if link href matches current file (ignoring query strings)
      if (link.getAttribute("href") && currentPath.includes(link.getAttribute("href"))) {
          link.classList.add("text-blue-600", "font-bold");
      }
  });

  // 2. Inject "Memoria de Cálculo" Footer for Printing
  // This ensures all tools have the required footer without manual HTML edits for the footer part.
  
  if (!document.getElementById("print-footer")) {
      const footer = document.createElement("footer");
      footer.id = "print-footer";
      footer.className = "hidden print:block fixed bottom-0 left-0 w-full bg-white border-t-2 border-green-600 pt-2 pb-4 text-xs text-gray-600";
      
      const now = new Date().toLocaleDateString('es-CO', { 
          weekday: 'long', 
          year: 'numeric', 
          month: 'long', 
          day: 'numeric',
          hour: '2-digit',
          minute: '2-digit'
      });

      footer.innerHTML = `
          <div class="max-w-7xl mx-auto px-4 flex justify-between items-end">
              <div>
                  <div class="font-bold text-gray-800 text-sm mb-1">MEMORIA DE CÁLCULO</div>
                  <div>Generado por: Freddy Roa Ingeniería Tools</div>
                  <div class="mt-1">Fuente: <span class="font-mono text-blue-800">${window.location.href}</span></div>
              </div>
              <div class="text-right">
                  <div class="font-bold text-gray-800">${now}</div>
                  <div class="italic text-[10px] mt-1">Este documento es para fines informativos. Verifique resultados.</div>
              </div>
          </div>
      `;
      
      document.body.appendChild(footer);
  }
});
