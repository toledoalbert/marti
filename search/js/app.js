twttr.ready(function (twttr) {

  var searchbutton = document.getElementById("search");
  searchbutton.onclick = searchButtonClicked;

  // $.ajax({

  //     // url: "http://martiapi.herokuapp.com/tweets",
  //     url: "http://martiapi.herokuapp.com/sunny+cloudy+cold/42.1497,-74.9384,500mi",
   
  //     // the name of the callback parameter, as specified by the YQL service
  //     json: "callback",
   
  //     // tell jQuery we're expecting JSONP
  //     dataType: "json",
   
  //     // work with the response
  //     success: function( response ) {
  //         $.each( response.data, function( key, val ) {
  //             console.log("in the loop", key, val.id);
  //             twttr.widgets.createTweetEmbed(
  //               val.id,
  //                 document.getElementById('results'),
  //                 {
  //                   theme: 'light', align: 'center'
  //                 });
  //         });
  //     }
  // });

});

var searchButtonClicked = function () {
  var results = document.getElementById("results");
  results.innerHTML = "<div id='spinner' class='spinner'> <div class='circle1 circle'></div> <div class='circle2 circle'></div><div class='circle3 circle'></div><div class='circle4 circle'></div><div class='circle5 circle'></div><div class='circle6 circle'></div><div class='circle7 circle'></div><div class='circle8 circle'></div><div class='circle9 circle'></div><div class='circle10 circle'></div><div class='circle11 circle'></div><div class='circle12 circle'></div></div>";
  var searchFieldValue = document.getElementById("searchField").value;
  console.log("searchFieldValue: " + searchFieldValue);
  searchFieldValue = searchFieldValue + "";
  var wordsToSearch = searchFieldValue.split(' ');
  // var wordsToSearch = ["cold", "sunny", "funny"];
  searchTweets(wordsToSearch);
};


var searchTweets = function(keywords) {
  console.log("Searching...");
  var words = concatWords(keywords);

  $.ajax({
      // url: "http://martiapi.herokuapp.com/tweets",
      url: "http://martiapi.herokuapp.com/" + words,
   
      // the name of the callback parameter, as specified by the YQL service
      json: "callback",
   
      // tell jQuery we're expecting JSONP
      dataType: "json",
   
      // work with the response
      success: function( response ) {
          $.each( response.data, function( key, val ) {
              console.log("in the loop", key, val.id);
              twttr.widgets.createTweetEmbed(
                val.id,
                  document.getElementById('results'),
                  {
                    theme: 'light', align: 'center'
                  }).then( function(el) {
                    document.getElementById("spinner").style.display = "none";
                  });
          });
      }
  });
};

var searchTweetsWithLocation = function(keywords, location) {
  
  var words = concatWords(keywords);

  $.ajax({
      // url: "http://martiapi.herokuapp.com/tweets",
      url: "http://martiapi.herokuapp.com/" + words + "/" + geo_codes[location],
   
      // the name of the callback parameter, as specified by the YQL service
      json: "callback",
   
      // tell jQuery we're expecting JSONP
      dataType: "json",
   
      // work with the response
      success: function( response ) {
          $.each( response.data, function( key, val ) {
              console.log("in the loop", key, val.id);
              twttr.widgets.createTweetEmbed(
                val.id,
                  document.getElementById('results'),
                  {
                    theme: 'light', align: 'center'
                  });
          });
      }
  });
};

var concatWords = function(wordsArray) {

  // wordsArray = ["cloudy", "rainy", "cold", "windy", "sunny", "hot", "warm", "chilly"];

  words = "";

  //Concatanate the words together for the request.
  for (var i = wordsArray.length - 1; i >= 0; i--) {
    if(i == 0){
      words += wordsArray[i];
    } else{
      words += wordsArray[i] + "+";
    }
  };

  return words;
};

var geo_codes = {

  "AK": "61.3850,-152.2683,500mi",
  "AL":"32.7990,-86.8073,500mi",
  "AR":"34.9513,-92.3809,500mi",
  "AS":"14.2417,-170.7197,500mi",
  "AZ":"33.7712,-111.3877,500mi",
  "CA":"36.1700,-119.7462,500mi",
  "CO":"39.0646,-105.3272,500mi",
  "CT":"41.5834,-72.7622,500mi",
  "DC":"38.8964,-77.0262,500mi",
  "DE":"39.3498,-75.5148,500mi",
  "FL":"27.8333,-81.7170,500mi",
  "GA":"32.9866,-83.6487,500mi",
  "HI":"21.1098,-157.5311,500mi",
  "IA":"42.0046,-93.2140,500mi",
  "ID":"44.2394,-114.5103,500mi",
  "IL":"40.3363,-89.0022,500mi",
  "IN":"39.8647,-86.2604,500mi",
  "KS":"38.5111,-96.8005,500mi",
  "KY":"37.6690,-84.6514,500mi",
  "LA":"31.1801,-91.8749,500mi",
  "MA":"42.2373,-71.5314,500mi",
  "MD":"39.0724,-76.7902,500mi",
  "ME":"44.6074,-69.3977,500mi",
  "MI":"43.3504,-84.5603,500mi",
  "MN":"45.7326,-93.9196,500mi",
  "MO":"38.4623,-92.3020,500mi",
  "MP":"14.8058,145.5505,500mi",
  "MS":"32.7673,-89.6812,500mi",
  "MT":"46.9048,-110.3261,500mi",
  "NC":"35.6411,-79.8431,500mi",
  "ND":"47.5362,-99.7930,500mi",
  "NE":"41.1289,-98.2883,500mi",
  "NH":"43.4108,-71.5653,500mi",
  "NJ":"40.3140,-74.5089,500mi",
  "NM":"34.8375,-106.2371,500mi",
  "NV":"38.4199,-117.1219,500mi",
  "NY":"42.1497,-74.9384,500mi",
  "OH":"40.3736,-82.7755,500mi",
  "OK":"35.5376,-96.9247,500mi",
  "OR":"44.5672,-122.1269,500mi",
  "PA":"40.5773,-77.2640,500mi",
  "PR":"18.2766,-66.3350,500mi",
  "RI":"41.6772,-71.5101,500mi",
  "SC":"33.8191,-80.9066,500mi",
  "SD":"44.2853,-99.4632,500mi",
  "TN":"35.7449,-86.7489,500mi",
  "TX":"31.1060,-97.6475,500mi",
  "UT":"40.1135,-111.8535,500mi",
  "VA":"37.7680,-78.2057,200mi",
  "VI":"18.0001,-64.8199,500mi",
  "VT":"44.0407,-72.7093,500mi",
  "WA":"47.3917,-121.5708,500mi",
  "WI":"44.2563,-89.6385,500mi",
  "WV":"38.4680,-80.9696,500mi",
  "WY":"42.7475,-107.2085,500mi",

};