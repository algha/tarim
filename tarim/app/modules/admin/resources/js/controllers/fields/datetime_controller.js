import Flatpickr from 'stimulus-flatpickr';

export default class extends Flatpickr {

    static targets (){
        return []
    }

    initialize() {
      this.config = {}
    }

    change(selectedDates, dateStr, instance) {
      return dateStr;
    }

  }
