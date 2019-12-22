import { Controller } from 'stimulus';

import tinymce from 'tinymce/tinymce';

export default class extends Controller {

    connect() {
        tinymce.baseURL = '/dashboard/assets/js/tinymce';

        const theme = this.element.dataset.theme
        const height = this.element.dataset.height


        const selector = this.element.querySelector('.tinymce');
        const input = this.element.querySelector('input');

        $(selector).height(height)

        let plugins = 'image media table link paste textpattern autolink codesample';
        let toolbar1 = '';
        let inline = true;

        if (theme === 'modern') {
            plugins = 'print autosave autoresize preview paste code searchreplace autolink directionality visualblocks visualchars fullscreen image link media template codesample table charmap hr pagebreak nonbreaking anchor toc insertdatetime advlist lists wordcount imagetools textpattern';
            toolbar1 = 'formatselect | bold italic strikethrough forecolor backcolor | link | alignleft aligncenter alignright alignjustify | numlist bullist outdent indent | removeformat | ltr rtl';
            inline = false;
        }

        tinymce.init({
            branding: false,
            selector: `#${selector.id}`,
            // theme: 'modern',
            min_height: 300,
            height: 300,
            max_height: 600,
            plugins,
            toolbar1,
            insert_toolbar: 'quickimage quicktable media codesample fullscreen',
            selection_toolbar:
                'bold italic | quicklink h2 h3 blockquote | alignleft aligncenter alignright alignjustify | outdent indent | removeformat ',
            inline,
            convert_urls: false,
            image_caption: true,
            image_title: true,
            image_class_list: [
                {
                    title: 'None',
                    value: '',
                },
                {
                    title: 'Responsive',
                    value: 'img-fluid',
                },
            ],
            setup: (element) => {
                element.on('change', () => {
                    $(input).val(element.getContent());
                });

                element.on('BeforeRenderUI', function(e) {

                });
                element.on('LoadContent', function(e) {

                });
            },
            images_upload_handler: this.upload,
        });

        document.addEventListener('turbolinks:before-cache', () => {
            tinymce.remove(`#${selector.id}`);
        }, { once: true });
    }

    /**
     *
     * @param blobInfo
     * @param success
     */
    upload(blobInfo, success) {

    }

    disconnect() {
        tinymce.remove(`#${this.element.querySelector('.tinymce').id}`);
    }
}
