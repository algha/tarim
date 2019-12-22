import { Controller } from 'stimulus';
import CodeFlask from 'codeflask';

export default class extends Controller {
    /**
     *
     */
    connect() {

        const input = this.element.querySelector('input');
        const code = this.element.querySelector('.code')
        const height = this.data.get('height')

        $(code).height(height)

        const flask = new CodeFlask(code, {
            language: this.data.get('language'),
            lineNumbers: this.data.get('lineNumbers'),
            defaultTheme: this.data.get('defaultTheme'),
        });

        flask.updateCode(input.value);

        flask.onUpdate((code) => {
            input.value = code;
        });
    }
}
