/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/*.{html,js}"],
  theme: {
    extend: {
      fontFamily: {
        sans: ["Inter", "system-ui", "-apple-system", "sans-serif"],
        heading: ["Inter", "system-ui", "-apple-system", "sans-serif"],
      },
      colors: {
        primary: "#0F172A", // Deep Ocean Navy (Autoridad)
        secondary: "#008F4C", // Industrial Teal (Ecopetrol Heritage)
        accent: "#D4E157", // Kinetic Lime (Energía)
        "accent-alt": "#FFD817", // Amarillo
        "accent-orange": "#FF5F00", // Naranja
        background: "#F8FAFC", // Cool Grey 50
        surface: "#ffffff",
        "text-primary": "#334155", // Slate 700 (Legibilidad)
        "text-secondary": "#1E293B", // Slate 800 (Encabezados)
      },
      boxShadow: {
        glass:
          "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06), inset 0 2px 4px 0 rgba(255, 255, 255, 0.05)",
        float:
          "0 10px 15px -3px rgba(0, 95, 163, 0.1), 0 4px 6px -2px rgba(0, 95, 163, 0.05)",
      },
    },
  },
  plugins: [],
};
