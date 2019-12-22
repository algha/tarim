import { Controller } from "stimulus"

export default class extends Controller {

    static targets (){
        return []
    }

    connect() {
      const select = this.element.querySelector('select');

      if (select.getAttribute('multiple') === null) {
          return;
      }

      $(select).select2({
          theme: "classic"
      });
    }

  }
