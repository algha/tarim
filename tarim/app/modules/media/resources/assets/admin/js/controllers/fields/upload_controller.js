import Media from '../../layouts/media'

export default class extends window.Controller {

    static targets (){
        return []
    }

    connect() {
      const name = this.element.dataset.name
      this.media = new Media({'params':
        {name: name}
      })

      this.registerEvents()
    }

    registerEvents(){
      this.element.querySelector('#upload-zone').addEventListener('click', this.mediaOpen.bind(this))
    }

    mediaOpen(e){
      this.media.open()
    }

    remove(e){
      var item = $(e.currentTarget);
      var id = item.data("id")
      var parent = item.parents().find(".column.is-half[data-id='"+id+"']")
      if(confirm('do you really want to remove this item?')){
          parent.remove()
      }
    }

}
