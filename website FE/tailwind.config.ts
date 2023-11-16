import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    fontFamily: {
      'poppins': ['Poppins', 'sans-serif'],
    },
    extend: {
      // animation: {
      //   'gradient': 'gradient 5s ease infinite',
      // },
      // keyframes: {
      //   gradient: {
      //     '0%, 100%': {
      //       'background-size':'200% 200%',
      //       'background-position': 'left center'
      //     },
      //     '50%': {
      //       'background-size':'200% 200%',
      //       'background-position': 'right center'
      //     }
      //   },
      // },
      backgroundSize: {
        'size-200': '200% 200%',
      },
      backgroundPosition: {
        'pos-0': '0% 0%',
        'pos-100': '-100% -100%',
      },
      backgroundImage: {
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
        'gradient-conic':
          'conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))',
      },
    },
  },
  plugins: [],
}
export default config
