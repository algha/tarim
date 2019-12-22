import { Controller } from 'stimulus';
import Turbolinks from 'turbolinks';
import Sortable from 'sortablejs';

export default class extends Controller {

    initialize() {

    }

    connect() {
      const sortable_url = this.element.dataset.sortableUrl
      if (sortable_url == undefined) {
        return ;
      }
      const self = this
      new Sortable(this.element.querySelector('tbody'), {
          animation: 150,
          onEnd: function (evt) {
              const data = self.createDataList(evt.to)
              self.syncSort(sortable_url, data)
        	},
      });
    }

    createDataList(list){
      var data = []
      const rows = list.rows
      for(var i = 0; i < rows.length; i++){
        data.push({
           'id' : rows[i].dataset.id,
           'sort' : i
        })
      }
      return data
    }

    syncSort(url, data){
      axios.post(url, data).then((response) => {
          console.log('response: ',response.data)
      });
    }
}
