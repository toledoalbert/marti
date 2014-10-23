twttr.ready(function (twttr) {

  $.ajax({
      // url: "http://martiapi.herokuapp.com/tweets",
      url: "http://martiapi.herokuapp.com/tweets",
   
      // the name of the callback parameter, as specified by the YQL service
      json: "callback",
   
      // tell jQuery we're expecting JSONP
      dataType: "json",
   
      // work with the response
      success: function( response ) {
          $.each( response.data, function( key, val ) {
              console.log("in the loop");
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