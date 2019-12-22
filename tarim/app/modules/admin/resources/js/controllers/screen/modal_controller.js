import {Controller} from "stimulus";

export default class extends Controller {

    connect(){

      this.background = this.element.querySelector('div.modal-background')
      this.title = this.element.querySelector('p.modal-card-title')

      this.registerEvents()
    }

    registerEvents(){
      this.background.addEventListener('click', this.close.bind(this))
    }

    close(event){
      this.element.classList.toggle("is-active")
    }

    open(options) {

        this.title.textContent = options.title;
        this.element.querySelector('form').action = options.submit;

        this.asyncLoadData(options);

        this.element.classList.toggle("is-active")
    }

    /**
     *
     * @param options
     */
    asyncLoadData(options) {

        let name = this.data.get('url') + '/' + this.data.get('slug') + '/' + options.load;

        var  params = JSON.parse(options.params)

        axios.post(name, params).then((response) => {
            this.element.querySelector('[data-async]').innerHTML = response.data;
        });
    }

}
