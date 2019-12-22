let mix = require('laravel-mix');

mix.setPublicPath('public');

mix.js('resources/js/auth.js', 'public/js/')
   .sass('resources/css/auth.scss', 'public/css/');

mix.js('resources/js/dashboard.js', 'public/js/')
  .sass('resources/css/dashboard.scss', 'public/css/');

if (mix.inProduction()) {
  mix.version();
}
