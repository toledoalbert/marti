twttr.ready(function (twttr) {

	


	
	twttr.widgets.createTweetEmbed(
		'20',
  		document.getElementById('container'),
  		{
    		theme: 'dark'
  		}).then(function (el) {
    		console.log("Tweet embedded")
  		});
    });