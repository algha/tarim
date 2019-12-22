import { Controller } from 'stimulus';
import Turbolinks from 'turbolinks';

export default class extends Controller {
    /**
     *
     */
    initialize() {

    }

    connect() {
      $(document).click(function (e) {
          var container = $(".dropdown.is-active");
          if (container.has(e.target).length === 0) {
             container.removeClass("is-active");
          }
      })

      $('.flash-message .delete').click(function(){
        $(this).parents('.flash-message').remove()
      })
    }
}
