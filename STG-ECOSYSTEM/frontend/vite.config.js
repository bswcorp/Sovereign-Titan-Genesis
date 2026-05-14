import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
  root: './',
  base: '/',
  server: {
    port: 3000,
    strictPort: true,
    host: '127.0.0.1',
    cors: true
  },
  build: {
    outDir: '../../dist/frontend',
    emptyOutDir: true,
    sourcemap: false,
    minify: 'terser',
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html')
      }
    }
  }
});
