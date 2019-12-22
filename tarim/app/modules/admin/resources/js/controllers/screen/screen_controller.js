import { Controller } from 'stimulus';
import Turbolinks from 'turbolinks';

export default class extends Controller {
    /**
     *
     */
    initialize() {

    }

    connect() {
    
    }

    targetModal(event){
      const key = event.target.dataset.modalKey;

      this.application.getControllerForElementAndIdentifier(
          document.getElementById(`screen-modal-${key}`),
          'screen--modal',
      ).open({
          title : event.target.dataset.modalTitle,
          load  : event.target.dataset.modalLoad,
          submit: event.target.dataset.modalAction,
          params: event.target.dataset.modalParams,
      });

      return event.preventDefault();
    }

}
