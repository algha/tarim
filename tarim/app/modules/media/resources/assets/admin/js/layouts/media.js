import Modal from '@vizuaalog/bulmajs/src/plugins/modal'

export default class{

  constructor(options = {}){
    this.options = Object.assign({
        'title': 'Media',
        'read_url': '/dashboard/media/ajax_media',
        'params': {}
    }, options)
  }

  getOption(key){
    return this.options[key]
  }

  initModal(){
    this.modal = new Modal({
      style : 'modal',
      title: this.getOption('title'),
      body: '<p class="image is-4by3"><img src="https://bulma.io/images/placeholders/1280x960.png"></p>',
      buttons: [
            {
                label: 'Save changes',
                classes: ['button', 'is-success'],
                onClick: function() { alert('Save button pressed'); }
            },
            {
                label: 'Close',
                classes: ['button', 'is-danger', 'is-outline'],
                onClick: function() { alert('Close button pressed'); }
            }
        ]
    });
  }

  getMediaData(){
    const params = this.getOption('params')
    const content = document.querySelector('.modal-content')
    axios.get(this.getOption('read_url'), {params}).then((response) => {
        content.innerHTML = response.data
        FontAwesome.dom.i2svg();
    });
  }

  open() {
    console.log("media opened method")
    if (this.modal == undefined){
      this.initModal()
    }
    $('.modal').addClass('media-modal')
    this.modal.open()
    this.getMediaData()

  }

  selectFile(e)
  {
    console.log('select')
  }

}
