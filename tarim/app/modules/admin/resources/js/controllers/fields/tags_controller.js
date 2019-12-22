import { Controller } from "stimulus"

export default class extends Controller {

    static targets (){
        return []
    }

    connect() {
      const select = this.element.querySelector('select');
      const url = this.element.dataset.url
      $(select).select2({
          theme: "classic",
          tags: true,
          templateResult: (state) => {
              if (!state.count) {
                  return $(`<span>${state.text}</span>`);
              }
              return $(`<span>${state.text}</span>
                        <span class="is-pulled-right has-background-info has-text-white">${state.count}</span>`);
          },
          templateSelection: function(tag) {
                return tag.text;
          },
          createTag(tag) {
              console.log('tag.term: ',tag.term)
              return {
                  id : tag.term,
                  text: tag.term,
                  isNewFlag: true
              };
          },
          ajax: {
              delay: 340,
              url: url,
              data: function (params) {
                var query = {
                  search: params.term
                }
                return query;
              },
              processResults(data) {
                  return {
                      results: data.data,
                  };
              },
            }
      }).on( 'select2:select', function( e ) {
        if (isNaN(e.params.data.id)) {
          return;
        }
        var $select = $(this);
        $select.find( '[value="'+e.params.data.text+'"]' ).remove();
        $select.find( '[value="'+e.params.data.id+'"]' )
              .replaceWith( '<option selected value="'+e.params.data.text+'">' + e.params.data.text + '</option>' );
      });
    }

  }
