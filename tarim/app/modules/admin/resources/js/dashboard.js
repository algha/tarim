import Turbolinks from 'turbolinks'
import { Application, Controller } from 'stimulus'
import { definitionsFromContext } from 'stimulus/webpack-helpers'


window.axios = require('axios');

global.$ = global.jQuery = require('jquery');

require('select2');

window.application = Application.start();
window.Controller = Controller;

const app = Application.start()
const context = require.context('./controllers', true, /\.js$/)
application.load(definitionsFromContext(context))

Turbolinks.start()

document.addEventListener("turbolinks:load", function() {

})
