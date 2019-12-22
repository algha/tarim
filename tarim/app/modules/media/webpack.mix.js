let mix = require('laravel-mix');

mix.setPublicPath('public');

mix.js('resources/assets/admin/js/admin.js', 'public/js/')
   .sass('resources/assets/admin/css/admin.scss', 'public/css/');

if (mix.inProduction()) {
  mix.version();
}
