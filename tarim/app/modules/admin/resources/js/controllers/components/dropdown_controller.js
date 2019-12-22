import { Controller } from "stimulus"

export default class extends Controller {

    connect() {
    }

   handleTriggerClick(event) {
       if(this.element.classList.contains('is-active')) {
           this.element.classList.remove('is-active');
       } else {
           this.element.classList.add('is-active');
       }
   }

   handleAjaxClick(event){
     this.element.classList.remove('is-active');

     const button = event.currentTarget

     var method = button.dataset.method
     var url = button.dataset.url
     var _confirm = button.dataset.confirm

     if (_confirm != ""){
       if (confirm(_confirm) == false){
         return;
       }
     }

     axios({
        method: method,
        url: url,
        responseType: 'json'
      })
      .then(function (response) {
        console.log("respose: ", response)
      });
   }

   handleClick(event){
     this.element.classList.remove('is-active');
     console.log("click is called")
   }

  }
