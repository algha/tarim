import * as FilePond from 'filepond'
import FilePondPluginImagePreview from 'filepond-plugin-image-preview'

export default class extends window.Controller {

    static targets (){
        return []
    }

    connect() {
      this.targetName = this.element.dataset.targetName
      this.targetElement = $('#post-form').find('[data-name='+this.targetName+'] #files')
      this.url = this.element.dataset.url


      this.tabs = this.element.querySelector('.tabs')
      this.tab_items = this.tabs.getElementsByClassName('tab-item')

      this.tabs_content = this.element.querySelector('.tabs-content')
      this.tab_content_items = this.tabs_content.getElementsByClassName('tab-content-item')

      this.registerEvents()

      this.initDropzone(this)

      this.items = []

      this.template = `<div class="column is-half" data-id="{id}">
                        <img class="image" src="{img_url}" />
                        <input type="hidden" name="`+this.targetName+`[]" value="{id}">
                        <div class="info">
                          <div>
                            <span class="info-item remove" data-id="{id}" data-action="click->fields--upload#remove"> <i class="fas fa-trash-alt"></i> </span>
                            <a class="info-item link" href="{file_url}" target="_blank"><i class="fas fa-link"></i></a>
                            <p class="name">{original_name}</p>
                          </div>
                        </div>
                      </div>`;

    }



    passImages(response){

      for (var img in response.data){
        var template = this.template
        img = response.data[img]
        if (img.file_type == 'photo') {
          template = template.replace('{img_url}',img.url)
        }else{
          template = template.replace('{img_url}','/storage/files/file.png')
        }

        template = template.replace('{file_url}',img.url)

        template = template.split('{id}').join(img.id)

        template = template.replace('{original_name}',img.original_name)

        this.targetElement.append(template)
      }
    }

    registerEvents(){
      var self = this
      $(this.tab_items).click(function(e){
        $(this).addClass('is-active').siblings().removeClass('is-active')
        self.showContentItem($(this).index())
      })
    }

    showContentItem(index){
      $(this.tab_content_items).each(function(i, item){
        if(i == index){
          $(item).addClass('is-active')
        }else{
          $(item).removeClass('is-active')
        }
      })

    }

    initDropzone(context){
      FilePond.registerPlugin(
        FilePondPluginImagePreview,
      );
      FilePond.setOptions({
          allowMultiple: true,
          server: {
            url: this.url,
            revert: null,
            restore: null,
            load: null,
            fetch: null,
            process: {
                method: 'POST',
                onload: (response) => {
                  context.passImages(JSON.parse(response))
                },
                onerror: (response) => {
                  console.log('server error: ',response.data)
                  alert('server error');
                },
                ondata: (formData) => {
                    // formData.append('Hello', 'World');
                    return formData;
                }
            },
          }
      });

      const pond = FilePond.create(document.querySelector('#filepond'));

    }




  }
