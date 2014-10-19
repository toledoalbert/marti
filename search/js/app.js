twttr.ready(function (twttr) {

	$.getJSON( "https://martiapi.herokuapp.com/tweets", function( data ) {
    var items = [];
    $.each( data, function( key, val ) {
      items.push( "<li id='" + key + "'>" + val + "</li>" );
    });
   
    $( "<ul/>", {
      "class": "my-new-list",
      html: items.join( "" )
    }).appendTo( "body" );
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