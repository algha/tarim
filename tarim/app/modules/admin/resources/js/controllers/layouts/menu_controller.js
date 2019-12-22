import { Controller } from "stimulus"

export default class extends Controller {

    static targets (){
        return []
    }

    connect() {
        console.log('menu is loaded')
    }

    toggleMenu(event) {
        console.log('menu is clicked')
        event.currentTarget.classList.toggle("is-active")
        $("li.has-children").not(event.currentTarget).removeClass("is-active")
    }
  }
