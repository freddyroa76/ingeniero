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
        primary: "#005fa3", // Professional Blue (vs old #0A66C2)
        secondary: "#00365a", // Deep Navy
        accent: "#0077cc", // Bright Blue
        background: "#f8f9fa", // Clean Light Grey
        surface: "#ffffff",
        "text-primary": "#0f172a", // Slate 900
        "text-secondary": "#475569", // Slate 600
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
