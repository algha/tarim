import Modal from '@vizuaalog/bulmajs/src/plugins/modal'
import Cropper from 'cropperjs';

export default class extends window.Controller {

    connect() {
      this.url = this.element.dataset.url
      this.lock = this.element.dataset.lock
      this.rounded = this.element.dataset.rounded
      this.width = this.element.dataset.width
      this.height = this.element.dataset.height

      this.selectbox = this.element.querySelector('.select-box')
      this.output = this.element.querySelector('.output')
      this.file = this.element.querySelector('#picture')
      this.file.addEventListener("change", this.imageSelect.bind(this));

      this.picture = this.element.querySelector('.picture')
    }

    imageSelect(event){
      var files = this.file.files;
      if (files.length) {
        this.showModal(files[0])
      }
    }

    showModal(file){
      var src = this.createObjectURL(file);

      this.modal = new Modal({
        style : 'modal',
        closable: false,
        body: '<div class="cropper-frame"><img id="photo" src="'+src+'"></div>',
      });
      this.modal.open()
      $('.modal').addClass('crop-modal')




      var options = {
        viewMode: 0,
        crop(event) {
          $("#w").val(parseInt(event.detail.width))
          $("#h").val(parseInt(event.detail.height))
        },
      }

      if (this.lock == "lock") {
        options.cropBoxResizable = false
      }

      if (this.width && this.height) {
        options = Object.assign(options, {
          minContainerHeight: parseInt(this.height),
          minContainerWidth: parseInt(this.width) ,
          minCanvasHeight: parseInt(this.height),
          minCanvasWidth: parseInt(this.width)
        });
      }

      const image = document.getElementById('photo');
      this.cropper = new Cropper(image, options);

      this.addControl(this.cropper)

    }


    addControl(cropper){
      var self = this
      var w = cropper.getImageData().width
      var h = cropper.getImageData().height

      // first line controller
      var control = $("<div class='image-controls has-padding-6'></control>")
      $(".cropper-frame").append(control)

      const disabled = this.lock == "lock" ? "disabled" : ""
      var resize = $("<p class='image-control resize has-margin-r-6'>Resize: <input id='w' value='"+w+"' "+disabled+" /> <input id='h' value='"+h+"' "+disabled+" /> </p>")
      var confirmize = $("<button id='resize-confirm'>confirm</button>")
      resize.append(confirmize)

      var rotate = $("<p class='image-control rotate'>rotate : </p>")
      var rotating = $("<button data-rotate='1' class='rotating'>Rotate Left</button> <button data-rotate='-1' class='rotating'>Rotate Right</button>")
      rotate.append(rotating)
      control.append([resize, rotate])

      // control events
      rotating.click(function(){
        var rotate = parseInt($(this).data("rotate")) * 90
        cropper.rotate(rotate);
      })

      confirmize.click(function(){
        self.setSize(cropper, parseInt($("#w").val()), parseInt($("#h").val()))
      })

      // second line controller
      var control = $("<div class='image-controls has-text-right has-padding-6 is-paddingless-t'></control>")
      $(".cropper-frame").append(control)

      var buttons = $("<p class='image-control'></p>")
      var confirm = $("<button class='button is-primary'>Confirm</button>")
      var cancel = $("<button class='button is-warning'>Cancel</button>")
      buttons.append([confirm,cancel])
      control.append(buttons)


      confirm.click(function(){
        self.confirm()
      })

      cancel.click(function(){
        self.close()
      })

    }

    confirm(){
      var self = this
      this.cropper.getCroppedCanvas().toBlob((blob) => {
        $(self.output).find("img").attr("src",self.createObjectURL(blob));

        const formData = new FormData();
        formData.append('croppedImage', blob, 'cropped.png');
        $.ajax(self.url, {
          method: "POST",
          data: formData,
          processData: false,
          contentType: false,
          success(data) {
            console.log('Upload success', data);
            if (data.status != 1) {
              alert(data.message)
              return ;
            }
            console.log("self.picture",self.picture)
            self.picture.value = data.data[0].url
          },
          error() {
            alert('Upload error')
            console.log('Upload error');
          },
        });
      },'image/png' );
      $(this.selectbox).hide()
      $(this.output).show()
      this.close()
    }

    close(){
      this.modal.close()
      $(".crop-modal").remove()
      this.cropper.destroy()
      this.cropper = null
      this.modal = null
    }

    setSize(cropper, w, h){
      var ratio = cropper.getImageData().width / cropper.getImageData().naturalWidth;
      cropper.setCropBoxData({
        width: w * ratio,
        height: h * ratio
      })
    }

    createObjectURL(object) {
        return (window.URL) ? window.URL.createObjectURL(object) : window.webkitURL.createObjectURL(object);
    }

    remove(e){
      console.log("xxx")
      $(this.selectbox).removeClass("is-hidden").show()
      $(this.output).hide()
    }
  }
