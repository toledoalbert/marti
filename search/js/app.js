twttr.ready(function (twttr) {

  $.ajax({
      // url: "http://martiapi.herokuapp.com/tweets",
      url: "http://0.0.0.0:5002/tweets",
   
      // the name of the callback parameter, as specified by the YQL service
      jsonp: "callback",
   
      // tell jQuery we're expecting JSONP
      dataType: "jsonp",
   
      // work with the response
      success: function( response ) {
          $.each( response.data, function( key, val ) {
              twttr.widgets.createTweetEmbed(
                val.id,
                  document.getElementById('container'),
                  {
                    theme: 'dark', align: 'center'
                  });
          });
      }
  });

});