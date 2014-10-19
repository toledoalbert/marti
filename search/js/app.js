twttr.ready(function (twttr) {

$.ajax({
    url: "http://martiapi.herokuapp.com/tweets",
 
    // the name of the callback parameter, as specified by the YQL service
    jsonp: "callback",
 
    // tell jQuery we're expecting JSONP
    dataType: "jsonp",
 
    // work with the response
    success: function( response ) {
        console.log( response ); // server response
    }
});


	
	twttr.widgets.createTweetEmbed(
		'20',
  		document.getElementById('container'),
  		{
    		theme: 'dark'
  		}).then(function (el) {
    		console.log("Tweet embedded")
  		});
    });